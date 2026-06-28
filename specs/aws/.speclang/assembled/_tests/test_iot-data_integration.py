"""Integration tests for IoT Data Plane."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "iot-data")

models_spec = importlib.util.spec_from_file_location("models", os.path.join(SERVICE_DIR, "models.code.py"))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

IoTDataStore = models_mod.IoTDataStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
InvalidRequestException = models_mod.InvalidRequestException
ConflictException = models_mod.ConflictException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.InvalidRequestException = InvalidRequestException
    mod.ConflictException = ConflictException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {"dataclass", "time", "uuid", "<lambda>"}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType) and not v.__name__.startswith("_") and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler found in {op_name}.code.py")


class TestThingShadow:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = IoTDataStore()
        return self._store

    def test_update_and_get_shadow(self):
        update = _load_handler("update-thing-shadow")
        get = _load_handler("get-thing-shadow")
        payload = {"state": {"reported": {"temp": 22}}}
        update(self.store, {"thingName": "sensor-1", "payload": payload})
        resp = get(self.store, {"thingName": "sensor-1"})
        assert resp["state"]["reported"]["temp"] == 22

    def test_get_shadow_not_found(self):
        get = _load_handler("get-thing-shadow")
        with pytest.raises(ResourceNotFoundException):
            get(self.store, {"thingName": "nonexistent"})

    def test_delete_shadow(self):
        update = _load_handler("update-thing-shadow")
        delete = _load_handler("delete-thing-shadow")
        get = _load_handler("get-thing-shadow")
        update(self.store, {"thingName": "del-sensor", "payload": {"state": {}}})
        delete(self.store, {"thingName": "del-sensor"})
        with pytest.raises(ResourceNotFoundException):
            get(self.store, {"thingName": "del-sensor"})

    def test_named_shadow(self):
        update = _load_handler("update-thing-shadow")
        get = _load_handler("get-thing-shadow")
        lst = _load_handler("list-named-shadows-for-thing")
        update(self.store, {"thingName": "thing-1", "shadowName": "config", "payload": {"version": 1}})
        resp = get(self.store, {"thingName": "thing-1", "shadowName": "config"})
        assert resp["version"] == 1
        results = lst(self.store, {"thingName": "thing-1"})
        assert "config" in results["results"]

    def test_publish(self):
        handler = _load_handler("publish")
        resp = handler(self.store, {"topic": "test/topic", "payload": b"hello"})
        assert resp["topic"] == "test/topic"
