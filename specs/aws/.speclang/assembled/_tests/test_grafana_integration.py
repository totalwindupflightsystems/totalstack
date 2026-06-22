"""Integration tests for Grafana — real store."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'grafana')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

GrafanaStore = models_mod.GrafanaStore
WorkspaceRecord = models_mod.WorkspaceRecord
ApiKeyRecord = models_mod.ApiKeyRecord
ServiceAccountRecord = models_mod.ServiceAccountRecord
ServiceAccountTokenRecord = models_mod.ServiceAccountTokenRecord
ValidationException = models_mod.ValidationException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException
InternalServerException = models_mod.InternalServerException
AccessDeniedException = models_mod.AccessDeniedException
ThrottlingException = models_mod.ThrottlingException
ServiceQuotaExceededException = models_mod.ServiceQuotaExceededException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ValidationException = ValidationException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.InternalServerException = InternalServerException
    mod.AccessDeniedException = AccessDeniedException
    mod.ThrottlingException = ThrottlingException
    mod.ServiceQuotaExceededException = ServiceQuotaExceededException
    mod.WorkspaceRecord = WorkspaceRecord
    mod.ApiKeyRecord = ApiKeyRecord
    mod.ServiceAccountRecord = ServiceAccountRecord
    mod.ServiceAccountTokenRecord = ServiceAccountTokenRecord
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestWorkspace:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GrafanaStore()
        return self._store

    def test_create_workspace_happy(self):
        handler = _load_handler('CreateWorkspace')
        resp = handler(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "my-workspace",
        })
        assert resp["workspaceName"] == "my-workspace"
        assert resp["status"] == "ACTIVE"
        assert "id" in resp
        assert "endpoint" in resp

    def test_create_workspace_duplicate(self):
        handler = _load_handler('CreateWorkspace')
        req = {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "dup-ws",
        }
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_create_workspace_missing_required(self):
        handler = _load_handler('CreateWorkspace')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_describe_workspace_happy(self):
        create = _load_handler('CreateWorkspace')
        describe = _load_handler('DescribeWorkspace')
        resp = create(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "desc-ws",
        })
        resp2 = describe(self.store, {"workspaceId": resp["id"]})
        assert resp2["workspaceName"] == "desc-ws"

    def test_describe_workspace_nonexistent(self):
        describe = _load_handler('DescribeWorkspace')
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"workspaceId": "nonexistent"})

    def test_list_workspaces(self):
        create = _load_handler('CreateWorkspace')
        list_handler = _load_handler('ListWorkspaces')
        create(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "list-ws1",
        })
        create(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "list-ws2",
        })
        resp = list_handler(self.store, {})
        assert len(resp["workspaces"]) == 2

    def test_update_workspace(self):
        create = _load_handler('CreateWorkspace')
        update = _load_handler('UpdateWorkspace')
        resp = create(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "update-ws",
        })
        resp2 = update(self.store, {
            "workspaceId": resp["id"],
            "workspaceName": "updated-name",
            "workspaceDescription": "Updated desc",
        })
        assert resp2["workspaceName"] == "updated-name"

    def test_update_workspace_nonexistent(self):
        update = _load_handler('UpdateWorkspace')
        with pytest.raises(ResourceNotFoundException):
            update(self.store, {"workspaceId": "nonexistent"})

    def test_delete_workspace(self):
        create = _load_handler('CreateWorkspace')
        delete = _load_handler('DeleteWorkspace')
        describe = _load_handler('DescribeWorkspace')
        resp = create(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "del-ws",
        })
        delete(self.store, {"workspaceId": resp["id"]})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"workspaceId": resp["id"]})

    def test_delete_workspace_nonexistent(self):
        delete = _load_handler('DeleteWorkspace')
        with pytest.raises(ResourceNotFoundException):
            delete(self.store, {"workspaceId": "nonexistent"})


class TestApiKey:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GrafanaStore()
        return self._store

    def _create_ws(self):
        handler = _load_handler('CreateWorkspace')
        return handler(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "api-key-ws",
        })

    def test_create_api_key_happy(self):
        ws = self._create_ws()
        handler = _load_handler('CreateWorkspaceApiKey')
        resp = handler(self.store, {
            "workspaceId": ws["id"],
            "keyName": "my-key",
            "keyRole": "ADMIN",
            "secondsToLive": 3600,
        })
        assert resp["keyName"] == "my-key"
        assert "key" in resp

    def test_create_api_key_duplicate(self):
        ws = self._create_ws()
        handler = _load_handler('CreateWorkspaceApiKey')
        req = {
            "workspaceId": ws["id"],
            "keyName": "dup-key",
            "keyRole": "ADMIN",
            "secondsToLive": 3600,
        }
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_delete_api_key(self):
        ws = self._create_ws()
        create = _load_handler('CreateWorkspaceApiKey')
        delete = _load_handler('DeleteWorkspaceApiKey')
        create(self.store, {
            "workspaceId": ws["id"],
            "keyName": "del-key",
            "keyRole": "ADMIN",
            "secondsToLive": 3600,
        })
        resp = delete(self.store, {"workspaceId": ws["id"], "keyName": "del-key"})
        assert resp["keyName"] == "del-key"

    def test_delete_api_key_nonexistent(self):
        ws = self._create_ws()
        delete = _load_handler('DeleteWorkspaceApiKey')
        with pytest.raises(ResourceNotFoundException):
            delete(self.store, {"workspaceId": ws["id"], "keyName": "nope"})


class TestServiceAccount:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GrafanaStore()
        return self._store

    def _create_ws(self):
        handler = _load_handler('CreateWorkspace')
        return handler(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "sa-ws",
        })

    def test_create_sa_happy(self):
        ws = self._create_ws()
        handler = _load_handler('CreateWorkspaceServiceAccount')
        resp = handler(self.store, {
            "workspaceId": ws["id"],
            "name": "my-sa",
            "grafanaRole": "ADMIN",
        })
        assert resp["name"] == "my-sa"
        assert resp["grafanaRole"] == "ADMIN"

    def test_create_sa_duplicate(self):
        ws = self._create_ws()
        handler = _load_handler('CreateWorkspaceServiceAccount')
        req = {"workspaceId": ws["id"], "name": "dup-sa", "grafanaRole": "ADMIN"}
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_delete_sa(self):
        ws = self._create_ws()
        create = _load_handler('CreateWorkspaceServiceAccount')
        delete = _load_handler('DeleteWorkspaceServiceAccount')
        sa = create(self.store, {
            "workspaceId": ws["id"],
            "name": "del-sa",
            "grafanaRole": "ADMIN",
        })
        resp = delete(self.store, {"workspaceId": ws["id"], "serviceAccountId": sa["id"]})
        assert resp["name"] == "del-sa"


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GrafanaStore()
        return self._store

    def _create_ws(self):
        handler = _load_handler('CreateWorkspace')
        return handler(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "tags-ws",
            "tags": [{"key": "env", "value": "test"}],
        })

    def test_list_tags(self):
        ws = self._create_ws()
        list_tags = _load_handler('ListTagsForResource')
        resp = list_tags(self.store, {"resourceArn": ws["arn"]})
        assert resp["tags"]["env"] == "test"

    def test_tag_resource(self):
        ws = self._create_ws()
        tag = _load_handler('TagResource')
        tag(self.store, {
            "resourceArn": ws["arn"],
            "tags": [{"key": "owner", "value": "team-a"}],
        })
        list_tags = _load_handler('ListTagsForResource')
        resp = list_tags(self.store, {"resourceArn": ws["arn"]})
        assert resp["tags"]["owner"] == "team-a"
        assert resp["tags"]["env"] == "test"

    def test_untag_resource(self):
        ws = self._create_ws()
        untag = _load_handler('UntagResource')
        untag(self.store, {
            "resourceArn": ws["arn"],
            "tagKeys": ["env"],
        })
        list_tags = _load_handler('ListTagsForResource')
        resp = list_tags(self.store, {"resourceArn": ws["arn"]})
        assert "env" not in resp["tags"]


class TestAuthentication:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GrafanaStore()
        return self._store

    def _create_ws(self):
        handler = _load_handler('CreateWorkspace')
        return handler(self.store, {
            "accountAccessType": "CURRENT_ACCOUNT",
            "permissionType": "SERVICE_MANAGED",
            "authenticationProviders": ["AWS_SSO"],
            "workspaceName": "auth-ws",
        })

    def test_describe_auth(self):
        ws = self._create_ws()
        handler = _load_handler('DescribeWorkspaceAuthentication')
        resp = handler(self.store, {"workspaceId": ws["id"]})
        assert "AWS_SSO" in resp["authentication"]["providers"]

    def test_update_auth(self):
        ws = self._create_ws()
        update = _load_handler('UpdateWorkspaceAuthentication')
        resp = update(self.store, {
            "workspaceId": ws["id"],
            "authenticationProviders": ["AWS_SSO", "SAML"],
        })
        assert "SAML" in resp["authentication"]["providers"]
