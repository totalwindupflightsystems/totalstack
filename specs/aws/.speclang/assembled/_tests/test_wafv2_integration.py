"""Integration tests for WAFv2 — real store (no mocks)."""
import importlib.util
import os
import types

import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'wafv2')

# ── Load models.code.py dynamically ────────────────────────────────────
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

WAFv2Store = models_mod.WAFv2Store
WAFInvalidParameterException = models_mod.WAFInvalidParameterException
WAFNonexistentItemException = models_mod.WAFNonexistentItemException
WAFDuplicateItemException = models_mod.WAFDuplicateItemException
WAFOptimisticLockException = models_mod.WAFOptimisticLockException
WAFAssociatedItemException = models_mod.WAFAssociatedItemException
# Record classes for injection
WebACLRecord = models_mod.WebACLRecord
IPSetRecord = models_mod.IPSetRecord
RegexPatternSetRecord = models_mod.RegexPatternSetRecord
RuleGroupRecord = models_mod.RuleGroupRecord

# ── Handler loader helpers ─────────────────────────────────────────────

def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    if not os.path.exists(path):
        raise FileNotFoundError(f"Handler not found: {path}")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes (generated code references these without imports)
    mod.WAFInvalidParameterException = WAFInvalidParameterException
    mod.WAFNonexistentItemException = WAFNonexistentItemException
    mod.WAFDuplicateItemException = WAFDuplicateItemException
    mod.WAFOptimisticLockException = WAFOptimisticLockException
    mod.WAFAssociatedItemException = WAFAssociatedItemException
    # Inject record classes
    mod.WebACLRecord = WebACLRecord
    mod.IPSetRecord = IPSetRecord
    mod.RegexPatternSetRecord = RegexPatternSetRecord
    mod.RuleGroupRecord = RuleGroupRecord
    # Inject stdlib
    mod.time = __import__('time')
    mod.uuid = __import__('uuid')
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    # Find the handler function (skip injected items)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    if handler is None:
        raise RuntimeError(f"No handler found in {op_name}.code.py")
    return handler


# ═══════════════════════════════════════════════════════════════════════
# WebACL Tests
# ═══════════════════════════════════════════════════════════════════════

class TestWebACL:
    @pytest.fixture
    def store(self):
        return WAFv2Store()

    def test_create_web_acl_happy(self, store):
        handler = _load_handler('CreateWebACL')
        response = handler(store, {
            'Name': 'test-web-acl',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {
                'SampledRequestsEnabled': True,
                'CloudWatchMetricsEnabled': True,
                'MetricName': 'test-metric',
            },
        })
        assert response is not None
        assert 'Name' in response
        assert response['Name'] == 'test-web-acl'
        assert 'ARN' in response

    def test_create_web_acl_missing_name(self, store):
        handler = _load_handler('CreateWebACL')
        with pytest.raises(WAFInvalidParameterException):
            handler(store, {
                'Scope': 'REGIONAL',
                'DefaultAction': {'Allow': {}},
                'VisibilityConfig': {'SampledRequestsEnabled': True,
                                     'CloudWatchMetricsEnabled': True,
                                     'MetricName': 'test'},
            })

    def test_create_web_acl_duplicate(self, store):
        handler = _load_handler('CreateWebACL')
        request = {
            'Name': 'dup-acl',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test'},
        }
        handler(store, request)
        with pytest.raises(WAFDuplicateItemException):
            handler(store, request)

    def test_get_web_acl_happy(self, store):
        create = _load_handler('CreateWebACL')
        get = _load_handler('GetWebACL')
        result = create(store, {
            'Name': 'read-acl',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test'},
        })
        response = get(store, {'Id': result['Id'], 'Name': result['Name'],
                               'Scope': 'REGIONAL'})
        assert response['Name'] == 'read-acl'

    def test_get_web_acl_nonexistent(self, store):
        get = _load_handler('GetWebACL')
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'Id': 'nonexistent', 'Name': 'nonexistent',
                        'Scope': 'REGIONAL'})

    def test_update_web_acl_happy(self, store):
        create = _load_handler('CreateWebACL')
        update = _load_handler('UpdateWebACL')
        result = create(store, {
            'Name': 'update-acl',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test'},
        })
        response = update(store, {
            'Id': result['Id'],
            'Name': 'update-acl',
            'Scope': 'REGIONAL',
            'LockToken': '',
            'DefaultAction': {'Allow': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': False,
                                 'CloudWatchMetricsEnabled': False,
                                 'MetricName': 'updated'},
            'Description': 'Updated ACL',
        })
        assert 'NextLockToken' in response

    def test_delete_web_acl_happy(self, store):
        create = _load_handler('CreateWebACL')
        delete = _load_handler('DeleteWebACL')
        get = _load_handler('GetWebACL')
        result = create(store, {
            'Name': 'delete-acl',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test'},
        })
        delete(store, {'Id': result['Id'], 'Name': 'delete-acl',
                       'Scope': 'REGIONAL', 'LockToken': ''})
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'Id': result['Id'], 'Name': 'delete-acl',
                        'Scope': 'REGIONAL'})

    def test_delete_web_acl_nonexistent(self, store):
        delete = _load_handler('DeleteWebACL')
        with pytest.raises(WAFNonexistentItemException):
            delete(store, {'Id': 'nonexistent', 'Name': 'nonexistent',
                           'Scope': 'REGIONAL', 'LockToken': ''})

    def test_list_web_acls(self, store):
        create = _load_handler('CreateWebACL')
        list_ = _load_handler('ListWebACLs')
        create(store, {
            'Name': 'list-acl-1',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test'},
        })
        create(store, {
            'Name': 'list-acl-2',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test2'},
        })
        response = list_(store, {'Scope': 'REGIONAL'})
        assert len(response['WebACLs']) >= 2


# ═══════════════════════════════════════════════════════════════════════
# IPSet Tests
# ═══════════════════════════════════════════════════════════════════════

class TestIPSet:
    @pytest.fixture
    def store(self):
        return WAFv2Store()

    def test_create_ip_set_happy(self, store):
        handler = _load_handler('CreateIPSet')
        response = handler(store, {
            'Name': 'test-ipset',
            'Scope': 'REGIONAL',
            'IPAddressVersion': 'IPV4',
            'Addresses': ['10.0.0.0/24', '192.168.0.0/16'],
        })
        assert response['Name'] == 'test-ipset'
        assert 'Id' in response

    def test_create_ip_set_missing_name(self, store):
        handler = _load_handler('CreateIPSet')
        with pytest.raises(WAFInvalidParameterException):
            handler(store, {'Scope': 'REGIONAL', 'IPAddressVersion': 'IPV4',
                            'Addresses': ['10.0.0.0/24']})

    def test_get_ip_set_happy(self, store):
        create = _load_handler('CreateIPSet')
        get = _load_handler('GetIPSet')
        result = create(store, {
            'Name': 'read-ipset',
            'Scope': 'REGIONAL',
            'IPAddressVersion': 'IPV4',
            'Addresses': ['10.0.0.0/24'],
        })
        response = get(store, {'Id': result['Id'], 'Name': 'read-ipset',
                               'Scope': 'REGIONAL'})
        assert response['IPSet']['Name'] == 'read-ipset'

    def test_get_ip_set_nonexistent(self, store):
        get = _load_handler('GetIPSet')
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'Id': 'nonexistent', 'Name': 'nonexistent',
                        'Scope': 'REGIONAL'})

    def test_update_ip_set_happy(self, store):
        create = _load_handler('CreateIPSet')
        update = _load_handler('UpdateIPSet')
        result = create(store, {
            'Name': 'update-ipset',
            'Scope': 'REGIONAL',
            'IPAddressVersion': 'IPV4',
            'Addresses': ['10.0.0.0/24'],
        })
        response = update(store, {
            'Id': result['Id'],
            'Name': 'update-ipset',
            'Scope': 'REGIONAL',
            'LockToken': '',
            'Addresses': ['10.0.0.0/24', '172.16.0.0/16'],
        })
        assert 'NextLockToken' in response

    def test_delete_ip_set_happy(self, store):
        create = _load_handler('CreateIPSet')
        delete = _load_handler('DeleteIPSet')
        get = _load_handler('GetIPSet')
        result = create(store, {
            'Name': 'delete-ipset',
            'Scope': 'REGIONAL',
            'IPAddressVersion': 'IPV4',
            'Addresses': ['10.0.0.0/24'],
        })
        delete(store, {'Id': result['Id'], 'Name': 'delete-ipset',
                       'Scope': 'REGIONAL', 'LockToken': ''})
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'Id': result['Id'], 'Name': 'delete-ipset',
                        'Scope': 'REGIONAL'})

    def test_list_ip_sets(self, store):
        create = _load_handler('CreateIPSet')
        list_ = _load_handler('ListIPSets')
        create(store, {
            'Name': 'list-ipset-1',
            'Scope': 'REGIONAL',
            'IPAddressVersion': 'IPV4',
            'Addresses': ['10.0.0.0/24'],
        })
        response = list_(store, {'Scope': 'REGIONAL'})
        assert len(response['IPSets']) >= 1


# ═══════════════════════════════════════════════════════════════════════
# RegexPatternSet Tests
# ═══════════════════════════════════════════════════════════════════════

class TestRegexPatternSet:
    @pytest.fixture
    def store(self):
        return WAFv2Store()

    def test_create_regex_set_happy(self, store):
        handler = _load_handler('CreateRegexPatternSet')
        response = handler(store, {
            'Name': 'test-regex-set',
            'Scope': 'REGIONAL',
            'RegularExpressionList': [{'RegexString': r'^\d{3}-\d{2}-\d{4}$'}],
        })
        assert response['Name'] == 'test-regex-set'

    def test_get_regex_set_nonexistent(self, store):
        get = _load_handler('GetRegexPatternSet')
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'Id': 'nonexistent', 'Name': 'nonexistent',
                        'Scope': 'REGIONAL'})

    def test_delete_regex_set_nonexistent(self, store):
        delete = _load_handler('DeleteRegexPatternSet')
        with pytest.raises(WAFNonexistentItemException):
            delete(store, {'Id': 'nonexistent', 'Name': 'nonexistent',
                           'Scope': 'REGIONAL', 'LockToken': ''})


# ═══════════════════════════════════════════════════════════════════════
# RuleGroup Tests
# ═══════════════════════════════════════════════════════════════════════

class TestRuleGroup:
    @pytest.fixture
    def store(self):
        return WAFv2Store()

    def test_create_rule_group_happy(self, store):
        handler = _load_handler('CreateRuleGroup')
        response = handler(store, {
            'Name': 'test-rule-group',
            'Scope': 'REGIONAL',
            'Capacity': 100,
            'VisibilityConfig': {
                'SampledRequestsEnabled': True,
                'CloudWatchMetricsEnabled': True,
                'MetricName': 'test-rg',
            },
        })
        assert response['Name'] == 'test-rule-group'

    def test_get_rule_group_nonexistent(self, store):
        get = _load_handler('GetRuleGroup')
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'Id': 'nonexistent', 'Name': 'nonexistent',
                        'Scope': 'REGIONAL'})

    def test_delete_rule_group_nonexistent(self, store):
        delete = _load_handler('DeleteRuleGroup')
        with pytest.raises(WAFNonexistentItemException):
            delete(store, {'Id': 'nonexistent', 'Name': 'nonexistent',
                           'Scope': 'REGIONAL', 'LockToken': ''})


# ═══════════════════════════════════════════════════════════════════════
# Logging Configuration Tests
# ═══════════════════════════════════════════════════════════════════════

class TestLoggingConfiguration:
    @pytest.fixture
    def store(self):
        return WAFv2Store()

    def test_put_logging_config_happy(self, store):
        handler = _load_handler('PutLoggingConfiguration')
        response = handler(store, {
            'LoggingConfiguration': {
                'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc',
                'LogDestinationConfigs': [
                    'arn:aws:firehose:us-east-1:123456789012:deliverystream/test-stream'
                ],
            },
        })
        assert response['LoggingConfiguration']['ResourceArn'] is not None

    def test_put_logging_config_missing_arn(self, store):
        handler = _load_handler('PutLoggingConfiguration')
        with pytest.raises(WAFInvalidParameterException):
            handler(store, {'LoggingConfiguration': {}})

    def test_get_logging_config_nonexistent(self, store):
        get = _load_handler('GetLoggingConfiguration')
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/nonexistent'})


# ═══════════════════════════════════════════════════════════════════════
# Permission Policy Tests
# ═══════════════════════════════════════════════════════════════════════

class TestPermissionPolicy:
    @pytest.fixture
    def store(self):
        return WAFv2Store()

    def test_put_permission_policy_happy(self, store):
        handler = _load_handler('PutPermissionPolicy')
        handler(store, {
            'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/rulegroup/test/abc',
            'Policy': '{"Version":"2012-10-17","Statement":[]}',
        })

    def test_get_permission_policy_nonexistent(self, store):
        get = _load_handler('GetPermissionPolicy')
        with pytest.raises(WAFNonexistentItemException):
            get(store, {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/rulegroup/nonexistent'})


# ═══════════════════════════════════════════════════════════════════════
# Association Tests
# ═══════════════════════════════════════════════════════════════════════

class TestAssociation:
    @pytest.fixture
    def store(self):
        """Store with a pre-created WebACL."""
        s = WAFv2Store()
        create = _load_handler('CreateWebACL')
        create(s, {
            'Name': 'assoc-acl',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test'},
        })
        return s

    def test_associate_disassociate_web_acl(self, store):
        associate = _load_handler('AssociateWebACL')
        disassociate = _load_handler('DisassociateWebACL')
        # Get the ARN from the created ACL
        acl = store.list_web_acls('REGIONAL')['WebACLs'][0]
        resource_arn = 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-lb/abc123'
        associate(store, {'WebACLArn': acl['ARN'], 'ResourceArn': resource_arn})
        disassociate(store, {'ResourceArn': resource_arn})

    def test_get_web_acl_for_resource(self, store):
        associate = _load_handler('AssociateWebACL')
        get_acl_for = _load_handler('GetWebACLForResource')
        acl = store.list_web_acls('REGIONAL')['WebACLs'][0]
        resource_arn = 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-lb/def456'
        associate(store, {'WebACLArn': acl['ARN'], 'ResourceArn': resource_arn})
        response = get_acl_for(store, {'ResourceArn': resource_arn})
        assert 'WebACL' in response

    def test_get_web_acl_for_resource_nonexistent(self, store):
        get_acl_for = _load_handler('GetWebACLForResource')
        with pytest.raises(WAFNonexistentItemException):
            get_acl_for(store, {'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/no-acl/xyz'})


# ═══════════════════════════════════════════════════════════════════════
# Tags Tests
# ═══════════════════════════════════════════════════════════════════════

class TestTags:
    @pytest.fixture
    def store(self):
        s = WAFv2Store()
        create = _load_handler('CreateWebACL')
        create(s, {
            'Name': 'tagged-acl',
            'Scope': 'REGIONAL',
            'DefaultAction': {'Block': {}},
            'VisibilityConfig': {'SampledRequestsEnabled': True,
                                 'CloudWatchMetricsEnabled': True,
                                 'MetricName': 'test'},
        })
        return s

    def test_tag_untag_resource(self, store):
        tag = _load_handler('TagResource')
        untag = _load_handler('UntagResource')
        list_tags = _load_handler('ListTagsForResource')
        acl = store.list_web_acls('REGIONAL')['WebACLs'][0]
        tag(store, {'ResourceARN': acl['ARN'],
                     'Tags': [{'Key': 'Environment', 'Value': 'test'}]})
        response = list_tags(store, {'ResourceARN': acl['ARN']})
        tag_list = response['TagInfoForResource']['TagList']
        assert any(t['Key'] == 'Environment' for t in tag_list)
        untag(store, {'ResourceARN': acl['ARN'], 'TagKeys': ['Environment']})
        response = list_tags(store, {'ResourceARN': acl['ARN']})
        tag_list = response['TagInfoForResource']['TagList']
        assert not any(t['Key'] == 'Environment' for t in tag_list)

    def test_list_tags_nonexistent_resource(self, store):
        list_tags = _load_handler('ListTagsForResource')
        with pytest.raises(WAFNonexistentItemException):
            list_tags(store, {'ResourceARN': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/nonexistent'})
