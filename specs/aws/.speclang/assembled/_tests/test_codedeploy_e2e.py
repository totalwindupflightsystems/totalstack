"""E2E test for CodeDeploy — boto3 against running localstack instance.
NOTE: CodeDeploy is a greenfield service — E2E tests are skipped until provider is wired."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test', 'region_name': 'us-east-1'}


def _localstack_ready():
    """Check if localstack is running and responsive."""
    import urllib.request
    import json
    try:
        req = urllib.request.Request(f'{ENDPOINT}/_localstack/health', method='GET')
        resp = urllib.request.urlopen(req, timeout=3)
        health = json.loads(resp.read())
        return health.get('services', {}).get('codedeploy') in ('available', 'running')
    except Exception:
        return False


def _provider_wired():
    """Check if a CodeDeploy provider is actually wired (not just forward-to-AWS)."""
    # For now, always skip — no provider exists
    return False


class TestCodeDeployE2E:

    @pytest.fixture
    def client(self):
        if not _localstack_ready():
            pytest.skip("LocalStack not running")
        return boto3.client('codedeploy', endpoint_url=ENDPOINT, **TEST_CREDS)

    @pytest.mark.skipif(not _provider_wired(), reason="CodeDeploy provider not yet wired — greenfield service")
    def test_full_application_crud(self, client):
        """Create → Get → List → Update → Delete application."""
        # 1. Create
        create_resp = client.create_application(applicationName='test-e2e-app', computePlatform='Server')
        assert 'applicationId' in create_resp

        # 2. Get
        get_resp = client.get_application(applicationName='test-e2e-app')
        assert get_resp['application']['applicationName'] == 'test-e2e-app'

        # 3. List
        list_resp = client.list_applications()
        assert 'test-e2e-app' in list_resp.get('applications', [])

        # 4. Update (rename)
        client.update_application(applicationName='test-e2e-app', newApplicationName='test-e2e-app-renamed')
        get2 = client.get_application(applicationName='test-e2e-app-renamed')
        assert get2['application']['applicationName'] == 'test-e2e-app-renamed'

        # 5. Delete
        client.delete_application(applicationName='test-e2e-app-renamed')

        # 6. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.get_application(applicationName='test-e2e-app-renamed')
        assert exc.value.response['Error']['Code'] == 'ApplicationDoesNotExistException'

    @pytest.mark.skipif(not _provider_wired(), reason="CodeDeploy provider not yet wired — greenfield service")
    def test_error_nonexistent_application(self, client):
        """Reading nonexistent application fails."""
        with pytest.raises(ClientError) as exc:
            client.get_application(applicationName='nonexistent-app')
        assert exc.value.response['Error']['Code'] == 'ApplicationDoesNotExistException'

    @pytest.mark.skipif(not _provider_wired(), reason="CodeDeploy provider not yet wired — greenfield service")
    def test_error_duplicate_application(self, client):
        """Creating duplicate application fails."""
        client.create_application(applicationName='dup-test')
        try:
            with pytest.raises(ClientError) as exc:
                client.create_application(applicationName='dup-test')
            assert exc.value.response['Error']['Code'] == 'ApplicationAlreadyExistsException'
        finally:
            client.delete_application(applicationName='dup-test')

    @pytest.mark.skipif(not _provider_wired(), reason="CodeDeploy provider not yet wired — greenfield service")
    def test_deployment_config_crud(self, client):
        """Create → Get → List → Delete deployment config."""
        resp = client.create_deployment_config(
            deploymentConfigName='test-e2e-config',
            minimumHealthyHosts={'type': 'HOST_COUNT', 'value': 2}
        )
        assert 'deploymentConfigId' in resp

        get_resp = client.get_deployment_config(deploymentConfigName='test-e2e-config')
        assert get_resp['deploymentConfigInfo']['deploymentConfigName'] == 'test-e2e-config'

        client.delete_deployment_config(deploymentConfigName='test-e2e-config')

        with pytest.raises(ClientError) as exc:
            client.get_deployment_config(deploymentConfigName='test-e2e-config')
        assert exc.value.response['Error']['Code'] == 'DeploymentConfigDoesNotExistException'

    @pytest.mark.skipif(not _provider_wired(), reason="CodeDeploy provider not yet wired — greenfield service")
    def test_deployment_group_crud(self, client):
        """Create → Get → List → Delete deployment group."""
        client.create_application(applicationName='e2e-group-app')
        try:
            resp = client.create_deployment_group(
                applicationName='e2e-group-app',
                deploymentGroupName='e2e-test-group',
                serviceRoleArn='arn:aws:iam::123456789012:role/TestRole'
            )
            assert 'deploymentGroupId' in resp

            get_resp = client.get_deployment_group(
                applicationName='e2e-group-app',
                deploymentGroupName='e2e-test-group'
            )
            assert get_resp['deploymentGroupInfo']['deploymentGroupName'] == 'e2e-test-group'

            client.delete_deployment_group(
                applicationName='e2e-group-app',
                deploymentGroupName='e2e-test-group'
            )

            with pytest.raises(ClientError) as exc:
                client.get_deployment_group(
                    applicationName='e2e-group-app',
                    deploymentGroupName='e2e-test-group'
                )
            assert exc.value.response['Error']['Code'] == 'DeploymentGroupDoesNotExistException'
        finally:
            client.delete_application(applicationName='e2e-group-app')

    @pytest.mark.skipif(not _provider_wired(), reason="CodeDeploy provider not yet wired — greenfield service")
    def test_deployment_workflow(self, client):
        """Create deployment → Get → List → Stop."""
        client.create_application(applicationName='e2e-deploy-app')
        try:
            resp = client.create_deployment(
                applicationName='e2e-deploy-app',
                revision={
                    'revisionType': 'S3',
                    's3Location': {'bucket': 'test', 'key': 'app.zip', 'bundleType': 'zip'}
                }
            )
            deployment_id = resp['deploymentId']
            assert deployment_id.startswith('d-')

            get_resp = client.get_deployment(deploymentId=deployment_id)
            assert get_resp['deploymentInfo']['deploymentId'] == deployment_id

            client.stop_deployment(deploymentId=deployment_id)

            stopped = client.get_deployment(deploymentId=deployment_id)
            assert stopped['deploymentInfo']['status'] == 'Stopped'
        finally:
            client.delete_application(applicationName='e2e-deploy-app')
