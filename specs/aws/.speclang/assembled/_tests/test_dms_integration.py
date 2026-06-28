"""Integration tests for DMS — 3 entities."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "dms")

models_spec = importlib.util.spec_from_file_location("models", os.path.join(SERVICE_DIR, "models.code.py"))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)
DMSStore = models_mod.DMSStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceAlreadyExistsException = models_mod.ResourceAlreadyExistsException
InvalidResourceStateException = models_mod.InvalidResourceStateException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceAlreadyExistsException = ResourceAlreadyExistsException
    mod.InvalidResourceStateException = InvalidResourceStateException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {"dataclass", "time", "uuid", "<lambda>"}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType) and not v.__name__.startswith("_") and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler in {op_name}")


class TestReplicationInstance:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DMSStore()
        return self._store

    def test_create_instance(self):
        h = _load_handler("create-replication-instance")
        resp = h(self.store, {"ReplicationInstanceIdentifier": "ri-1", "ReplicationInstanceClass": "dms.t3.medium"})
        assert resp["ReplicationInstanceIdentifier"] == "ri-1"

    def test_create_instance_duplicate(self):
        h = _load_handler("create-replication-instance")
        h(self.store, {"ReplicationInstanceIdentifier": "ri-dup"})
        with pytest.raises(ResourceAlreadyExistsException):
            h(self.store, {"ReplicationInstanceIdentifier": "ri-dup"})

    def test_describe_instances(self):
        create = _load_handler("create-replication-instance")
        desc = _load_handler("describe-replication-instances")
        create(self.store, {"ReplicationInstanceIdentifier": "ri-a"})
        create(self.store, {"ReplicationInstanceIdentifier": "ri-b"})
        assert len(desc(self.store, {})["ReplicationInstances"]) >= 2

    def test_delete_instance(self):
        create = _load_handler("create-replication-instance")
        delete = _load_handler("delete-replication-instance")
        desc = _load_handler("describe-replication-instances")
        create(self.store, {"ReplicationInstanceIdentifier": "ri-del"})
        delete(self.store, {"ReplicationInstanceIdentifier": "ri-del"})
        assert len(desc(self.store, {})["ReplicationInstances"]) == 0


class TestEndpoint:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DMSStore()
        return self._store

    def test_create_endpoint(self):
        h = _load_handler("create-endpoint")
        resp = h(self.store, {"EndpointIdentifier": "ep-1", "EngineName": "mysql", "EndpointType": "source"})
        assert resp["EndpointIdentifier"] == "ep-1"

    def test_create_endpoint_duplicate(self):
        h = _load_handler("create-endpoint")
        h(self.store, {"EndpointIdentifier": "ep-dup"})
        with pytest.raises(ResourceAlreadyExistsException):
            h(self.store, {"EndpointIdentifier": "ep-dup"})

    def test_describe_endpoints(self):
        create = _load_handler("create-endpoint")
        desc = _load_handler("describe-endpoints")
        create(self.store, {"EndpointIdentifier": "ep-a"})
        create(self.store, {"EndpointIdentifier": "ep-b"})
        assert len(desc(self.store, {})["Endpoints"]) >= 2

    def test_delete_endpoint(self):
        create = _load_handler("create-endpoint")
        delete = _load_handler("delete-endpoint")
        desc = _load_handler("describe-endpoints")
        create(self.store, {"EndpointIdentifier": "ep-del"})
        delete(self.store, {"EndpointIdentifier": "ep-del"})
        assert len(desc(self.store, {})["Endpoints"]) == 0


class TestReplicationTask:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DMSStore()
        return self._store

    def test_create_task(self):
        h = _load_handler("create-replication-task")
        resp = h(self.store, {"ReplicationTaskIdentifier": "task-1"})
        assert resp["ReplicationTaskIdentifier"] == "task-1"

    def test_create_task_duplicate(self):
        h = _load_handler("create-replication-task")
        h(self.store, {"ReplicationTaskIdentifier": "task-dup"})
        with pytest.raises(ResourceAlreadyExistsException):
            h(self.store, {"ReplicationTaskIdentifier": "task-dup"})

    def test_describe_tasks(self):
        create = _load_handler("create-replication-task")
        desc = _load_handler("describe-replication-tasks")
        create(self.store, {"ReplicationTaskIdentifier": "task-a"})
        create(self.store, {"ReplicationTaskIdentifier": "task-b"})
        assert len(desc(self.store, {})["ReplicationTasks"]) >= 2

    def test_start_stop_task(self):
        create = _load_handler("create-replication-task")
        start = _load_handler("start-replication-task")
        stop = _load_handler("stop-replication-task")
        desc = _load_handler("describe-replication-tasks")
        create(self.store, {"ReplicationTaskIdentifier": "task-s"})
        start(self.store, {"ReplicationTaskIdentifier": "task-s"})
        assert [t for t in desc(self.store, {})["ReplicationTasks"] if t["Status"] == "running"]
        stop(self.store, {"ReplicationTaskIdentifier": "task-s"})
        assert [t for t in desc(self.store, {})["ReplicationTasks"] if t["Status"] == "stopped"]

    def test_delete_task(self):
        create = _load_handler("create-replication-task")
        delete = _load_handler("delete-replication-task")
        desc = _load_handler("describe-replication-tasks")
        create(self.store, {"ReplicationTaskIdentifier": "task-del"})
        delete(self.store, {"ReplicationTaskIdentifier": "task-del"})
        assert len(desc(self.store, {})["ReplicationTasks"]) == 0
