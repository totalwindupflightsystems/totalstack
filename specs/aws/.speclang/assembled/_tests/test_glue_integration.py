"""Integration test for AWS Glue — real GlueStore with generated handlers."""
import pytest
import os
import importlib.util
import types


# ── Module loading ─────────────────────────────────────────────
ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'glue')

# Load models
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

GlueStore = models_mod.GlueStore
EntityNotFoundException = models_mod.EntityNotFoundException
AlreadyExistsException = models_mod.AlreadyExistsException
InvalidInputException = models_mod.InvalidInputException


def _load_handler(op_name):
    """Load a generated .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes (generated code references these without imports)
    mod.EntityNotFoundException = EntityNotFoundException
    mod.AlreadyExistsException = AlreadyExistsException
    mod.InvalidInputException = InvalidInputException
    spec.loader.exec_module(mod)
    # Find the handler function (skip injected classes, imports)
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ != 'dataclass'):
            return v
    raise RuntimeError(f"No handler found in {op_name}.code.py")


# ── Test Classes ──────────────────────────────────────────────

class TestGlueDatabaseIntegration:
    """CreateDatabase + GetDatabase happy path and error paths."""

    @pytest.fixture
    def store(self):
        return GlueStore()

    def test_create_database_happy(self, store):
        handler = _load_handler('create-database')
        response = handler(store, {"Name": "testdb", "Description": "Test database"})
        assert response == {"Name": "testdb"}

    def test_create_database_duplicate(self, store):
        handler = _load_handler('create-database')
        handler(store, {"Name": "testdb"})
        with pytest.raises(AlreadyExistsException):
            handler(store, {"Name": "testdb"})

    def test_create_database_missing_name(self, store):
        handler = _load_handler('create-database')
        with pytest.raises(InvalidInputException):
            handler(store, {})

    def test_get_database_happy(self, store):
        create = _load_handler('create-database')
        get = _load_handler('get-database')
        create(store, {"Name": "testdb", "Description": "Test database"})
        response = get(store, {"Name": "testdb"})
        assert response["Database"]["Name"] == "testdb"
        assert response["Database"]["Description"] == "Test database"

    def test_get_database_nonexistent(self, store):
        handler = _load_handler('get-database')
        with pytest.raises(EntityNotFoundException):
            handler(store, {"Name": "nonexistent"})


class TestGlueJobIntegration:
    """CreateJob happy path and error paths."""

    @pytest.fixture
    def store(self):
        return GlueStore()

    def test_create_job_happy(self, store):
        handler = _load_handler('create-job')
        response = handler(store, {
            "Name": "test-job",
            "Role": "arn:aws:iam::123456789012:role/GlueRole",
            "Command": {"Name": "glueetl", "ScriptLocation": "s3://bucket/script.py"},
        })
        assert response == {"Name": "test-job"}

    def test_create_job_duplicate(self, store):
        handler = _load_handler('create-job')
        handler(store, {"Name": "test-job"})
        with pytest.raises(AlreadyExistsException):
            handler(store, {"Name": "test-job"})

    def test_create_job_missing_name(self, store):
        handler = _load_handler('create-job')
        with pytest.raises(InvalidInputException):
            handler(store, {})

    def test_store_persists_job(self, store):
        """Verify the store actually holds the job after creation."""
        create = _load_handler('create-job')
        create(store, {"Name": "test-job"})
        job = store.jobs("test-job")
        assert job is not None
        assert job["Name"] == "test-job"
