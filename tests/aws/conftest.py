import json
import os
import sys
import time
import urllib.error
import urllib.request
import warnings
from urllib.parse import urlparse

import pytest
from _pytest.config import Config
from localstack_snapshot.snapshots import SnapshotSession
from localstack_snapshot.snapshots.transformer import RegexTransformer

from localstack import config as localstack_config
from localstack import constants
from localstack.testing import config as test_config
from localstack.testing.snapshots.transformer_utility import (
    SNAPSHOT_BASIC_TRANSFORMER,
    SNAPSHOT_BASIC_TRANSFORMER_NEW,
    TransformerUtility,
)
from localstack.utils.aws.arns import get_partition


def pytest_configure(config: Config):
    # FIXME: note that this should be the same as in tests/integration/conftest.py since both are currently
    #  run in the same CI test step, but only one localstack instance is started for both.
    config.option.start_localstack = True
    localstack_config.FORCE_SHUTDOWN = False
    localstack_config.GATEWAY_LISTEN = localstack_config.UniqueHostAndPortList(
        [localstack_config.HostAndPort(host="0.0.0.0", port=constants.DEFAULT_PORT_EDGE)]
    )


def pytest_runtestloop(session):
    """
    This pytest plugin allows us to pre-install external dependencies that are usually lazy-loaded by the services.
    This helps us surface download issues earlier.
    This is not needed if we are running the test against an external instance, as it installs the dependencies on the
    runner running the tests.
    """
    if not session.items:
        return

    if session.config.option.collectonly:
        return

    if test_config.TEST_SKIP_LOCALSTACK_START:
        return

    from localstack.testing.aws.util import is_aws_cloud

    if is_aws_cloud() and not test_config.TEST_FORCE_LOCALSTACK_START:
        return

    # second pytest lifecycle hook (before test runner starts)
    test_init_functions = set()

    # collect test classes
    test_classes = set()
    for item in session.items:
        if item.parent and item.parent.cls:
            test_classes.add(item.parent.cls)
        # OpenSearch/Elasticsearch are pytests, not unit test classes, so we check based on the item parent's name.
        # Any pytests that rely on opensearch/elasticsearch must be special-cased by adding them to the list below
        parent_name = str(item.parent).lower()
        if any(opensearch_test in parent_name for opensearch_test in ["opensearch", "firehose"]):
            from tests.aws.services.opensearch.test_opensearch import (
                install_async as opensearch_install_async,
            )

            test_init_functions.add(opensearch_install_async)

        if any(es_test in parent_name for es_test in ["elasticsearch", "firehose"]):
            from tests.aws.services.es.test_es import install_async as es_install_async

            test_init_functions.add(es_install_async)

        if "transcribe" in parent_name:
            from tests.aws.services.transcribe.test_transcribe import (
                install_async as transcribe_install_async,
            )

            test_init_functions.add(transcribe_install_async)

    for fn in test_init_functions:
        fn()


# Note: Don't move this into testing lib
@pytest.fixture(scope="session")
def cdk_template_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "cdk_templates"))


# Note: Don't move this into testing lib
@pytest.fixture(scope="session")
def infrastructure_setup(cdk_template_path, aws_client):
    # Note: import needs to be local to avoid CDK import on every test run, which takes quite some time
    from localstack.testing.scenario.provisioning import InfraProvisioner

    def _infrastructure_setup(namespace: str, force_synth: bool | None = False) -> InfraProvisioner:
        """
        :param namespace: repo-unique identifier for this CDK app.
            A directory with this name will be created at `tests/aws/cdk_templates/<namespace>/`
        :param force_synth: set to True to always re-synth the CDK app
        :return: an instantiated CDK InfraProvisioner which can be used to deploy a CDK app
        """
        return InfraProvisioner(
            base_path=cdk_template_path,
            aws_client=aws_client,
            namespace=namespace,
            force_synth=force_synth,
            persist_output=True,
        )

    return _infrastructure_setup


@pytest.fixture(scope="function")
def snapshot(request, _snapshot_session: SnapshotSession, account_id, region_name):
    # Overwrite utility with our own => Will be refactored in the future
    _snapshot_session.transform = TransformerUtility

    _snapshot_session.add_transformer(RegexTransformer(account_id, "1" * 12), priority=2)
    _snapshot_session.add_transformer(RegexTransformer(region_name, "<region>"), priority=2)
    _snapshot_session.add_transformer(
        RegexTransformer(f"arn:{get_partition(region_name)}:", "arn:<partition>:"), priority=2
    )

    # Removes the 'x-localstack' header from all responses
    _snapshot_session.add_transformer(_snapshot_session.transform.remove_key("x-localstack"))

    # TODO: temporary to migrate to new default transformers.
    #   remove this after all exemptions are gone
    exemptions = [
        "tests/aws/services/acm",
        "tests/aws/services/apigateway",
        "tests/aws/services/cloudwatch",
        "tests/aws/services/cloudformation",
        "tests/aws/services/dynamodb",
        "tests/aws/services/events",
        "tests/aws/services/kinesis",
        "tests/aws/services/kms",
        "tests/aws/services/lambda_",
        "tests/aws/services/logs",
        "tests/aws/services/route53",
        "tests/aws/services/route53resolver",
        "tests/aws/services/s3",
        "tests/aws/services/secretsmanager",
        "tests/aws/services/ses",
        "tests/aws/services/sns",
        "tests/aws/services/stepfunctions",
        "tests/aws/services/sqs",
        "tests/aws/services/transcribe",
        "tests/aws/scenario/bookstore",
        "tests/aws/scenario/note_taking",
        "tests/aws/scenario/lambda_destination",
        "tests/aws/scenario/loan_broker",
    ]
    if any(e in request.fspath.dirname for e in exemptions):
        _snapshot_session.add_transformer(SNAPSHOT_BASIC_TRANSFORMER, priority=2)
    else:
        _snapshot_session.add_transformer(SNAPSHOT_BASIC_TRANSFORMER_NEW, priority=2)

    return _snapshot_session


def _real_stderr_fd(request) -> int | None:
    """
    Return the file descriptor of the real stderr stream.

    pytest's fd-level capture is already active when this conftest is imported and
    temporarily redirects fd 2 to a temp file, so a plain ``os.dup(2)`` would capture the
    temp file. The capture machinery keeps the original fd in
    ``FDCapture.targetfd_save``; use it so the fail-fast message reaches the terminal or
    the caller's redirect target.
    """
    try:
        from _pytest.capture import MultiCapture

        capman = request.config.pluginmanager.getplugin("capturemanager")
        global_capture = capman._global_capturing
        if isinstance(global_capture, MultiCapture) and global_capture.err is not None:
            return global_capture.err.targetfd_save
    except Exception:
        pass
    return None


# Total amount of time (in seconds) the session health check waits for the emulator to
# become reachable before failing fast. The in-process runtime takes ~20-30s to boot, but
# the ``in_memory_localstack`` plugin already blocks on the runtime ready event before any
# fixture runs, so this budget only needs to cover the (small) gap between the ready event
# and the gateway actually serving the health endpoint.
EMULATOR_HEALTH_TIMEOUT = 30


def _emulator_health_probe(endpoint: str) -> tuple[bool, str | None]:
    """
    Perform a single health probe against the emulator.

    :param endpoint: base URL of the emulator (e.g. ``http://localhost:4566``)
    :return: ``(True, None)`` if the emulator answered with HTTP 200 and a JSON body,
        otherwise ``(False, error_description)``
    """
    health_url = f"{endpoint.rstrip('/')}/_localstack/health"
    try:
        with urllib.request.urlopen(health_url, timeout=2) as response:
            if response.status != 200:
                return False, f"unexpected HTTP status {response.status}"
            json.loads(response.read().decode("utf-8"))
            return True, None
    except (OSError, ValueError) as e:
        # URLError (incl. connection refused/timeouts) is an OSError subclass
        return False, str(e)


def _emulator_health_error(endpoint: str, timeout: float = EMULATOR_HEALTH_TIMEOUT) -> str | None:
    """
    Poll the emulator health endpoint until it responds or ``timeout`` elapses.

    :param endpoint: base URL of the emulator (e.g. ``http://localhost:4566``)
    :param timeout: total time budget in seconds
    :return: ``None`` if the emulator answered with HTTP 200 and a JSON body,
        otherwise a description of the failure
    """
    deadline = time.monotonic() + timeout
    last_error = "no attempt made"
    while time.monotonic() < deadline:
        ok, last_error = _emulator_health_probe(endpoint)
        if ok:
            return None
        time.sleep(1)
    return f"no healthy response within {timeout:.0f}s (last error: {last_error})"


# Whether an emulator instance was already serving the health endpoint when the pytest
# session started — i.e. BEFORE the in-memory runtime boot attempt in
# ``pytest_runtestloop``. Set by ``pytest_sessionstart``; consumed by the
# ``_emulator_reachability_check`` fixture to warn about ambient instances.
_ambient_emulator_at_session_start: bool | None = None


def _detect_ambient_emulator(endpoint: str) -> bool:
    """
    Detect an ambient emulator instance with a single health probe.

    The suite's own in-process runtime does not boot before ``pytest_runtestloop``, so a
    health-answering emulator at session-start time is necessarily an ambient instance
    (e.g. a ``make start`` the developer already has running) that the suite would
    silently attach to instead of a fresh one.

    :param endpoint: base URL of the emulator (e.g. ``http://localhost:4566``)
    :return: ``True`` if the health endpoint answered with HTTP 200 and a JSON body
    """
    ok, _ = _emulator_health_probe(endpoint)
    return ok


def _warn_reusing_instance(request, endpoint: str) -> None:
    """
    Emit a loud, capture-surviving warning when an ambient emulator instance was already
    serving before the suite started, so runs against it are not mistaken for runs
    against a fresh instance.
    """
    port = urlparse(endpoint).port or constants.DEFAULT_PORT_EDGE
    message = (
        f"reusing running instance at :{port} — integration tests will run against "
        f"the ambient emulator and may mutate its state"
    )
    # pytest captures stderr by default, so also surface the warning through the real
    # stderr fd (same mechanism as the fail-fast message) — it shows up in plain
    # ``pytest -q`` output before/while the tests run. warnings.warn additionally puts
    # it into the warnings summary.
    warnings.warn(message, UserWarning, stacklevel=2)
    line = f"\nWARNING: {message}\n"
    stderr_fd = _real_stderr_fd(request)
    if stderr_fd is not None:
        os.write(stderr_fd, line.encode())
    else:
        sys.__stderr__.write(line)
        sys.__stderr__.flush()


@pytest.hookimpl()
def pytest_sessionstart(session):
    """
    Detect an ambient emulator instance BEFORE the in-process runtime boot attempt.

    The ``in_memory_localstack`` plugin boots the suite's own runtime in
    ``pytest_runtestloop``, i.e. after this hook, so a healthy emulator at this point is
    necessarily an ambient instance (e.g. a ``make start`` the developer has running).
    The result is consumed by ``_emulator_reachability_check`` to warn that the suite
    will attach to (and may mutate) that instance instead of a fresh one.
    """
    global _ambient_emulator_at_session_start

    from localstack.testing.aws.util import is_aws_cloud

    if is_aws_cloud():
        _ambient_emulator_at_session_start = False
        return

    endpoint = test_config.TEST_AWS_ENDPOINT_URL or localstack_config.internal_service_url()
    _ambient_emulator_at_session_start = _detect_ambient_emulator(endpoint)


@pytest.fixture(scope="session", autouse=True)
def _emulator_reachability_check(request):
    """
    Fail fast when the emulator is not reachable, instead of letting the boto3 clients sit
    in connection-retry loops for minutes (observed: pytest still running at 229s, >140s
    after the runtime was terminated mid-run).

    Runs after the in-process runtime boot attempt (the ``in_memory_localstack`` plugin
    blocks in ``pytest_runtestloop`` until the runtime signals ready), so the ~20-30s boot
    time of the in-process runtime is tolerated. The check only fails when the health
    endpoint genuinely never answers — e.g. a zombie/foreign listener on :4566 makes the
    runtime ready-monitor report "Ready." while the gateway is not actually serving.

    Additionally, if an ambient emulator instance was already serving the health endpoint
    when the session started (detected by ``pytest_sessionstart``, before any in-process
    boot attempt), a loud warning is emitted: the suite will attach to — and may mutate —
    that pre-existing instance instead of a fresh one.

    Skipped when running against real AWS (``TEST_TARGET=AWS_CLOUD``).
    """
    from localstack.testing.aws.util import is_aws_cloud

    if is_aws_cloud():
        return

    endpoint = test_config.TEST_AWS_ENDPOINT_URL or localstack_config.internal_service_url()
    error = _emulator_health_error(endpoint)
    if error:
        # NOTE: we deliberately do not use pytest.exit() here. The in-process runtime runs
        # in a non-daemon thread, and when the emulator is unreachable its shutdown hooks
        # can block against the dead endpoint (and the gateway thread may never terminate),
        # which would keep the pytest process alive long past the fail-fast deadline.
        message = (
            f"emulator not reachable at {endpoint} — run `make start` before running this "
            f"suite ({error})"
        )
        stderr_fd = _real_stderr_fd(request)
        if stderr_fd is not None:
            os.write(stderr_fd, f"\nERROR: {message}\n".encode())
        else:
            sys.__stderr__.write(f"\nERROR: {message}\n")
            sys.__stderr__.flush()
        os._exit(1)

    if _ambient_emulator_at_session_start:
        _warn_reusing_instance(request, endpoint)


@pytest.hookimpl()
def pytest_addhooks(pluginmanager):
    try:
        # This is only relevant when running Community Tests against Pro pipeline
        from localstack.pro.core.testing.pytest.store import StoreSerializationCheckerPlugin

        from localstack.testing.aws.util import is_aws_cloud

        if not test_config.TEST_SKIP_LOCALSTACK_START and not is_aws_cloud():
            # this directly accesses LocalStack state in memory, so it is not worth running in tests against external
            # instances
            pluginmanager.register(StoreSerializationCheckerPlugin(with_pickle=False))
    except ImportError:
        pass
