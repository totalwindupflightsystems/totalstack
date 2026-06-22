"""Integration test for MemoryDB — real store with 6 entities."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'memorydb')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

MemoryDBStore = models_mod.MemoryDBStore
ClusterAlreadyExistsFault = models_mod.ClusterAlreadyExistsFault
ClusterNotFoundFault = models_mod.ClusterNotFoundFault
ACLAlreadyExistsFault = models_mod.ACLAlreadyExistsFault
ACLNotFoundFault = models_mod.ACLNotFoundFault
UserAlreadyExistsFault = models_mod.UserAlreadyExistsFault
UserNotFoundFault = models_mod.UserNotFoundFault
ParameterGroupAlreadyExistsFault = models_mod.ParameterGroupAlreadyExistsFault
ParameterGroupNotFoundFault = models_mod.ParameterGroupNotFoundFault
SubnetGroupAlreadyExistsFault = models_mod.SubnetGroupAlreadyExistsFault
SubnetGroupNotFoundFault = models_mod.SubnetGroupNotFoundFault
SnapshotAlreadyExistsFault = models_mod.SnapshotAlreadyExistsFault
SnapshotNotFoundFault = models_mod.SnapshotNotFoundFault
ClusterRecord = models_mod.ClusterRecord
ACLRecord = models_mod.ACLRecord
UserRecord = models_mod.UserRecord
ParameterGroupRecord = models_mod.ParameterGroupRecord
SubnetGroupRecord = models_mod.SubnetGroupRecord
SnapshotRecord = models_mod.SnapshotRecord

EXCEPTIONS = {
    "ClusterAlreadyExistsFault": ClusterAlreadyExistsFault,
    "ClusterNotFoundFault": ClusterNotFoundFault,
    "ACLAlreadyExistsFault": ACLAlreadyExistsFault,
    "ACLNotFoundFault": ACLNotFoundFault,
    "UserAlreadyExistsFault": UserAlreadyExistsFault,
    "UserNotFoundFault": UserNotFoundFault,
    "ParameterGroupAlreadyExistsFault": ParameterGroupAlreadyExistsFault,
    "ParameterGroupNotFoundFault": ParameterGroupNotFoundFault,
    "SubnetGroupAlreadyExistsFault": SubnetGroupAlreadyExistsFault,
    "SubnetGroupNotFoundFault": SubnetGroupNotFoundFault,
    "SnapshotAlreadyExistsFault": SnapshotAlreadyExistsFault,
    "SnapshotNotFoundFault": SnapshotNotFoundFault,
}
RECORDS = {
    "ClusterRecord": ClusterRecord,
    "ACLRecord": ACLRecord,
    "UserRecord": UserRecord,
    "ParameterGroupRecord": ParameterGroupRecord,
    "SubnetGroupRecord": SubnetGroupRecord,
    "SnapshotRecord": SnapshotRecord,
}

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    for k, v in EXCEPTIONS.items():
        setattr(mod, k, v)
    for k, v in RECORDS.items():
        setattr(mod, k, v)
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestCluster:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MemoryDBStore()
        return self._store

    def test_create_cluster(self):
        h = _load_handler('CreateCluster')
        resp = h(self.store, {
            "ClusterName": "test-cluster",
            "NodeType": "db.r6g.large",
            "ACLName": "open-access",
        })
        assert resp["Name"] == "test-cluster"
        assert resp["Status"] == "creating"

    def test_create_cluster_duplicate(self):
        h = _load_handler('CreateCluster')
        req = {"ClusterName": "dup-cluster", "NodeType": "db.r6g.large", "ACLName": "open-access"}
        h(self.store, req)
        with pytest.raises(ClusterAlreadyExistsFault):
            h(self.store, req)

    def test_create_cluster_missing_required(self):
        h = _load_handler('CreateCluster')
        with pytest.raises(TypeError):
            h(self.store, {})

    def test_describe_clusters_list(self):
        h = _load_handler('CreateCluster')
        h(self.store, {"ClusterName": "c1", "NodeType": "db.r6g.large", "ACLName": "open-access"})
        h(self.store, {"ClusterName": "c2", "NodeType": "db.r6g.large", "ACLName": "open-access"})
        dh = _load_handler('DescribeClusters')
        resp = dh(self.store, {})
        assert len(resp["Clusters"]) == 2

    def test_describe_clusters_single(self):
        h = _load_handler('CreateCluster')
        h(self.store, {"ClusterName": "c-single", "NodeType": "db.r6g.large", "ACLName": "open-access"})
        dh = _load_handler('DescribeClusters')
        resp = dh(self.store, {"ClusterName": "c-single"})
        assert resp["Clusters"][0]["Name"] == "c-single"

    def test_describe_cluster_nonexistent(self):
        dh = _load_handler('DescribeClusters')
        with pytest.raises(ClusterNotFoundFault):
            dh(self.store, {"ClusterName": "nonexistent"})

    def test_delete_cluster(self):
        h = _load_handler('CreateCluster')
        h(self.store, {"ClusterName": "to-delete", "NodeType": "db.r6g.large", "ACLName": "open-access"})
        dh = _load_handler('DeleteCluster')
        resp = dh(self.store, {"ClusterName": "to-delete"})
        assert resp["Name"] == "to-delete"

    def test_delete_cluster_nonexistent(self):
        dh = _load_handler('DeleteCluster')
        with pytest.raises(ClusterNotFoundFault):
            dh(self.store, {"ClusterName": "nonexistent"})


class TestACL:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MemoryDBStore()
        return self._store

    def test_create_acl(self):
        h = _load_handler('CreateACL')
        resp = h(self.store, {"ACLName": "test-acl"})
        assert resp["Name"] == "test-acl"

    def test_create_acl_duplicate(self):
        h = _load_handler('CreateACL')
        h(self.store, {"ACLName": "dup-acl"})
        with pytest.raises(ACLAlreadyExistsFault):
            h(self.store, {"ACLName": "dup-acl"})

    def test_describe_acls(self):
        h = _load_handler('CreateACL')
        h(self.store, {"ACLName": "a1"})
        h(self.store, {"ACLName": "a2"})
        dh = _load_handler('DescribeACLs')
        resp = dh(self.store, {})
        assert len(resp["ACLs"]) == 2

    def test_describe_acl_nonexistent(self):
        dh = _load_handler('DescribeACLs')
        with pytest.raises(ACLNotFoundFault):
            dh(self.store, {"ACLName": "nonexistent"})

    def test_delete_acl(self):
        h = _load_handler('CreateACL')
        h(self.store, {"ACLName": "to-delete"})
        dh = _load_handler('DeleteACL')
        resp = dh(self.store, {"ACLName": "to-delete"})
        assert resp["Name"] == "to-delete"


class TestUser:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MemoryDBStore()
        return self._store

    def test_create_user(self):
        h = _load_handler('CreateUser')
        resp = h(self.store, {"UserName": "test-user", "AuthenticationMode": {"Type": "password", "Passwords": ["pwd123"]}})
        assert resp["Name"] == "test-user"

    def test_create_user_duplicate(self):
        h = _load_handler('CreateUser')
        h(self.store, {"UserName": "dup-user", "AuthenticationMode": {"Type": "password", "Passwords": ["pwd123"]}})
        with pytest.raises(UserAlreadyExistsFault):
            h(self.store, {"UserName": "dup-user", "AuthenticationMode": {"Type": "password", "Passwords": ["pwd123"]}})

    def test_describe_users(self):
        h = _load_handler('CreateUser')
        h(self.store, {"UserName": "u1", "AuthenticationMode": {"Type": "password", "Passwords": ["pwd123"]}})
        dh = _load_handler('DescribeUsers')
        resp = dh(self.store, {})
        assert len(resp["Users"]) == 1

    def test_delete_user(self):
        h = _load_handler('CreateUser')
        h(self.store, {"UserName": "to-delete", "AuthenticationMode": {"Type": "password", "Passwords": ["pwd123"]}})
        dh = _load_handler('DeleteUser')
        resp = dh(self.store, {"UserName": "to-delete"})
        assert resp["Name"] == "to-delete"


class TestParameterGroup:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MemoryDBStore()
        return self._store

    def test_create_parameter_group(self):
        h = _load_handler('CreateParameterGroup')
        resp = h(self.store, {"ParameterGroupName": "test-pg", "Family": "memorydb_redis7"})
        assert resp["Name"] == "test-pg"

    def test_create_pg_duplicate(self):
        h = _load_handler('CreateParameterGroup')
        h(self.store, {"ParameterGroupName": "dup-pg", "Family": "memorydb_redis7"})
        with pytest.raises(ParameterGroupAlreadyExistsFault):
            h(self.store, {"ParameterGroupName": "dup-pg", "Family": "memorydb_redis7"})


class TestSubnetGroup:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MemoryDBStore()
        return self._store

    def test_create_subnet_group(self):
        h = _load_handler('CreateSubnetGroup')
        resp = h(self.store, {"SubnetGroupName": "test-sg", "SubnetIds": ["subnet-abc"]})
        assert resp["Name"] == "test-sg"

    def test_create_sg_duplicate(self):
        h = _load_handler('CreateSubnetGroup')
        h(self.store, {"SubnetGroupName": "dup-sg", "SubnetIds": ["subnet-abc"]})
        with pytest.raises(SubnetGroupAlreadyExistsFault):
            h(self.store, {"SubnetGroupName": "dup-sg", "SubnetIds": ["subnet-abc"]})


class TestSnapshot:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MemoryDBStore()
        return self._store

    def _create_cluster(self, name="snap-cluster"):
        h = _load_handler('CreateCluster')
        h(self.store, {"ClusterName": name, "NodeType": "db.r6g.large", "ACLName": "open-access"})

    def test_create_snapshot(self):
        self._create_cluster()
        h = _load_handler('CreateSnapshot')
        resp = h(self.store, {"SnapshotName": "test-snap", "ClusterName": "snap-cluster"})
        assert resp["Name"] == "test-snap"

    def test_create_snapshot_missing_cluster(self):
        h = _load_handler('CreateSnapshot')
        with pytest.raises(ClusterNotFoundFault):
            h(self.store, {"SnapshotName": "bad-snap", "ClusterName": "nonexistent"})

    def test_create_snapshot_duplicate(self):
        self._create_cluster()
        h = _load_handler('CreateSnapshot')
        h(self.store, {"SnapshotName": "dup-snap", "ClusterName": "snap-cluster"})
        with pytest.raises(SnapshotAlreadyExistsFault):
            h(self.store, {"SnapshotName": "dup-snap", "ClusterName": "snap-cluster"})


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = MemoryDBStore()
        return self._store

    def test_tag_resource(self):
        h = _load_handler('TagResource')
        arn = "arn:aws:memorydb:us-east-1:000000000000:cluster/my-cluster"
        resp = h(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "prod"}]})
        assert len(resp["TagList"]) == 1

    def test_list_tags(self):
        h = _load_handler('TagResource')
        arn = "arn:aws:memorydb:us-east-1:000000000000:cluster/my-cluster"
        h(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "prod"}]})
        lh = _load_handler('ListTags')
        resp = lh(self.store, {"ResourceArn": arn})
        assert resp["TagList"][0]["Key"] == "env"

    def test_untag_resource(self):
        h = _load_handler('TagResource')
        lh = _load_handler('ListTags')
        uh = _load_handler('UntagResource')
        arn = "arn:aws:memorydb:us-east-1:000000000000:cluster/my-cluster"
        h(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "prod"}]})
        uh(self.store, {"ResourceArn": arn, "TagKeys": ["env"]})
        resp = lh(self.store, {"ResourceArn": arn})
        assert len(resp["TagList"]) == 0
