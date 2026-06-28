"""Integration test for GlobalAccelerator — real store."""
import os
import importlib.util
import types
import time as _time

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'globalaccelerator')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
GlobalAcceleratorStore = models_mod.GlobalAcceleratorStore
AcceleratorRecord = models_mod.AcceleratorRecord
ListenerRecord = models_mod.ListenerRecord
EndpointGroupRecord = models_mod.EndpointGroupRecord
AcceleratorNotFoundException = models_mod.AcceleratorNotFoundException
AcceleratorNotDisabledException = models_mod.AcceleratorNotDisabledException
AssociatedEndpointGroupFoundException = models_mod.AssociatedEndpointGroupFoundException
AssociatedListenerFoundException = models_mod.AssociatedListenerFoundException
EndpointGroupAlreadyExistsException = models_mod.EndpointGroupAlreadyExistsException
EndpointGroupNotFoundException = models_mod.EndpointGroupNotFoundException
InvalidArgumentException = models_mod.InvalidArgumentException
ListenerNotFoundException = models_mod.ListenerNotFoundException

# Exception class name mapping for injection (use the generic names from botocore)
InvalidParameterException = models_mod.InvalidArgumentException

skip_names = {'time', 'uuid', '<lambda>', 'dataclass'}


def _load_handler(op_name):
    """Load a single-handler .code.py file."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception + record classes
    mod.AcceleratorNotFoundException = AcceleratorNotFoundException
    mod.AcceleratorNotDisabledException = AcceleratorNotDisabledException
    mod.AccessDeniedException = models_mod.AccessDeniedException
    mod.AssociatedEndpointGroupFoundException = AssociatedEndpointGroupFoundException
    mod.AssociatedListenerFoundException = AssociatedListenerFoundException
    mod.ConflictException = models_mod.ConflictException
    mod.EndpointGroupAlreadyExistsException = EndpointGroupAlreadyExistsException
    mod.EndpointGroupNotFoundException = EndpointGroupNotFoundException
    mod.InternalServiceErrorException = models_mod.InternalServiceErrorException
    mod.InvalidArgumentException = InvalidArgumentException
    mod.InvalidPortRangeException = models_mod.InvalidPortRangeException
    mod.LimitExceededException = models_mod.LimitExceededException
    mod.ListenerNotFoundException = ListenerNotFoundException
    mod.TransactionInProgressException = models_mod.TransactionInProgressException
    mod.AcceleratorRecord = AcceleratorRecord
    mod.ListenerRecord = ListenerRecord
    mod.EndpointGroupRecord = EndpointGroupRecord
    mod.time = _time
    mod.uuid = __import__('uuid')
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestAcceleratorIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GlobalAcceleratorStore()
        return self._store

    def _create_accelerator(self, name="test-accel", enabled=True):
        h = _load_handler('create-accelerator')
        return h(self.store, {
            "Name": name,
            "IdempotencyToken": "test-token",
            "Enabled": enabled,
        })

    def test_create_accelerator_happy(self):
        resp = self._create_accelerator("test-accel-1")
        assert resp["Accelerator"]["Name"] == "test-accel-1"
        assert "AcceleratorArn" in resp["Accelerator"]
        assert resp["Accelerator"]["Status"] == "DEPLOYED"

    def test_create_accelerator_duplicate_name(self):
        self._create_accelerator("dup-accel")
        with __import__('pytest').raises(InvalidArgumentException):
            self._create_accelerator("dup-accel")

    def test_describe_accelerator_happy(self):
        resp = self._create_accelerator("desc-accel")
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('describe-accelerator')
        resp2 = h(self.store, {"AcceleratorArn": arn})
        assert resp2["Accelerator"]["Name"] == "desc-accel"

    def test_describe_accelerator_nonexistent(self):
        h = _load_handler('describe-accelerator')
        with __import__('pytest').raises(AcceleratorNotFoundException):
            h(self.store, {"AcceleratorArn": "arn:aws:globalaccelerator::nonexistent"})

    def test_update_accelerator_happy(self):
        resp = self._create_accelerator("update-accel")
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('update-accelerator')
        resp2 = h(self.store, {"AcceleratorArn": arn, "Name": "updated-name", "Enabled": True})
        assert resp2["Accelerator"]["Name"] == "updated-name"

    def test_update_accelerator_nonexistent(self):
        h = _load_handler('update-accelerator')
        with __import__('pytest').raises(AcceleratorNotFoundException):
            h(self.store, {"AcceleratorArn": "arn:aws:globalaccelerator::nonexistent", "Name": "x"})

    def test_list_accelerators(self):
        self._create_accelerator("list-a1")
        self._create_accelerator("list-a2")
        h = _load_handler('list-accelerators')
        resp = h(self.store, {})
        assert len(resp["Accelerators"]) >= 2

    def test_delete_accelerator_happy(self):
        resp = self._create_accelerator("del-accel", enabled=False)
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('delete-accelerator')
        h(self.store, {"AcceleratorArn": arn})
        h2 = _load_handler('describe-accelerator')
        with __import__('pytest').raises(AcceleratorNotFoundException):
            h2(self.store, {"AcceleratorArn": arn})

    def test_delete_accelerator_when_enabled(self):
        resp = self._create_accelerator("enabled-del", enabled=True)
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('delete-accelerator')
        with __import__('pytest').raises(AcceleratorNotDisabledException):
            h(self.store, {"AcceleratorArn": arn})

    def test_delete_accelerator_nonexistent(self):
        h = _load_handler('delete-accelerator')
        with __import__('pytest').raises(AcceleratorNotFoundException):
            h(self.store, {"AcceleratorArn": "arn:aws:globalaccelerator::nonexistent"})


class TestAcceleratorAttributesIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GlobalAcceleratorStore()
        return self._store

    def _make_accel(self):
        h = _load_handler('create-accelerator')
        return h(self.store, {"Name": "attr-accel", "IdempotencyToken": "tok"})

    def test_describe_attributes(self):
        resp = self._make_accel()
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('describe-accelerator-attributes')
        resp2 = h(self.store, {"AcceleratorArn": arn})
        assert "FlowLogsEnabled" in resp2

    def test_describe_attributes_nonexistent(self):
        h = _load_handler('describe-accelerator-attributes')
        with __import__('pytest').raises(AcceleratorNotFoundException):
            h(self.store, {"AcceleratorArn": "arn:nonexistent"})

    def test_update_attributes(self):
        resp = self._make_accel()
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('update-accelerator-attributes')
        resp2 = h(self.store, {
            "AcceleratorArn": arn,
            "FlowLogsEnabled": True,
            "FlowLogsS3Bucket": "my-bucket",
            "FlowLogsS3Prefix": "logs/",
        })
        assert resp2["FlowLogsEnabled"] is True
        assert resp2["FlowLogsS3Bucket"] == "my-bucket"


class TestListenerIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GlobalAcceleratorStore()
        return self._store

    def _make_accel(self, name="listener-accel"):
        h = _load_handler('create-accelerator')
        return h(self.store, {"Name": name, "IdempotencyToken": "tok"})

    def test_create_listener_happy(self):
        accel = self._make_accel()
        arn = accel["Accelerator"]["AcceleratorArn"]
        h = _load_handler('create-listener')
        resp = h(self.store, {
            "AcceleratorArn": arn,
            "PortRanges": [{"FromPort": 80, "ToPort": 80}],
            "Protocol": "TCP",
        })
        assert "ListenerArn" in resp["Listener"]
        assert resp["Listener"]["Protocol"] == "TCP"

    def test_create_listener_nonexistent_accelerator(self):
        h = _load_handler('create-listener')
        with __import__('pytest').raises(AcceleratorNotFoundException):
            h(self.store, {
                "AcceleratorArn": "arn:nonexistent",
                "PortRanges": [{"FromPort": 80, "ToPort": 80}],
                "Protocol": "TCP",
            })

    def test_describe_listener_happy(self):
        accel = self._make_accel()
        h = _load_handler('create-listener')
        resp = h(self.store, {
            "AcceleratorArn": accel["Accelerator"]["AcceleratorArn"],
            "PortRanges": [{"FromPort": 80, "ToPort": 80}],
            "Protocol": "TCP",
        })
        la = resp["Listener"]["ListenerArn"]
        h2 = _load_handler('describe-listener')
        resp2 = h2(self.store, {"ListenerArn": la})
        assert resp2["Listener"]["Protocol"] == "TCP"

    def test_describe_listener_nonexistent(self):
        h = _load_handler('describe-listener')
        with __import__('pytest').raises(ListenerNotFoundException):
            h(self.store, {"ListenerArn": "arn:nonexistent"})

    def test_update_listener_happy(self):
        accel = self._make_accel()
        h = _load_handler('create-listener')
        resp = h(self.store, {
            "AcceleratorArn": accel["Accelerator"]["AcceleratorArn"],
            "PortRanges": [{"FromPort": 80, "ToPort": 80}],
            "Protocol": "TCP",
        })
        la = resp["Listener"]["ListenerArn"]
        h2 = _load_handler('update-listener')
        resp2 = h2(self.store, {"ListenerArn": la, "Protocol": "UDP"})
        assert resp2["Listener"]["Protocol"] == "UDP"

    def test_list_listeners(self):
        accel = self._make_accel("multi-listener")
        a_arn = accel["Accelerator"]["AcceleratorArn"]
        h = _load_handler('create-listener')
        h(self.store, {
            "AcceleratorArn": a_arn,
            "PortRanges": [{"FromPort": 80, "ToPort": 80}],
            "Protocol": "TCP",
        })
        h(self.store, {
            "AcceleratorArn": a_arn,
            "PortRanges": [{"FromPort": 443, "ToPort": 443}],
            "Protocol": "TCP",
        })
        h2 = _load_handler('list-listeners')
        resp = h2(self.store, {"AcceleratorArn": a_arn})
        assert len(resp["Listeners"]) == 2

    def test_delete_listener_happy(self):
        accel = self._make_accel("del-listen-accel")
        h = _load_handler('create-listener')
        resp = h(self.store, {
            "AcceleratorArn": accel["Accelerator"]["AcceleratorArn"],
            "PortRanges": [{"FromPort": 80, "ToPort": 80}],
            "Protocol": "TCP",
        })
        la = resp["Listener"]["ListenerArn"]
        h2 = _load_handler('delete-listener')
        h2(self.store, {"ListenerArn": la})
        h3 = _load_handler('describe-listener')
        with __import__('pytest').raises(ListenerNotFoundException):
            h3(self.store, {"ListenerArn": la})


class TestEndpointGroupIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GlobalAcceleratorStore()
        return self._store

    def _setup_listener(self):
        h = _load_handler('create-accelerator')
        accel = h(self.store, {"Name": "eg-accel", "IdempotencyToken": "tok"})
        a_arn = accel["Accelerator"]["AcceleratorArn"]
        h2 = _load_handler('create-listener')
        listener = h2(self.store, {
            "AcceleratorArn": a_arn,
            "PortRanges": [{"FromPort": 80, "ToPort": 80}],
            "Protocol": "TCP",
        })
        return listener["Listener"]["ListenerArn"]

    def test_create_endpoint_group_happy(self):
        la = self._setup_listener()
        h = _load_handler('create-endpoint-group')
        resp = h(self.store, {
            "EndpointGroupRegion": "us-west-2",
            "ListenerArn": la,
        })
        assert "EndpointGroupArn" in resp["EndpointGroup"]
        assert resp["EndpointGroup"]["EndpointGroupRegion"] == "us-west-2"

    def test_create_endpoint_group_duplicate(self):
        la = self._setup_listener()
        h = _load_handler('create-endpoint-group')
        h(self.store, {"EndpointGroupRegion": "us-east-1", "ListenerArn": la})
        with __import__('pytest').raises(EndpointGroupAlreadyExistsException):
            h(self.store, {"EndpointGroupRegion": "us-east-1", "ListenerArn": la})

    def test_create_endpoint_group_nonexistent_listener(self):
        h = _load_handler('create-endpoint-group')
        with __import__('pytest').raises(ListenerNotFoundException):
            h(self.store, {
                "EndpointGroupRegion": "us-west-2",
                "ListenerArn": "arn:nonexistent",
            })

    def test_describe_endpoint_group_happy(self):
        la = self._setup_listener()
        h = _load_handler('create-endpoint-group')
        resp = h(self.store, {"EndpointGroupRegion": "us-west-2", "ListenerArn": la})
        eg_arn = resp["EndpointGroup"]["EndpointGroupArn"]
        h2 = _load_handler('describe-endpoint-group')
        resp2 = h2(self.store, {"EndpointGroupArn": eg_arn})
        assert resp2["EndpointGroup"]["EndpointGroupRegion"] == "us-west-2"

    def test_describe_endpoint_group_nonexistent(self):
        h = _load_handler('describe-endpoint-group')
        with __import__('pytest').raises(EndpointGroupNotFoundException):
            h(self.store, {"EndpointGroupArn": "arn:nonexistent"})

    def test_update_endpoint_group_happy(self):
        la = self._setup_listener()
        h = _load_handler('create-endpoint-group')
        resp = h(self.store, {"EndpointGroupRegion": "us-west-2", "ListenerArn": la})
        eg_arn = resp["EndpointGroup"]["EndpointGroupArn"]
        h2 = _load_handler('update-endpoint-group')
        resp2 = h2(self.store, {
            "EndpointGroupArn": eg_arn,
            "HealthCheckIntervalSeconds": 60,
            "TrafficDialPercentage": 50,
        })
        assert resp2["EndpointGroup"]["HealthCheckIntervalSeconds"] == 60
        assert resp2["EndpointGroup"]["TrafficDialPercentage"] == 50

    def test_list_endpoint_groups(self):
        la = self._setup_listener()
        h = _load_handler('create-endpoint-group')
        h(self.store, {"EndpointGroupRegion": "us-west-2", "ListenerArn": la})
        h(self.store, {"EndpointGroupRegion": "us-east-1", "ListenerArn": la})
        h2 = _load_handler('list-endpoint-groups')
        resp = h2(self.store, {"ListenerArn": la})
        assert len(resp["EndpointGroups"]) == 2

    def test_delete_endpoint_group_happy(self):
        la = self._setup_listener()
        h = _load_handler('create-endpoint-group')
        resp = h(self.store, {"EndpointGroupRegion": "us-west-2", "ListenerArn": la})
        eg_arn = resp["EndpointGroup"]["EndpointGroupArn"]
        h2 = _load_handler('delete-endpoint-group')
        h2(self.store, {"EndpointGroupArn": eg_arn})
        h3 = _load_handler('describe-endpoint-group')
        with __import__('pytest').raises(EndpointGroupNotFoundException):
            h3(self.store, {"EndpointGroupArn": eg_arn})


class TestEndpointsIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GlobalAcceleratorStore()
        return self._store

    def _setup_eg(self):
        h = _load_handler('create-accelerator')
        accel = h(self.store, {"Name": "ep-accel", "IdempotencyToken": "tok"})
        h2 = _load_handler('create-listener')
        listener = h2(self.store, {
            "AcceleratorArn": accel["Accelerator"]["AcceleratorArn"],
            "PortRanges": [{"FromPort": 80, "ToPort": 80}],
            "Protocol": "TCP",
        })
        h3 = _load_handler('create-endpoint-group')
        eg = h3(self.store, {
            "EndpointGroupRegion": "us-west-2",
            "ListenerArn": listener["Listener"]["ListenerArn"],
        })
        return eg["EndpointGroup"]["EndpointGroupArn"]

    def test_add_endpoints_happy(self):
        eg_arn = self._setup_eg()
        h = _load_handler('add-endpoints')
        resp = h(self.store, {
            "EndpointGroupArn": eg_arn,
            "EndpointConfigurations": [
                {"EndpointId": "ep-1", "Weight": 128},
                {"EndpointId": "ep-2", "Weight": 128},
            ],
        })
        assert len(resp["EndpointDescriptions"]) == 2

    def test_add_endpoints_nonexistent_eg(self):
        h = _load_handler('add-endpoints')
        with __import__('pytest').raises(EndpointGroupNotFoundException):
            h(self.store, {
                "EndpointGroupArn": "arn:nonexistent",
                "EndpointConfigurations": [{"EndpointId": "x"}],
            })

    def test_remove_endpoints_happy(self):
        eg_arn = self._setup_eg()
        h = _load_handler('add-endpoints')
        h(self.store, {
            "EndpointGroupArn": eg_arn,
            "EndpointConfigurations": [
                {"EndpointId": "ep-1"}, {"EndpointId": "ep-2"},
            ],
        })
        h2 = _load_handler('remove-endpoints')
        h2(self.store, {
            "EndpointGroupArn": eg_arn,
            "EndpointIdentifiers": ["ep-1"],
        })
        h3 = _load_handler('describe-endpoint-group')
        resp = h3(self.store, {"EndpointGroupArn": eg_arn})
        ep_ids = [e["EndpointId"] for e in resp["EndpointGroup"]["EndpointDescriptions"]]
        assert "ep-1" not in ep_ids
        assert "ep-2" in ep_ids


class TestTagsIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = GlobalAcceleratorStore()
        return self._store

    def _make_accel(self):
        h = _load_handler('create-accelerator')
        return h(self.store, {"Name": "tag-accel", "IdempotencyToken": "tok",
                              "Tags": [{"Key": "env", "Value": "test"}]})

    def test_tag_resource(self):
        resp = self._make_accel()
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('tag-resource')
        h(self.store, {
            "ResourceArn": arn,
            "Tags": [{"Key": "team", "Value": "platform"}],
        })
        h2 = _load_handler('list-tags-for-resource')
        resp2 = h2(self.store, {"ResourceArn": arn})
        tags = {t["Key"]: t["Value"] for t in resp2["Tags"]}
        assert tags.get("env") == "test"
        assert tags.get("team") == "platform"

    def test_list_tags(self):
        resp = self._make_accel()
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('list-tags-for-resource')
        resp2 = h(self.store, {"ResourceArn": arn})
        tags = {t["Key"]: t["Value"] for t in resp2["Tags"]}
        assert tags["env"] == "test"

    def test_untag_resource(self):
        resp = self._make_accel()
        arn = resp["Accelerator"]["AcceleratorArn"]
        h = _load_handler('tag-resource')
        h(self.store, {"ResourceArn": arn,
                       "Tags": [{"Key": "tmp", "Value": "del"}]})
        h2 = _load_handler('untag-resource')
        h2(self.store, {"ResourceArn": arn, "TagKeys": ["tmp"]})
        h3 = _load_handler('list-tags-for-resource')
        resp3 = h3(self.store, {"ResourceArn": arn})
        tags = {t["Key"]: t["Value"] for t in resp3["Tags"]}
        assert "tmp" not in tags
        assert tags["env"] == "test"
