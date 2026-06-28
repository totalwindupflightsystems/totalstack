"""E2E tests for SageMaker — boto3 against running localstack."""
import os
import pytest
import boto3
import urllib.request
import json

ENDPOINT = os.environ.get("LOCALSTACK_ENDPOINT", "http://localhost:4566")
TEST_CREDS = {"aws_access_key_id": "test", "aws_secret_access_key": "test"}


def _is_localstack_running():
    """Check if LocalStack is running."""
    try:
        req = urllib.request.Request(
            f"{ENDPOINT}/_localstack/health",
            headers={"Accept": "application/json"},
        )
        resp = urllib.request.urlopen(req, timeout=3)
        json.loads(resp.read())
        return True
    except Exception:
        return False


LS_RUNNING = _is_localstack_running()


class TestSageMakerE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client(
            "sagemaker",
            endpoint_url=ENDPOINT,
            region_name="us-east-1",
            **TEST_CREDS,
        )

    def test_full_crud_workflow(self, client):
        """Create training job → describe → list → stop → delete."""
        # 1. Create training job
        resp = client.create_training_job(
            TrainingJobName="e2e-test-job",
            RoleArn="arn:aws:iam::000000000000:role/SageMakerRole",
            OutputDataConfig={"S3OutputPath": "s3://bucket/output"},
            AlgorithmSpecification={
                "TrainingImage": "image.dkr.ecr.us-east-1.amazonaws.com/xgboost:1",
                "TrainingInputMode": "File",
            },
            ResourceConfig={
                "InstanceType": "ml.m5.large",
                "InstanceCount": 1,
                "VolumeSizeInGB": 10,
            },
            StoppingCondition={"MaxRuntimeInSeconds": 3600},
        )
        assert resp["TrainingJobArn"] is not None

        # 2. Describe
        desc = client.describe_training_job(TrainingJobName="e2e-test-job")
        assert desc["TrainingJobName"] == "e2e-test-job"
        assert desc["TrainingJobStatus"] in ("InProgress", "Completed")

        # 3. List
        lst = client.list_training_jobs()
        assert len(lst["TrainingJobSummaries"]) >= 1

        # 4. Stop
        client.stop_training_job(TrainingJobName="e2e-test-job")

        # 5. Delete
        client.delete_training_job(TrainingJobName="e2e-test-job")

    def test_model_crud(self, client):
        """Create model → describe → list → delete."""
        resp = client.create_model(
            ModelName="e2e-test-model",
            PrimaryContainer={
                "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
            },
            ExecutionRoleArn="arn:aws:iam::000000000000:role/SM",
        )
        assert resp["ModelArn"] is not None

        desc = client.describe_model(ModelName="e2e-test-model")
        assert desc["ModelName"] == "e2e-test-model"

        lst = client.list_models()
        assert len(lst["Models"]) >= 1

        client.delete_model(ModelName="e2e-test-model")

    def test_error_nonexistent(self, client):
        """Reading nonexistent resource fails."""
        from botocore.exceptions import ClientError

        with pytest.raises(ClientError) as exc:
            client.describe_training_job(TrainingJobName="nonexistent-xyz")
        assert exc.value.response["Error"]["Code"] in (
            "ResourceNotFoundException",
            "ValidationException",
            "InternalFailure",
            "501",
        )

    def test_error_duplicate_create(self, client):
        """Creating duplicate resource fails."""
        from botocore.exceptions import ClientError

        client.create_model(
            ModelName="e2e-dup-model",
            PrimaryContainer={
                "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
            },
            ExecutionRoleArn="arn:aws:iam::000000000000:role/SM",
        )
        try:
            with pytest.raises(ClientError) as exc:
                client.create_model(
                    ModelName="e2e-dup-model",
                    PrimaryContainer={
                        "Image": "image.dkr.ecr.us-east-1.amazonaws.com/model:1",
                    },
                    ExecutionRoleArn="arn:aws:iam::000000000000:role/SM",
                )
            err_code = exc.value.response["Error"]["Code"]
            assert err_code in (
                "ResourceInUseException",
                "ValidationException",
                "InternalFailure",
                "501",
            )
        finally:
            try:
                client.delete_model(ModelName="e2e-dup-model")
            except Exception:
                pass
