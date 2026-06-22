"""Integration tests for Timestream for InfluxDB — real store."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'timestream-influxdb')

# Dynamically load models.code.py
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
TimestreamForInfluxDBStore = models_mod.TimestreamForInfluxDBStore
DbClusterRecord = models_mod.DbClusterRecord
DbInstanceRecord = models_mod.DbInstanceRecord
DbParameterGroupRecord = models_mod.DbParameterGroupRecord
LogDeliveryConfiguration = models_mod.LogDeliveryConfiguration
S3Configuration = models_mod.S3Configuration
ValidationException = models_mod.ValidationException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException
InternalServerException = models_mod.InternalServerException
AccessDeniedException = models_mod.AccessDeniedException
ThrottlingException = models_mod.ThrottlingException
ServiceQuotaExceededException = models_mod.ServiceQuotaExceededException


def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.ValidationException = ValidationException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.InternalServerException = InternalServerException
    mod.AccessDeniedException = AccessDeniedException
    mod.ThrottlingException = ThrottlingException
    mod.ServiceQuotaExceededException = ServiceQuotaExceededException
    # Inject Record classes
    mod.DbClusterRecord = DbClusterRecord
    mod.DbInstanceRecord = DbInstanceRecord
    mod.DbParameterGroupRecord = DbParameterGroupRecord
    mod.LogDeliveryConfiguration = LogDeliveryConfiguration
    mod.S3Configuration = S3Configuration
    # Inject stdlib
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    # Find handler (skip lambdas, exceptions, stdlib)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


# ============================================================
# DbCluster Tests
# ============================================================

class TestDbCluster:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TimestreamForInfluxDBStore()
        return self._store

    def test_create_cluster_happy(self):
        handler = _load_handler('CreateDbCluster')
        resp = handler(self.store, {
            "name": "my-cluster",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
        })
        assert resp["name"] == "my-cluster"
        assert "id" in resp
        assert resp["status"] == "CREATING"
        assert resp["port"] == 8086

    def test_create_cluster_duplicate(self):
        handler = _load_handler('CreateDbCluster')
        req = {
            "name": "dup-cluster",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
        }
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_create_cluster_missing_required(self):
        handler = _load_handler('CreateDbCluster')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_get_cluster_happy(self):
        create = _load_handler('CreateDbCluster')
        get_handler = _load_handler('GetDbCluster')
        resp = create(self.store, {
            "name": "get-cluster",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
        })
        cluster_id = resp["id"]
        resp2 = get_handler(self.store, {"dbClusterId": cluster_id})
        assert resp2["name"] == "get-cluster"

    def test_get_cluster_nonexistent(self):
        get_handler = _load_handler('GetDbCluster')
        with pytest.raises(ResourceNotFoundException):
            get_handler(self.store, {"dbClusterId": "nonexistent"})

    def test_list_clusters(self):
        create = _load_handler('CreateDbCluster')
        list_handler = _load_handler('ListDbClusters')
        create(self.store, {
            "name": "list-c1",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
        })
        create(self.store, {
            "name": "list-c2",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-456"],
            "vpcSecurityGroupIds": ["sg-456"],
        })
        resp = list_handler(self.store, {})
        assert len(resp["items"]) == 2

    def test_update_cluster(self):
        create = _load_handler('CreateDbCluster')
        update = _load_handler('UpdateDbCluster')
        resp = create(self.store, {
            "name": "update-cluster",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
        })
        cid = resp["id"]
        resp2 = update(self.store, {
            "dbClusterId": cid,
            "port": 9999,
            "dbParameterGroupIdentifier": "pg-abc",
        })
        assert resp2["port"] == 9999
        assert resp2["dbParameterGroupIdentifier"] == "pg-abc"

    def test_update_cluster_nonexistent(self):
        update = _load_handler('UpdateDbCluster')
        with pytest.raises(ResourceNotFoundException):
            update(self.store, {"dbClusterId": "nonexistent", "port": 9999})

    def test_delete_cluster(self):
        create = _load_handler('CreateDbCluster')
        delete = _load_handler('DeleteDbCluster')
        get_handler = _load_handler('GetDbCluster')
        resp = create(self.store, {
            "name": "del-cluster",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
        })
        cid = resp["id"]
        delete(self.store, {"dbClusterId": cid})
        with pytest.raises(ResourceNotFoundException):
            get_handler(self.store, {"dbClusterId": cid})

    def test_delete_cluster_nonexistent(self):
        delete = _load_handler('DeleteDbCluster')
        with pytest.raises(ResourceNotFoundException):
            delete(self.store, {"dbClusterId": "nonexistent"})

    def test_reboot_cluster(self):
        create = _load_handler('CreateDbCluster')
        reboot = _load_handler('RebootDbCluster')
        resp = create(self.store, {
            "name": "reboot-cluster",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
        })
        resp2 = reboot(self.store, {"dbClusterId": resp["id"]})
        assert resp2["name"] == "reboot-cluster"

    def test_reboot_cluster_nonexistent(self):
        reboot = _load_handler('RebootDbCluster')
        with pytest.raises(ResourceNotFoundException):
            reboot(self.store, {"dbClusterId": "nonexistent"})


# ============================================================
# DbInstance Tests
# ============================================================

class TestDbInstance:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TimestreamForInfluxDBStore()
        return self._store

    def test_create_instance_happy(self):
        handler = _load_handler('CreateDbInstance')
        resp = handler(self.store, {
            "name": "my-instance",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
        })
        assert resp["name"] == "my-instance"
        assert "id" in resp
        assert resp["status"] == "CREATING"
        assert resp["allocatedStorage"] == 400

    def test_create_instance_duplicate(self):
        handler = _load_handler('CreateDbInstance')
        req = {
            "name": "dup-instance",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
        }
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_create_instance_missing_required(self):
        handler = _load_handler('CreateDbInstance')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_get_instance_happy(self):
        create = _load_handler('CreateDbInstance')
        get_handler = _load_handler('GetDbInstance')
        resp = create(self.store, {
            "name": "get-instance",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
        })
        resp2 = get_handler(self.store, {"identifier": resp["id"]})
        assert resp2["name"] == "get-instance"

    def test_get_instance_nonexistent(self):
        get_handler = _load_handler('GetDbInstance')
        with pytest.raises(ResourceNotFoundException):
            get_handler(self.store, {"identifier": "nonexistent"})

    def test_list_instances(self):
        create = _load_handler('CreateDbInstance')
        list_handler = _load_handler('ListDbInstances')
        create(self.store, {
            "name": "list-i1",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
        })
        create(self.store, {
            "name": "list-i2",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-456"],
            "vpcSecurityGroupIds": ["sg-456"],
            "allocatedStorage": 400,
        })
        resp = list_handler(self.store, {})
        assert len(resp["items"]) == 2

    def test_update_instance(self):
        create = _load_handler('CreateDbInstance')
        update = _load_handler('UpdateDbInstance')
        resp = create(self.store, {
            "name": "update-instance",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
        })
        iid = resp["id"]
        resp2 = update(self.store, {
            "identifier": iid,
            "port": 9999,
            "dbInstanceType": "db.influx.xlarge",
        })
        assert resp2["port"] == 9999
        assert resp2["dbInstanceType"] == "db.influx.xlarge"

    def test_update_instance_nonexistent(self):
        update = _load_handler('UpdateDbInstance')
        with pytest.raises(ResourceNotFoundException):
            update(self.store, {"identifier": "nonexistent", "port": 9999})

    def test_delete_instance(self):
        create = _load_handler('CreateDbInstance')
        delete = _load_handler('DeleteDbInstance')
        get_handler = _load_handler('GetDbInstance')
        resp = create(self.store, {
            "name": "del-instance",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
        })
        iid = resp["id"]
        delete(self.store, {"identifier": iid})
        with pytest.raises(ResourceNotFoundException):
            get_handler(self.store, {"identifier": iid})

    def test_delete_instance_nonexistent(self):
        delete = _load_handler('DeleteDbInstance')
        with pytest.raises(ResourceNotFoundException):
            delete(self.store, {"identifier": "nonexistent"})

    def test_reboot_instance(self):
        create = _load_handler('CreateDbInstance')
        reboot = _load_handler('RebootDbInstance')
        resp = create(self.store, {
            "name": "reboot-instance",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
        })
        resp2 = reboot(self.store, {"identifier": resp["id"]})
        assert resp2["name"] == "reboot-instance"

    def test_reboot_instance_nonexistent(self):
        reboot = _load_handler('RebootDbInstance')
        with pytest.raises(ResourceNotFoundException):
            reboot(self.store, {"identifier": "nonexistent"})

    def test_list_instances_for_cluster(self):
        create_instance = _load_handler('CreateDbInstance')
        list_for = _load_handler('ListDbInstancesForCluster')
        create_instance(self.store, {
            "name": "cluster-i1",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "allocatedStorage": 400,
            "dbClusterId": "cluster-abc",
        })
        create_instance(self.store, {
            "name": "cluster-i2",
            "password": "Passw0rd!",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-456"],
            "vpcSecurityGroupIds": ["sg-456"],
            "allocatedStorage": 400,
            "dbClusterId": "cluster-abc",
        })
        resp = list_for(self.store, {"dbClusterId": "cluster-abc"})
        assert len(resp["items"]) == 2
        # Empty for different cluster
        resp2 = list_for(self.store, {"dbClusterId": "cluster-xyz"})
        assert len(resp2["items"]) == 0


# ============================================================
# DbParameterGroup Tests
# ============================================================

class TestDbParameterGroup:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TimestreamForInfluxDBStore()
        return self._store

    def test_create_param_group_happy(self):
        handler = _load_handler('CreateDbParameterGroup')
        resp = handler(self.store, {
            "name": "my-pg",
            "description": "Test parameter group",
        })
        assert resp["name"] == "my-pg"
        assert resp["description"] == "Test parameter group"
        assert "id" in resp

    def test_create_param_group_duplicate(self):
        handler = _load_handler('CreateDbParameterGroup')
        handler(self.store, {"name": "dup-pg"})
        with pytest.raises(ConflictException):
            handler(self.store, {"name": "dup-pg"})

    def test_create_param_group_missing_required(self):
        handler = _load_handler('CreateDbParameterGroup')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_get_param_group_happy(self):
        create = _load_handler('CreateDbParameterGroup')
        get_handler = _load_handler('GetDbParameterGroup')
        resp = create(self.store, {"name": "get-pg"})
        resp2 = get_handler(self.store, {"identifier": resp["id"]})
        assert resp2["name"] == "get-pg"

    def test_get_param_group_nonexistent(self):
        get_handler = _load_handler('GetDbParameterGroup')
        with pytest.raises(ResourceNotFoundException):
            get_handler(self.store, {"identifier": "nonexistent"})

    def test_list_param_groups(self):
        create = _load_handler('CreateDbParameterGroup')
        list_handler = _load_handler('ListDbParameterGroups')
        create(self.store, {"name": "list-pg1"})
        create(self.store, {"name": "list-pg2"})
        resp = list_handler(self.store, {})
        assert len(resp["items"]) == 2


# ============================================================
# Tags Tests
# ============================================================

class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TimestreamForInfluxDBStore()
        return self._store

    def _create_cluster(self):
        create = _load_handler('CreateDbCluster')
        return create(self.store, {
            "name": "tagged-cluster",
            "dbInstanceType": "db.influx.large",
            "vpcSubnetIds": ["subnet-123"],
            "vpcSecurityGroupIds": ["sg-123"],
            "tags": [{"key": "env", "value": "test"}],
        })

    def test_tag_resource(self):
        resp = self._create_cluster()
        arn = resp["arn"]
        tag_handler = _load_handler('TagResource')
        tag_handler(self.store, {
            "resourceArn": arn,
            "tags": [{"key": "owner", "value": "team-a"}],
        })
        list_tags = _load_handler('ListTagsForResource')
        tags_resp = list_tags(self.store, {"resourceArn": arn})
        assert tags_resp["tags"]["env"] == "test"
        assert tags_resp["tags"]["owner"] == "team-a"

    def test_untag_resource(self):
        resp = self._create_cluster()
        arn = resp["arn"]
        untag = _load_handler('UntagResource')
        untag(self.store, {
            "resourceArn": arn,
            "tagKeys": ["env"],
        })
        list_tags = _load_handler('ListTagsForResource')
        tags_resp = list_tags(self.store, {"resourceArn": arn})
        assert "env" not in tags_resp["tags"]

    def test_list_tags_for_resource(self):
        resp = self._create_cluster()
        arn = resp["arn"]
        list_tags = _load_handler('ListTagsForResource')
        tags_resp = list_tags(self.store, {"resourceArn": arn})
        assert tags_resp["tags"]["env"] == "test"
