import json
import os
import types

import pytest

import localstack.testing.aws.util as aws_util
from localstack import config as localstack_config
from localstack.testing import config as test_config
from tests.aws import conftest
from tests.aws.conftest import (
    _detect_ambient_emulator,
    _emulator_health_error,
    _emulator_health_probe,
    _warn_reusing_instance,
)


class _FakeResponse:
    def __init__(self, status=200, body=None):
        self.status = status
        self._body = body if body is not None else json.dumps({"services": {"acm": "available"}})

    def read(self):
        return self._body.encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def _patch_urlopen(monkeypatch, fn):
    monkeypatch.setattr("urllib.request.urlopen", fn)


def _pipe_stderr(monkeypatch):
    """Point the conftest's real-stderr helper at a pipe and return its read end."""
    read_fd, write_fd = os.pipe()
    monkeypatch.setattr(conftest, "_real_stderr_fd", lambda request: write_fd)
    return read_fd, write_fd


def _read_pipe(read_fd):
    output = os.read(read_fd, 4096).decode()
    os.close(read_fd)
    return output


def _patch_emulator_config(monkeypatch):
    """Force the fixture/sessionstart to use http://localhost:4566 and not AWS cloud."""
    monkeypatch.setattr(aws_util, "is_aws_cloud", lambda: False)
    monkeypatch.setattr(test_config, "TEST_AWS_ENDPOINT_URL", None)
    monkeypatch.setattr(localstack_config, "internal_service_url", lambda: "http://localhost:4566")


def _call_reachability_fixture(request):
    """Invoke the underlying fixture function, bypassing pytest's fixture wrapper."""
    return conftest._emulator_reachability_check.__wrapped__(request)


def test_health_ok(monkeypatch):
    def fake_urlopen(url, timeout):
        assert url == "http://localhost:4566/_localstack/health"
        assert timeout == 2
        return _FakeResponse()

    _patch_urlopen(monkeypatch, fake_urlopen)
    assert _emulator_health_error("http://localhost:4566", timeout=5) is None


def test_health_ok_with_trailing_slash(monkeypatch):
    def fake_urlopen(url, timeout):
        assert url == "http://localhost:4566/_localstack/health"
        return _FakeResponse()

    _patch_urlopen(monkeypatch, fake_urlopen)
    assert _emulator_health_error("http://localhost:4566/", timeout=5) is None


def test_health_non_json_body_is_an_error(monkeypatch):
    def fake_urlopen(url, timeout):
        return _FakeResponse(status=200, body="<html>not a localstack instance</html>")

    _patch_urlopen(monkeypatch, fake_urlopen)
    error = _emulator_health_error("http://localhost:4566", timeout=3)
    assert error is not None
    assert "no healthy response" in error


def test_health_unexpected_status_is_an_error(monkeypatch):
    def fake_urlopen(url, timeout):
        return _FakeResponse(status=503, body="{}")

    _patch_urlopen(monkeypatch, fake_urlopen)
    error = _emulator_health_error("http://localhost:4566", timeout=3)
    assert error is not None
    assert "no healthy response" in error


def test_health_connection_error_is_an_error(monkeypatch):
    def fake_urlopen(url, timeout):
        raise ConnectionRefusedError("connection refused")

    _patch_urlopen(monkeypatch, fake_urlopen)
    error = _emulator_health_error("http://localhost:4566", timeout=3)
    assert error is not None
    assert "connection refused" in error


def test_health_recovers_after_transient_failures(monkeypatch):
    calls = {"n": 0}

    def fake_urlopen(url, timeout):
        calls["n"] += 1
        if calls["n"] < 3:
            raise ConnectionRefusedError("connection refused")
        return _FakeResponse()

    _patch_urlopen(monkeypatch, fake_urlopen)
    assert _emulator_health_error("http://localhost:4566", timeout=10) is None


def test_probe_ok(monkeypatch):
    def fake_urlopen(url, timeout):
        assert url == "http://localhost:4566/_localstack/health"
        assert timeout == 2
        return _FakeResponse()

    _patch_urlopen(monkeypatch, fake_urlopen)
    assert _emulator_health_probe("http://localhost:4566") == (True, None)


def test_probe_non_json_body_is_an_error(monkeypatch):
    def fake_urlopen(url, timeout):
        return _FakeResponse(status=200, body="<html>not a localstack instance</html>")

    _patch_urlopen(monkeypatch, fake_urlopen)
    ok, error = _emulator_health_probe("http://localhost:4566")
    assert ok is False
    assert error is not None


def test_probe_unexpected_status_is_an_error(monkeypatch):
    def fake_urlopen(url, timeout):
        return _FakeResponse(status=503, body="{}")

    _patch_urlopen(monkeypatch, fake_urlopen)
    ok, error = _emulator_health_probe("http://localhost:4566")
    assert ok is False
    assert error is not None
    assert "unexpected HTTP status 503" in error


def test_probe_connection_error_is_an_error(monkeypatch):
    def fake_urlopen(url, timeout):
        raise ConnectionRefusedError("connection refused")

    _patch_urlopen(monkeypatch, fake_urlopen)
    ok, error = _emulator_health_probe("http://localhost:4566")
    assert ok is False
    assert error is not None
    assert "connection refused" in error


def test_ambient_detection_true_when_health_ok(monkeypatch):
    def fake_urlopen(url, timeout):
        return _FakeResponse()

    _patch_urlopen(monkeypatch, fake_urlopen)
    assert _detect_ambient_emulator("http://localhost:4566") is True


def test_ambient_detection_false_when_unreachable(monkeypatch):
    def fake_urlopen(url, timeout):
        raise ConnectionRefusedError("connection refused")

    _patch_urlopen(monkeypatch, fake_urlopen)
    assert _detect_ambient_emulator("http://localhost:4566") is False


def test_warn_reusing_instance_emits_exact_warning_text(monkeypatch):
    read_fd, write_fd = _pipe_stderr(monkeypatch)

    with pytest.warns(UserWarning) as records:
        _warn_reusing_instance(types.SimpleNamespace(), "http://localhost:4566")

    os.close(write_fd)
    output = _read_pipe(read_fd)

    assert any("reusing running instance at :4566" in str(r.message) for r in records)
    assert "WARNING: reusing running instance at :4566" in output
    assert "may mutate its state" in output


def test_warn_reusing_instance_uses_endpoint_port(monkeypatch):
    read_fd, write_fd = _pipe_stderr(monkeypatch)

    with pytest.warns(UserWarning) as records:
        _warn_reusing_instance(types.SimpleNamespace(), "http://localhost:5000")

    os.close(write_fd)
    output = _read_pipe(read_fd)

    assert any("reusing running instance at :5000" in str(r.message) for r in records)
    assert "WARNING: reusing running instance at :5000" in output


def test_sessionstart_detects_ambient_instance(monkeypatch):
    _patch_emulator_config(monkeypatch)
    monkeypatch.setattr(conftest, "_detect_ambient_emulator", lambda endpoint: True)

    conftest.pytest_sessionstart(types.SimpleNamespace())

    assert conftest._ambient_emulator_at_session_start is True


def test_sessionstart_skips_when_aws_cloud(monkeypatch):
    _patch_emulator_config(monkeypatch)
    monkeypatch.setattr(aws_util, "is_aws_cloud", lambda: True)

    conftest.pytest_sessionstart(types.SimpleNamespace())

    assert conftest._ambient_emulator_at_session_start is False


def test_fixture_warns_when_ambient_detected(monkeypatch):
    """Ambient-up: the fixture emits the reusing-instance warning and does not exit."""
    _patch_emulator_config(monkeypatch)
    monkeypatch.setattr(conftest, "_emulator_health_error", lambda endpoint: None)
    monkeypatch.setattr(conftest, "_ambient_emulator_at_session_start", True)
    read_fd, write_fd = _pipe_stderr(monkeypatch)
    exit_calls = []
    monkeypatch.setattr(os, "_exit", lambda code: exit_calls.append(code))

    with pytest.warns(UserWarning, match="reusing running instance at :4566"):
        _call_reachability_fixture(types.SimpleNamespace())

    os.close(write_fd)
    output = _read_pipe(read_fd)

    assert exit_calls == []
    assert "WARNING: reusing running instance at :4566" in output


def test_fixture_fails_fast_when_emulator_unreachable(monkeypatch):
    """Ambient-down: the existing fail-fast behavior is unchanged (exit 1 + error)."""
    _patch_emulator_config(monkeypatch)
    monkeypatch.setattr(
        conftest,
        "_emulator_health_error",
        lambda endpoint: "no healthy response within 30s (last error: connection refused)",
    )
    read_fd, write_fd = _pipe_stderr(monkeypatch)
    exit_calls = []
    monkeypatch.setattr(os, "_exit", lambda code: exit_calls.append(code))

    _call_reachability_fixture(types.SimpleNamespace())

    os.close(write_fd)
    output = _read_pipe(read_fd)

    assert exit_calls == [1]
    assert "ERROR: emulator not reachable" in output
    assert "run `make start`" in output
    assert "reusing running instance" not in output


def test_fixture_skips_when_aws_cloud(monkeypatch):
    """TEST_TARGET=AWS_CLOUD: neither warning nor fail-fast runs."""
    _patch_emulator_config(monkeypatch)
    monkeypatch.setattr(aws_util, "is_aws_cloud", lambda: True)
    monkeypatch.setattr(conftest, "_ambient_emulator_at_session_start", True)
    read_fd, write_fd = _pipe_stderr(monkeypatch)
    exit_calls = []
    monkeypatch.setattr(os, "_exit", lambda code: exit_calls.append(code))

    _call_reachability_fixture(types.SimpleNamespace())

    os.close(write_fd)
    output = _read_pipe(read_fd)

    assert exit_calls == []
    assert output == ""
