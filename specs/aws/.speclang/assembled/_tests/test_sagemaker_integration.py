"""Integration tests for SageMaker — real store with 4 entities, 18 handlers."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "sagemaker")

# ── Load models.code.py dynamically ─────────────────────────────────
models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(SERVICE_DIR, "models.code.py")
)
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

SageMakerStore = models_mod.SageMakerStore
TrainingJobRecord = models_mod.TrainingJobRecord
ModelRecord = models_mod.ModelRecord
EndpointConfigRecord = models_mod.EndpointConfigRecord
EndpointRecord = models_mod.EndpointRecord
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
ResourceLimitExceededException = models_mod.ResourceLimitExceededException
ValidationException = models_mod.ValidationException

# ── Handler loader ──────────────────────────────────────────────────
def _load_handler(op_name):
    """Load a generated .code.py handler — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    mod.ResourceLimitExceededException = ResourceLimitExceededException
    mod.ValidationException = ValidationException
    # Inject record classes
    mod.TrainingJobRecord = TrainingJobRecord
    mod.ModelRecord = ModelRecord
    mod.EndpointConfigRecord = EndpointConfigRecord
    mod.EndpointRecord = EndpointRecord
    # Standard library injections
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {"dataclass", "time", "uuid", "<lambda>"}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith("_")
                and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler found in {op_name}.code.py")


# ═══════════════════════════════════════════════════════════════════
# TrainingJob Tests
# ═══════════════════════════════════════════════════════════════════

class TestTrainingJob:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SageMakerStore()
        return self._store

    def test_create_training_job_happy(self):
        handler = _load_handler("create-training-job")
        resp = handler(self.store, {
            "TrainingJobName": "my-train-job",
            "RoleArn": "arn:aws:iam::000000000000:role/SageMakerRole",
            "OutputDataConfig": {"S3OutputPath": "s3://bucket/output"},
            "AlgorithmSpecification": {
                "TrainingImage": "image.dkr.ecr.us-east-1.amazonaws.com/xgboost:1",
                "TrainingInputMode": "File",
            },
            "ResourceConfig": {
                "InstanceType": "ml.m5.large",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10,
            },
            "StoppingCondition": {"MaxRuntimeInSeconds": 3600},
        })
        assert resp["TrainingJobName"] == "my-train-job"
        assert "TrainingJobArn" in resp
        assert resp["TrainingJobStatus"] == "InProgress"

    def test_create_training_job_duplicate(self):
        handler = _load_handler("create-training-job")
        req = {
            "TrainingJobName": "dup-job",
            "RoleArn": "arn:aws:iam::000000000000:role/SM",
            "OutputDataConfig": {"S3OutputPath": "s3://b/o"},
            "AlgorithmSpecification": {
                "TrainingImage": "img",
                "TrainingInputMode": "File",
            },
            "ResourceConfig": {
                "InstanceType": "ml.m5.large",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10,
            },
            "StoppingCondition": {"MaxRuntimeInSeconds": 3600},
        }
        handler(self.store, req)
        with pytest.raises(ResourceInUseException):
            handler(self.store, req)

    def test_describe_training_job_happy(self):
        create = _load_handler("create-training-job")
        describe = _load_handler("describe-training-job")
        create(self.store, {
            "TrainingJobName": "desc-test-job",
            "RoleArn": "arn:aws:iam::000000000000:role/SM",
            "OutputDataConfig": {"S3OutputPath": "s3://b/o"},
            "AlgorithmSpecification": {
                "TrainingImage": "img",
                "TrainingInputMode": "File",
            },
            "ResourceConfig": {
                "InstanceType": "ml.m5.large",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10,
            },
            "StoppingCondition": {"MaxRuntimeInSeconds": 3600},
        })
        resp = describe(self.store, {"TrainingJobName": "desc-test-job"})
        assert resp["TrainingJobName"] == "desc-test-job"
        assert resp["TrainingJobStatus"] == "InProgress"

    def test_describe_training_job_not_found(self):
        handler = _load_handler("describe-training-job")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"TrainingJobName": "nonexistent"})

    def test_list_training_jobs(self):
        create = _load_handler("create-training-job")
        lst = _load_handler("list-training-jobs")
        base = {
            "RoleArn": "arn:aws:iam::000000000000:role/SM",
            "OutputDataConfig": {"S3OutputPath": "s3://b/o"},
            "AlgorithmSpecification": {
                "TrainingImage": "img",
                "TrainingInputMode": "File",
            },
            "ResourceConfig": {
                "InstanceType": "ml.m5.large",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10,
            },
            "StoppingCondition": {"MaxRuntimeInSeconds": 3600},
        }
        create(self.store, {**base, "TrainingJobName": "job-a"})
        create(self.store, {**base, "TrainingJobName": "job-b"})
        resp = lst(self.store, {})
        assert len(resp["TrainingJobSummaries"]) >= 2

    def test_delete_training_job(self):
        create = _load_handler("create-training-job")
        delete = _load_handler("delete-training-job")
        describe = _load_handler("describe-training-job")
        create(self.store, {
            "TrainingJobName": "to-delete",
            "RoleArn": "arn:aws:iam::000000000000:role/SM",
            "OutputDataConfig": {"S3OutputPath": "s3://b/o"},
            "AlgorithmSpecification": {
                "TrainingImage": "img",
                "TrainingInputMode": "File",
            },
            "ResourceConfig": {
                "InstanceType": "ml.m5.large",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10,
            },
            "StoppingCondition": {"MaxRuntimeInSeconds": 3600},
        })
        delete(self.store, {"TrainingJobName": "to-delete"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"TrainingJobName": "to-delete"})

    def test_delete_training_job_not_found(self):
        handler = _load_handler("delete-training-job")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"TrainingJobName": "nonexistent"})

    def test_stop_training_job(self):
        create = _load_handler("create-training-job")
        stop = _load_handler("stop-training-job")
        describe = _load_handler("describe-training-job")
        create(self.store, {
            "TrainingJobName": "to-stop",
            "RoleArn": "arn:aws:iam::000000000000:role/SM",
            "OutputDataConfig": {"S3OutputPath": "s3://b/o"},
            "AlgorithmSpecification": {
                "TrainingImage": "img",
                "TrainingInputMode": "File",
            },
            "ResourceConfig": {
                "InstanceType": "ml.m5.large",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10,
            },
            "StoppingCondition": {"MaxRuntimeInSeconds": 3600},
        })
        stop(self.store, {"TrainingJobName": "to-stop"})
        resp = describe(self.store, {"TrainingJobName": "to-stop"})
        assert resp["TrainingJobStatus"] == "Stopped"

    def test_stop_training_job_not_found(self):
        handler = _load_handler("stop-training-job")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"TrainingJobName": "nonexistent"})


# ═══════════════════════════════════════════════════════════════════
# Model Tests
# ═══════════════════════════════════════════════════════════════════

class TestModel:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SageMakerStore()
        return self._store

    def test_create_model_happy(self):
        handler = _load_handler("create-model")
        resp = handler(self.store, {
            "ModelName": "my-model",
            "PrimaryContainer": {
                "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
            },
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/SM",
        })
        assert resp["ModelName"] == "my-model"
        assert "ModelArn" in resp

    def test_create_model_duplicate(self):
        handler = _load_handler("create-model")
        req = {
            "ModelName": "dup-model",
            "PrimaryContainer": {
                "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
            },
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/SM",
        }
        handler(self.store, req)
        with pytest.raises(ResourceInUseException):
            handler(self.store, req)

    def test_describe_model_happy(self):
        create = _load_handler("create-model")
        describe = _load_handler("describe-model")
        create(self.store, {
            "ModelName": "desc-model",
            "PrimaryContainer": {
                "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
            },
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/SM",
        })
        resp = describe(self.store, {"ModelName": "desc-model"})
        assert resp["ModelName"] == "desc-model"

    def test_describe_model_not_found(self):
        handler = _load_handler("describe-model")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"ModelName": "nonexistent"})

    def test_list_models(self):
        create = _load_handler("create-model")
        lst = _load_handler("list-models")
        base = {
            "PrimaryContainer": {
                "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
            },
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/SM",
        }
        create(self.store, {**base, "ModelName": "model-a"})
        create(self.store, {**base, "ModelName": "model-b"})
        resp = lst(self.store, {})
        assert len(resp["Models"]) >= 2

    def test_delete_model(self):
        create = _load_handler("create-model")
        delete = _load_handler("delete-model")
        describe = _load_handler("describe-model")
        create(self.store, {
            "ModelName": "to-delete",
            "PrimaryContainer": {
                "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
            },
            "ExecutionRoleArn": "arn:aws:iam::000000000000:role/SM",
        })
        delete(self.store, {"ModelName": "to-delete"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"ModelName": "to-delete"})

    def test_delete_model_not_found(self):
        handler = _load_handler("delete-model")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"ModelName": "nonexistent"})


# ═══════════════════════════════════════════════════════════════════
# EndpointConfig Tests
# ═══════════════════════════════════════════════════════════════════

class TestEndpointConfig:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SageMakerStore()
        return self._store

    def test_create_endpoint_config_happy(self):
        handler = _load_handler("create-endpoint-config")
        resp = handler(self.store, {
            "EndpointConfigName": "my-config",
            "ProductionVariants": [{
                "VariantName": "variant-1",
                "ModelName": "my-model",
                "InstanceType": "ml.m5.large",
                "InitialInstanceCount": 1,
            }],
        })
        assert resp["EndpointConfigName"] == "my-config"
        assert "EndpointConfigArn" in resp

    def test_create_endpoint_config_duplicate(self):
        handler = _load_handler("create-endpoint-config")
        req = {
            "EndpointConfigName": "dup-config",
            "ProductionVariants": [{
                "VariantName": "v1",
                "ModelName": "m",
                "InstanceType": "ml.m5.large",
                "InitialInstanceCount": 1,
            }],
        }
        handler(self.store, req)
        with pytest.raises(ResourceInUseException):
            handler(self.store, req)

    def test_describe_endpoint_config_happy(self):
        create = _load_handler("create-endpoint-config")
        describe = _load_handler("describe-endpoint-config")
        create(self.store, {
            "EndpointConfigName": "desc-config",
            "ProductionVariants": [{
                "VariantName": "v1",
                "ModelName": "m",
                "InstanceType": "ml.m5.large",
                "InitialInstanceCount": 1,
            }],
        })
        resp = describe(self.store, {"EndpointConfigName": "desc-config"})
        assert resp["EndpointConfigName"] == "desc-config"

    def test_describe_endpoint_config_not_found(self):
        handler = _load_handler("describe-endpoint-config")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"EndpointConfigName": "nonexistent"})

    def test_list_endpoint_configs(self):
        create = _load_handler("create-endpoint-config")
        lst = _load_handler("list-endpoint-configs")
        base = {"ProductionVariants": [{
            "VariantName": "v1",
            "ModelName": "m",
            "InstanceType": "ml.m5.large",
            "InitialInstanceCount": 1,
        }]}
        create(self.store, {**base, "EndpointConfigName": "cfg-a"})
        create(self.store, {**base, "EndpointConfigName": "cfg-b"})
        resp = lst(self.store, {})
        assert len(resp["EndpointConfigs"]) >= 2

    def test_delete_endpoint_config(self):
        create = _load_handler("create-endpoint-config")
        delete = _load_handler("delete-endpoint-config")
        describe = _load_handler("describe-endpoint-config")
        create(self.store, {
            "EndpointConfigName": "to-delete",
            "ProductionVariants": [{
                "VariantName": "v1",
                "ModelName": "m",
                "InstanceType": "ml.m5.large",
                "InitialInstanceCount": 1,
            }],
        })
        delete(self.store, {"EndpointConfigName": "to-delete"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"EndpointConfigName": "to-delete"})

    def test_delete_endpoint_config_not_found(self):
        handler = _load_handler("delete-endpoint-config")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"EndpointConfigName": "nonexistent"})


# ═══════════════════════════════════════════════════════════════════
# Endpoint Tests
# ═══════════════════════════════════════════════════════════════════

class TestEndpoint:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SageMakerStore()
        return self._store

    def test_create_endpoint_happy(self):
        handler = _load_handler("create-endpoint")
        resp = handler(self.store, {
            "EndpointName": "my-endpoint",
            "EndpointConfigName": "my-config",
        })
        assert resp["EndpointName"] == "my-endpoint"
        assert "EndpointArn" in resp
        assert resp["EndpointStatus"] == "Creating"

    def test_create_endpoint_duplicate(self):
        handler = _load_handler("create-endpoint")
        req = {
            "EndpointName": "dup-endpoint",
            "EndpointConfigName": "cfg",
        }
        handler(self.store, req)
        with pytest.raises(ResourceInUseException):
            handler(self.store, req)

    def test_describe_endpoint_happy(self):
        create = _load_handler("create-endpoint")
        describe = _load_handler("describe-endpoint")
        create(self.store, {
            "EndpointName": "desc-ep",
            "EndpointConfigName": "cfg",
        })
        resp = describe(self.store, {"EndpointName": "desc-ep"})
        assert resp["EndpointName"] == "desc-ep"
        assert resp["EndpointStatus"] == "Creating"

    def test_describe_endpoint_not_found(self):
        handler = _load_handler("describe-endpoint")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"EndpointName": "nonexistent"})

    def test_list_endpoints(self):
        create = _load_handler("create-endpoint")
        lst = _load_handler("list-endpoints")
        create(self.store, {"EndpointName": "ep-a", "EndpointConfigName": "cfg"})
        create(self.store, {"EndpointName": "ep-b", "EndpointConfigName": "cfg"})
        resp = lst(self.store, {})
        assert len(resp["Endpoints"]) >= 2

    def test_delete_endpoint(self):
        create = _load_handler("create-endpoint")
        delete = _load_handler("delete-endpoint")
        describe = _load_handler("describe-endpoint")
        create(self.store, {"EndpointName": "to-delete", "EndpointConfigName": "cfg"})
        delete(self.store, {"EndpointName": "to-delete"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"EndpointName": "to-delete"})

    def test_delete_endpoint_not_found(self):
        handler = _load_handler("delete-endpoint")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"EndpointName": "nonexistent"})

    def test_update_endpoint_happy(self):
        create = _load_handler("create-endpoint")
        update = _load_handler("update-endpoint")
        describe = _load_handler("describe-endpoint")
        create(self.store, {"EndpointName": "to-update", "EndpointConfigName": "old-cfg"})
        resp = update(self.store, {"EndpointName": "to-update", "EndpointConfigName": "new-cfg"})
        assert resp["EndpointConfigName"] == "new-cfg"
        resp2 = describe(self.store, {"EndpointName": "to-update"})
        assert resp2["EndpointConfigName"] == "new-cfg"

    def test_update_endpoint_not_found(self):
        handler = _load_handler("update-endpoint")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"EndpointName": "nonexistent"})
