import json

from tests.aws.conftest import _emulator_health_error


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
