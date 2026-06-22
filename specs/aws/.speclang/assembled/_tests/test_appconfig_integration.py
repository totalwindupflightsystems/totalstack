"""Integration test for AppConfig."""
import os
import importlib.util
import types
import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'appconfig')

ms = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
mm = importlib.util.module_from_spec(ms)
ms.loader.exec_module(mm)

AppConfigStore = mm.AppConfigStore
BadRequestException = mm.BadRequestException
ResourceNotFoundException = mm.ResourceNotFoundException
ConflictException = mm.ConflictException

def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.BadRequestException = BadRequestException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    spec.loader.exec_module(mod)
    for v in mod.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ != '<lambda>':
            return v
    return None

def _create_app(store):
    return _load_handler('CreateApplication')(store, {'name': 'test-app'})['id']


class TestApplication:
    _store = None
    @property
    def store(self):
        if self._store is None:
            self._store = AppConfigStore()
        return self._store

    def test_create(self):
        r = _load_handler('CreateApplication')(self.store, {'name': 'test-app'})
        assert r['id'] is not None and r['name'] == 'test-app'

    def test_get(self):
        aid = _create_app(self.store)
        r = _load_handler('GetApplication')(self.store, {'applicationId': aid})
        assert r['name'] == 'test-app'

    def test_get_nonexistent(self):
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetApplication')(self.store, {'applicationId': 'nonexistent'})

    def test_list(self):
        _create_app(self.store)
        r = _load_handler('ListApplications')(self.store, {})
        assert len(r['items']) >= 1

    def test_update(self):
        aid = _create_app(self.store)
        r = _load_handler('UpdateApplication')(self.store, {'applicationId': aid, 'name': 'updated'})
        assert r['name'] == 'updated'

    def test_delete(self):
        aid = _create_app(self.store)
        _load_handler('DeleteApplication')(self.store, {'applicationId': aid})
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetApplication')(self.store, {'applicationId': aid})


class TestConfigProfile:
    _store = None
    @property
    def store(self):
        if self._store is None:
            self._store = AppConfigStore()
        return self._store

    @pytest.fixture(autouse=True)
    def setup(self):
        self.aid = _create_app(self.store)

    def test_create(self):
        r = _load_handler('CreateConfigurationProfile')(self.store, {'applicationId': self.aid, 'name': 'cp1', 'locationUri': 'hosted'})
        assert r['name'] == 'cp1'

    def test_create_duplicate(self):
        _load_handler('CreateConfigurationProfile')(self.store, {'applicationId': self.aid, 'name': 'cp2', 'locationUri': 'hosted'})
        # Duplicate creates are allowed (just different IDs)

    def test_get(self):
        r = _load_handler('CreateConfigurationProfile')(self.store, {'applicationId': self.aid, 'name': 'cp3', 'locationUri': 'hosted'})
        r2 = _load_handler('GetConfigurationProfile')(self.store, {'applicationId': self.aid, 'configurationProfileId': r['id']})
        assert r2['name'] == 'cp3'

    def test_list(self):
        _load_handler('CreateConfigurationProfile')(self.store, {'applicationId': self.aid, 'name': 'cp4', 'locationUri': 'hosted'})
        r = _load_handler('ListConfigurationProfiles')(self.store, {'applicationId': self.aid})
        assert len(r['items']) >= 1

    def test_delete(self):
        r = _load_handler('CreateConfigurationProfile')(self.store, {'applicationId': self.aid, 'name': 'cp5', 'locationUri': 'hosted'})
        _load_handler('DeleteConfigurationProfile')(self.store, {'applicationId': self.aid, 'configurationProfileId': r['id']})
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetConfigurationProfile')(self.store, {'applicationId': self.aid, 'configurationProfileId': r['id']})


class TestEnvironment:
    _store = None
    @property
    def store(self):
        if self._store is None:
            self._store = AppConfigStore()
        return self._store

    @pytest.fixture(autouse=True)
    def setup(self):
        self.aid = _create_app(self.store)

    def test_create(self):
        r = _load_handler('CreateEnvironment')(self.store, {'applicationId': self.aid, 'name': 'prod'})
        assert r['name'] == 'prod'

    def test_get(self):
        r = _load_handler('CreateEnvironment')(self.store, {'applicationId': self.aid, 'name': 'staging'})
        r2 = _load_handler('GetEnvironment')(self.store, {'applicationId': self.aid, 'environmentId': r['id']})
        assert r2['name'] == 'staging'

    def test_list(self):
        _load_handler('CreateEnvironment')(self.store, {'applicationId': self.aid, 'name': 'dev'})
        r = _load_handler('ListEnvironments')(self.store, {'applicationId': self.aid})
        assert len(r['items']) >= 1

    def test_delete(self):
        r = _load_handler('CreateEnvironment')(self.store, {'applicationId': self.aid, 'name': 'test'})
        _load_handler('DeleteEnvironment')(self.store, {'applicationId': self.aid, 'environmentId': r['id']})
        with pytest.raises(ResourceNotFoundException):
            _load_handler('GetEnvironment')(self.store, {'applicationId': self.aid, 'environmentId': r['id']})


class TestTags:
    _store = None
    @property
    def store(self):
        if self._store is None:
            self._store = AppConfigStore()
        return self._store

    def test_tag_and_list(self):
        _load_handler('TagResource')(self.store, {'resourceArn': 'arn:test', 'tags': [{'key': 'env', 'value': 'prod'}]})
        r = _load_handler('ListTagsForResource')(self.store, {'resourceArn': 'arn:test'})
        assert r['tags'].get('env') == 'prod'

    def test_untag(self):
        arn = 'arn:test2'
        _load_handler('TagResource')(self.store, {'resourceArn': arn, 'tags': [{'key': 'a', 'value': '1'}, {'key': 'b', 'value': '2'}]})
        _load_handler('UntagResource')(self.store, {'resourceArn': arn, 'tagKeys': ['a']})
        r = _load_handler('ListTagsForResource')(self.store, {'resourceArn': arn})
        assert 'a' not in r['tags'] and r['tags'].get('b') == '2'
