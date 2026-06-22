"""Integration test for Bedrock Runtime — real LocalStack store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'bedrock-runtime')

# Load the models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

BedrockRuntimeStore = models_mod.BedrockRuntimeStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
ValidationException = models_mod.ValidationException
AccessDeniedException = models_mod.AccessDeniedException
ThrottlingException = models_mod.ThrottlingException
InternalServerException = models_mod.InternalServerException
ServiceQuotaExceededException = models_mod.ServiceQuotaExceededException


def _load_handler(op_name, globals_inject=None):
    """Load a generated .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ValidationException = ValidationException
    mod.AccessDeniedException = AccessDeniedException
    mod.ThrottlingException = ThrottlingException
    mod.InternalServerException = InternalServerException
    mod.ServiceQuotaExceededException = ServiceQuotaExceededException
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    # Find the handler function
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestStartAsyncInvoke:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def test_start_async_invoke_happy_path(self):
        """Start a new async invoke job and verify it's tracked."""
        handler = _load_handler('StartAsyncInvoke')
        req = {
            "modelId": "anthropic.claude-3-sonnet",
            "modelInput": {"prompt": "Hello"},
            "outputDataConfig": {"s3OutputDataConfig": {"s3Uri": "s3://bucket/output/"}},
        }
        resp = handler(self.store, req)
        assert resp is not None
        assert "invocationArn" in resp
        assert resp["status"] == "InProgress"
        assert resp["modelInput"] == {"prompt": "Hello"}

    def test_start_async_invoke_missing_required(self):
        """Missing modelId raises KeyError."""
        handler = _load_handler('StartAsyncInvoke')
        with pytest.raises(KeyError):
            handler(self.store, {})


class TestGetAsyncInvoke:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def _create_job(self):
        handler = _load_handler('StartAsyncInvoke')
        return handler(self.store, {
            "modelId": "anthropic.claude-3-sonnet",
            "modelInput": {"prompt": "test"},
            "outputDataConfig": {"s3OutputDataConfig": {"s3Uri": "s3://b/o/"}},
        })

    def test_get_async_invoke_happy_path(self):
        """Create a job, then get it by ARN."""
        created = self._create_job()
        arn = created["invocationArn"]
        handler = _load_handler('GetAsyncInvoke')
        resp = handler(self.store, {"invocationArn": arn})
        assert resp["invocationArn"] == arn
        assert resp["status"] == "InProgress"

    def test_get_async_invoke_nonexistent(self):
        """Get nonexistent job raises ResourceNotFoundException."""
        handler = _load_handler('GetAsyncInvoke')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"invocationArn": "nonexistent"})


class TestListAsyncInvokes:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def _create_job(self, model_id="anthropic.claude-3-sonnet"):
        handler = _load_handler('StartAsyncInvoke')
        return handler(self.store, {
            "modelId": model_id,
            "modelInput": {"prompt": "test"},
            "outputDataConfig": {"s3OutputDataConfig": {"s3Uri": "s3://b/o/"}},
        })

    def test_list_async_invokes_empty(self):
        """List when store is empty returns empty list."""
        handler = _load_handler('ListAsyncInvokes')
        resp = handler(self.store, {})
        assert resp["asyncInvokeSummaries"] == []
        assert resp["nextToken"] is None

    def test_list_async_invokes_with_jobs(self):
        """List returns created jobs."""
        self._create_job()
        self._create_job()
        handler = _load_handler('ListAsyncInvokes')
        resp = handler(self.store, {})
        assert len(resp["asyncInvokeSummaries"]) == 2

    def test_list_async_invokes_status_filter(self):
        """List with status filter."""
        self._create_job()
        handler = _load_handler('ListAsyncInvokes')
        resp = handler(self.store, {"statusEquals": "InProgress"})
        assert len(resp["asyncInvokeSummaries"]) == 1
        resp = handler(self.store, {"statusEquals": "Completed"})
        assert len(resp["asyncInvokeSummaries"]) == 0


class TestConverse:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def test_converse_happy_path(self):
        """Converse returns a mock response."""
        handler = _load_handler('Converse')
        resp = handler(self.store, {
            "modelId": "anthropic.claude-3-sonnet",
            "messages": [{"role": "user", "content": [{"text": "Hello"}]}],
        })
        assert "output" in resp
        assert "stopReason" in resp
        assert resp["stopReason"] == "end_turn"
        assert resp["usage"]["totalTokens"] == 25

    def test_converse_missing_model(self):
        """Handler gracefully handles empty request (mock response)."""
        handler = _load_handler('Converse')
        resp = handler(self.store, {})
        assert "output" in resp
        assert resp["stopReason"] == "end_turn"


class TestInvokeModel:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def test_invoke_model_happy_path(self):
        """InvokeModel returns mock response."""
        handler = _load_handler('InvokeModel')
        resp = handler(self.store, {
            "modelId": "anthropic.claude-3-sonnet",
            "body": "{}",
            "contentType": "application/json",
        })
        assert "body" in resp
        assert "contentType" in resp
        assert resp["contentType"] == "application/json"

    def test_invoke_model_missing_model(self):
        """Handler gracefully handles empty request (mock response)."""
        handler = _load_handler('InvokeModel')
        resp = handler(self.store, {})
        assert "body" in resp


class TestCountTokens:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def test_count_tokens_happy_path(self):
        """CountTokens returns estimated count."""
        handler = _load_handler('CountTokens')
        resp = handler(self.store, {
            "modelId": "anthropic.claude-3-sonnet",
            "input": {"text": "Hello world"},
        })
        assert "inputTokens" in resp
        assert resp["inputTokens"] > 0

    def test_count_tokens_missing_model(self):
        """Handler gracefully handles empty request (returns 1 token for empty)."""
        handler = _load_handler('CountTokens')
        resp = handler(self.store, {})
        assert resp["inputTokens"] >= 0


class TestApplyGuardrail:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def test_apply_guardrail_happy_path(self):
        """ApplyGuardrail returns mock response."""
        handler = _load_handler('ApplyGuardrail')
        resp = handler(self.store, {
            "guardrailIdentifier": "gr-123",
            "guardrailVersion": "1",
            "source": "INPUT",
            "content": [{"text": {"text": "Hello"}}],
        })
        assert "action" in resp
        assert resp["action"] == "NONE"
        assert "assessments" in resp


class TestConverseStream:

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockRuntimeStore()
        return self._store

    def test_converse_stream_happy_path(self):
        """ConverseStream returns stream events."""
        handler = _load_handler('ConverseStream')
        resp = handler(self.store, {
            "modelId": "anthropic.claude-3-sonnet",
            "messages": [{"role": "user", "content": [{"text": "Hi"}]}],
        })
        assert "stream" in resp
        assert len(resp["stream"]) > 0
