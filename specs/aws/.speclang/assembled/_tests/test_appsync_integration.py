"""Integration test for AppSync — real store."""
import os
import importlib.util
import types
import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'appsync')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

AppSyncStore = models_mod.AppSyncStore
GraphqlApiRecord = models_mod.GraphqlApiRecord
ApiKeyRecord = models_mod.ApiKeyRecord
DataSourceRecord = models_mod.DataSourceRecord
ResolverRecord = models_mod.ResolverRecord
BadRequestException = models_mod.BadRequestException
NotFoundException = models_mod.NotFoundException
ConcurrentModificationException = models_mod.ConcurrentModificationException
InternalFailureException = models_mod.InternalFailureException


def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.BadRequestException = BadRequestException
    mod.NotFoundException = NotFoundException
    mod.ConcurrentModificationException = ConcurrentModificationException
    mod.InternalFailureException = InternalFailureException
    mod.GraphqlApiRecord = GraphqlApiRecord
    mod.ApiKeyRecord = ApiKeyRecord
    mod.DataSourceRecord = DataSourceRecord
    mod.ResolverRecord = ResolverRecord
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


def _create_test_api(store):
    h = _load_handler('CreateGraphqlApi')
    resp = h(store, {'name': 'test-api', 'authenticationType': 'API_KEY'})
    return resp['graphqlApi']['apiId']


class TestGraphqlApi:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppSyncStore()
        return self._store

    def test_create_happy(self):
        h = _load_handler('CreateGraphqlApi')
        resp = h(self.store, {'name': 'test-api', 'authenticationType': 'API_KEY'})
        assert resp['graphqlApi']['apiId'] is not None
        assert resp['graphqlApi']['name'] == 'test-api'

    def test_get_happy(self):
        h_c = _load_handler('CreateGraphqlApi')
        h_g = _load_handler('GetGraphqlApi')
        created = h_c(self.store, {'name': 'test-api-2', 'authenticationType': 'API_KEY'})
        resp = h_g(self.store, {'apiId': created['graphqlApi']['apiId']})
        assert resp['graphqlApi']['name'] == 'test-api-2'

    def test_get_nonexistent(self):
        h_g = _load_handler('GetGraphqlApi')
        with pytest.raises(NotFoundException):
            h_g(self.store, {'apiId': 'nonexistent'})

    def test_list(self):
        h_c = _load_handler('CreateGraphqlApi')
        h_l = _load_handler('ListGraphqlApis')
        h_c(self.store, {'name': 'test-api-3', 'authenticationType': 'API_KEY'})
        resp = h_l(self.store, {})
        assert len(resp['graphqlApis']) >= 1

    def test_update(self):
        h_c = _load_handler('CreateGraphqlApi')
        h_u = _load_handler('UpdateGraphqlApi')
        created = h_c(self.store, {'name': 'test-api-4', 'authenticationType': 'API_KEY'})
        resp = h_u(self.store, {'apiId': created['graphqlApi']['apiId'],
                                 'name': 'updated-api', 'authenticationType': 'AWS_IAM'})
        assert resp['graphqlApi']['name'] == 'updated-api'

    def test_delete(self):
        h_c = _load_handler('CreateGraphqlApi')
        h_d = _load_handler('DeleteGraphqlApi')
        h_g = _load_handler('GetGraphqlApi')
        created = h_c(self.store, {'name': 'test-api-5', 'authenticationType': 'API_KEY'})
        h_d(self.store, {'apiId': created['graphqlApi']['apiId']})
        with pytest.raises(NotFoundException):
            h_g(self.store, {'apiId': created['graphqlApi']['apiId']})


class TestApiKey:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppSyncStore()
        return self._store

    @pytest.fixture(autouse=True)
    def setup_api(self):
        self.api_id = _create_test_api(self.store)

    def test_create_happy(self):
        h = _load_handler('CreateApiKey')
        resp = h(self.store, {'apiId': self.api_id, 'description': 'test key'})
        assert resp['apiKey']['id'] is not None
        assert resp['apiKey']['apiId'] == self.api_id

    def test_list(self):
        h_c = _load_handler('CreateApiKey')
        h_l = _load_handler('ListApiKeys')
        h_c(self.store, {'apiId': self.api_id})
        resp = h_l(self.store, {'apiId': self.api_id})
        assert len(resp['apiKeys']) >= 1

    def test_update(self):
        h_c = _load_handler('CreateApiKey')
        h_u = _load_handler('UpdateApiKey')
        created = h_c(self.store, {'apiId': self.api_id, 'description': 'key1'})
        resp = h_u(self.store, {'apiId': self.api_id,
                                 'id': created['apiKey']['id'],
                                 'description': 'updated key'})
        assert resp['apiKey']['description'] == 'updated key'

    def test_delete(self):
        h_c = _load_handler('CreateApiKey')
        h_d = _load_handler('DeleteApiKey')
        h_l = _load_handler('ListApiKeys')
        created = h_c(self.store, {'apiId': self.api_id})
        h_d(self.store, {'apiId': self.api_id, 'id': created['apiKey']['id']})
        resp = h_l(self.store, {'apiId': self.api_id})
        assert len(resp['apiKeys']) == 0


class TestDataSource:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppSyncStore()
        return self._store

    @pytest.fixture(autouse=True)
    def setup_api(self):
        self.api_id = _create_test_api(self.store)

    def test_create_happy(self):
        h = _load_handler('CreateDataSource')
        resp = h(self.store, {'apiId': self.api_id, 'name': 'ds1',
                               'type': 'AWS_LAMBDA'})
        assert resp['dataSource']['name'] == 'ds1'

    def test_create_duplicate(self):
        h = _load_handler('CreateDataSource')
        h(self.store, {'apiId': self.api_id, 'name': 'ds2', 'type': 'NONE'})
        with pytest.raises(ConcurrentModificationException):
            h(self.store, {'apiId': self.api_id, 'name': 'ds2', 'type': 'NONE'})

    def test_get_happy(self):
        h_c = _load_handler('CreateDataSource')
        h_g = _load_handler('GetDataSource')
        h_c(self.store, {'apiId': self.api_id, 'name': 'ds3', 'type': 'NONE'})
        resp = h_g(self.store, {'apiId': self.api_id, 'name': 'ds3'})
        assert resp['dataSource']['name'] == 'ds3'

    def test_get_nonexistent(self):
        h_g = _load_handler('GetDataSource')
        with pytest.raises(NotFoundException):
            h_g(self.store, {'apiId': self.api_id, 'name': 'nonexistent'})

    def test_list(self):
        h_c = _load_handler('CreateDataSource')
        h_l = _load_handler('ListDataSources')
        h_c(self.store, {'apiId': self.api_id, 'name': 'ds4', 'type': 'NONE'})
        resp = h_l(self.store, {'apiId': self.api_id})
        assert len(resp['dataSources']) >= 1

    def test_update(self):
        h_c = _load_handler('CreateDataSource')
        h_u = _load_handler('UpdateDataSource')
        h_c(self.store, {'apiId': self.api_id, 'name': 'ds5', 'type': 'NONE'})
        resp = h_u(self.store, {'apiId': self.api_id, 'name': 'ds5',
                                 'type': 'AMAZON_DYNAMODB'})
        assert resp['dataSource']['type'] == 'AMAZON_DYNAMODB'

    def test_delete(self):
        h_c = _load_handler('CreateDataSource')
        h_d = _load_handler('DeleteDataSource')
        h_g = _load_handler('GetDataSource')
        h_c(self.store, {'apiId': self.api_id, 'name': 'ds6', 'type': 'NONE'})
        h_d(self.store, {'apiId': self.api_id, 'name': 'ds6'})
        with pytest.raises(NotFoundException):
            h_g(self.store, {'apiId': self.api_id, 'name': 'ds6'})


class TestResolver:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppSyncStore()
        return self._store

    @pytest.fixture(autouse=True)
    def setup_api(self):
        self.api_id = _create_test_api(self.store)

    def test_create_happy(self):
        h = _load_handler('CreateResolver')
        resp = h(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                               'fieldName': 'getItem'})
        assert resp['resolver']['fieldName'] == 'getItem'

    def test_create_duplicate(self):
        h = _load_handler('CreateResolver')
        h(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                        'fieldName': 'getItem2'})
        with pytest.raises(ConcurrentModificationException):
            h(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                            'fieldName': 'getItem2'})

    def test_get_happy(self):
        h_c = _load_handler('CreateResolver')
        h_g = _load_handler('GetResolver')
        h_c(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                          'fieldName': 'getItem3'})
        resp = h_g(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                                 'fieldName': 'getItem3'})
        assert resp['resolver']['fieldName'] == 'getItem3'

    def test_get_nonexistent(self):
        h_g = _load_handler('GetResolver')
        with pytest.raises(NotFoundException):
            h_g(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                              'fieldName': 'nonexistent'})

    def test_list(self):
        h_c = _load_handler('CreateResolver')
        h_l = _load_handler('ListResolvers')
        h_c(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                          'fieldName': 'getItem4'})
        resp = h_l(self.store, {'apiId': self.api_id, 'typeName': 'Query'})
        assert len(resp['resolvers']) >= 1

    def test_delete(self):
        h_c = _load_handler('CreateResolver')
        h_d = _load_handler('DeleteResolver')
        h_g = _load_handler('GetResolver')
        h_c(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                          'fieldName': 'getItem5'})
        h_d(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                          'fieldName': 'getItem5'})
        with pytest.raises(NotFoundException):
            h_g(self.store, {'apiId': self.api_id, 'typeName': 'Query',
                              'fieldName': 'getItem5'})


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppSyncStore()
        return self._store

    def test_tag_and_list(self):
        h_t = _load_handler('TagResource')
        h_l = _load_handler('ListTagsForResource')
        arn = 'arn:aws:appsync:us-east-1:123:apis/test'
        h_t(self.store, {'resourceArn': arn,
                          'tags': [{'key': 'env', 'value': 'prod'}]})
        resp = h_l(self.store, {'resourceArn': arn})
        assert resp['tags'].get('env') == 'prod'

    def test_untag(self):
        h_t = _load_handler('TagResource')
        h_u = _load_handler('UntagResource')
        h_l = _load_handler('ListTagsForResource')
        arn = 'arn:aws:appsync:us-east-1:123:apis/test2'
        h_t(self.store, {'resourceArn': arn,
                          'tags': [{'key': 'env', 'value': 'test'},
                                   {'key': 'team', 'value': 'ops'}]})
        h_u(self.store, {'resourceArn': arn, 'tagKeys': ['env']})
        resp = h_l(self.store, {'resourceArn': arn})
        assert 'env' not in resp['tags']
        assert resp['tags'].get('team') == 'ops'

    def test_list_tags_empty(self):
        h_l = _load_handler('ListTagsForResource')
        resp = h_l(self.store, {'resourceArn': 'arn:nonexistent'})
        assert resp['tags'] == {}
