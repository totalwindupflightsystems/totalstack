"""Integration tests for GreengrassV2 — 3 entities."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "greengrassv2")

models_spec = importlib.util.spec_from_file_location("models", os.path.join(SERVICE_DIR, "models.code.py"))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)
GreengrassV2Store = models_mod.GreengrassV2Store
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException
ValidationException = models_mod.ValidationException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.ValidationException = ValidationException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {"dataclass", "time", "uuid", "<lambda>"}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType) and not v.__name__.startswith("_") and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler in {op_name}")


class TestComponent:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GreengrassV2Store()
        return self._store

    def test_create_component(self):
        h = _load_handler("create-component-version")
        resp = h(self.store, {"componentName": "HelloWorld", "componentVersion": "1.0.0"})
        assert resp["componentName"] == "HelloWorld"
        assert resp["componentVersion"] == "1.0.0"

    def test_create_component_duplicate(self):
        h = _load_handler("create-component-version")
        req = {"componentName": "DupComp", "componentVersion": "1.0.0"}
        h(self.store, req)
        with pytest.raises(ConflictException):
            h(self.store, req)

    def test_describe_component(self):
        create = _load_handler("create-component-version")
        describe = _load_handler("describe-component")
        create(self.store, {"componentName": "DescComp", "componentVersion": "1.0.0"})
        resp = describe(self.store, {"componentName": "DescComp", "componentVersion": "1.0.0"})
        assert resp["componentName"] == "DescComp"

    def test_list_components(self):
        create = _load_handler("create-component-version")
        lst = _load_handler("list-components")
        create(self.store, {"componentName": "C1", "componentVersion": "1.0.0"})
        create(self.store, {"componentName": "C2", "componentVersion": "1.0.0"})
        assert len(lst(self.store, {})["components"]) >= 2

    def test_delete_component(self):
        create = _load_handler("create-component-version")
        delete = _load_handler("delete-component")
        describe = _load_handler("describe-component")
        create(self.store, {"componentName": "DelComp", "componentVersion": "1.0.0"})
        delete(self.store, {"componentName": "DelComp", "componentVersion": "1.0.0"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"componentName": "DelComp", "componentVersion": "1.0.0"})


class TestDeployment:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GreengrassV2Store()
        return self._store

    def test_create_deployment(self):
        h = _load_handler("create-deployment")
        resp = h(self.store, {"deploymentName": "dep-1", "targetArn": "arn:aws:iot:thing/device"})
        assert resp["deploymentName"] == "dep-1"
        assert "deploymentId" in resp

    def test_describe_deployment(self):
        create = _load_handler("create-deployment")
        describe = _load_handler("describe-deployment")
        resp = create(self.store, {"deploymentName": "dep-2", "targetArn": "arn:aws:iot:thing/device"})
        desc = describe(self.store, {"deploymentId": resp["deploymentId"]})
        assert desc["deploymentName"] == "dep-2"

    def test_list_deployments(self):
        create = _load_handler("create-deployment")
        lst = _load_handler("list-deployments")
        create(self.store, {"deploymentName": "d1", "targetArn": "arn:a"})
        create(self.store, {"deploymentName": "d2", "targetArn": "arn:b"})
        assert len(lst(self.store, {})["deployments"]) >= 2

    def test_delete_deployment(self):
        create = _load_handler("create-deployment")
        delete = _load_handler("delete-deployment")
        describe = _load_handler("describe-deployment")
        resp = create(self.store, {"deploymentName": "dd", "targetArn": "arn:x"})
        delete(self.store, {"deploymentId": resp["deploymentId"]})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"deploymentId": resp["deploymentId"]})


class TestCoreDevice:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GreengrassV2Store()
        return self._store

    def test_create_core_device(self):
        h = _load_handler("create-core-device")
        resp = h(self.store, {"coreDeviceThingName": "edge-device-1"})
        assert resp["coreDeviceThingName"] == "edge-device-1"

    def test_describe_core_device(self):
        create = _load_handler("create-core-device")
        describe = _load_handler("describe-core-device")
        create(self.store, {"coreDeviceThingName": "edge-2"})
        resp = describe(self.store, {"coreDeviceThingName": "edge-2"})
        assert resp["coreDeviceThingName"] == "edge-2"

    def test_list_core_devices(self):
        create = _load_handler("create-core-device")
        lst = _load_handler("list-core-devices")
        create(self.store, {"coreDeviceThingName": "e1"})
        create(self.store, {"coreDeviceThingName": "e2"})
        assert len(lst(self.store, {})["coreDevices"]) >= 2

    def test_delete_core_device(self):
        create = _load_handler("create-core-device")
        delete = _load_handler("delete-core-device")
        describe = _load_handler("describe-core-device")
        create(self.store, {"coreDeviceThingName": "ed"})
        delete(self.store, {"coreDeviceThingName": "ed"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"coreDeviceThingName": "ed"})
