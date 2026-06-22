"""Integration tests for S3 Tables — real store with generated handlers."""
import os
import importlib.util
import types
import pytest
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 's3tables')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
S3TablesStore = models_mod.S3TablesStore
InternalServerErrorException = models_mod.InternalServerErrorException
ForbiddenException = models_mod.ForbiddenException
NotFoundException = models_mod.NotFoundException
AccessDeniedException = models_mod.AccessDeniedException
TooManyRequestsException = models_mod.TooManyRequestsException
ConflictException = models_mod.ConflictException
BadRequestException = models_mod.BadRequestException
TableBucketRecord = models_mod.TableBucketRecord
NamespaceRecord = models_mod.NamespaceRecord
TableRecord = models_mod.TableRecord

# Record classes for handler injection
RECORD_CLASSES = {
    'TableBucketRecord': TableBucketRecord,
    'NamespaceRecord': NamespaceRecord,
    'TableRecord': TableRecord,
}

EXCEPTION_CLASSES = {
    'InternalServerErrorException': InternalServerErrorException,
    'ForbiddenException': ForbiddenException,
    'NotFoundException': NotFoundException,
    'AccessDeniedException': AccessDeniedException,
    'TooManyRequestsException': TooManyRequestsException,
    'ConflictException': ConflictException,
    'BadRequestException': BadRequestException,
}

SKIP_NAMES = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    for exc_name, exc_cls in EXCEPTION_CLASSES.items():
        setattr(mod, exc_name, exc_cls)
    # Inject record classes
    for rec_name, rec_cls in RECORD_CLASSES.items():
        setattr(mod, rec_name, rec_cls)
    # Inject stdlib items
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    # Discover handler function
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in SKIP_NAMES):
            handler = v
            break
    assert handler is not None, f"No handler found in {op_name}"
    return handler


class TestTableBucketIntegration:
    """CRUD for Table Buckets."""

    @pytest.fixture
    def store(self):
        return S3TablesStore()

    def test_create_table_bucket_happy(self, store):
        handler = _load_handler('CreateTableBucket')
        response = handler(store, {"name": "my-bucket"})
        assert response is not None
        assert "arn" in response
        assert "my-bucket" in response["arn"]

    def test_create_table_bucket_with_tags(self, store):
        handler = _load_handler('CreateTableBucket')
        response = handler(store, {
            "name": "tagged-bucket",
            "tags": [{"key": "env", "value": "test"}],
        })
        assert "arn" in response

    def test_create_table_bucket_duplicate(self, store):
        handler = _load_handler('CreateTableBucket')
        handler(store, {"name": "dup-bucket"})
        with pytest.raises(ConflictException):
            handler(store, {"name": "dup-bucket"})

    def test_get_table_bucket_happy(self, store):
        create = _load_handler('CreateTableBucket')
        get = _load_handler('GetTableBucket')
        resp = create(store, {"name": "get-bucket"})
        response = get(store, {"tableBucketARN": resp["arn"]})
        assert response["name"] == "get-bucket"
        assert "tableBucketId" in response
        assert "createdAt" in response

    def test_get_table_bucket_nonexistent(self, store):
        handler = _load_handler('GetTableBucket')
        with pytest.raises(NotFoundException):
            handler(store, {"tableBucketARN": "arn:aws:s3tables:::bucket/nonexistent"})

    def test_delete_table_bucket_happy(self, store):
        create = _load_handler('CreateTableBucket')
        delete = _load_handler('DeleteTableBucket')
        get = _load_handler('GetTableBucket')
        resp = create(store, {"name": "del-bucket"})
        delete(store, {"tableBucketARN": resp["arn"]})
        with pytest.raises(NotFoundException):
            get(store, {"tableBucketARN": resp["arn"]})

    def test_delete_table_bucket_nonexistent(self, store):
        handler = _load_handler('DeleteTableBucket')
        with pytest.raises(NotFoundException):
            handler(store, {"tableBucketARN": "arn:aws:s3tables:::bucket/nonexistent"})

    def test_list_table_buckets_empty(self, store):
        handler = _load_handler('ListTableBuckets')
        response = handler(store, {})
        assert response["tableBuckets"] == []

    def test_list_table_buckets_populated(self, store):
        create = _load_handler('CreateTableBucket')
        list_h = _load_handler('ListTableBuckets')
        create(store, {"name": "bucket-a"})
        create(store, {"name": "bucket-b"})
        response = list_h(store, {})
        assert len(response["tableBuckets"]) == 2

    def test_list_table_buckets_prefix(self, store):
        create = _load_handler('CreateTableBucket')
        list_h = _load_handler('ListTableBuckets')
        create(store, {"name": "prod-bucket"})
        create(store, {"name": "dev-bucket"})
        response = list_h(store, {"prefix": "prod"})
        assert len(response["tableBuckets"]) == 1


class TestNamespaceIntegration:
    """CRUD for Namespaces within a Table Bucket."""

    @pytest.fixture
    def store_with_bucket(self):
        store = S3TablesStore()
        create_bucket = _load_handler('CreateTableBucket')
        resp = create_bucket(store, {"name": "ns-bucket"})
        store._bucket_arn = resp["arn"]
        return store

    def test_create_namespace_happy(self, store_with_bucket):
        store = store_with_bucket
        handler = _load_handler('CreateNamespace')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": ["my-namespace"],
        })
        assert "namespace" in response
        assert "my-namespace" in response["namespace"]

    def test_create_namespace_multiple(self, store_with_bucket):
        store = store_with_bucket
        handler = _load_handler('CreateNamespace')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": ["ns-a", "ns-b"],
        })
        assert len(response["namespace"]) == 2

    def test_create_namespace_duplicate(self, store_with_bucket):
        store = store_with_bucket
        handler = _load_handler('CreateNamespace')
        handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": ["dup-ns"],
        })
        with pytest.raises(ConflictException):
            handler(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": ["dup-ns"],
            })

    def test_create_namespace_bucket_not_found(self, store_with_bucket):
        store = store_with_bucket
        handler = _load_handler('CreateNamespace')
        with pytest.raises(NotFoundException):
            handler(store, {
                "tableBucketARN": "arn:aws:s3tables:::bucket/nonexistent",
                "namespace": ["test"],
            })

    def test_get_namespace_happy(self, store_with_bucket):
        store = store_with_bucket
        create = _load_handler('CreateNamespace')
        get = _load_handler('GetNamespace')
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": ["get-ns"],
        })
        response = get(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": "get-ns",
        })
        assert "namespace" in response

    def test_get_namespace_nonexistent(self, store_with_bucket):
        store = store_with_bucket
        handler = _load_handler('GetNamespace')
        with pytest.raises(NotFoundException):
            handler(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": "nonexistent",
            })

    def test_delete_namespace_happy(self, store_with_bucket):
        store = store_with_bucket
        create = _load_handler('CreateNamespace')
        delete = _load_handler('DeleteNamespace')
        get = _load_handler('GetNamespace')
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": ["del-ns"],
        })
        delete(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": "del-ns",
        })
        with pytest.raises(NotFoundException):
            get(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": "del-ns",
            })

    def test_list_namespaces_empty(self, store_with_bucket):
        store = store_with_bucket
        handler = _load_handler('ListNamespaces')
        response = handler(store, {"tableBucketARN": store._bucket_arn})
        assert response["namespaces"] == []

    def test_list_namespaces_populated(self, store_with_bucket):
        store = store_with_bucket
        create = _load_handler('CreateNamespace')
        list_h = _load_handler('ListNamespaces')
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": ["ns-1"],
        })
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": ["ns-2"],
        })
        response = list_h(store, {"tableBucketARN": store._bucket_arn})
        assert len(response["namespaces"]) == 2


class TestTableIntegration:
    """CRUD for Tables within a Namespace."""

    @pytest.fixture
    def store_with_ns(self):
        store = S3TablesStore()
        create_bucket = _load_handler('CreateTableBucket')
        create_ns = _load_handler('CreateNamespace')
        resp = create_bucket(store, {"name": "table-bucket"})
        create_ns(store, {
            "tableBucketARN": resp["arn"],
            "namespace": ["table-ns"],
        })
        store._bucket_arn = resp["arn"]
        store._namespace = "table-ns"
        return store

    def test_create_table_happy(self, store_with_ns):
        store = store_with_ns
        handler = _load_handler('CreateTable')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "my-table",
            "format": "ICEBERG",
        })
        assert response["name"] == "my-table"
        assert response["format"] == "ICEBERG"

    def test_create_table_duplicate(self, store_with_ns):
        store = store_with_ns
        handler = _load_handler('CreateTable')
        handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "dup-table",
        })
        with pytest.raises(ConflictException):
            handler(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": store._namespace,
                "name": "dup-table",
            })

    def test_create_table_namespace_not_found(self, store_with_ns):
        store = store_with_ns
        handler = _load_handler('CreateTable')
        with pytest.raises(NotFoundException):
            handler(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": "nonexistent",
                "name": "test-table",
            })

    def test_get_table_happy(self, store_with_ns):
        store = store_with_ns
        create = _load_handler('CreateTable')
        get = _load_handler('GetTable')
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "get-table",
        })
        response = get(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "get-table",
        })
        assert response["name"] == "get-table"

    def test_get_table_nonexistent(self, store_with_ns):
        store = store_with_ns
        handler = _load_handler('GetTable')
        with pytest.raises(NotFoundException):
            handler(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": store._namespace,
                "name": "nonexistent",
            })

    def test_delete_table_happy(self, store_with_ns):
        store = store_with_ns
        create = _load_handler('CreateTable')
        delete = _load_handler('DeleteTable')
        get = _load_handler('GetTable')
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "del-table",
        })
        delete(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "del-table",
        })
        with pytest.raises(NotFoundException):
            get(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": store._namespace,
                "name": "del-table",
            })

    def test_list_tables_empty(self, store_with_ns):
        store = store_with_ns
        handler = _load_handler('ListTables')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
        })
        assert response["tables"] == []

    def test_list_tables_populated(self, store_with_ns):
        store = store_with_ns
        create = _load_handler('CreateTable')
        list_h = _load_handler('ListTables')
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "table-a",
        })
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "table-b",
        })
        response = list_h(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
        })
        assert len(response["tables"]) == 2

    def test_rename_table_happy(self, store_with_ns):
        store = store_with_ns
        create = _load_handler('CreateTable')
        rename = _load_handler('RenameTable')
        get = _load_handler('GetTable')
        create(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "old-name",
        })
        response = rename(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": "old-name",
            "newName": "new-name",
        })
        assert response["name"] == "new-name"
        # Old name should not exist
        with pytest.raises(NotFoundException):
            get(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": store._namespace,
                "name": "old-name",
            })

    def test_rename_table_nonexistent(self, store_with_ns):
        store = store_with_ns
        handler = _load_handler('RenameTable')
        with pytest.raises(NotFoundException):
            handler(store, {
                "tableBucketARN": store._bucket_arn,
                "namespace": store._namespace,
                "name": "nonexistent",
                "newName": "whatever",
            })


class TestEncryptionAndMaintenance:
    """Read-only encryption and maintenance operations."""

    @pytest.fixture
    def store_with_table(self):
        store = S3TablesStore()
        create_bucket = _load_handler('CreateTableBucket')
        create_ns = _load_handler('CreateNamespace')
        create_table = _load_handler('CreateTable')
        resp = create_bucket(store, {
            "name": "enc-bucket",
            "encryptionConfiguration": {"sseType": "SSE_S3"},
        })
        bucket_arn = resp["arn"]
        create_ns(store, {
            "tableBucketARN": bucket_arn,
            "namespace": ["enc-ns"],
        })
        create_table(store, {
            "tableBucketARN": bucket_arn,
            "namespace": "enc-ns",
            "name": "enc-table",
        })
        store._bucket_arn = bucket_arn
        store._namespace = "enc-ns"
        store._table = "enc-table"
        return store

    def test_get_table_encryption(self, store_with_table):
        store = store_with_table
        handler = _load_handler('GetTableEncryption')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": store._table,
        })
        assert isinstance(response, dict)

    def test_get_table_bucket_encryption(self, store_with_table):
        store = store_with_table
        handler = _load_handler('GetTableBucketEncryption')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
        })
        assert isinstance(response, dict)

    def test_get_table_maintenance_configuration(self, store_with_table):
        store = store_with_table
        handler = _load_handler('GetTableMaintenanceConfiguration')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
            "namespace": store._namespace,
            "name": store._table,
        })
        assert isinstance(response, dict)

    def test_get_table_bucket_maintenance_configuration(self, store_with_table):
        store = store_with_table
        handler = _load_handler('GetTableBucketMaintenanceConfiguration')
        response = handler(store, {
            "tableBucketARN": store._bucket_arn,
        })
        assert isinstance(response, dict)


class TestTagOperations:
    """Tag resource operations."""

    @pytest.fixture
    def store_with_tagged(self):
        store = S3TablesStore()
        create_bucket = _load_handler('CreateTableBucket')
        resp = create_bucket(store, {
            "name": "tag-bucket",
            "tags": [{"key": "env", "value": "test"}],
        })
        store._arn = resp["arn"]
        return store

    def test_tag_resource(self, store_with_tagged):
        store = store_with_tagged
        handler = _load_handler('TagResource')
        response = handler(store, {
            "resourceArn": store._arn,
            "tags": [{"key": "team", "value": "platform"}],
        })
        assert response == {}
        # Verify via list
        list_h = _load_handler('ListTagsForResource')
        tags_resp = list_h(store, {"resourceArn": store._arn})
        tags = {t["key"]: t["value"] for t in tags_resp["tags"]}
        assert tags.get("team") == "platform"

    def test_untag_resource(self, store_with_tagged):
        store = store_with_tagged
        tag_handler = _load_handler('TagResource')
        untag_handler = _load_handler('UntagResource')
        list_handler = _load_handler('ListTagsForResource')
        tag_handler(store, {
            "resourceArn": store._arn,
            "tags": [{"key": "temp", "value": "remove-me"}],
        })
        untag_handler(store, {
            "resourceArn": store._arn,
            "tagKeys": ["temp"],
        })
        tags_resp = list_handler(store, {"resourceArn": store._arn})
        tags = {t["key"]: t["value"] for t in tags_resp["tags"]}
        assert "temp" not in tags

    def test_list_tags_for_resource(self, store_with_tagged):
        store = store_with_tagged
        handler = _load_handler('ListTagsForResource')
        response = handler(store, {"resourceArn": store._arn})
        assert "tags" in response
        tags = {t["key"]: t["value"] for t in response["tags"]}
        assert tags.get("env") == "test"
