"""Integration tests for Amplify — App, Branch, BackendEnvironment, DomainAssociation, Webhook + tags."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'amplify')

def _load_models():
    path = os.path.join(SERVICE_DIR, 'models.code.py')
    spec = importlib.util.spec_from_file_location('amplify_models', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_models = _load_models()
AmplifyStore = _models.AmplifyStore
NotFoundException = _models.NotFoundException
BadRequestException = _models.BadRequestException

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}

def _inject(mod):
    mod.NotFoundException = NotFoundException
    mod.BadRequestException = BadRequestException
    mod.ResourceNotFoundException = _models.ResourceNotFoundException
    mod.LimitExceededException = _models.LimitExceededException
    mod.UnauthorizedException = _models.UnauthorizedException
    mod.InternalFailureException = _models.InternalFailureException
    mod.DependentServiceFailureException = _models.DependentServiceFailureException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f

def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    _inject(mod)
    spec.loader.exec_module(mod)
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType) and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    return None


class TestAppIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AmplifyStore()
        return self._store

    def test_create_app_happy(self):
        h = _load_handler('create-app')
        resp = h(self.store, {"name": "test-app"})
        assert resp["app"]["name"] == "test-app"
        assert "appId" in resp["app"]

    def test_get_app_happy(self):
        create = _load_handler('create-app')
        get = _load_handler('get-app')
        resp = create(self.store, {"name": "getapp"})
        resp2 = get(self.store, {"appId": resp["app"]["appId"]})
        assert resp2["app"]["name"] == "getapp"

    def test_get_app_nonexistent(self):
        h = _load_handler('get-app')
        with pytest.raises(NotFoundException):
            h(self.store, {"appId": "no-such"})

    def test_list_apps(self):
        create = _load_handler('create-app')
        list_h = _load_handler('list-apps')
        create(self.store, {"name": "la1"})
        create(self.store, {"name": "la2"})
        resp = list_h(self.store, {})
        assert len(resp["apps"]) >= 2

    def test_delete_app(self):
        create = _load_handler('create-app')
        delete = _load_handler('delete-app')
        get = _load_handler('get-app')
        resp = create(self.store, {"name": "delapp"})
        aid = resp["app"]["appId"]
        delete(self.store, {"appId": aid})
        with pytest.raises(NotFoundException):
            get(self.store, {"appId": aid})

    def test_update_app(self):
        create = _load_handler('create-app')
        update = _load_handler('update-app')
        resp = create(self.store, {"name": "updapp"})
        aid = resp["app"]["appId"]
        resp2 = update(self.store, {"appId": aid, "description": "updated"})
        assert resp2["app"]["description"] == "updated"


class TestBranchIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AmplifyStore()
            create_a = _load_handler('create-app')
            self._app_resp = create_a(self._store, {"name": "br-app"})
            self._app_id = self._app_resp["app"]["appId"]
        return self._store

    @property
    def app_id(self):
        return self._app_id

    def test_create_branch_happy(self):
        h = _load_handler('create-branch')
        resp = h(self.store, {"appId": self.app_id, "branchName": "main"})
        assert resp["branch"]["branchName"] == "main"

    def test_create_branch_duplicate(self):
        h = _load_handler('create-branch')
        h(self.store, {"appId": self.app_id, "branchName": "dup"})
        with pytest.raises(BadRequestException):
            h(self.store, {"appId": self.app_id, "branchName": "dup"})

    def test_get_branch(self):
        create = _load_handler('create-branch')
        get = _load_handler('get-branch')
        create(self.store, {"appId": self.app_id, "branchName": "get-br"})
        resp = get(self.store, {"appId": self.app_id, "branchName": "get-br"})
        assert resp["branch"]["branchName"] == "get-br"

    def test_list_branches(self):
        h = _load_handler('list-branches')
        resp = h(self.store, {"appId": self.app_id})
        assert isinstance(resp["branches"], list)

    def test_delete_branch(self):
        create = _load_handler('create-branch')
        delete = _load_handler('delete-branch')
        get = _load_handler('get-branch')
        create(self.store, {"appId": self.app_id, "branchName": "del-br"})
        delete(self.store, {"appId": self.app_id, "branchName": "del-br"})
        with pytest.raises(NotFoundException):
            get(self.store, {"appId": self.app_id, "branchName": "del-br"})


class TestBackendEnvironmentIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AmplifyStore()
            create_a = _load_handler('create-app')
            r = create_a(self._store, {"name": "be-app"})
            self._app_id = r["app"]["appId"]
        return self._store

    @property
    def app_id(self):
        return self._app_id

    def test_create_backend_env_happy(self):
        h = _load_handler('create-backend-environment')
        resp = h(self.store, {"appId": self.app_id, "environmentName": "staging"})
        assert resp["backendEnvironment"]["environmentName"] == "staging"

    def test_list_backend_envs(self):
        h = _load_handler('list-backend-environments')
        resp = h(self.store, {"appId": self.app_id})
        assert isinstance(resp["backendEnvironments"], list)

    def test_delete_backend_env(self):
        create = _load_handler('create-backend-environment')
        delete = _load_handler('delete-backend-environment')
        get = _load_handler('get-backend-environment')
        create(self.store, {"appId": self.app_id, "environmentName": "del-be"})
        delete(self.store, {"appId": self.app_id, "environmentName": "del-be"})
        with pytest.raises(NotFoundException):
            get(self.store, {"appId": self.app_id, "environmentName": "del-be"})


class TestDomainAssociationIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AmplifyStore()
            create_a = _load_handler('create-app')
            r = create_a(self._store, {"name": "da-app"})
            self._app_id = r["app"]["appId"]
        return self._store

    @property
    def app_id(self):
        return self._app_id

    def test_create_domain_happy(self):
        h = _load_handler('create-domain-association')
        resp = h(self.store, {
            "appId": self.app_id,
            "domainName": "example.com",
            "subDomainSettings": [{"prefix": "www", "branchName": "main"}]
        })
        assert resp["domainAssociation"]["domainName"] == "example.com"


class TestWebhookIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AmplifyStore()
            create_a = _load_handler('create-app')
            r = create_a(self._store, {"name": "wh-app"})
            self._app_id = r["app"]["appId"]
        return self._store

    @property
    def app_id(self):
        return self._app_id

    def test_create_webhook_happy(self):
        h = _load_handler('create-webhook')
        resp = h(self.store, {"appId": self.app_id, "branchName": "main"})
        assert "webhookId" in resp["webhook"]

    def test_get_webhook(self):
        create = _load_handler('create-webhook')
        get = _load_handler('get-webhook')
        r = create(self.store, {"appId": self.app_id, "branchName": "main"})
        wid = r["webhook"]["webhookId"]
        resp = get(self.store, {"webhookId": wid})
        assert resp["webhook"]["webhookId"] == wid

    def test_list_webhooks(self):
        h = _load_handler('list-webhooks')
        resp = h(self.store, {"appId": self.app_id})
        assert isinstance(resp["webhooks"], list)

    def test_delete_webhook(self):
        create = _load_handler('create-webhook')
        delete = _load_handler('delete-webhook')
        get = _load_handler('get-webhook')
        r = create(self.store, {"appId": self.app_id, "branchName": "main"})
        wid = r["webhook"]["webhookId"]
        delete(self.store, {"webhookId": wid})
        with pytest.raises(NotFoundException):
            get(self.store, {"webhookId": wid})
