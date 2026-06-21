"""Integration test for Shield — real ShieldStore."""
import importlib.util
import os
import types

import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'shield')

# Load the models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out all needed names
ShieldStore = models_mod.ShieldStore
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceAlreadyExistsException = models_mod.ResourceAlreadyExistsException
InvalidOperationException = models_mod.InvalidOperationException
NoAssociatedRoleException = models_mod.NoAssociatedRoleException
LimitsExceededException = models_mod.LimitsExceededException

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}

def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestProtectionIntegration:

    @pytest.fixture
    def store(self):
        return ShieldStore()

    def test_create_protection_happy_path(self, store):
        handler = _load_handler('CreateProtection')
        response = handler(store, {
            'Name': 'test-protection',
            'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-lb/123'
        })
        assert response['ProtectionId'].startswith('p-')

    def test_create_protection_duplicate(self, store):
        handler = _load_handler('CreateProtection')
        handler(store, {
            'Name': 'test-protection',
            'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-lb/123'
        })
        with pytest.raises(ResourceAlreadyExistsException):
            handler(store, {
                'Name': 'test-protection',
                'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-lb/123'
            })

    def test_describe_protection_by_id(self, store):
        create = _load_handler('CreateProtection')
        desc = _load_handler('DescribeProtection')
        result = create(store, {
            'Name': 'test-protection',
            'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-lb/123'
        })
        response = desc(store, {'ProtectionId': result['ProtectionId']})
        assert response['Name'] == 'test-protection'

    def test_describe_protection_nonexistent(self, store):
        handler = _load_handler('DescribeProtection')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'ProtectionId': 'p-nonexistent'})

    def test_delete_protection(self, store):
        create = _load_handler('CreateProtection')
        delete = _load_handler('DeleteProtection')
        desc = _load_handler('DescribeProtection')
        result = create(store, {
            'Name': 'test-protection',
            'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-lb/123'
        })
        delete(store, {'ProtectionId': result['ProtectionId']})
        with pytest.raises(ResourceNotFoundException):
            desc(store, {'ProtectionId': result['ProtectionId']})

    def test_delete_protection_nonexistent(self, store):
        handler = _load_handler('DeleteProtection')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'ProtectionId': 'p-nonexistent'})

    def test_list_protections(self, store):
        create = _load_handler('CreateProtection')
        lst = _load_handler('ListProtections')
        create(store, {
            'Name': 'test-1',
            'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/lb1/1'
        })
        create(store, {
            'Name': 'test-2',
            'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/lb2/2'
        })
        response = lst(store, {})
        assert len(response['Protections']) == 2


class TestProtectionGroupIntegration:

    @pytest.fixture
    def store(self):
        return ShieldStore()

    def test_create_pg_happy_path(self, store):
        handler = _load_handler('CreateProtectionGroup')
        response = handler(store, {
            'ProtectionGroupId': 'pg-test',
            'Aggregation': 'SUM',
            'Pattern': 'ARBITRARY'
        })
        assert response['ProtectionGroupId'] == 'pg-test'

    def test_create_pg_duplicate(self, store):
        handler = _load_handler('CreateProtectionGroup')
        handler(store, {
            'ProtectionGroupId': 'pg-test',
            'Aggregation': 'SUM',
            'Pattern': 'ARBITRARY'
        })
        with pytest.raises(ResourceAlreadyExistsException):
            handler(store, {
                'ProtectionGroupId': 'pg-test',
                'Aggregation': 'MAX',
                'Pattern': 'BY_RESOURCE_TYPE',
                'ResourceType': 'CLOUDFRONT_DISTRIBUTION'
            })

    def test_create_pg_missing_resource_type(self, store):
        handler = _load_handler('CreateProtectionGroup')
        with pytest.raises(InvalidParameterException):
            handler(store, {
                'ProtectionGroupId': 'pg-test',
                'Aggregation': 'SUM',
                'Pattern': 'BY_RESOURCE_TYPE'
            })

    def test_describe_pg(self, store):
        create = _load_handler('CreateProtectionGroup')
        desc = _load_handler('DescribeProtectionGroup')
        create(store, {
            'ProtectionGroupId': 'pg-test',
            'Aggregation': 'SUM',
            'Pattern': 'ARBITRARY'
        })
        response = desc(store, {'ProtectionGroupId': 'pg-test'})
        assert response['Aggregation'] == 'SUM'

    def test_describe_pg_nonexistent(self, store):
        handler = _load_handler('DescribeProtectionGroup')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'ProtectionGroupId': 'nonexistent'})

    def test_update_pg(self, store):
        create = _load_handler('CreateProtectionGroup')
        update = _load_handler('UpdateProtectionGroup')
        desc = _load_handler('DescribeProtectionGroup')
        create(store, {
            'ProtectionGroupId': 'pg-test',
            'Aggregation': 'SUM',
            'Pattern': 'ARBITRARY'
        })
        update(store, {
            'ProtectionGroupId': 'pg-test',
            'Aggregation': 'MAX',
            'Pattern': 'ARBITRARY'
        })
        response = desc(store, {'ProtectionGroupId': 'pg-test'})
        assert response['Aggregation'] == 'MAX'

    def test_delete_pg(self, store):
        create = _load_handler('CreateProtectionGroup')
        delete = _load_handler('DeleteProtectionGroup')
        desc = _load_handler('DescribeProtectionGroup')
        create(store, {
            'ProtectionGroupId': 'pg-test',
            'Aggregation': 'SUM',
            'Pattern': 'ARBITRARY'
        })
        delete(store, {'ProtectionGroupId': 'pg-test'})
        with pytest.raises(ResourceNotFoundException):
            desc(store, {'ProtectionGroupId': 'pg-test'})

    def test_delete_pg_nonexistent(self, store):
        handler = _load_handler('DeleteProtectionGroup')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'ProtectionGroupId': 'nonexistent'})

    def test_list_pgs(self, store):
        create = _load_handler('CreateProtectionGroup')
        lst = _load_handler('ListProtectionGroups')
        create(store, {
            'ProtectionGroupId': 'pg-1',
            'Aggregation': 'SUM',
            'Pattern': 'ARBITRARY'
        })
        create(store, {
            'ProtectionGroupId': 'pg-2',
            'Aggregation': 'MAX',
            'Pattern': 'ARBITRARY'
        })
        response = lst(store, {})
        assert len(response['ProtectionGroups']) == 2

    def test_list_resources_in_pg(self, store):
        create = _load_handler('CreateProtectionGroup')
        lst_resources = _load_handler('ListResourcesInProtectionGroup')
        create(store, {
            'ProtectionGroupId': 'pg-test',
            'Aggregation': 'SUM',
            'Pattern': 'ARBITRARY',
            'Members': ['arn:aws:ec2:us-east-1:123456789012:instance/i-123']
        })
        response = lst_resources(store, {'ProtectionGroupId': 'pg-test'})
        assert 'arn:aws:ec2:us-east-1:123456789012:instance/i-123' in response['ResourceArns']


class TestSubscriptionIntegration:

    @pytest.fixture
    def store(self):
        return ShieldStore()

    def test_create_subscription(self, store):
        handler = _load_handler('CreateSubscription')
        handler(store, {})
        desc = _load_handler('DescribeSubscription')
        response = desc(store, {})
        assert response is not None

    def test_create_subscription_duplicate(self, store):
        handler = _load_handler('CreateSubscription')
        handler(store, {})
        with pytest.raises(ResourceAlreadyExistsException):
            handler(store, {})

    def test_describe_subscription_nonexistent(self, store):
        handler = _load_handler('DescribeSubscription')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {})

    def test_update_subscription(self, store):
        create = _load_handler('CreateSubscription')
        update = _load_handler('UpdateSubscription')
        desc = _load_handler('DescribeSubscription')
        create(store, {})
        update(store, {'AutoRenew': 'ENABLED'})
        response = desc(store, {})
        assert response['AutoRenew'] == 'ENABLED'

    def test_delete_subscription(self, store):
        create = _load_handler('CreateSubscription')
        delete = _load_handler('DeleteSubscription')
        desc = _load_handler('DescribeSubscription')
        create(store, {})
        delete(store, {})
        with pytest.raises(ResourceNotFoundException):
            desc(store, {})

    def test_get_subscription_state(self, store):
        handler = _load_handler('GetSubscriptionState')
        response = handler(store, {})
        assert response['SubscriptionState'] == 'INACTIVE'

        create = _load_handler('CreateSubscription')
        create(store, {})
        response = handler(store, {})
        assert response['SubscriptionState'] == 'ACTIVE'


class TestDRTIntegration:

    @pytest.fixture
    def store(self):
        return ShieldStore()

    def test_associate_drt_role(self, store):
        handler = _load_handler('AssociateDRTRole')
        handler(store, {'RoleArn': 'arn:aws:iam::123456789012:role/ShieldDRTRole'})
        desc = _load_handler('DescribeDRTAccess')
        response = desc(store, {})
        assert 'arn:aws:iam::123456789012:role/ShieldDRTRole' in response['RoleArn']

    def test_associate_drt_log_bucket_no_role(self, store):
        handler = _load_handler('AssociateDRTLogBucket')
        with pytest.raises(NoAssociatedRoleException):
            handler(store, {'LogBucket': 'my-shield-logs'})

    def test_associate_drt_log_bucket_happy_path(self, store):
        associate_role = _load_handler('AssociateDRTRole')
        associate_bucket = _load_handler('AssociateDRTLogBucket')
        desc = _load_handler('DescribeDRTAccess')
        associate_role(store, {'RoleArn': 'arn:aws:iam::123456789012:role/ShieldDRTRole'})
        associate_bucket(store, {'LogBucket': 'my-shield-logs'})
        response = desc(store, {})
        assert 'my-shield-logs' in response['LogBucketList']

    def test_disassociate_drt_log_bucket(self, store):
        associate_role = _load_handler('AssociateDRTRole')
        associate_bucket = _load_handler('AssociateDRTLogBucket')
        disassociate = _load_handler('DisassociateDRTLogBucket')
        desc = _load_handler('DescribeDRTAccess')
        associate_role(store, {'RoleArn': 'arn:aws:iam::123456789012:role/ShieldDRTRole'})
        associate_bucket(store, {'LogBucket': 'my-shield-logs'})
        disassociate(store, {'LogBucket': 'my-shield-logs'})
        response = desc(store, {})
        assert 'my-shield-logs' not in response['LogBucketList']

    def test_disassociate_drt_log_bucket_nonexistent(self, store):
        handler = _load_handler('DisassociateDRTLogBucket')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {'LogBucket': 'nonexistent'})

    def test_disassociate_drt_role(self, store):
        associate = _load_handler('AssociateDRTRole')
        disassociate = _load_handler('DisassociateDRTRole')
        desc = _load_handler('DescribeDRTAccess')
        associate(store, {'RoleArn': 'arn:aws:iam::123456789012:role/ShieldDRTRole'})
        disassociate(store, {})
        response = desc(store, {})
        assert response['RoleArn'] == ''


class TestTagsIntegration:

    @pytest.fixture
    def store(self):
        return ShieldStore()

    def test_tag_resource(self, store):
        handler = _load_handler('TagResource')
        lst = _load_handler('ListTagsForResource')
        handler(store, {
            'ResourceARN': 'arn:aws:shield::000000000000:protection/p-1',
            'Tags': [{'Key': 'Environment', 'Value': 'test'}]
        })
        response = lst(store, {'ResourceARN': 'arn:aws:shield::000000000000:protection/p-1'})
        assert len(response['Tags']) == 1
        assert response['Tags'][0]['Key'] == 'Environment'

    def test_untag_resource(self, store):
        tag = _load_handler('TagResource')
        untag = _load_handler('UntagResource')
        lst = _load_handler('ListTagsForResource')
        tag(store, {
            'ResourceARN': 'arn:aws:shield::000000000000:protection/p-1',
            'Tags': [{'Key': 'Environment', 'Value': 'test'}, {'Key': 'Owner', 'Value': 'me'}]
        })
        untag(store, {
            'ResourceARN': 'arn:aws:shield::000000000000:protection/p-1',
            'TagKeys': ['Environment']
        })
        response = lst(store, {'ResourceARN': 'arn:aws:shield::000000000000:protection/p-1'})
        assert len(response['Tags']) == 1
        assert response['Tags'][0]['Key'] == 'Owner'

    def test_list_tags_nonexistent(self, store):
        handler = _load_handler('ListTagsForResource')
        response = handler(store, {'ResourceARN': 'arn:aws:shield::nonexistent'})
        assert response['Tags'] == []
