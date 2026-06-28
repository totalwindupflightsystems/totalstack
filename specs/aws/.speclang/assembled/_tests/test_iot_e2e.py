"""E2E tests for IoT."""
import os
import pytest
import boto3
import urllib.request
ENDPOINT = os.environ.get("LOCALSTACK_ENDPOINT", "http://localhost:4566")
TEST_CREDS = {"aws_access_key_id": "test", "aws_secret_access_key": "test"}

def _ls_running():
    try:
        req = urllib.request.Request(f"{ENDPOINT}/_localstack/health", headers={"Accept": "application/json"})
        urllib.request.urlopen(req, timeout=3)
        return True
    except Exception:
        return False
LS_RUNNING = _ls_running()

class TestIotE2E:
    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client("iot", endpoint_url=ENDPOINT, region_name="us-east-1", **TEST_CREDS)

    def test_thing_crud(self, client):
        resp = client.create_thing(thingName="e2e-thing")
        assert resp["thingArn"] is not None
        desc = client.describe_thing(thingName="e2e-thing")
        assert desc["thingName"] == "e2e-thing"
        things = client.list_things()
        assert len(things.get("things", [])) >= 1
        client.delete_thing(thingName="e2e-thing")

    def test_thing_group_crud(self, client):
        resp = client.create_thing_group(thingGroupName="e2e-group")
        assert resp["thingGroupArn"] is not None
        desc = client.describe_thing_group(thingGroupName="e2e-group")
        assert desc["thingGroupName"] == "e2e-group"
        client.delete_thing_group(thingGroupName="e2e-group")

    def test_policy_crud(self, client):
        resp = client.create_policy(policyName="e2e-policy", policyDocument='{"Version":"2012-10-17","Statement":[]}')
        assert resp["policyArn"] is not None
        desc = client.describe_policy(policyName="e2e-policy")
        assert desc["policyName"] == "e2e-policy"
        client.delete_policy(policyName="e2e-policy")

    def test_error_nonexistent(self, client):
        from botocore.exceptions import ClientError
        with pytest.raises(ClientError) as exc:
            client.describe_thing(thingName="nonexistent-xyz")
        assert exc.value.response["Error"]["Code"] in ("ResourceNotFoundException", "ValidationException", "InternalFailure", "501")
