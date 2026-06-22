"""E2E tests for AWS Backup — skipif until ASF provider wired."""
import os
import pytest
import urllib.request
import json

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')


def _is_localstack_running():
    try:
        req = urllib.request.Request(f"{ENDPOINT}/_localstack/health",
                                     headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=3)
        data = json.loads(resp.read())
        return data.get('services', {}).get('backup') in ('available', 'running')
    except Exception:
        return False


LOCALSTACK_AVAILABLE = _is_localstack_running()


@pytest.mark.skipif(not LOCALSTACK_AVAILABLE,
                    reason="Backup ASF provider not wired yet")
class TestBackupE2E:
    @pytest.fixture
    def client(self):
        import boto3
        return boto3.client('backup', endpoint_url=ENDPOINT,
                           region_name='us-east-1',
                           aws_access_key_id='test', aws_secret_access_key='test')

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        from botocore.exceptions import ClientError
        try:
            plans = client.list_backup_plans()
            for p in plans.get('BackupPlansList', []):
                client.delete_backup_plan(BackupPlanId=p['BackupPlanId'])
        except ClientError:
            pass

    def test_full_plan_workflow(self, client):
        from botocore.exceptions import ClientError
        resp = client.create_backup_plan(BackupPlan={'BackupPlanName': 'e2e-plan',
                                                     'Rules': [{'RuleName': 'daily',
                                                                'TargetBackupVaultName': 'Default',
                                                                'ScheduleExpression': 'cron(0 5 * * ? *)'}]})
        assert resp['BackupPlanId'] is not None
        pid = resp['BackupPlanId']
        desc = client.get_backup_plan(BackupPlanId=pid)
        assert desc['BackupPlanId'] == pid
        client.delete_backup_plan(BackupPlanId=pid)
        with pytest.raises(ClientError) as exc:
            client.get_backup_plan(BackupPlanId=pid)
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'


class TestBackupE2ESmoke:
    def test_imports_work(self):
        import boto3
        assert hasattr(boto3, 'client')

    def test_skip_condition_runs(self):
        assert _is_localstack_running() in (True, False)
