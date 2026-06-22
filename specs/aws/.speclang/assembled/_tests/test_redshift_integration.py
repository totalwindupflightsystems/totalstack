"""Integration test for Redshift — real store with generated handlers."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'redshift')

# Load the models module
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

RedshiftStore = models_mod.RedshiftStore
ClusterRecord = models_mod.ClusterRecord
ClusterParameterGroupRecord = models_mod.ClusterParameterGroupRecord
ClusterSnapshotRecord = models_mod.ClusterSnapshotRecord
ClusterSubnetGroupRecord = models_mod.ClusterSubnetGroupRecord
EventSubscriptionRecord = models_mod.EventSubscriptionRecord
ClusterNotFoundFault = models_mod.ClusterNotFoundFault
ClusterAlreadyExistsFault = models_mod.ClusterAlreadyExistsFault
ClusterParameterGroupNotFoundFault = models_mod.ClusterParameterGroupNotFoundFault
ClusterParameterGroupAlreadyExistsFault = models_mod.ClusterParameterGroupAlreadyExistsFault
ClusterSnapshotNotFoundFault = models_mod.ClusterSnapshotNotFoundFault
ClusterSnapshotAlreadyExistsFault = models_mod.ClusterSnapshotAlreadyExistsFault
ClusterSubnetGroupNotFoundFault = models_mod.ClusterSubnetGroupNotFoundFault
ClusterSubnetGroupAlreadyExistsFault = models_mod.ClusterSubnetGroupAlreadyExistsFault
SubscriptionNotFoundFault = models_mod.SubscriptionNotFoundFault
SubscriptionAlreadyExistFault = models_mod.SubscriptionAlreadyExistFault


def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.ClusterNotFoundFault = ClusterNotFoundFault
    mod.ClusterAlreadyExistsFault = ClusterAlreadyExistsFault
    mod.ClusterParameterGroupNotFoundFault = ClusterParameterGroupNotFoundFault
    mod.ClusterParameterGroupAlreadyExistsFault = ClusterParameterGroupAlreadyExistsFault
    mod.ClusterSnapshotNotFoundFault = ClusterSnapshotNotFoundFault
    mod.ClusterSnapshotAlreadyExistsFault = ClusterSnapshotAlreadyExistsFault
    mod.ClusterSubnetGroupNotFoundFault = ClusterSubnetGroupNotFoundFault
    mod.ClusterSubnetGroupAlreadyExistsFault = ClusterSubnetGroupAlreadyExistsFault
    mod.SubscriptionNotFoundFault = SubscriptionNotFoundFault
    mod.SubscriptionAlreadyExistFault = SubscriptionAlreadyExistFault
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v


# ─── Cluster Tests ────────────────────────────────────────────────────────────

class TestCluster:
    @pytest.fixture
    def store(self):
        return RedshiftStore()

    def test_create_cluster_happy(self, store):
        handler = _load_handler('CreateCluster')
        response = handler(store, {
            "ClusterIdentifier": "test-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
            "MasterUserPassword": "Password1!",
        })
        assert response["Cluster"]["ClusterIdentifier"] == "test-cluster"
        assert response["Cluster"]["ClusterStatus"] == "available"
        assert response["Cluster"]["NodeType"] == "dc2.large"

    def test_create_cluster_duplicate(self, store):
        handler = _load_handler('CreateCluster')
        handler(store, {
            "ClusterIdentifier": "dup-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
            "MasterUserPassword": "Password1!",
        })
        with pytest.raises(ClusterAlreadyExistsFault):
            handler(store, {
                "ClusterIdentifier": "dup-cluster",
                "NodeType": "dc2.large",
                "MasterUsername": "admin",
            })

    def test_describe_clusters_all(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "cluster-a",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        create(store, {
            "ClusterIdentifier": "cluster-b",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        handler = _load_handler('DescribeClusters')
        response = handler(store, {})
        assert len(response["Clusters"]) == 2

    def test_describe_clusters_single(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "my-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        handler = _load_handler('DescribeClusters')
        response = handler(store, {"ClusterIdentifier": "my-cluster"})
        assert response["Clusters"][0]["ClusterIdentifier"] == "my-cluster"

    def test_describe_clusters_nonexistent(self, store):
        handler = _load_handler('DescribeClusters')
        with pytest.raises(ClusterNotFoundFault):
            handler(store, {"ClusterIdentifier": "no-such-cluster"})

    def test_modify_cluster_happy(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "mod-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        handler = _load_handler('ModifyCluster')
        response = handler(store, {
            "ClusterIdentifier": "mod-cluster",
            "ClusterType": "multi-node",
            "NumberOfNodes": 4,
        })
        assert response["Cluster"]["ClusterType"] == "multi-node"
        assert response["Cluster"]["NumberOfNodes"] == 4

    def test_modify_cluster_new_identifier(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "old-name",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        handler = _load_handler('ModifyCluster')
        response = handler(store, {
            "ClusterIdentifier": "old-name",
            "NewClusterIdentifier": "new-name",
        })
        assert response["Cluster"]["ClusterIdentifier"] == "new-name"

    def test_modify_cluster_nonexistent(self, store):
        handler = _load_handler('ModifyCluster')
        with pytest.raises(ClusterNotFoundFault):
            handler(store, {"ClusterIdentifier": "no-cluster", "ClusterType": "multi-node"})

    def test_delete_cluster_skip_final_snapshot(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "del-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        handler = _load_handler('DeleteCluster')
        handler(store, {
            "ClusterIdentifier": "del-cluster",
            "SkipFinalClusterSnapshot": True,
        })
        assert store.clusters("del-cluster") is None

    def test_delete_cluster_nonexistent(self, store):
        handler = _load_handler('DeleteCluster')
        with pytest.raises(ClusterNotFoundFault):
            handler(store, {"ClusterIdentifier": "no-cluster", "SkipFinalClusterSnapshot": True})

    def test_pause_cluster(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "pause-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        handler = _load_handler('PauseCluster')
        response = handler(store, {"ClusterIdentifier": "pause-cluster"})
        assert response["Cluster"]["ClusterStatus"] == "paused"

    def test_resume_cluster(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "resume-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        _load_handler('PauseCluster')(store, {"ClusterIdentifier": "resume-cluster"})
        handler = _load_handler('ResumeCluster')
        response = handler(store, {"ClusterIdentifier": "resume-cluster"})
        assert response["Cluster"]["ClusterStatus"] == "available"

    def test_resize_cluster(self, store):
        create = _load_handler('CreateCluster')
        create(store, {
            "ClusterIdentifier": "resize-cluster",
            "NodeType": "dc2.large",
            "MasterUsername": "admin",
        })
        handler = _load_handler('ResizeCluster')
        response = handler(store, {
            "ClusterIdentifier": "resize-cluster",
            "ClusterType": "multi-node",
            "NumberOfNodes": 4,
        })
        assert response["Cluster"]["NumberOfNodes"] == 4


# ─── Parameter Group Tests ────────────────────────────────────────────────────

class TestParameterGroup:
    @pytest.fixture
    def store(self):
        return RedshiftStore()

    def test_create_happy(self, store):
        handler = _load_handler('CreateClusterParameterGroup')
        response = handler(store, {
            "ParameterGroupName": "test-pg",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "Test PG",
        })
        assert response["ClusterParameterGroup"]["ParameterGroupName"] == "test-pg"
        assert response["ClusterParameterGroup"]["ParameterGroupFamily"] == "redshift-1.0"

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateClusterParameterGroup')
        handler(store, {
            "ParameterGroupName": "dup-pg",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "Dup PG",
        })
        with pytest.raises(ClusterParameterGroupAlreadyExistsFault):
            handler(store, {
                "ParameterGroupName": "dup-pg",
                "ParameterGroupFamily": "redshift-1.0",
                "Description": "Dup PG",
            })

    def test_describe_all(self, store):
        handler = _load_handler('CreateClusterParameterGroup')
        handler(store, {
            "ParameterGroupName": "pg-1",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "PG 1",
        })
        handler(store, {
            "ParameterGroupName": "pg-2",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "PG 2",
        })
        desc = _load_handler('DescribeClusterParameterGroups')
        response = desc(store, {})
        assert len(response["ParameterGroups"]) == 2

    def test_describe_single(self, store):
        handler = _load_handler('CreateClusterParameterGroup')
        handler(store, {
            "ParameterGroupName": "my-pg",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "My PG",
        })
        desc = _load_handler('DescribeClusterParameterGroups')
        response = desc(store, {"ParameterGroupName": "my-pg"})
        assert response["ParameterGroups"][0]["ParameterGroupName"] == "my-pg"

    def test_describe_nonexistent(self, store):
        handler = _load_handler('DescribeClusterParameterGroups')
        with pytest.raises(ClusterParameterGroupNotFoundFault):
            handler(store, {"ParameterGroupName": "no-pg"})

    def test_modify_happy(self, store):
        create = _load_handler('CreateClusterParameterGroup')
        create(store, {
            "ParameterGroupName": "mod-pg",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "Mod PG",
        })
        handler = _load_handler('ModifyClusterParameterGroup')
        response = handler(store, {
            "ParameterGroupName": "mod-pg",
            "Parameters": [
                {"ParameterName": "max_connections", "ParameterValue": "100"}
            ],
        })
        assert response["ParameterGroupName"] == "mod-pg"

    def test_delete_happy(self, store):
        create = _load_handler('CreateClusterParameterGroup')
        create(store, {
            "ParameterGroupName": "del-pg",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "Del PG",
        })
        handler = _load_handler('DeleteClusterParameterGroup')
        handler(store, {"ParameterGroupName": "del-pg"})
        assert store.parameter_groups("del-pg") is None

    def test_delete_nonexistent(self, store):
        handler = _load_handler('DeleteClusterParameterGroup')
        with pytest.raises(ClusterParameterGroupNotFoundFault):
            handler(store, {"ParameterGroupName": "no-pg"})

    def test_reset_all(self, store):
        create = _load_handler('CreateClusterParameterGroup')
        create(store, {
            "ParameterGroupName": "reset-pg",
            "ParameterGroupFamily": "redshift-1.0",
            "Description": "Reset PG",
        })
        handler = _load_handler('ResetClusterParameterGroup')
        response = handler(store, {
            "ParameterGroupName": "reset-pg",
            "ResetAllParameters": True,
        })
        assert response["ParameterGroupStatus"] == "in-sync"


# ─── Snapshot Tests ───────────────────────────────────────────────────────────

class TestSnapshot:
    @pytest.fixture
    def store(self):
        s = RedshiftStore()
        s.create_cluster("snap-cluster", "dc2.large", "admin")
        return s

    def test_create_happy(self, store):
        handler = _load_handler('CreateClusterSnapshot')
        response = handler(store, {
            "SnapshotIdentifier": "snap-1",
            "ClusterIdentifier": "snap-cluster",
        })
        assert response["Snapshot"]["SnapshotIdentifier"] == "snap-1"
        assert response["Snapshot"]["Status"] == "available"

    def test_create_cluster_not_found(self, store):
        handler = _load_handler('CreateClusterSnapshot')
        with pytest.raises(ClusterNotFoundFault):
            handler(store, {
                "SnapshotIdentifier": "snap-x",
                "ClusterIdentifier": "no-cluster",
            })

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateClusterSnapshot')
        handler(store, {"SnapshotIdentifier": "dup-snap", "ClusterIdentifier": "snap-cluster"})
        with pytest.raises(ClusterSnapshotAlreadyExistsFault):
            handler(store, {"SnapshotIdentifier": "dup-snap", "ClusterIdentifier": "snap-cluster"})

    def test_describe_single(self, store):
        create = _load_handler('CreateClusterSnapshot')
        create(store, {"SnapshotIdentifier": "my-snap", "ClusterIdentifier": "snap-cluster"})
        desc = _load_handler('DescribeClusterSnapshots')
        response = desc(store, {"SnapshotIdentifier": "my-snap"})
        assert response["Snapshots"][0]["SnapshotIdentifier"] == "my-snap"

    def test_describe_nonexistent(self, store):
        handler = _load_handler('DescribeClusterSnapshots')
        with pytest.raises(ClusterSnapshotNotFoundFault):
            handler(store, {"SnapshotIdentifier": "no-snap"})

    def test_delete_happy(self, store):
        create = _load_handler('CreateClusterSnapshot')
        create(store, {"SnapshotIdentifier": "del-snap", "ClusterIdentifier": "snap-cluster"})
        handler = _load_handler('DeleteClusterSnapshot')
        handler(store, {"SnapshotIdentifier": "del-snap"})
        assert store.snapshots("del-snap") is None

    def test_copy_happy(self, store):
        create = _load_handler('CreateClusterSnapshot')
        create(store, {"SnapshotIdentifier": "src-snap", "ClusterIdentifier": "snap-cluster"})
        handler = _load_handler('CopyClusterSnapshot')
        response = handler(store, {
            "SourceSnapshotIdentifier": "src-snap",
            "TargetSnapshotIdentifier": "cpy-snap",
        })
        assert response["Snapshot"]["SnapshotIdentifier"] == "cpy-snap"
        assert store.snapshots("cpy-snap") is not None


# ─── Subnet Group Tests ───────────────────────────────────────────────────────

class TestSubnetGroup:
    @pytest.fixture
    def store(self):
        return RedshiftStore()

    def test_create_happy(self, store):
        handler = _load_handler('CreateClusterSubnetGroup')
        response = handler(store, {
            "ClusterSubnetGroupName": "test-subnet",
            "Description": "Test subnet group",
            "SubnetIds": ["subnet-abc", "subnet-def"],
        })
        assert response["ClusterSubnetGroup"]["ClusterSubnetGroupName"] == "test-subnet"

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateClusterSubnetGroup')
        handler(store, {
            "ClusterSubnetGroupName": "dup-sg",
            "Description": "Dup SG",
            "SubnetIds": ["subnet-1"],
        })
        with pytest.raises(ClusterSubnetGroupAlreadyExistsFault):
            handler(store, {
                "ClusterSubnetGroupName": "dup-sg",
                "Description": "Dup SG",
                "SubnetIds": ["subnet-1"],
            })

    def test_describe_single(self, store):
        create = _load_handler('CreateClusterSubnetGroup')
        create(store, {
            "ClusterSubnetGroupName": "my-sg",
            "Description": "My SG",
            "SubnetIds": ["subnet-1"],
        })
        desc = _load_handler('DescribeClusterSubnetGroups')
        response = desc(store, {"ClusterSubnetGroupName": "my-sg"})
        assert response["ClusterSubnetGroups"][0]["ClusterSubnetGroupName"] == "my-sg"

    def test_describe_all(self, store):
        create = _load_handler('CreateClusterSubnetGroup')
        create(store, {"ClusterSubnetGroupName": "sg-1", "Description": "SG 1", "SubnetIds": ["subnet-1"]})
        create(store, {"ClusterSubnetGroupName": "sg-2", "Description": "SG 2", "SubnetIds": ["subnet-2"]})
        desc = _load_handler('DescribeClusterSubnetGroups')
        response = desc(store, {})
        assert len(response["ClusterSubnetGroups"]) == 2

    def test_describe_nonexistent(self, store):
        handler = _load_handler('DescribeClusterSubnetGroups')
        with pytest.raises(ClusterSubnetGroupNotFoundFault):
            handler(store, {"ClusterSubnetGroupName": "no-sg"})

    def test_modify_happy(self, store):
        create = _load_handler('CreateClusterSubnetGroup')
        create(store, {"ClusterSubnetGroupName": "mod-sg", "Description": "Mod SG", "SubnetIds": ["subnet-1"]})
        handler = _load_handler('ModifyClusterSubnetGroup')
        response = handler(store, {
            "ClusterSubnetGroupName": "mod-sg",
            "SubnetIds": ["subnet-2", "subnet-3"],
            "Description": "Updated",
        })
        assert len(response["ClusterSubnetGroup"]["Subnets"]) == 2

    def test_delete_happy(self, store):
        create = _load_handler('CreateClusterSubnetGroup')
        create(store, {"ClusterSubnetGroupName": "del-sg", "Description": "Del SG", "SubnetIds": ["subnet-1"]})
        handler = _load_handler('DeleteClusterSubnetGroup')
        handler(store, {"ClusterSubnetGroupName": "del-sg"})
        assert store.subnet_groups("del-sg") is None

    def test_delete_nonexistent(self, store):
        handler = _load_handler('DeleteClusterSubnetGroup')
        with pytest.raises(ClusterSubnetGroupNotFoundFault):
            handler(store, {"ClusterSubnetGroupName": "no-sg"})


# ─── Event Subscription Tests ─────────────────────────────────────────────────

class TestEventSubscription:
    @pytest.fixture
    def store(self):
        return RedshiftStore()

    def test_create_happy(self, store):
        handler = _load_handler('CreateEventSubscription')
        response = handler(store, {
            "SubscriptionName": "test-sub",
            "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:redshift-events",
            "SourceType": "cluster",
        })
        assert response["EventSubscription"]["SubscriptionName"] == "test-sub"
        assert response["EventSubscription"]["Enabled"] is True

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateEventSubscription')
        handler(store, {
            "SubscriptionName": "dup-sub",
            "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:topic",
        })
        with pytest.raises(SubscriptionAlreadyExistFault):
            handler(store, {
                "SubscriptionName": "dup-sub",
                "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:topic",
            })

    def test_describe_single(self, store):
        create = _load_handler('CreateEventSubscription')
        create(store, {"SubscriptionName": "my-sub", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:topic"})
        desc = _load_handler('DescribeEventSubscriptions')
        response = desc(store, {"SubscriptionName": "my-sub"})
        assert response["EventSubscriptionsList"][0]["SubscriptionName"] == "my-sub"

    def test_describe_nonexistent(self, store):
        handler = _load_handler('DescribeEventSubscriptions')
        with pytest.raises(SubscriptionNotFoundFault):
            handler(store, {"SubscriptionName": "no-sub"})

    def test_modify_happy(self, store):
        create = _load_handler('CreateEventSubscription')
        create(store, {"SubscriptionName": "mod-sub", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:topic"})
        handler = _load_handler('ModifyEventSubscription')
        response = handler(store, {
            "SubscriptionName": "mod-sub",
            "Enabled": False,
        })
        assert response["EventSubscription"]["Enabled"] is False

    def test_delete_happy(self, store):
        create = _load_handler('CreateEventSubscription')
        create(store, {"SubscriptionName": "del-sub", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:topic"})
        handler = _load_handler('DeleteEventSubscription')
        handler(store, {"SubscriptionName": "del-sub"})
        assert store.subscriptions("del-sub") is None

    def test_delete_nonexistent(self, store):
        handler = _load_handler('DeleteEventSubscription')
        with pytest.raises(SubscriptionNotFoundFault):
            handler(store, {"SubscriptionName": "no-sub"})
