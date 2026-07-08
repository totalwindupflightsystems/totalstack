"""Integration test for Verified Permissions — real store."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'verifiedpermissions')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

VerifiedPermissionsStore = models_mod.VerifiedPermissionsStore
InvalidRequestException = models_mod.InvalidRequestException
ResourceNotFoundException = models_mod.ResourceNotFoundException
PolicyStoreRecord = models_mod.PolicyStoreRecord
PolicyRecord = models_mod.PolicyRecord
IdentitySourceRecord = models_mod.IdentitySourceRecord


def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidRequestException = InvalidRequestException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.PolicyStoreRecord = PolicyStoreRecord
    mod.PolicyRecord = PolicyRecord
    mod.IdentitySourceRecord = IdentitySourceRecord
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    return None


class TestPolicyStore:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = VerifiedPermissionsStore()
        return self._store

    def test_create_policy_store_happy(self):
        handler = _load_handler('CreatePolicyStore')
        resp = handler(self.store, {"ValidationSettings": {"Mode": "OFF"}})
        assert "PolicyStoreId" in resp
        assert "Arn" in resp

    def test_create_missing_required(self):
        handler = _load_handler('CreatePolicyStore')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_get_policy_store_happy(self):
        create = _load_handler('CreatePolicyStore')
        psid = create(self.store, {"ValidationSettings": {"Mode": "OFF"}})["PolicyStoreId"]
        handler = _load_handler('GetPolicyStore')
        desc = handler(self.store, {"PolicyStoreId": psid})
        assert desc["PolicyStoreId"] == psid

    def test_get_policy_store_nonexistent(self):
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetPolicyStore')(self.store, {"PolicyStoreId": "nonexistent"})

    def test_list_policy_stores(self):
        resp = _load_handler('ListPolicyStores')(self.store, {})
        assert "policyStores" in resp

    def test_delete_policy_store_happy(self):
        create = _load_handler('CreatePolicyStore')
        psid = create(self.store, {"ValidationSettings": {"Mode": "OFF"}})["PolicyStoreId"]
        _load_handler('DeletePolicyStore')(self.store, {"PolicyStoreId": psid})
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetPolicyStore')(self.store, {"PolicyStoreId": psid})

    def test_put_schema_happy(self):
        create = _load_handler('CreatePolicyStore')
        psid = create(self.store, {"ValidationSettings": {"Mode": "OFF"}})["PolicyStoreId"]
        resp = _load_handler('PutSchema')(self.store, {
            "PolicyStoreId": psid,
            "Definition": {"cedarJson": '{"entityTypes":{}}'},
        })
        assert resp["PolicyStoreId"] == psid

    def test_get_schema(self):
        create = _load_handler('CreatePolicyStore')
        psid = create(self.store, {"ValidationSettings": {"Mode": "OFF"}})["PolicyStoreId"]
        resp = _load_handler('GetSchema')(self.store, {"PolicyStoreId": psid})
        assert resp["PolicyStoreId"] == psid


class TestPolicy:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = VerifiedPermissionsStore()
        return self._store

    def _create_store(self):
        return _load_handler('CreatePolicyStore')(
            self.store, {"ValidationSettings": {"Mode": "OFF"}})["PolicyStoreId"]

    def test_create_policy_happy(self):
        psid = self._create_store()
        resp = _load_handler('CreatePolicy')(self.store, {
            "PolicyStoreId": psid,
            "Definition": {"Static": {"Statement": "permit(principal,action,resource);"}},
        })
        assert "PolicyId" in resp

    def test_get_policy_happy(self):
        psid = self._create_store()
        pid = _load_handler('CreatePolicy')(self.store, {
            "PolicyStoreId": psid,
            "Definition": {"Static": {"Statement": "permit(principal,action,resource);"}},
        })["PolicyId"]
        desc = _load_handler('GetPolicy')(self.store, {"PolicyStoreId": psid, "PolicyId": pid})
        assert desc["PolicyId"] == pid

    def test_get_policy_nonexistent(self):
        psid = self._create_store()
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetPolicy')(self.store, {"PolicyStoreId": psid, "PolicyId": "nonexistent"})

    def test_list_policies(self):
        psid = self._create_store()
        resp = _load_handler('ListPolicies')(self.store, {"PolicyStoreId": psid})
        assert "Policies" in resp

    def test_delete_policy_happy(self):
        psid = self._create_store()
        pid = _load_handler('CreatePolicy')(self.store, {
            "PolicyStoreId": psid,
            "Definition": {"Static": {"Statement": "permit(principal,action,resource);"}},
        })["PolicyId"]
        _load_handler('DeletePolicy')(self.store, {"PolicyStoreId": psid, "PolicyId": pid})
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetPolicy')(self.store, {"PolicyStoreId": psid, "PolicyId": pid})


class TestIdentitySource:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = VerifiedPermissionsStore()
        return self._store

    def _create_store(self):
        return _load_handler('CreatePolicyStore')(
            self.store, {"ValidationSettings": {"Mode": "OFF"}})["PolicyStoreId"]

    def test_create_identity_source_happy(self):
        psid = self._create_store()
        resp = _load_handler('CreateIdentitySource')(self.store, {
            "PolicyStoreId": psid,
            "Configuration": {"CognitoUserPoolConfiguration": {"UserPoolArn": "arn:aws:cognito-idp:..."}},
        })
        assert "IdentitySourceId" in resp

    def test_get_identity_source_happy(self):
        psid = self._create_store()
        isid = _load_handler('CreateIdentitySource')(self.store, {
            "PolicyStoreId": psid,
            "Configuration": {"CognitoUserPoolConfiguration": {"UserPoolArn": "arn:aws:cognito-idp:..."}},
        })["IdentitySourceId"]
        desc = _load_handler('GetIdentitySource')(self.store, {
            "PolicyStoreId": psid, "IdentitySourceId": isid})
        assert desc["IdentitySourceId"] == isid

    def test_delete_identity_source_happy(self):
        psid = self._create_store()
        isid = _load_handler('CreateIdentitySource')(self.store, {
            "PolicyStoreId": psid,
            "Configuration": {"CognitoUserPoolConfiguration": {"UserPoolArn": "arn:aws:cognito-idp:..."}},
        })["IdentitySourceId"]
        _load_handler('DeleteIdentitySource')(self.store, {
            "PolicyStoreId": psid, "IdentitySourceId": isid})
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetIdentitySource')(self.store, {
                "PolicyStoreId": psid, "IdentitySourceId": isid})


class TestAuth:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = VerifiedPermissionsStore()
        return self._store

    def _create_store(self):
        return _load_handler('CreatePolicyStore')(
            self.store, {"ValidationSettings": {"Mode": "OFF"}})["PolicyStoreId"]

    def test_is_authorized_happy(self):
        psid = self._create_store()
        resp = _load_handler('IsAuthorized')(self.store, {
            "PolicyStoreId": psid,
            "Principal": {"EntityType": "User", "EntityId": "alice"},
            "Action": {"ActionType": "Action", "ActionId": "view"},
            "Resource": {"EntityType": "Photo", "EntityId": "photo-123"},
        })
        assert resp["Decision"] == "ALLOW"


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = VerifiedPermissionsStore()
        return self._store

    def _create_store_arn(self):
        resp = _load_handler('CreatePolicyStore')(
            self.store, {"ValidationSettings": {"Mode": "OFF"}})
        return resp["Arn"]

    def test_tag_resource_happy(self):
        arn = self._create_store_arn()
        resp = _load_handler('TagResource')(self.store, {
            "ResourceArn": arn,
            "Tags": [{"Key": "env", "Value": "test"}],
        })
        assert resp == {}

    def test_list_tags_happy(self):
        arn = self._create_store_arn()
        _load_handler('TagResource')(self.store, {
            "ResourceArn": arn,
            "Tags": [{"Key": "team", "Value": "cedar"}],
        })
        resp = _load_handler('ListTagsForResource')(self.store, {"ResourceArn": arn})
        assert "Tags" in resp
        assert any(t["Key"] == "team" for t in resp["Tags"])

    def test_list_tags_nonexistent(self):
        with pytest.raises(ResourceNotFoundException):
            _load_handler('ListTagsForResource')(self.store, {"ResourceArn": "arn:nonexistent"})
