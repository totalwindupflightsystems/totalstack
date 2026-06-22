"""Integration test for OpenSearchServerless — real store."""
import os
import importlib.util
import types
import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'opensearchserverless')

# Load models module
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

OpenSearchServerlessStore = models_mod.OpenSearchServerlessStore
CollectionRecord = models_mod.CollectionRecord
PolicyRecord = models_mod.PolicyRecord
LifecyclePolicyRecord = models_mod.LifecyclePolicyRecord
ValidationException = models_mod.ValidationException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException
InternalServerException = models_mod.InternalServerException
ServiceQuotaExceededException = models_mod.ServiceQuotaExceededException
OcuLimitExceededException = models_mod.OcuLimitExceededException


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ValidationException = ValidationException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.InternalServerException = InternalServerException
    mod.ServiceQuotaExceededException = ServiceQuotaExceededException
    mod.OcuLimitExceededException = OcuLimitExceededException
    mod.CollectionRecord = CollectionRecord
    mod.PolicyRecord = PolicyRecord
    mod.LifecyclePolicyRecord = LifecyclePolicyRecord
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    skip_names = {'<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestCollection:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = OpenSearchServerlessStore()
        return self._store

    def test_create_collection_happy(self):
        h = _load_handler('CreateCollection')
        resp = h(self.store, {'name': 'test-coll', 'type': 'SEARCH',
                               'description': 'Test collection'})
        assert resp.get('id') is not None
        assert resp.get('name') == 'test-coll'
        assert resp.get('status') == 'ACTIVE'

    def test_create_collection_duplicate(self):
        h = _load_handler('CreateCollection')
        h(self.store, {'name': 'test-coll-2', 'type': 'SEARCH'})
        with pytest.raises(ConflictException):
            h(self.store, {'name': 'test-coll-2', 'type': 'SEARCH'})

    def test_batch_get_by_name(self):
        h_c = _load_handler('CreateCollection')
        h_g = _load_handler('BatchGetCollection')
        h_c(self.store, {'name': 'test-coll-3', 'type': 'SEARCH'})
        resp = h_g(self.store, {'names': ['test-coll-3']})
        assert len(resp.get('collectionDetails', [])) == 1

    def test_batch_get_by_id(self):
        h_c = _load_handler('CreateCollection')
        h_g = _load_handler('BatchGetCollection')
        created = h_c(self.store, {'name': 'test-coll-4', 'type': 'SEARCH'})
        resp = h_g(self.store, {'ids': [created['id']]})
        assert len(resp.get('collectionDetails', [])) == 1

    def test_list_collections(self):
        h_c = _load_handler('CreateCollection')
        h_l = _load_handler('ListCollections')
        h_c(self.store, {'name': 'test-coll-5', 'type': 'SEARCH'})
        resp = h_l(self.store, {})
        assert len(resp.get('collectionSummaries', [])) >= 1

    def test_update_collection(self):
        h_c = _load_handler('CreateCollection')
        h_u = _load_handler('UpdateCollection')
        created = h_c(self.store, {'name': 'test-coll-6', 'type': 'SEARCH'})
        resp = h_u(self.store, {'id': created['id'],
                                 'description': 'Updated description'})
        assert resp.get('description') == 'Updated description'

    def test_update_nonexistent(self):
        h_u = _load_handler('UpdateCollection')
        with pytest.raises(ResourceNotFoundException):
            h_u(self.store, {'id': 'nonexistent-id'})

    def test_delete_collection(self):
        h_c = _load_handler('CreateCollection')
        h_d = _load_handler('DeleteCollection')
        h_g = _load_handler('BatchGetCollection')
        created = h_c(self.store, {'name': 'test-coll-7', 'type': 'SEARCH'})
        h_d(self.store, {'id': created['id']})
        resp = h_g(self.store, {'ids': [created['id']]})
        assert len(resp.get('collectionDetails', [])) == 0

    def test_delete_nonexistent(self):
        h_d = _load_handler('DeleteCollection')
        with pytest.raises(ResourceNotFoundException):
            h_d(self.store, {'id': 'nonexistent-id'})


class TestAccessPolicy:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = OpenSearchServerlessStore()
        return self._store

    def test_create_happy(self):
        h = _load_handler('CreateAccessPolicy')
        resp = h(self.store, {'type': 'data', 'name': 'my-policy',
                               'policy': '{"Version":"2012-10-17"}',
                               'description': 'Test policy'})
        detail = resp.get('accessPolicyDetail', {})
        assert detail.get('name') == 'my-policy'
        assert detail.get('type') == 'data'

    def test_create_duplicate(self):
        h = _load_handler('CreateAccessPolicy')
        h(self.store, {'type': 'data', 'name': 'my-policy-2',
                        'policy': '{}'})
        with pytest.raises(ConflictException):
            h(self.store, {'type': 'data', 'name': 'my-policy-2',
                            'policy': '{}'})

    def test_get_happy(self):
        h_c = _load_handler('CreateAccessPolicy')
        h_g = _load_handler('GetAccessPolicy')
        h_c(self.store, {'type': 'data', 'name': 'my-policy-3',
                          'policy': '{}'})
        resp = h_g(self.store, {'type': 'data', 'name': 'my-policy-3'})
        detail = resp.get('accessPolicyDetail', {})
        assert detail.get('name') == 'my-policy-3'

    def test_get_nonexistent(self):
        h_g = _load_handler('GetAccessPolicy')
        with pytest.raises(ResourceNotFoundException):
            h_g(self.store, {'type': 'data', 'name': 'nonexistent'})

    def test_list_by_type(self):
        h_c = _load_handler('CreateAccessPolicy')
        h_l = _load_handler('ListAccessPolicies')
        h_c(self.store, {'type': 'data', 'name': 'my-policy-4',
                          'policy': '{}'})
        h_c(self.store, {'type': 'data', 'name': 'my-policy-5',
                          'policy': '{}'})
        resp = h_l(self.store, {'type': 'data'})
        assert len(resp.get('accessPolicySummaries', [])) >= 2

    def test_update_happy(self):
        h_c = _load_handler('CreateAccessPolicy')
        h_u = _load_handler('UpdateAccessPolicy')
        h_g = _load_handler('GetAccessPolicy')
        h_c(self.store, {'type': 'data', 'name': 'my-policy-6',
                          'policy': '{}'})
        h_u(self.store, {'type': 'data', 'name': 'my-policy-6',
                          'policyVersion': '2',
                          'description': 'Updated'})
        resp = h_g(self.store, {'type': 'data', 'name': 'my-policy-6'})
        detail = resp.get('accessPolicyDetail', {})
        assert detail.get('policyVersion') == '2'
        assert detail.get('description') == 'Updated'

    def test_delete_happy(self):
        h_c = _load_handler('CreateAccessPolicy')
        h_d = _load_handler('DeleteAccessPolicy')
        h_g = _load_handler('GetAccessPolicy')
        h_c(self.store, {'type': 'data', 'name': 'my-policy-7',
                          'policy': '{}'})
        h_d(self.store, {'type': 'data', 'name': 'my-policy-7'})
        with pytest.raises(ResourceNotFoundException):
            h_g(self.store, {'type': 'data', 'name': 'my-policy-7'})


class TestSecurityPolicy:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = OpenSearchServerlessStore()
        return self._store

    def test_create_happy(self):
        h = _load_handler('CreateSecurityPolicy')
        resp = h(self.store, {'type': 'encryption', 'name': 'sec-policy',
                               'policy': '{"Rules":[]}',
                               'description': 'Security policy'})
        detail = resp.get('securityPolicyDetail', {})
        assert detail.get('name') == 'sec-policy'

    def test_create_duplicate(self):
        h = _load_handler('CreateSecurityPolicy')
        h(self.store, {'type': 'encryption', 'name': 'sec-policy-2',
                        'policy': '{}'})
        with pytest.raises(ConflictException):
            h(self.store, {'type': 'encryption', 'name': 'sec-policy-2',
                            'policy': '{}'})

    def test_get_happy(self):
        h_c = _load_handler('CreateSecurityPolicy')
        h_g = _load_handler('GetSecurityPolicy')
        h_c(self.store, {'type': 'encryption', 'name': 'sec-policy-3',
                          'policy': '{}'})
        resp = h_g(self.store, {'type': 'encryption', 'name': 'sec-policy-3'})
        assert resp.get('securityPolicyDetail', {}).get('name') == 'sec-policy-3'

    def test_get_nonexistent(self):
        h_g = _load_handler('GetSecurityPolicy')
        with pytest.raises(ResourceNotFoundException):
            h_g(self.store, {'type': 'encryption', 'name': 'nonexistent'})

    def test_list_by_type(self):
        h_c = _load_handler('CreateSecurityPolicy')
        h_l = _load_handler('ListSecurityPolicies')
        h_c(self.store, {'type': 'encryption', 'name': 'sec-policy-4',
                          'policy': '{}'})
        resp = h_l(self.store, {'type': 'encryption'})
        assert len(resp.get('securityPolicySummaries', [])) >= 1

    def test_update_happy(self):
        h_c = _load_handler('CreateSecurityPolicy')
        h_u = _load_handler('UpdateSecurityPolicy')
        h_c(self.store, {'type': 'encryption', 'name': 'sec-policy-5',
                          'policy': '{}'})
        h_u(self.store, {'type': 'encryption', 'name': 'sec-policy-5',
                          'policyVersion': '2'})
        resp = h_u(self.store, {'type': 'encryption', 'name': 'sec-policy-5',
                                 'policyVersion': '3'})
        detail = resp.get('securityPolicyDetail', {})
        assert detail.get('policyVersion') == '3'

    def test_delete_happy(self):
        h_c = _load_handler('CreateSecurityPolicy')
        h_d = _load_handler('DeleteSecurityPolicy')
        h_g = _load_handler('GetSecurityPolicy')
        h_c(self.store, {'type': 'encryption', 'name': 'sec-policy-6',
                          'policy': '{}'})
        h_d(self.store, {'type': 'encryption', 'name': 'sec-policy-6'})
        with pytest.raises(ResourceNotFoundException):
            h_g(self.store, {'type': 'encryption', 'name': 'sec-policy-6'})


class TestLifecyclePolicy:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = OpenSearchServerlessStore()
        return self._store

    def test_create_happy(self):
        h = _load_handler('CreateLifecyclePolicy')
        resp = h(self.store, {'type': 'retention', 'name': 'lc-policy',
                               'policy': '{"Rules":[]}',
                               'description': 'Lifecycle policy'})
        detail = resp.get('lifecyclePolicyDetail', {})
        assert detail.get('name') == 'lc-policy'

    def test_create_duplicate(self):
        h = _load_handler('CreateLifecyclePolicy')
        h(self.store, {'type': 'retention', 'name': 'lc-policy-2',
                        'policy': '{}'})
        with pytest.raises(ConflictException):
            h(self.store, {'type': 'retention', 'name': 'lc-policy-2',
                            'policy': '{}'})

    def test_batch_get_happy(self):
        h_c = _load_handler('CreateLifecyclePolicy')
        h_g = _load_handler('BatchGetLifecyclePolicy')
        h_c(self.store, {'type': 'retention', 'name': 'lc-policy-3',
                          'policy': '{}'})
        resp = h_g(self.store, {
            'identifiers': [{'type': 'retention', 'name': 'lc-policy-3'}]
        })
        assert len(resp.get('lifecyclePolicyDetails', [])) == 1

    def test_list_by_type(self):
        h_c = _load_handler('CreateLifecyclePolicy')
        h_l = _load_handler('ListLifecyclePolicies')
        h_c(self.store, {'type': 'retention', 'name': 'lc-policy-4',
                          'policy': '{}'})
        resp = h_l(self.store, {'type': 'retention'})
        assert len(resp.get('lifecyclePolicySummaries', [])) >= 1

    def test_update_happy(self):
        h_c = _load_handler('CreateLifecyclePolicy')
        h_u = _load_handler('UpdateLifecyclePolicy')
        h_c(self.store, {'type': 'retention', 'name': 'lc-policy-5',
                          'policy': '{}'})
        h_u(self.store, {'type': 'retention', 'name': 'lc-policy-5',
                          'policyVersion': '2'})
        resp = h_u(self.store, {'type': 'retention', 'name': 'lc-policy-5',
                                 'policyVersion': '3'})
        detail = resp.get('lifecyclePolicyDetail', {})
        assert detail.get('policyVersion') == '3'

    def test_delete_happy(self):
        h_c = _load_handler('CreateLifecyclePolicy')
        h_d = _load_handler('DeleteLifecyclePolicy')
        h_g = _load_handler('BatchGetLifecyclePolicy')
        h_c(self.store, {'type': 'retention', 'name': 'lc-policy-6',
                          'policy': '{}'})
        h_d(self.store, {'type': 'retention', 'name': 'lc-policy-6'})
        resp = h_g(self.store, {
            'identifiers': [{'type': 'retention', 'name': 'lc-policy-6'}]
        })
        assert len(resp.get('lifecyclePolicyDetails', [])) == 0


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = OpenSearchServerlessStore()
        return self._store

    def test_tag_resource(self):
        h_t = _load_handler('TagResource')
        h_l = _load_handler('ListTagsForResource')
        h_t(self.store, {
            'resourceArn': 'arn:aws:aoss:us-east-1:123:collection/test',
            'tags': [{'key': 'env', 'value': 'test'}, {'key': 'team', 'value': 'ops'}]
        })
        resp = h_l(self.store, {
            'resourceArn': 'arn:aws:aoss:us-east-1:123:collection/test'
        })
        tags = resp.get('tags', [])
        tag_dict = {t['key']: t['value'] for t in tags}
        assert tag_dict.get('env') == 'test'
        assert tag_dict.get('team') == 'ops'

    def test_untag_resource(self):
        h_t = _load_handler('TagResource')
        h_u = _load_handler('UntagResource')
        h_l = _load_handler('ListTagsForResource')
        arn = 'arn:aws:aoss:us-east-1:123:collection/test2'
        h_t(self.store, {
            'resourceArn': arn,
            'tags': [{'key': 'env', 'value': 'test'}, {'key': 'team', 'value': 'ops'}]
        })
        h_u(self.store, {'resourceArn': arn, 'tagKeys': ['env']})
        resp = h_l(self.store, {'resourceArn': arn})
        tags = resp.get('tags', [])
        tag_dict = {t['key']: t['value'] for t in tags}
        assert 'env' not in tag_dict
        assert tag_dict.get('team') == 'ops'

    def test_list_tags_empty(self):
        h_l = _load_handler('ListTagsForResource')
        resp = h_l(self.store, {
            'resourceArn': 'arn:aws:aoss:us-east-1:123:collection/nonexistent'
        })
        assert resp.get('tags', []) == []
