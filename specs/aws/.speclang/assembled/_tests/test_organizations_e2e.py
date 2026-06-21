"""E2E test for Organizations — boto3 against running localstack.

These tests require a running localstack instance with the Organizations provider wired.
They will be automatically skipped if the endpoint is not available or the API is
not yet implemented (greenfield service pattern).
"""
import os

import boto3
import pytest
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _is_available():
    """Check if Organizations endpoint is available."""
    try:
        client = boto3.client('organizations', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        client.describe_organization()
        return True
    except ClientError as e:
        code = e.response['Error']['Code']
        # 400 means the endpoint exists (got past routing to handler)
        if code in ('AWSOrganizationsNotInUseException',):
            return True
        return False
    except Exception:
        return False


SKIP_REASON = "Organizations provider not yet wired (greenfield service)"


class TestOrganizationsE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('organizations', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Try to clean up any test resources
        if not _is_available():
            return
        try:
            # List and delete all non-management accounts
            resp = client.list_accounts()
            for acc in resp.get('Accounts', []):
                try:
                    client.remove_account_from_organization(AccountId=acc['Id'])
                except ClientError:
                    pass
        except ClientError:
            pass

    @pytest.mark.skipif(not _is_available(), reason=SKIP_REASON)
    def test_full_crud_workflow(self, client):
        """Create org → describe → create account → describe → list → cleanup."""
        # 1. Create organization
        response = client.create_organization(FeatureSet='ALL')
        assert response['Organization']['FeatureSet'] == 'ALL'
        org_id = response['Organization']['Id']

        # 2. Describe organization
        response = client.describe_organization()
        assert response['Organization']['Id'] == org_id

        # 3. Create member account
        import uuid
        acct_name = f"e2e-{uuid.uuid4().hex[:8]}"
        response = client.create_account(
            Email=f"{acct_name}@test.com",
            AccountName=acct_name,
        )
        status = response['CreateAccountStatus']
        assert status['AccountId'] is not None
        acct_id = status['AccountId']

        # 4. Describe the account
        response = client.describe_account(AccountId=acct_id)
        assert response['Account']['Id'] == acct_id
        assert response['Account']['Email'] == f"{acct_name}@test.com"

        # 5. List accounts
        response = client.list_accounts()
        assert len(response['Accounts']) >= 2  # management + created

        # 6. Remove the account
        client.remove_account_from_organization(AccountId=acct_id)

        # 7. Verify removed
        with pytest.raises(ClientError) as exc:
            client.describe_account(AccountId=acct_id)
        assert exc.value.response['Error']['Code'] == 'AccountNotFoundException'

    @pytest.mark.skipif(not _is_available(), reason=SKIP_REASON)
    def test_ou_crud_workflow(self, client):
        """Create org → create OU → describe → list → delete."""
        # Create organization (may already exist from other test)
        try:
            client.create_organization(FeatureSet='ALL')
        except ClientError:
            pass

        # Get root
        roots = client.list_roots()
        root_id = roots['Roots'][0]['Id']

        # Create OU
        response = client.create_organizational_unit(
            ParentId=root_id, Name='E2ETestOU')
        ou_id = response['OrganizationalUnit']['Id']

        # Describe OU
        response = client.describe_organizational_unit(
            OrganizationalUnitId=ou_id)
        assert response['OrganizationalUnit']['Name'] == 'E2ETestOU'

        # List OUs under root
        response = client.list_organizational_units_for_parent(
            ParentId=root_id)
        ou_names = [ou['Name'] for ou in response['OrganizationalUnits']]
        assert 'E2ETestOU' in ou_names

        # Delete OU
        client.delete_organizational_unit(OrganizationalUnitId=ou_id)

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_organizational_unit(
                OrganizationalUnitId=ou_id)
        assert exc.value.response['Error']['Code'] == 'OrganizationalUnitNotFoundException'

    @pytest.mark.skipif(not _is_available(), reason=SKIP_REASON)
    def test_policy_crud_workflow(self, client):
        """Create org → create policy → attach → detach → delete."""
        try:
            client.create_organization(FeatureSet='ALL')
        except ClientError:
            pass

        # Enable SCP (required for full-featured orgs)
        roots = client.list_roots()
        root_id = roots['Roots'][0]['Id']

        # Create policy
        SCP_CONTENT = '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"*","Resource":"*"}]}'
        response = client.create_policy(
            Content=SCP_CONTENT,
            Description='E2E test policy',
            Name='E2ETestPolicy',
            Type='SERVICE_CONTROL_POLICY',
        )
        policy_id = response['Policy']['PolicySummary']['Id']

        # Describe policy
        response = client.describe_policy(PolicyId=policy_id)
        assert response['Policy']['PolicySummary']['Name'] == 'E2ETestPolicy'

        # Attach to root
        client.attach_policy(PolicyId=policy_id, TargetId=root_id)

        # List policies for target
        response = client.list_policies_for_target(
            TargetId=root_id, Filter='SERVICE_CONTROL_POLICY')
        attached_ids = [p['Id'] for p in response['Policies']]
        assert policy_id in attached_ids

        # Detach
        client.detach_policy(PolicyId=policy_id, TargetId=root_id)

        # Delete
        client.delete_policy(PolicyId=policy_id)

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_policy(PolicyId=policy_id)
        assert exc.value.response['Error']['Code'] == 'PolicyNotFoundException'

    @pytest.mark.skipif(not _is_available(), reason=SKIP_REASON)
    def test_error_nonexistent_organization(self, client):
        """Accessing org operations without creating one should fail."""
        with pytest.raises(ClientError) as exc:
            client.describe_organization()
        assert exc.value.response['Error']['Code'] in (
            'AWSOrganizationsNotInUseException', '400')

    @pytest.mark.skipif(not _is_available(), reason=SKIP_REASON)
    def test_error_nonexistent_account(self, client):
        """Accessing nonexistent account should fail."""
        try:
            client.create_organization(FeatureSet='ALL')
        except ClientError:
            pass

        with pytest.raises(ClientError):
            client.describe_account(AccountId='999999999999')
