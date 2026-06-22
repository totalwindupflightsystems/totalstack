"""E2E test for EKS — boto3 against running localstack (skip if EKS provider missing)."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _eks_available():
    """Check if EKS endpoint responds (not 501)."""
    try:
        c = boto3.client('eks', endpoint_url=ENDPOINT, region_name='us-east-1', **TEST_CREDS)
        c.list_clusters()
        return True
    except ClientError as e:
        code = e.response['Error']['Code']
        return code != '501' and 'NotImplemented' not in code and code != 'InternalFailure'
    except Exception:
        return False


EKS_AVAILABLE = _eks_available()


@pytest.mark.skipif(not EKS_AVAILABLE, reason="EKS provider not available in LocalStack")
class TestEKSE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('eks', endpoint_url=ENDPOINT, region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Clean up test resources
        try:
            client.delete_cluster(name='e2e-test-cluster')
        except ClientError:
            pass
        try:
            client.delete_nodegroup(clusterName='e2e-test-cluster', nodegroupName='e2e-ng')
        except ClientError:
            pass

    def test_full_cluster_crud_workflow(self, client):
        """Create cluster → describe → list → update → delete."""
        # 1. Create
        resp = client.create_cluster(
            name='e2e-test-cluster',
            roleArn='arn:aws:iam::123456789012:role/EKSClusterRole',
            resourcesVpcConfig={
                'subnetIds': ['subnet-abc123'],
                'securityGroupIds': ['sg-abc123']
            }
        )
        assert resp['cluster']['name'] == 'e2e-test-cluster'
        assert resp['cluster']['status'] in ('ACTIVE', 'CREATING')

        # 2. Describe
        resp = client.describe_cluster(name='e2e-test-cluster')
        assert resp['cluster']['name'] == 'e2e-test-cluster'

        # 3. List
        resp = client.list_clusters()
        assert 'e2e-test-cluster' in resp['clusters']

        # 4. Update version
        resp = client.update_cluster_version(name='e2e-test-cluster', version='1.33')
        assert 'update' in resp

        # 5. Delete
        resp = client.delete_cluster(name='e2e-test-cluster')
        assert resp['cluster']['name'] == 'e2e-test-cluster'

        # 6. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_cluster(name='e2e-test-cluster')
        assert exc.value.response['Error']['Code'] in ('ResourceNotFoundException', '404')

    def test_error_duplicate_cluster(self, client):
        """Creating duplicate cluster fails."""
        client.create_cluster(
            name='e2e-dup-cluster',
            roleArn='arn:aws:iam::123456789012:role/R',
            resourcesVpcConfig={'subnetIds': ['subnet-1']}
        )
        try:
            with pytest.raises(ClientError) as exc:
                client.create_cluster(
                    name='e2e-dup-cluster',
                    roleArn='arn:aws:iam::123456789012:role/R',
                    resourcesVpcConfig={'subnetIds': ['subnet-1']}
                )
            assert exc.value.response['Error']['Code'] in ('ResourceInUseException', '409', 'AlreadyExistsException')
        finally:
            client.delete_cluster(name='e2e-dup-cluster')

    def test_error_nonexistent_cluster(self, client):
        """Describing nonexistent cluster fails."""
        with pytest.raises(ClientError) as exc:
            client.describe_cluster(name='e2e-nonexistent')
        assert exc.value.response['Error']['Code'] in ('ResourceNotFoundException', '404')

    def test_nodegroup_crud_workflow(self, client):
        """Create nodegroup → describe → list → delete."""
        client.create_cluster(
            name='e2e-ng-cluster',
            roleArn='arn:aws:iam::123456789012:role/R',
            resourcesVpcConfig={'subnetIds': ['subnet-1']}
        )

        try:
            # Create nodegroup
            resp = client.create_nodegroup(
                clusterName='e2e-ng-cluster',
                nodegroupName='e2e-ng',
                subnets=['subnet-1'],
                scalingConfig={'minSize': 1, 'maxSize': 3, 'desiredSize': 1}
            )
            assert resp['nodegroup']['nodegroupName'] == 'e2e-ng'

            # Describe
            resp = client.describe_nodegroup(clusterName='e2e-ng-cluster', nodegroupName='e2e-ng')
            assert resp['nodegroup']['nodegroupName'] == 'e2e-ng'

            # List
            resp = client.list_nodegroups(clusterName='e2e-ng-cluster')
            assert 'e2e-ng' in resp['nodegroups']

            # Delete
            resp = client.delete_nodegroup(clusterName='e2e-ng-cluster', nodegroupName='e2e-ng')
        finally:
            client.delete_cluster(name='e2e-ng-cluster')

    def test_fargate_profile_crud_workflow(self, client):
        """Create Fargate profile → describe → list → delete."""
        client.create_cluster(
            name='e2e-fg-cluster',
            roleArn='arn:aws:iam::123456789012:role/R',
            resourcesVpcConfig={'subnetIds': ['subnet-1']}
        )

        try:
            resp = client.create_fargate_profile(
                clusterName='e2e-fg-cluster',
                fargateProfileName='e2e-fp',
                podExecutionRoleArn='arn:aws:iam::123456789012:role/FargatePodRole'
            )
            assert resp['fargateProfile']['fargateProfileName'] == 'e2e-fp'

            resp = client.describe_fargate_profile(
                clusterName='e2e-fg-cluster', fargateProfileName='e2e-fp')
            assert resp['fargateProfile']['fargateProfileName'] == 'e2e-fp'

            resp = client.list_fargate_profiles(clusterName='e2e-fg-cluster')
            assert 'e2e-fp' in resp['fargateProfileNames']

            client.delete_fargate_profile(
                clusterName='e2e-fg-cluster', fargateProfileName='e2e-fp')
        finally:
            client.delete_cluster(name='e2e-fg-cluster')
