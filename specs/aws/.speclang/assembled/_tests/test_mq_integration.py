"""Integration tests for Amazon MQ — real store with generated handlers."""
import os
import importlib.util
import types
import pytest
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'mq')

# Load models
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

MqStore = models_mod.MqStore
BadRequestException = models_mod.BadRequestException
UnauthorizedException = models_mod.UnauthorizedException
InternalServerErrorException = models_mod.InternalServerErrorException
ConflictException = models_mod.ConflictException
ForbiddenException = models_mod.ForbiddenException
NotFoundException = models_mod.NotFoundException
BrokerRecord = models_mod.BrokerRecord
ConfigurationRecord = models_mod.ConfigurationRecord
UserRecord = models_mod.UserRecord

RECORD_CLASSES = {
    'BrokerRecord': BrokerRecord,
    'ConfigurationRecord': ConfigurationRecord,
    'UserRecord': UserRecord,
}

EXCEPTION_CLASSES = {
    'BadRequestException': BadRequestException,
    'UnauthorizedException': UnauthorizedException,
    'InternalServerErrorException': InternalServerErrorException,
    'ConflictException': ConflictException,
    'ForbiddenException': ForbiddenException,
    'NotFoundException': NotFoundException,
}

SKIP_NAMES = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    for exc_name, exc_cls in EXCEPTION_CLASSES.items():
        setattr(mod, exc_name, exc_cls)
    for rec_name, rec_cls in RECORD_CLASSES.items():
        setattr(mod, rec_name, rec_cls)
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in SKIP_NAMES):
            handler = v
            break
    assert handler is not None, f"No handler found in {op_name}"
    return handler


class TestBrokerIntegration:
    @pytest.fixture
    def store(self):
        return MqStore()

    def test_create_broker_happy(self, store):
        h = _load_handler('CreateBroker')
        resp = h(store, {
            "BrokerName": "test-broker",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
            "HostInstanceType": "mq.t3.micro",
        })
        assert "BrokerId" in resp
        assert "BrokerArn" in resp

    def test_create_broker_missing_name(self, store):
        h = _load_handler('CreateBroker')
        with pytest.raises(BadRequestException):
            h(store, {"EngineType": "ActiveMQ"})

    def test_create_broker_duplicate(self, store):
        h = _load_handler('CreateBroker')
        h(store, {
            "BrokerName": "dup-broker",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
        })
        with pytest.raises(ConflictException):
            h(store, {
                "BrokerName": "dup-broker",
                "EngineType": "ActiveMQ",
                "DeploymentMode": "SINGLE_INSTANCE",
            })

    def test_describe_broker_happy(self, store):
        create = _load_handler('CreateBroker')
        describe = _load_handler('DescribeBroker')
        resp = create(store, {
            "BrokerName": "desc-broker",
            "EngineType": "RabbitMQ",
            "DeploymentMode": "CLUSTER_MULTI_AZ",
            "HostInstanceType": "mq.m5.large",
        })
        result = describe(store, {"BrokerId": resp["BrokerId"]})
        assert result["BrokerName"] == "desc-broker"
        assert result["EngineType"] == "RabbitMQ"

    def test_describe_broker_nonexistent(self, store):
        h = _load_handler('DescribeBroker')
        with pytest.raises(NotFoundException):
            h(store, {"BrokerId": "nonexistent"})

    def test_delete_broker_happy(self, store):
        create = _load_handler('CreateBroker')
        delete = _load_handler('DeleteBroker')
        describe = _load_handler('DescribeBroker')
        resp = create(store, {
            "BrokerName": "del-broker",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
        })
        delete(store, {"BrokerId": resp["BrokerId"]})
        with pytest.raises(NotFoundException):
            describe(store, {"BrokerId": resp["BrokerId"]})

    def test_delete_broker_nonexistent(self, store):
        h = _load_handler('DeleteBroker')
        with pytest.raises(NotFoundException):
            h(store, {"BrokerId": "nonexistent"})

    def test_list_brokers_empty(self, store):
        h = _load_handler('ListBrokers')
        resp = h(store, {})
        assert resp["BrokerSummaries"] == []

    def test_list_brokers_populated(self, store):
        create = _load_handler('CreateBroker')
        list_h = _load_handler('ListBrokers')
        create(store, {
            "BrokerName": "b1",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
        })
        create(store, {
            "BrokerName": "b2",
            "EngineType": "RabbitMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
        })
        resp = list_h(store, {})
        assert len(resp["BrokerSummaries"]) == 2

    def test_update_broker_happy(self, store):
        create = _load_handler('CreateBroker')
        update = _load_handler('UpdateBroker')
        describe = _load_handler('DescribeBroker')
        resp = create(store, {
            "BrokerName": "update-broker",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
        })
        update(store, {
            "BrokerId": resp["BrokerId"],
            "AutoMinorVersionUpgrade": False,
        })
        result = describe(store, {"BrokerId": resp["BrokerId"]})
        assert result["AutoMinorVersionUpgrade"] is False

    def test_update_broker_nonexistent(self, store):
        h = _load_handler('UpdateBroker')
        with pytest.raises(NotFoundException):
            h(store, {"BrokerId": "nonexistent"})

    def test_reboot_broker_happy(self, store):
        create = _load_handler('CreateBroker')
        reboot = _load_handler('RebootBroker')
        resp = create(store, {
            "BrokerName": "reboot-broker",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
        })
        result = reboot(store, {"BrokerId": resp["BrokerId"]})
        assert result["BrokerId"] == resp["BrokerId"]


class TestConfigurationIntegration:
    @pytest.fixture
    def store(self):
        return MqStore()

    def test_create_configuration_happy(self, store):
        h = _load_handler('CreateConfiguration')
        resp = h(store, {
            "Name": "test-config",
            "EngineType": "ActiveMQ",
            "EngineVersion": "5.17",
        })
        assert "Id" in resp
        assert resp["Name"] == "test-config"

    def test_create_configuration_duplicate(self, store):
        h = _load_handler('CreateConfiguration')
        h(store, {
            "Name": "dup-config",
            "EngineType": "ActiveMQ",
            "EngineVersion": "5.17",
        })
        with pytest.raises(ConflictException):
            h(store, {
                "Name": "dup-config",
                "EngineType": "ActiveMQ",
                "EngineVersion": "5.17",
            })

    def test_describe_configuration_happy(self, store):
        create = _load_handler('CreateConfiguration')
        describe = _load_handler('DescribeConfiguration')
        resp = create(store, {
            "Name": "desc-config",
            "EngineType": "RabbitMQ",
            "EngineVersion": "3.13",
        })
        result = describe(store, {"ConfigurationId": resp["Id"]})
        assert result["Name"] == "desc-config"

    def test_describe_configuration_nonexistent(self, store):
        h = _load_handler('DescribeConfiguration')
        with pytest.raises(NotFoundException):
            h(store, {"ConfigurationId": "nonexistent"})

    def test_delete_configuration_happy(self, store):
        create = _load_handler('CreateConfiguration')
        delete = _load_handler('DeleteConfiguration')
        describe = _load_handler('DescribeConfiguration')
        resp = create(store, {
            "Name": "del-config",
            "EngineType": "ActiveMQ",
            "EngineVersion": "5.17",
        })
        delete(store, {"ConfigurationId": resp["Id"]})
        with pytest.raises(NotFoundException):
            describe(store, {"ConfigurationId": resp["Id"]})

    def test_update_configuration_happy(self, store):
        create = _load_handler('CreateConfiguration')
        update = _load_handler('UpdateConfiguration')
        describe_rev = _load_handler('DescribeConfigurationRevision')
        resp = create(store, {
            "Name": "update-config",
            "EngineType": "ActiveMQ",
            "EngineVersion": "5.17",
        })
        update(store, {
            "ConfigurationId": resp["Id"],
            "Data": "<broker xmlns='...'><plugins/></broker>",
            "Description": "updated desc",
        })
        rev = describe_rev(store, {
            "ConfigurationId": resp["Id"],
            "ConfigurationRevision": 2,
        })
        assert rev["Revision"] == 2

    def test_describe_configuration_revision_nonexistent(self, store):
        create = _load_handler('CreateConfiguration')
        describe_rev = _load_handler('DescribeConfigurationRevision')
        resp = create(store, {
            "Name": "rev-config",
            "EngineType": "ActiveMQ",
            "EngineVersion": "5.17",
        })
        with pytest.raises(NotFoundException):
            describe_rev(store, {
                "ConfigurationId": resp["Id"],
                "ConfigurationRevision": 999,
            })

    def test_list_configurations(self, store):
        create = _load_handler('CreateConfiguration')
        list_h = _load_handler('ListConfigurations')
        create(store, {
            "Name": "c1",
            "EngineType": "ActiveMQ",
            "EngineVersion": "5.17",
        })
        resp = list_h(store, {})
        assert len(resp["Configurations"]) == 1


class TestUserIntegration:
    @pytest.fixture
    def store_with_broker(self):
        store = MqStore()
        create = _load_handler('CreateBroker')
        resp = create(store, {
            "BrokerName": "user-broker",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
        })
        store._broker_id = resp["BrokerId"]
        return store

    def test_create_user_happy(self, store_with_broker):
        store = store_with_broker
        h = _load_handler('CreateUser')
        resp = h(store, {
            "BrokerId": store._broker_id,
            "Username": "admin",
            "Password": "secret123",
            "ConsoleAccess": True,
        })
        assert resp == {}

    def test_create_user_duplicate(self, store_with_broker):
        store = store_with_broker
        h = _load_handler('CreateUser')
        h(store, {
            "BrokerId": store._broker_id,
            "Username": "dup-user",
            "Password": "pw",
        })
        with pytest.raises(ConflictException):
            h(store, {
                "BrokerId": store._broker_id,
                "Username": "dup-user",
                "Password": "pw",
            })

    def test_create_user_broker_not_found(self, store_with_broker):
        store = store_with_broker
        h = _load_handler('CreateUser')
        with pytest.raises(NotFoundException):
            h(store, {
                "BrokerId": "nonexistent",
                "Username": "admin",
                "Password": "pw",
            })

    def test_describe_user_happy(self, store_with_broker):
        store = store_with_broker
        create = _load_handler('CreateUser')
        describe = _load_handler('DescribeUser')
        create(store, {
            "BrokerId": store._broker_id,
            "Username": "testuser",
            "Password": "pw",
            "Groups": ["admin"],
        })
        result = describe(store, {
            "BrokerId": store._broker_id,
            "Username": "testuser",
        })
        assert result["Username"] == "testuser"

    def test_describe_user_nonexistent(self, store_with_broker):
        store = store_with_broker
        h = _load_handler('DescribeUser')
        with pytest.raises(NotFoundException):
            h(store, {
                "BrokerId": store._broker_id,
                "Username": "nonexistent",
            })

    def test_delete_user_happy(self, store_with_broker):
        store = store_with_broker
        create = _load_handler('CreateUser')
        delete = _load_handler('DeleteUser')
        describe = _load_handler('DescribeUser')
        create(store, {
            "BrokerId": store._broker_id,
            "Username": "del-user",
            "Password": "pw",
        })
        delete(store, {
            "BrokerId": store._broker_id,
            "Username": "del-user",
        })
        with pytest.raises(NotFoundException):
            describe(store, {
                "BrokerId": store._broker_id,
                "Username": "del-user",
            })

    def test_list_users_empty(self, store_with_broker):
        store = store_with_broker
        h = _load_handler('ListUsers')
        resp = h(store, {"BrokerId": store._broker_id})
        assert resp["Users"] == []

    def test_list_users_populated(self, store_with_broker):
        store = store_with_broker
        create = _load_handler('CreateUser')
        list_h = _load_handler('ListUsers')
        create(store, {
            "BrokerId": store._broker_id,
            "Username": "u1",
            "Password": "pw",
        })
        create(store, {
            "BrokerId": store._broker_id,
            "Username": "u2",
            "Password": "pw",
        })
        resp = list_h(store, {"BrokerId": store._broker_id})
        assert len(resp["Users"]) == 2

    def test_update_user_happy(self, store_with_broker):
        store = store_with_broker
        create = _load_handler('CreateUser')
        update = _load_handler('UpdateUser')
        describe = _load_handler('DescribeUser')
        create(store, {
            "BrokerId": store._broker_id,
            "Username": "update-user",
            "Password": "pw",
        })
        update(store, {
            "BrokerId": store._broker_id,
            "Username": "update-user",
            "ConsoleAccess": True,
            "Groups": ["ops"],
        })
        result = describe(store, {
            "BrokerId": store._broker_id,
            "Username": "update-user",
        })
        assert result["ConsoleAccess"] is True
        assert "ops" in result["Groups"]


class TestTagIntegration:
    @pytest.fixture
    def store_with_broker(self):
        store = MqStore()
        create = _load_handler('CreateBroker')
        resp = create(store, {
            "BrokerName": "tag-broker",
            "EngineType": "ActiveMQ",
            "DeploymentMode": "SINGLE_INSTANCE",
            "Tags": {"env": "test"},
        })
        store._arn = resp["BrokerArn"]
        return store

    def test_create_tags(self, store_with_broker):
        store = store_with_broker
        h = _load_handler('CreateTags')
        resp = h(store, {
            "ResourceArn": store._arn,
            "Tags": {"team": "platform"},
        })
        assert resp == {}
        list_h = _load_handler('ListTags')
        tags = list_h(store, {"ResourceArn": store._arn})
        assert tags["Tags"].get("team") == "platform"

    def test_delete_tags(self, store_with_broker):
        store = store_with_broker
        tag_h = _load_handler('CreateTags')
        delete_h = _load_handler('DeleteTags')
        list_h = _load_handler('ListTags')
        tag_h(store, {
            "ResourceArn": store._arn,
            "Tags": {"temp": "remove-me"},
        })
        delete_h(store, {
            "ResourceArn": store._arn,
            "TagKeys": ["temp"],
        })
        tags = list_h(store, {"ResourceArn": store._arn})
        assert "temp" not in tags["Tags"]

    def test_list_tags(self, store_with_broker):
        store = store_with_broker
        h = _load_handler('ListTags')
        resp = h(store, {"ResourceArn": store._arn})
        assert resp["Tags"]["env"] == "test"
