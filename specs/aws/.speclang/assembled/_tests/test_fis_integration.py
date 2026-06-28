"""Integration tests for FIS."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "fis")

models_spec = importlib.util.spec_from_file_location("models", os.path.join(SERVICE_DIR, "models.code.py"))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)
FISStore = models_mod.FISStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {"dataclass", "time", "uuid", "<lambda>"}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType) and not v.__name__.startswith("_") and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler in {op_name}")


class TestExperimentTemplate:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FISStore()
        return self._store

    def test_create_template(self):
        h = _load_handler("create-experiment-template")
        resp = h(self.store, {"id": "ext-1", "description": "test", "roleArn": "arn:aws:iam::role"})
        assert resp["id"] == "ext-1"

    def test_describe_template(self):
        create = _load_handler("create-experiment-template")
        describe = _load_handler("describe-experiment-template")
        create(self.store, {"id": "ext-2", "description": "d", "roleArn": "arn"})
        resp = describe(self.store, {"id": "ext-2"})
        assert resp["id"] == "ext-2"

    def test_list_templates(self):
        create = _load_handler("create-experiment-template")
        lst = _load_handler("list-experiment-templates")
        create(self.store, {"id": "t1", "description": "", "roleArn": ""})
        create(self.store, {"id": "t2", "description": "", "roleArn": ""})
        assert len(lst(self.store, {})["experimentTemplates"]) >= 2

    def test_delete_template(self):
        create = _load_handler("create-experiment-template")
        delete = _load_handler("delete-experiment-template")
        describe = _load_handler("describe-experiment-template")
        create(self.store, {"id": "td", "description": "", "roleArn": ""})
        delete(self.store, {"id": "td"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"id": "td"})

    def test_update_template(self):
        create = _load_handler("create-experiment-template")
        update = _load_handler("update-experiment-template")
        describe = _load_handler("describe-experiment-template")
        create(self.store, {"id": "tu", "description": "old", "roleArn": ""})
        update(self.store, {"id": "tu", "description": "new"})
        assert describe(self.store, {"id": "tu"})["description"] == "new"


class TestExperiment:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FISStore()
        return self._store

    def test_start_experiment(self):
        h = _load_handler("start-experiment")
        resp = h(self.store, {"experimentTemplateId": "ext-t1"})
        assert resp["status"] == "running"
        assert "id" in resp

    def test_describe_experiment(self):
        start = _load_handler("start-experiment")
        describe = _load_handler("describe-experiment")
        resp = start(self.store, {"experimentTemplateId": "ext-t2"})
        desc = describe(self.store, {"id": resp["id"]})
        assert desc["id"] == resp["id"]

    def test_list_experiments(self):
        start = _load_handler("start-experiment")
        lst = _load_handler("list-experiments")
        start(self.store, {"experimentTemplateId": "ext-e1"})
        start(self.store, {"experimentTemplateId": "ext-e2"})
        assert len(lst(self.store, {})["experiments"]) >= 2

    def test_stop_experiment(self):
        start = _load_handler("start-experiment")
        stop = _load_handler("stop-experiment")
        describe = _load_handler("describe-experiment")
        resp = start(self.store, {"experimentTemplateId": "ext-s1"})
        stop(self.store, {"id": resp["id"]})
        assert describe(self.store, {"id": resp["id"]})["status"] == "stopped"

    def test_delete_experiment(self):
        start = _load_handler("start-experiment")
        delete = _load_handler("delete-experiment")
        describe = _load_handler("describe-experiment")
        resp = start(self.store, {"experimentTemplateId": "ext-d1"})
        delete(self.store, {"id": resp["id"]})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"id": resp["id"]})
