"""Integration test for Keyspaces — real store with 3 entities."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'keyspaces')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

KeyspacesStore = models_mod.KeyspacesStore
ConflictException = models_mod.ConflictException
ResourceNotFoundException = models_mod.ResourceNotFoundException

EXCEPTIONS = {
    "ConflictException": ConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
}

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    for k, v in EXCEPTIONS.items():
        setattr(mod, k, v)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestKeyspace:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KeyspacesStore()
        return self._store

    def test_create_keyspace(self):
        h = _load_handler('CreateKeyspace')
        resp = h(self.store, {"keyspaceName": "test_ks"})
        assert resp["keyspaceName"] == "test_ks"

    def test_create_duplicate(self):
        h = _load_handler('CreateKeyspace')
        h(self.store, {"keyspaceName": "dup_ks"})
        with pytest.raises(ConflictException):
            h(self.store, {"keyspaceName": "dup_ks"})

    def test_get(self):
        h = _load_handler('CreateKeyspace')
        h(self.store, {"keyspaceName": "get_ks"})
        gh = _load_handler('GetKeyspace')
        resp = gh(self.store, {"keyspaceName": "get_ks"})
        assert resp["keyspaceName"] == "get_ks"

    def test_get_nonexistent(self):
        gh = _load_handler('GetKeyspace')
        with pytest.raises(ResourceNotFoundException):
            gh(self.store, {"keyspaceName": "nonexistent"})

    def test_list(self):
        h = _load_handler('CreateKeyspace')
        h(self.store, {"keyspaceName": "ks1"})
        h(self.store, {"keyspaceName": "ks2"})
        lh = _load_handler('ListKeyspaces')
        resp = lh(self.store, {})
        assert len(resp["keyspaces"]) == 2

    def test_delete(self):
        h = _load_handler('CreateKeyspace')
        h(self.store, {"keyspaceName": "del_ks"})
        dh = _load_handler('DeleteKeyspace')
        dh(self.store, {"keyspaceName": "del_ks"})
        gh = _load_handler('GetKeyspace')
        with pytest.raises(ResourceNotFoundException):
            gh(self.store, {"keyspaceName": "del_ks"})


class TestTable:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KeyspacesStore()
        return self._store

    def _create_keyspace(self, name="table_ks"):
        h = _load_handler('CreateKeyspace')
        h(self.store, {"keyspaceName": name})

    def test_create_table(self):
        self._create_keyspace()
        h = _load_handler('CreateTable')
        resp = h(self.store, {
            "keyspaceName": "table_ks",
            "tableName": "test_table",
            "schemaDefinition": {
                "allColumns": [
                    {"name": "id", "type": "uuid"},
                    {"name": "name", "type": "text"},
                ],
                "partitionKeys": [{"name": "id"}],
            },
        })
        assert resp["tableName"] == "test_table"

    def test_create_table_missing_keyspace(self):
        h = _load_handler('CreateTable')
        with pytest.raises(ResourceNotFoundException):
            h(self.store, {
                "keyspaceName": "nonexistent",
                "tableName": "t",
                "schemaDefinition": {
                    "allColumns": [{"name": "id", "type": "uuid"}],
                    "partitionKeys": [{"name": "id"}],
                },
            })

    def test_get_table(self):
        self._create_keyspace("gt_ks")
        h = _load_handler('CreateTable')
        h(self.store, {
            "keyspaceName": "gt_ks", "tableName": "gt_table",
            "schemaDefinition": {
                "allColumns": [{"name": "id", "type": "uuid"}],
                "partitionKeys": [{"name": "id"}],
            },
        })
        gh = _load_handler('GetTable')
        resp = gh(self.store, {"keyspaceName": "gt_ks", "tableName": "gt_table"})
        assert resp["tableName"] == "gt_table"

    def test_list_tables(self):
        self._create_keyspace("lt_ks")
        h = _load_handler('CreateTable')
        h(self.store, {
            "keyspaceName": "lt_ks", "tableName": "t1",
            "schemaDefinition": {
                "allColumns": [{"name": "id", "type": "uuid"}],
                "partitionKeys": [{"name": "id"}],
            },
        })
        lh = _load_handler('ListTables')
        resp = lh(self.store, {"keyspaceName": "lt_ks"})
        assert len(resp["tables"]) == 1

    def test_delete_table(self):
        self._create_keyspace("dt_ks")
        h = _load_handler('CreateTable')
        h(self.store, {
            "keyspaceName": "dt_ks", "tableName": "dt_table",
            "schemaDefinition": {
                "allColumns": [{"name": "id", "type": "uuid"}],
                "partitionKeys": [{"name": "id"}],
            },
        })
        dh = _load_handler('DeleteTable')
        dh(self.store, {"keyspaceName": "dt_ks", "tableName": "dt_table"})
        gh = _load_handler('GetTable')
        with pytest.raises(ResourceNotFoundException):
            gh(self.store, {"keyspaceName": "dt_ks", "tableName": "dt_table"})


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KeyspacesStore()
        return self._store

    def test_tag_and_list(self):
        h = _load_handler('TagResource')
        arn = "arn:aws:cassandra:us-east-1:000000000000:/keyspace/myks"
        h(self.store, {"resourceArn": arn, "tags": [{"key": "env", "value": "prod"}]})
        lh = _load_handler('ListTagsForResource')
        resp = lh(self.store, {"resourceArn": arn})
        assert resp["tags"][0]["key"] == "env"

    def test_untag(self):
        arn = "arn:aws:cassandra:us-east-1:000000000000:/keyspace/myks"
        h = _load_handler('TagResource')
        h(self.store, {"resourceArn": arn, "tags": [{"key": "env", "value": "prod"}]})
        uh = _load_handler('UntagResource')
        uh(self.store, {"resourceArn": arn, "tags": [{"tagKey": "env"}]})
        lh = _load_handler('ListTagsForResource')
        resp = lh(self.store, {"resourceArn": arn})
        assert len(resp["tags"]) == 0
