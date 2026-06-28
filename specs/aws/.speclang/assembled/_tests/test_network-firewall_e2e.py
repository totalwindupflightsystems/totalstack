"""E2E test for Network Firewall — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}
LS_RUNNING = False

try:
    import urllib.request
    resp = urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
    LS_RUNNING = True
except Exception:
    pass


class TestNetworkFirewallE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('network-firewall', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_firewall_crud_workflow(self, client):
        """Create → describe → list → delete firewall."""
        resp = client.create_firewall(
            FirewallName='e2e-test-fw',
            FirewallPolicyArn='arn:aws:network-firewall:us-east-1:000000000000:firewall-policy/test-pol',
        )
        assert resp is not None
        assert 'Firewall' in resp
        fw_arn = resp['Firewall']['FirewallArn']
        assert resp['Firewall']['FirewallName'] == 'e2e-test-fw'

        resp = client.describe_firewall(FirewallArn=fw_arn)
        assert resp['Firewall']['FirewallName'] == 'e2e-test-fw'

        resp = client.list_firewalls()
        assert len(resp['Firewalls']) >= 1

        client.delete_firewall(FirewallArn=fw_arn)
        with pytest.raises(ClientError) as exc:
            client.describe_firewall(FirewallArn=fw_arn)
        assert 'ResourceNotFoundException' in str(exc.value)

    def test_policy_crud_workflow(self, client):
        """Create → describe → update → delete firewall policy."""
        resp = client.create_firewall_policy(
            FirewallPolicyName='e2e-test-pol',
            FirewallPolicy={
                'StatelessDefaultActions': ['aws:forward_to_sfe'],
                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe'],
            },
        )
        pol_arn = resp['FirewallPolicyResponse']['FirewallPolicyArn']

        resp = client.describe_firewall_policy(FirewallPolicyArn=pol_arn)
        assert resp['FirewallPolicyResponse']['FirewallPolicyName'] == 'e2e-test-pol'

        resp = client.update_firewall_policy(
            UpdateToken='tok',
            FirewallPolicyArn=pol_arn,
            FirewallPolicy={
                'StatelessDefaultActions': ['aws:drop'],
                'StatelessFragmentDefaultActions': ['aws:drop'],
            },
            Description='updated policy',
        )
        assert resp['FirewallPolicyResponse']['Description'] == 'updated policy'

        client.delete_firewall_policy(FirewallPolicyArn=pol_arn)

    def test_rule_group_crud_workflow(self, client):
        """Create → describe → delete rule group."""
        resp = client.create_rule_group(
            RuleGroupName='e2e-test-rg',
            Type='STATELESS',
            Capacity=100,
        )
        rg_arn = resp['RuleGroupResponse']['RuleGroupArn']

        resp = client.describe_rule_group(RuleGroupArn=rg_arn)
        assert resp['RuleGroupResponse']['RuleGroupName'] == 'e2e-test-rg'

        client.delete_rule_group(RuleGroupArn=rg_arn)
        with pytest.raises(ClientError) as exc:
            client.describe_rule_group(RuleGroupArn=rg_arn)
        assert 'ResourceNotFoundException' in str(exc.value)

    def test_error_nonexistent(self, client):
        with pytest.raises(ClientError) as exc:
            client.describe_firewall(
                FirewallArn='arn:aws:network-firewall:us-east-1:000000000000:firewall/nonexistent')
        assert 'ResourceNotFoundException' in str(exc.value)
