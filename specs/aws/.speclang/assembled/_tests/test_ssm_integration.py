"""Integration tests for SSM Parameter Store."""
import os
import importlib.util
import types
import pytest
ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'ssm')

models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)
SsmStore = models_mod.SsmStore
ParameterNotFound = models_mod.ParameterNotFound
ParameterAlreadyExists = models_mod.ParameterAlreadyExists

def _load(name):
    path = os.path.join(SERVICE_DIR, name + '.code.py')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for v in mod.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ != '<lambda>':
            return v
    return None

class TestSSM:
    @pytest.fixture
    def store(self):
        return SsmStore()

    def test_put_get(self, store):
        _load('putparameter')(store, {'Name': '/app/config', 'Value': '42', 'Type': 'String'})
        r = _load('getparameter')(store, {'Name': '/app/config'})
        assert r['Parameter']['Value'] == '42'

    def test_put_duplicate(self, store):
        _load('putparameter')(store, {'Name': '/app/config', 'Value': '42'})
        with pytest.raises(ParameterAlreadyExists):
            _load('putparameter')(store, {'Name': '/app/config', 'Value': '43'})

    def test_put_overwrite(self, store):
        _load('putparameter')(store, {'Name': '/app/config', 'Value': 'v1'})
        _load('putparameter')(store, {'Name': '/app/config', 'Value': 'v2', 'Overwrite': True})
        r = _load('getparameter')(store, {'Name': '/app/config'})
        assert r['Parameter']['Value'] == 'v2'

    def test_get_parameters(self, store):
        _load('putparameter')(store, {'Name': '/p1', 'Value': 'a'})
        _load('putparameter')(store, {'Name': '/p2', 'Value': 'b'})
        r = _load('getparameters')(store, {'Names': ['/p1', '/p2']})
        assert len(r['Parameters']) == 2

    def test_describe(self, store):
        _load('putparameter')(store, {'Name': '/p1', 'Value': 'a'})
        _load('putparameter')(store, {'Name': '/p2', 'Value': 'b'})
        r = _load('describeparameters')(store, {})
        assert len(r['Parameters']) == 2

    def test_delete(self, store):
        _load('putparameter')(store, {'Name': '/tmp', 'Value': 'x'})
        _load('deleteparameter')(store, {'Name': '/tmp'})
        with pytest.raises(ParameterNotFound):
            _load('getparameter')(store, {'Name': '/tmp'})

    def test_nonexistent(self, store):
        with pytest.raises(ParameterNotFound):
            _load('getparameter')(store, {'Name': '/ghost'})

    def test_history(self, store):
        _load('putparameter')(store, {'Name': '/h1', 'Value': 'v1'})
        _load('putparameter')(store, {'Name': '/h1', 'Value': 'v2', 'Overwrite': True})
        r = _load('getparameterhistory')(store, {'Name': '/h1'})
        assert len(r['Parameters']) >= 2

    def test_tags(self, store):
        _load('addtagstoresource')(store, {'ResourceId': 'arn:ssm:param', 'Tags': [{'Key': 'env', 'Value': 'prod'}]})
        r = _load('listtagsforresource')(store, {'ResourceId': 'arn:ssm:param'})
        assert r['TagList'][0]['Key'] == 'env'
        _load('removetagsfromresource')(store, {'ResourceId': 'arn:ssm:param', 'TagKeys': ['env']})
        r = _load('listtagsforresource')(store, {'ResourceId': 'arn:ssm:param'})
        assert len(r['TagList']) == 0

