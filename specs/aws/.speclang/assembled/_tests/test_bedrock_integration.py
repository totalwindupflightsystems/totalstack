"""Integration test for Bedrock — real store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'bedrock')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out all needed names
BedrockStore = models_mod.BedrockStore
FoundationModelDetails = models_mod.FoundationModelDetails
GuardrailRecord = models_mod.GuardrailRecord
ModelCustomizationJobRecord = models_mod.ModelCustomizationJobRecord
ProvisionedModelRecord = models_mod.ProvisionedModelRecord
ResourceNotFoundException = models_mod.ResourceNotFoundException
AccessDeniedException = models_mod.AccessDeniedException
ValidationException = models_mod.ValidationException
ConflictException = models_mod.ConflictException
InternalServerException = models_mod.InternalServerException
ThrottlingException = models_mod.ThrottlingException
TooManyTagsException = models_mod.TooManyTagsException
ServiceQuotaExceededException = models_mod.ServiceQuotaExceededException


def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject ALL exception classes
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.AccessDeniedException = AccessDeniedException
    mod.ValidationException = ValidationException
    mod.ConflictException = ConflictException
    mod.InternalServerException = InternalServerException
    mod.ThrottlingException = ThrottlingException
    mod.TooManyTagsException = TooManyTagsException
    mod.ServiceQuotaExceededException = ServiceQuotaExceededException
    # Inject ALL record classes
    mod.FoundationModelDetails = FoundationModelDetails
    mod.GuardrailRecord = GuardrailRecord
    mod.ModelCustomizationJobRecord = ModelCustomizationJobRecord
    mod.ProvisionedModelRecord = ProvisionedModelRecord
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


# ═════════════════════════════════════════════════════════════════════
# Foundation Models
# ═════════════════════════════════════════════════════════════════════

class TestFoundationModels:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockStore()
        return self._store

    def test_get_foundation_model_happy(self):
        handler = _load_handler('GetFoundationModel')
        resp = handler(self.store, {"modelIdentifier": "anthropic.claude-v2"})
        assert resp["modelDetails"]["modelId"] == "anthropic.claude-v2"
        assert resp["modelDetails"]["providerName"] == "Anthropic"

    def test_get_foundation_model_not_found(self):
        handler = _load_handler('GetFoundationModel')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"modelIdentifier": "nonexistent.model"})

    def test_list_foundation_models_all(self):
        handler = _load_handler('ListFoundationModels')
        resp = handler(self.store, {})
        assert len(resp["modelSummaries"]) >= 3

    def test_list_foundation_models_by_provider(self):
        handler = _load_handler('ListFoundationModels')
        resp = handler(self.store, {"byProvider": "Anthropic"})
        assert len(resp["modelSummaries"]) == 2
        for m in resp["modelSummaries"]:
            assert m["providerName"] == "Anthropic"

    def test_get_foundation_model_availability(self):
        handler = _load_handler('GetFoundationModelAvailability')
        resp = handler(self.store, {"modelId": "anthropic.claude-v2"})
        assert resp["modelId"] == "anthropic.claude-v2"
        assert "authorizationStatus" in resp


# ═════════════════════════════════════════════════════════════════════
# Guardrails
# ═════════════════════════════════════════════════════════════════════

class TestGuardrails:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockStore()
        return self._store

    def test_create_guardrail_happy(self):
        handler = _load_handler('CreateGuardrail')
        resp = handler(self.store, {
            "name": "test-guardrail",
            "blockedInputMessaging": "Blocked input message",
            "blockedOutputsMessaging": "Blocked output message",
            "description": "Test guardrail"
        })
        assert resp["guardrailId"]
        assert resp["guardrailArn"]
        assert resp["version"] == "DRAFT"

    def test_create_guardrail_with_tags(self):
        handler = _load_handler('CreateGuardrail')
        resp = handler(self.store, {
            "name": "tagged-guardrail",
            "blockedInputMessaging": "Blocked",
            "blockedOutputsMessaging": "Blocked",
            "tags": [{"key": "env", "value": "test"}, {"key": "team", "value": "bedrock"}]
        })
        assert resp["guardrailId"]

        # Verify tags through ListTagsForResource
        tag_handler = _load_handler('ListTagsForResource')
        tag_resp = tag_handler(self.store, {"resourceARN": resp["guardrailArn"]})
        assert len(tag_resp["tags"]) == 2

    def test_get_guardrail_happy(self):
        create = _load_handler('CreateGuardrail')
        created = create(self.store, {
            "name": "get-me",
            "blockedInputMessaging": "Blocked input",
            "blockedOutputsMessaging": "Blocked output",
        })
        get_handler = _load_handler('GetGuardrail')
        resp = get_handler(self.store, {"guardrailIdentifier": created["guardrailId"]})
        assert resp["name"] == "get-me"
        assert resp["guardrailId"] == created["guardrailId"]

    def test_get_guardrail_not_found(self):
        handler = _load_handler('GetGuardrail')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"guardrailIdentifier": "gr-nonexistent"})

    def test_update_guardrail_happy(self):
        create = _load_handler('CreateGuardrail')
        created = create(self.store, {
            "name": "update-me",
            "blockedInputMessaging": "Blocked input",
            "blockedOutputsMessaging": "Blocked output",
        })
        update = _load_handler('UpdateGuardrail')
        resp = update(self.store, {
            "guardrailIdentifier": created["guardrailId"],
            "name": "updated-name",
            "blockedInputMessaging": "Updated blocked input",
            "blockedOutputsMessaging": "Updated blocked output",
        })
        assert resp["guardrailId"] == created["guardrailId"]
        assert resp["version"] == "DRAFT"

        get_handler = _load_handler('GetGuardrail')
        updated = get_handler(self.store, {"guardrailIdentifier": created["guardrailId"]})
        assert updated["name"] == "updated-name"

    def test_delete_guardrail_happy(self):
        create = _load_handler('CreateGuardrail')
        created = create(self.store, {
            "name": "delete-me",
            "blockedInputMessaging": "Blocked",
            "blockedOutputsMessaging": "Blocked",
        })
        delete_handler = _load_handler('DeleteGuardrail')
        delete_handler(self.store, {"guardrailIdentifier": created["guardrailId"]})
        with pytest.raises(ResourceNotFoundException):
            get_handler = _load_handler('GetGuardrail')
            get_handler(self.store, {"guardrailIdentifier": created["guardrailId"]})

    def test_create_guardrail_version(self):
        create = _load_handler('CreateGuardrail')
        created = create(self.store, {
            "name": "versioned",
            "blockedInputMessaging": "Blocked",
            "blockedOutputsMessaging": "Blocked",
        })
        version_handler = _load_handler('CreateGuardrailVersion')
        resp = version_handler(self.store, {
            "guardrailIdentifier": created["guardrailId"],
            "description": "Version 1",
        })
        assert resp["guardrailId"] == created["guardrailId"]
        assert resp["version"] is not None

    def test_list_guardrails_empty(self):
        store = BedrockStore()
        handler = _load_handler('ListGuardrails')
        resp = handler(store, {})
        assert resp["guardrails"] == []

    def test_list_guardrails_with_items(self):
        create = _load_handler('CreateGuardrail')
        create(self.store, {
            "name": "gr1",
            "blockedInputMessaging": "Blocked",
            "blockedOutputsMessaging": "Blocked",
        })
        create(self.store, {
            "name": "gr2",
            "blockedInputMessaging": "Blocked",
            "blockedOutputsMessaging": "Blocked",
        })
        handler = _load_handler('ListGuardrails')
        resp = handler(self.store, {})
        assert len(resp["guardrails"]) == 2


# ═════════════════════════════════════════════════════════════════════
# Model Customization Jobs
# ═════════════════════════════════════════════════════════════════════

class TestModelCustomizationJobs:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockStore()
        return self._store

    def test_create_job_happy(self):
        handler = _load_handler('CreateModelCustomizationJob')
        resp = handler(self.store, {
            "jobName": "my-customization-job",
            "customModelName": "my-custom-model",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "baseModelIdentifier": "anthropic.claude-v2",
            "trainingDataConfig": {"s3Uri": "s3://bucket/train/"},
            "outputDataConfig": {"s3Uri": "s3://bucket/output/"},
        })
        assert resp["jobArn"]

    def test_get_job_happy(self):
        create = _load_handler('CreateModelCustomizationJob')
        created = create(self.store, {
            "jobName": "get-job",
            "customModelName": "get-model",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "baseModelIdentifier": "meta.llama3-70b-instruct-v1:0",
            "trainingDataConfig": {"s3Uri": "s3://bucket/train/"},
            "outputDataConfig": {"s3Uri": "s3://bucket/output/"},
        })
        get_handler = _load_handler('GetModelCustomizationJob')
        resp = get_handler(self.store, {"jobIdentifier": created["jobArn"]})
        assert resp["jobName"] == "get-job"
        assert resp["status"] == "InProgress"

    def test_get_job_not_found(self):
        handler = _load_handler('GetModelCustomizationJob')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"jobIdentifier": "arn:aws:bedrock:us-east-1:000000000000:nonexistent"})

    def test_stop_job(self):
        create = _load_handler('CreateModelCustomizationJob')
        created = create(self.store, {
            "jobName": "stop-me",
            "customModelName": "stop-model",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "baseModelIdentifier": "meta.llama3-70b-instruct-v1:0",
            "trainingDataConfig": {"s3Uri": "s3://bucket/train/"},
            "outputDataConfig": {"s3Uri": "s3://bucket/output/"},
        })
        stop_handler = _load_handler('StopModelCustomizationJob')
        stop_handler(self.store, {"jobIdentifier": created["jobArn"]})
        get_handler = _load_handler('GetModelCustomizationJob')
        resp = get_handler(self.store, {"jobIdentifier": created["jobArn"]})
        assert resp["status"] == "Stopping"

    def test_list_jobs_empty(self):
        store = BedrockStore()
        handler = _load_handler('ListModelCustomizationJobs')
        resp = handler(store, {})
        assert resp["modelCustomizationJobSummaries"] == []

    def test_list_jobs_with_items(self):
        create = _load_handler('CreateModelCustomizationJob')
        create(self.store, {
            "jobName": "job-1",
            "customModelName": "model-1",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "baseModelIdentifier": "anthropic.claude-v2",
            "trainingDataConfig": {"s3Uri": "s3://bucket/train/"},
            "outputDataConfig": {"s3Uri": "s3://bucket/output/"},
        })
        create(self.store, {
            "jobName": "job-2",
            "customModelName": "model-2",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "baseModelIdentifier": "meta.llama3-70b-instruct-v1:0",
            "trainingDataConfig": {"s3Uri": "s3://bucket/train/"},
            "outputDataConfig": {"s3Uri": "s3://bucket/output/"},
        })
        handler = _load_handler('ListModelCustomizationJobs')
        resp = handler(self.store, {})
        assert len(resp["modelCustomizationJobSummaries"]) == 2

    def test_list_jobs_by_status(self):
        create = _load_handler('CreateModelCustomizationJob')
        create(self.store, {
            "jobName": "in-progress-job",
            "customModelName": "ip-model",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "baseModelIdentifier": "anthropic.claude-v2",
            "trainingDataConfig": {"s3Uri": "s3://bucket/train/"},
            "outputDataConfig": {"s3Uri": "s3://bucket/output/"},
        })
        handler = _load_handler('ListModelCustomizationJobs')
        resp = handler(self.store, {"statusEquals": "InProgress"})
        assert len(resp["modelCustomizationJobSummaries"]) == 1


# ═════════════════════════════════════════════════════════════════════
# Provisioned Model Throughput
# ═════════════════════════════════════════════════════════════════════

class TestProvisionedModelThroughput:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockStore()
        return self._store

    def test_create_throughput_happy(self):
        handler = _load_handler('CreateProvisionedModelThroughput')
        resp = handler(self.store, {
            "modelUnits": 1,
            "provisionedModelName": "my-provisioned-model",
            "modelId": "anthropic.claude-v2",
        })
        assert resp["provisionedModelArn"]

    def test_get_throughput_happy(self):
        create = _load_handler('CreateProvisionedModelThroughput')
        created = create(self.store, {
            "modelUnits": 2,
            "provisionedModelName": "get-throughput",
            "modelId": "anthropic.claude-3-sonnet-20240229-v1:0",
        })
        get_handler = _load_handler('GetProvisionedModelThroughput')
        resp = get_handler(self.store, {"provisionedModelId": created["provisionedModelArn"].split("/")[-1]})
        assert resp["provisionedModelName"] == "get-throughput"
        assert resp["modelUnits"] == 2

    def test_get_throughput_not_found(self):
        handler = _load_handler('GetProvisionedModelThroughput')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"provisionedModelId": "nonexistent"})

    def test_update_throughput(self):
        create = _load_handler('CreateProvisionedModelThroughput')
        created = create(self.store, {
            "modelUnits": 1,
            "provisionedModelName": "update-throughput",
            "modelId": "anthropic.claude-v2",
        })
        model_id = created["provisionedModelArn"].split("/")[-1]
        update = _load_handler('UpdateProvisionedModelThroughput')
        update(self.store, {
            "provisionedModelId": model_id,
            "desiredProvisionedModelName": "updated-throughput-name",
        })
        get_handler = _load_handler('GetProvisionedModelThroughput')
        resp = get_handler(self.store, {"provisionedModelId": model_id})
        assert resp["provisionedModelName"] == "updated-throughput-name"

    def test_delete_throughput(self):
        create = _load_handler('CreateProvisionedModelThroughput')
        created = create(self.store, {
            "modelUnits": 1,
            "provisionedModelName": "delete-throughput",
            "modelId": "anthropic.claude-v2",
        })
        model_id = created["provisionedModelArn"].split("/")[-1]
        delete_handler = _load_handler('DeleteProvisionedModelThroughput')
        delete_handler(self.store, {"provisionedModelId": model_id})
        with pytest.raises(ResourceNotFoundException):
            get_handler = _load_handler('GetProvisionedModelThroughput')
            get_handler(self.store, {"provisionedModelId": model_id})

    def test_list_throughputs_empty(self):
        store = BedrockStore()
        handler = _load_handler('ListProvisionedModelThroughputs')
        resp = handler(store, {})
        assert resp["provisionedModelSummaries"] == []

    def test_list_throughputs_with_items(self):
        create = _load_handler('CreateProvisionedModelThroughput')
        create(self.store, {
            "modelUnits": 1,
            "provisionedModelName": "pt-1",
            "modelId": "anthropic.claude-v2",
        })
        create(self.store, {
            "modelUnits": 2,
            "provisionedModelName": "pt-2",
            "modelId": "anthropic.claude-3-sonnet-20240229-v1:0",
        })
        handler = _load_handler('ListProvisionedModelThroughputs')
        resp = handler(self.store, {})
        assert len(resp["provisionedModelSummaries"]) == 2


# ═════════════════════════════════════════════════════════════════════
# Tags
# ═════════════════════════════════════════════════════════════════════

class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockStore()
        return self._store

    def test_tag_resource(self):
        handler = _load_handler('TagResource')
        handler(self.store, {
            "resourceARN": "arn:aws:bedrock:us-east-1:000000000000:guardrail/gr-123",
            "tags": [{"key": "env", "value": "prod"}, {"key": "owner", "value": "team-a"}],
        })
        list_handler = _load_handler('ListTagsForResource')
        resp = list_handler(self.store, {
            "resourceARN": "arn:aws:bedrock:us-east-1:000000000000:guardrail/gr-123"
        })
        assert len(resp["tags"]) == 2
        keys = {t["key"] for t in resp["tags"]}
        assert keys == {"env", "owner"}

    def test_untag_resource(self):
        handler = _load_handler('TagResource')
        handler(self.store, {
            "resourceARN": "arn:aws:bedrock:us-east-1:000000000000:guardrail/gr-456",
            "tags": [{"key": "env", "value": "test"}, {"key": "temp", "value": "yes"}],
        })
        untag_handler = _load_handler('UntagResource')
        untag_handler(self.store, {
            "resourceARN": "arn:aws:bedrock:us-east-1:000000000000:guardrail/gr-456",
            "tagKeys": ["temp"],
        })
        list_handler = _load_handler('ListTagsForResource')
        resp = list_handler(self.store, {
            "resourceARN": "arn:aws:bedrock:us-east-1:000000000000:guardrail/gr-456"
        })
        assert len(resp["tags"]) == 1
        assert resp["tags"][0]["key"] == "env"

    def test_list_tags_empty(self):
        handler = _load_handler('ListTagsForResource')
        resp = handler(self.store, {
            "resourceARN": "arn:aws:bedrock:us-east-1:000000000000:guardrail/gr-none"
        })
        assert resp["tags"] == []
