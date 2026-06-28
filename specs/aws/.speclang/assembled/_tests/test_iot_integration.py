"""Integration tests for IoT — 5 entities: Thing, ThingGroup, ThingType, Policy, Certificate."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "iot")

models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(SERVICE_DIR, "models.code.py")
)
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

IoTStore = models_mod.IoTStore
ThingRecord = models_mod.ThingRecord
ThingGroupRecord = models_mod.ThingGroupRecord
ThingTypeRecord = models_mod.ThingTypeRecord
PolicyRecord = models_mod.PolicyRecord
CertificateRecord = models_mod.CertificateRecord
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
ResourceAlreadyExistsException = models_mod.ResourceAlreadyExistsException
ValidationException = models_mod.ValidationException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    mod.ResourceAlreadyExistsException = ResourceAlreadyExistsException
    mod.ValidationException = ValidationException
    mod.ThingRecord = ThingRecord
    mod.ThingGroupRecord = ThingGroupRecord
    mod.ThingTypeRecord = ThingTypeRecord
    mod.PolicyRecord = PolicyRecord
    mod.CertificateRecord = CertificateRecord
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {"dataclass", "time", "uuid", "<lambda>"}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith("_")
                and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler found in {op_name}.code.py")


class TestThing:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = IoTStore()
        return self._store

    def test_create_thing(self):
        handler = _load_handler("create-thing")
        resp = handler(self.store, {"thingName": "sensor-1"})
        assert resp["thingName"] == "sensor-1"
        assert "thingArn" in resp

    def test_create_thing_duplicate(self):
        handler = _load_handler("create-thing")
        handler(self.store, {"thingName": "dup-thing"})
        with pytest.raises(ResourceAlreadyExistsException):
            handler(self.store, {"thingName": "dup-thing"})

    def test_describe_thing(self):
        create = _load_handler("create-thing")
        describe = _load_handler("describe-thing")
        create(self.store, {"thingName": "desc-thing"})
        resp = describe(self.store, {"thingName": "desc-thing"})
        assert resp["thingName"] == "desc-thing"

    def test_describe_thing_not_found(self):
        with pytest.raises(ResourceNotFoundException):
            _load_handler("describe-thing")(self.store, {"thingName": "nonexistent"})

    def test_list_things(self):
        create = _load_handler("create-thing")
        lst = _load_handler("list-things")
        create(self.store, {"thingName": "t1"})
        create(self.store, {"thingName": "t2"})
        resp = lst(self.store, {})
        assert len(resp["things"]) >= 2

    def test_delete_thing(self):
        create = _load_handler("create-thing")
        delete = _load_handler("delete-thing")
        describe = _load_handler("describe-thing")
        create(self.store, {"thingName": "del-thing"})
        delete(self.store, {"thingName": "del-thing"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"thingName": "del-thing"})

    def test_update_thing(self):
        create = _load_handler("create-thing")
        update = _load_handler("update-thing")
        describe = _load_handler("describe-thing")
        create(self.store, {"thingName": "upd-thing"})
        update(self.store, {"thingName": "upd-thing", "attributes": {"env": "prod"}})
        resp = describe(self.store, {"thingName": "upd-thing"})
        assert resp["attributes"]["env"] == "prod"


class TestThingGroup:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = IoTStore()
        return self._store

    def test_create_thing_group(self):
        handler = _load_handler("create-thing-group")
        resp = handler(self.store, {"thingGroupName": "group-1"})
        assert resp["thingGroupName"] == "group-1"

    def test_create_thing_group_duplicate(self):
        handler = _load_handler("create-thing-group")
        handler(self.store, {"thingGroupName": "dup-group"})
        with pytest.raises(ResourceAlreadyExistsException):
            handler(self.store, {"thingGroupName": "dup-group"})

    def test_describe_thing_group(self):
        create = _load_handler("create-thing-group")
        describe = _load_handler("describe-thing-group")
        create(self.store, {"thingGroupName": "desc-group"})
        resp = describe(self.store, {"thingGroupName": "desc-group"})
        assert resp["thingGroupName"] == "desc-group"

    def test_list_thing_groups(self):
        create = _load_handler("create-thing-group")
        lst = _load_handler("list-thing-groups")
        create(self.store, {"thingGroupName": "g1"})
        create(self.store, {"thingGroupName": "g2"})
        resp = lst(self.store, {})
        assert len(resp["thingGroups"]) >= 2

    def test_delete_thing_group(self):
        create = _load_handler("create-thing-group")
        delete = _load_handler("delete-thing-group")
        describe = _load_handler("describe-thing-group")
        create(self.store, {"thingGroupName": "del-group"})
        delete(self.store, {"thingGroupName": "del-group"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"thingGroupName": "del-group"})


class TestThingType:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = IoTStore()
        return self._store

    def test_create_thing_type(self):
        handler = _load_handler("create-thing-type")
        resp = handler(self.store, {"thingTypeName": "SensorType"})
        assert resp["thingTypeName"] == "SensorType"

    def test_create_thing_type_duplicate(self):
        handler = _load_handler("create-thing-type")
        handler(self.store, {"thingTypeName": "DupType"})
        with pytest.raises(ResourceAlreadyExistsException):
            handler(self.store, {"thingTypeName": "DupType"})

    def test_describe_thing_type(self):
        create = _load_handler("create-thing-type")
        describe = _load_handler("describe-thing-type")
        create(self.store, {"thingTypeName": "DescType"})
        resp = describe(self.store, {"thingTypeName": "DescType"})
        assert resp["thingTypeName"] == "DescType"

    def test_list_thing_types(self):
        create = _load_handler("create-thing-type")
        lst = _load_handler("list-thing-types")
        create(self.store, {"thingTypeName": "T1"})
        create(self.store, {"thingTypeName": "T2"})
        assert len(lst(self.store, {})["thingTypes"]) >= 2

    def test_delete_thing_type(self):
        create = _load_handler("create-thing-type")
        delete = _load_handler("delete-thing-type")
        describe = _load_handler("describe-thing-type")
        create(self.store, {"thingTypeName": "DelType"})
        delete(self.store, {"thingTypeName": "DelType"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"thingTypeName": "DelType"})


class TestPolicy:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = IoTStore()
        return self._store

    def test_create_policy(self):
        handler = _load_handler("create-policy")
        resp = handler(self.store, {"policyName": "DevicePolicy"})
        assert resp["policyName"] == "DevicePolicy"

    def test_create_policy_duplicate(self):
        handler = _load_handler("create-policy")
        handler(self.store, {"policyName": "DupPolicy"})
        with pytest.raises(ResourceAlreadyExistsException):
            handler(self.store, {"policyName": "DupPolicy"})

    def test_describe_policy(self):
        create = _load_handler("create-policy")
        describe = _load_handler("describe-policy")
        create(self.store, {"policyName": "DescPolicy"})
        resp = describe(self.store, {"policyName": "DescPolicy"})
        assert resp["policyName"] == "DescPolicy"

    def test_list_policies(self):
        create = _load_handler("create-policy")
        lst = _load_handler("list-policies")
        create(self.store, {"policyName": "P1"})
        create(self.store, {"policyName": "P2"})
        assert len(lst(self.store, {})["policies"]) >= 2

    def test_delete_policy(self):
        create = _load_handler("create-policy")
        delete = _load_handler("delete-policy")
        describe = _load_handler("describe-policy")
        create(self.store, {"policyName": "DelPolicy"})
        delete(self.store, {"policyName": "DelPolicy"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"policyName": "DelPolicy"})


class TestCertificate:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = IoTStore()
        return self._store

    def test_create_keys_and_certificate(self):
        handler = _load_handler("create-keys-and-certificate")
        resp = handler(self.store, {})
        assert "certificateId" in resp
        assert "certificateArn" in resp

    def test_describe_certificate(self):
        create = _load_handler("create-keys-and-certificate")
        describe = _load_handler("describe-certificate")
        resp = create(self.store, {})
        cert = describe(self.store, {"certificateId": resp["certificateId"]})
        assert cert["certificateId"] == resp["certificateId"]

    def test_list_certificates(self):
        create = _load_handler("create-keys-and-certificate")
        lst = _load_handler("list-certificates")
        create(self.store, {})
        create(self.store, {})
        assert len(lst(self.store, {})["certificates"]) >= 2

    def test_delete_certificate(self):
        create = _load_handler("create-keys-and-certificate")
        delete = _load_handler("delete-certificate")
        describe = _load_handler("describe-certificate")
        resp = create(self.store, {})
        delete(self.store, {"certificateId": resp["certificateId"]})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"certificateId": resp["certificateId"]})
