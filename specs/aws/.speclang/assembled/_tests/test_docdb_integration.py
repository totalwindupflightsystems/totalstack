"""Integration test for DocumentDB — real DocumentDBStore."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'docdb')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
DocumentDBStore = models_mod.DocumentDBStore
ClusterRecord = models_mod.ClusterRecord
InstanceRecord = models_mod.InstanceRecord
SubnetGroupRecord = models_mod.SubnetGroupRecord
SnapshotRecord = models_mod.SnapshotRecord
ParameterGroupRecord = models_mod.ParameterGroupRecord
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
DBClusterNotFoundException = models_mod.DBClusterNotFoundException
DBInstanceNotFoundException = models_mod.DBInstanceNotFoundException
DBSubnetGroupNotFoundException = models_mod.DBSubnetGroupNotFoundException
DBClusterSnapshotNotFoundException = models_mod.DBClusterSnapshotNotFoundException
DBClusterParameterGroupNotFoundException = models_mod.DBClusterParameterGroupNotFoundException
DBClusterAlreadyExistsException = models_mod.DBClusterAlreadyExistsException
DBInstanceAlreadyExistsException = models_mod.DBInstanceAlreadyExistsException
DBSubnetGroupAlreadyExistsException = models_mod.DBSubnetGroupAlreadyExistsException
DBClusterSnapshotAlreadyExistsException = models_mod.DBClusterSnapshotAlreadyExistsException
DBParameterGroupAlreadyExistsException = models_mod.DBParameterGroupAlreadyExistsException
InvalidDBClusterStateException = models_mod.InvalidDBClusterStateException
InternalServerException = models_mod.InternalServerException


def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.DBClusterNotFoundException = DBClusterNotFoundException
    mod.DBInstanceNotFoundException = DBInstanceNotFoundException
    mod.DBSubnetGroupNotFoundException = DBSubnetGroupNotFoundException
    mod.DBClusterSnapshotNotFoundException = DBClusterSnapshotNotFoundException
    mod.DBClusterParameterGroupNotFoundException = DBClusterParameterGroupNotFoundException
    mod.DBClusterAlreadyExistsException = DBClusterAlreadyExistsException
    mod.DBInstanceAlreadyExistsException = DBInstanceAlreadyExistsException
    mod.DBSubnetGroupAlreadyExistsException = DBSubnetGroupAlreadyExistsException
    mod.DBClusterSnapshotAlreadyExistsException = DBClusterSnapshotAlreadyExistsException
    mod.DBParameterGroupAlreadyExistsException = DBParameterGroupAlreadyExistsException
    mod.InvalidDBClusterStateException = InvalidDBClusterStateException
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.InternalServerException = InternalServerException
    # Inject record classes
    mod.ClusterRecord = ClusterRecord
    mod.InstanceRecord = InstanceRecord
    mod.SubnetGroupRecord = SubnetGroupRecord
    mod.SnapshotRecord = SnapshotRecord
    mod.ParameterGroupRecord = ParameterGroupRecord
    # Inject stdlib
    import time as _time
    import uuid as _uuid
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    # Find handler function
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler function found in {op_name}")


class TestClusterIntegration:
    """DBCluster CRUD tests."""

    @pytest.fixture
    def store(self):
        return DocumentDBStore()

    # ---- CreateDBCluster ----

    def test_create_cluster_happy(self, store):
        handler = _load_handler('CreateDBCluster')
        response = handler(store, {
            'DBClusterIdentifier': 'test-cluster',
            'Engine': 'docdb',
        })
        assert response is not None
        assert response['DBCluster']['DBClusterIdentifier'] == 'test-cluster'
        assert response['DBCluster']['Engine'] == 'docdb'
        assert response['DBCluster']['Status'] == 'available'

    def test_create_cluster_duplicate(self, store):
        handler = _load_handler('CreateDBCluster')
        handler(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
        with pytest.raises(DBClusterAlreadyExistsException):
            handler(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})

    # ---- DescribeDBClusters ----

    def test_describe_clusters_list(self, store):
        create_handler = _load_handler('CreateDBCluster')
        create_handler(store, {'DBClusterIdentifier': 'c1', 'Engine': 'docdb'})
        create_handler(store, {'DBClusterIdentifier': 'c2', 'Engine': 'docdb'})
        handler = _load_handler('DescribeDBClusters')
        response = handler(store, {})
        assert len(response['DBClusters']) == 2

    def test_describe_cluster_by_id(self, store):
        create_handler = _load_handler('CreateDBCluster')
        create_handler(store, {'DBClusterIdentifier': 'my-cluster', 'Engine': 'docdb'})
        handler = _load_handler('DescribeDBClusters')
        response = handler(store, {'DBClusterIdentifier': 'my-cluster'})
        assert response['DBClusters'][0]['DBClusterIdentifier'] == 'my-cluster'

    def test_describe_cluster_nonexistent(self, store):
        handler = _load_handler('DescribeDBClusters')
        with pytest.raises(DBClusterNotFoundException):
            handler(store, {'DBClusterIdentifier': 'nonexistent'})

    # ---- ModifyDBCluster ----

    def test_modify_cluster_happy(self, store):
        create_handler = _load_handler('CreateDBCluster')
        create_handler(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
        handler = _load_handler('ModifyDBCluster')
        response = handler(store, {
            'DBClusterIdentifier': 'test-cluster',
            'BackupRetentionPeriod': 7,
            'DeletionProtection': True,
        })
        assert response['DBCluster']['BackupRetentionPeriod'] == 7
        assert response['DBCluster']['DeletionProtection'] is True

    def test_modify_cluster_nonexistent(self, store):
        handler = _load_handler('ModifyDBCluster')
        with pytest.raises(DBClusterNotFoundException):
            handler(store, {'DBClusterIdentifier': 'nonexistent'})

    # ---- DeleteDBCluster ----

    def test_delete_cluster_happy(self, store):
        create_handler = _load_handler('CreateDBCluster')
        create_handler(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
        handler = _load_handler('DeleteDBCluster')
        response = handler(store, {'DBClusterIdentifier': 'test-cluster'})
        assert response['DBCluster']['DBClusterIdentifier'] == 'test-cluster'
        assert store.clusters('test-cluster') is None

    def test_delete_cluster_nonexistent(self, store):
        handler = _load_handler('DeleteDBCluster')
        with pytest.raises(DBClusterNotFoundException):
            handler(store, {'DBClusterIdentifier': 'nonexistent'})

    def test_delete_cluster_protected(self, store):
        create_handler = _load_handler('CreateDBCluster')
        create_handler(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
        mod_handler = _load_handler('ModifyDBCluster')
        mod_handler(store, {'DBClusterIdentifier': 'test-cluster', 'DeletionProtection': True})
        handler = _load_handler('DeleteDBCluster')
        with pytest.raises(InvalidDBClusterStateException):
            handler(store, {'DBClusterIdentifier': 'test-cluster'})

    # ---- StartDBCluster ----

    def test_start_cluster_happy(self, store):
        create_handler = _load_handler('CreateDBCluster')
        create_handler(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
        # Stop first
        stop_handler = _load_handler('StopDBCluster')
        stop_handler(store, {'DBClusterIdentifier': 'test-cluster'})
        handler = _load_handler('StartDBCluster')
        response = handler(store, {'DBClusterIdentifier': 'test-cluster'})
        assert response['DBCluster']['Status'] == 'available'

    def test_start_cluster_nonexistent(self, store):
        handler = _load_handler('StartDBCluster')
        with pytest.raises(DBClusterNotFoundException):
            handler(store, {'DBClusterIdentifier': 'nonexistent'})

    # ---- StopDBCluster ----

    def test_stop_cluster_happy(self, store):
        create_handler = _load_handler('CreateDBCluster')
        create_handler(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
        handler = _load_handler('StopDBCluster')
        response = handler(store, {'DBClusterIdentifier': 'test-cluster'})
        assert response['DBCluster']['Status'] == 'stopped'

    def test_stop_cluster_nonexistent(self, store):
        handler = _load_handler('StopDBCluster')
        with pytest.raises(DBClusterNotFoundException):
            handler(store, {'DBClusterIdentifier': 'nonexistent'})


class TestInstanceIntegration:
    """DBInstance CRUD tests."""

    @pytest.fixture
    def store_with_cluster(self):
        store = DocumentDBStore()
        # Create a cluster first
        cp = os.path.join(SERVICE_DIR, 'CreateDBCluster.code.py')
        spec = importlib.util.spec_from_file_location('CreateDBCluster', cp)
        mod = importlib.util.module_from_spec(spec)
        mod.DBClusterAlreadyExistsException = DBClusterAlreadyExistsException
        import time as _time
        import uuid as _uuid
        mod.time = _time
        mod.uuid = _uuid
        mod.dataclass = lambda f: f
        mod.ClusterRecord = ClusterRecord
        spec.loader.exec_module(mod)
        skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
        for v in mod.__dict__.values():
            if (isinstance(v, types.FunctionType) and not v.__name__.startswith('_')
                    and v.__name__ not in skip_names):
                v(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
                break
        return store

    # ---- CreateDBInstance ----

    def test_create_instance_happy(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBInstance')
        response = handler(store, {
            'DBInstanceIdentifier': 'test-instance',
            'DBClusterIdentifier': 'test-cluster',
            'DBInstanceClass': 'db.r5.large',
            'Engine': 'docdb',
        })
        assert response['DBInstance']['DBInstanceIdentifier'] == 'test-instance'
        assert response['DBInstance']['DBClusterIdentifier'] == 'test-cluster'

    def test_create_instance_duplicate(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBInstance')
        handler(store, {
            'DBInstanceIdentifier': 'test-instance',
            'DBClusterIdentifier': 'test-cluster',
            'DBInstanceClass': 'db.r5.large',
            'Engine': 'docdb',
        })
        with pytest.raises(DBInstanceAlreadyExistsException):
            handler(store, {
                'DBInstanceIdentifier': 'test-instance',
                'DBClusterIdentifier': 'test-cluster',
                'DBInstanceClass': 'db.r5.large',
                'Engine': 'docdb',
            })

    def test_create_instance_no_cluster(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBInstance')
        with pytest.raises(DBClusterNotFoundException):
            handler(store, {
                'DBInstanceIdentifier': 'test-instance',
                'DBClusterIdentifier': 'no-such-cluster',
                'DBInstanceClass': 'db.r5.large',
                'Engine': 'docdb',
            })

    # ---- DescribeDBInstances ----

    def test_describe_instances_list(self, store_with_cluster):
        store = store_with_cluster
        create_handler = _load_handler('CreateDBInstance')
        create_handler(store, {'DBInstanceIdentifier': 'i1', 'DBClusterIdentifier': 'test-cluster', 'DBInstanceClass': 'db.r5.large', 'Engine': 'docdb'})
        create_handler(store, {'DBInstanceIdentifier': 'i2', 'DBClusterIdentifier': 'test-cluster', 'DBInstanceClass': 'db.r5.large', 'Engine': 'docdb'})
        handler = _load_handler('DescribeDBInstances')
        response = handler(store, {})
        assert len(response['DBInstances']) == 2

    def test_describe_instance_nonexistent(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('DescribeDBInstances')
        with pytest.raises(DBInstanceNotFoundException):
            handler(store, {'DBInstanceIdentifier': 'nonexistent'})

    # ---- ModifyDBInstance ----

    def test_modify_instance_happy(self, store_with_cluster):
        store = store_with_cluster
        create_handler = _load_handler('CreateDBInstance')
        create_handler(store, {'DBInstanceIdentifier': 'test-instance', 'DBClusterIdentifier': 'test-cluster', 'DBInstanceClass': 'db.r5.large', 'Engine': 'docdb'})
        handler = _load_handler('ModifyDBInstance')
        response = handler(store, {
            'DBInstanceIdentifier': 'test-instance',
            'DBInstanceClass': 'db.r5.xlarge',
        })
        assert response['DBInstance']['DBInstanceClass'] == 'db.r5.xlarge'

    def test_modify_instance_nonexistent(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('ModifyDBInstance')
        with pytest.raises(DBInstanceNotFoundException):
            handler(store, {'DBInstanceIdentifier': 'nonexistent'})

    # ---- DeleteDBInstance ----

    def test_delete_instance_happy(self, store_with_cluster):
        store = store_with_cluster
        create_handler = _load_handler('CreateDBInstance')
        create_handler(store, {'DBInstanceIdentifier': 'test-instance', 'DBClusterIdentifier': 'test-cluster', 'DBInstanceClass': 'db.r5.large', 'Engine': 'docdb'})
        handler = _load_handler('DeleteDBInstance')
        response = handler(store, {'DBInstanceIdentifier': 'test-instance'})
        assert response['DBInstance']['DBInstanceIdentifier'] == 'test-instance'
        assert store.instances('test-instance') is None

    def test_delete_instance_nonexistent(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('DeleteDBInstance')
        with pytest.raises(DBInstanceNotFoundException):
            handler(store, {'DBInstanceIdentifier': 'nonexistent'})

    # ---- RebootDBInstance ----

    def test_reboot_instance_happy(self, store_with_cluster):
        store = store_with_cluster
        create_handler = _load_handler('CreateDBInstance')
        create_handler(store, {'DBInstanceIdentifier': 'test-instance', 'DBClusterIdentifier': 'test-cluster', 'DBInstanceClass': 'db.r5.large', 'Engine': 'docdb'})
        handler = _load_handler('RebootDBInstance')
        response = handler(store, {'DBInstanceIdentifier': 'test-instance'})
        assert response['DBInstance']['DBInstanceStatus'] == 'rebooting'

    def test_reboot_instance_nonexistent(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('RebootDBInstance')
        with pytest.raises(DBInstanceNotFoundException):
            handler(store, {'DBInstanceIdentifier': 'nonexistent'})


class TestSubnetGroupIntegration:
    """DBSubnetGroup CRUD tests."""

    @pytest.fixture
    def store(self):
        return DocumentDBStore()

    def test_create_subnet_group_happy(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        response = handler(store, {
            'DBSubnetGroupName': 'test-subnet',
            'DBSubnetGroupDescription': 'Test subnet group',
            'SubnetIds': ['subnet-abc123', 'subnet-def456'],
        })
        assert response['DBSubnetGroup']['DBSubnetGroupName'] == 'test-subnet'

    def test_create_subnet_group_duplicate(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        handler(store, {'DBSubnetGroupName': 'test-subnet', 'DBSubnetGroupDescription': 'Test', 'SubnetIds': ['subnet-abc']})
        with pytest.raises(DBSubnetGroupAlreadyExistsException):
            handler(store, {'DBSubnetGroupName': 'test-subnet', 'DBSubnetGroupDescription': 'Test', 'SubnetIds': ['subnet-abc']})

    def test_describe_subnet_groups_list(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        handler(store, {'DBSubnetGroupName': 'sg1', 'DBSubnetGroupDescription': 'D1', 'SubnetIds': ['subnet-1']})
        handler(store, {'DBSubnetGroupName': 'sg2', 'DBSubnetGroupDescription': 'D2', 'SubnetIds': ['subnet-2']})
        desc_handler = _load_handler('DescribeDBSubnetGroups')
        response = desc_handler(store, {})
        assert len(response['DBSubnetGroups']) == 2

    def test_describe_subnet_group_nonexistent(self, store):
        handler = _load_handler('DescribeDBSubnetGroups')
        with pytest.raises(DBSubnetGroupNotFoundException):
            handler(store, {'DBSubnetGroupName': 'nonexistent'})

    def test_modify_subnet_group_happy(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        handler(store, {'DBSubnetGroupName': 'test-subnet', 'DBSubnetGroupDescription': 'Test', 'SubnetIds': ['subnet-abc']})
        mod_handler = _load_handler('ModifyDBSubnetGroup')
        response = mod_handler(store, {
            'DBSubnetGroupName': 'test-subnet',
            'DBSubnetGroupDescription': 'Updated description',
        })
        assert response['DBSubnetGroup']['DBSubnetGroupDescription'] == 'Updated description'

    def test_delete_subnet_group_happy(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        handler(store, {'DBSubnetGroupName': 'test-subnet', 'DBSubnetGroupDescription': 'Test', 'SubnetIds': ['subnet-abc']})
        del_handler = _load_handler('DeleteDBSubnetGroup')
        response = del_handler(store, {'DBSubnetGroupName': 'test-subnet'})
        assert response == {}
        assert store.subnet_groups('test-subnet') is None

    def test_delete_subnet_group_nonexistent(self, store):
        handler = _load_handler('DeleteDBSubnetGroup')
        with pytest.raises(DBSubnetGroupNotFoundException):
            handler(store, {'DBSubnetGroupName': 'nonexistent'})


class TestSnapshotIntegration:
    """DBClusterSnapshot CRUD tests."""

    @pytest.fixture
    def store_with_cluster(self):
        store = DocumentDBStore()
        cp = os.path.join(SERVICE_DIR, 'CreateDBCluster.code.py')
        spec = importlib.util.spec_from_file_location('CreateDBCluster', cp)
        mod = importlib.util.module_from_spec(spec)
        mod.DBClusterAlreadyExistsException = DBClusterAlreadyExistsException
        mod.ClusterRecord = ClusterRecord
        import time as _time
        import uuid as _uuid
        mod.time = _time
        mod.uuid = _uuid
        mod.dataclass = lambda f: f
        spec.loader.exec_module(mod)
        skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
        for v in mod.__dict__.values():
            if (isinstance(v, types.FunctionType) and not v.__name__.startswith('_')
                    and v.__name__ not in skip_names):
                v(store, {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'})
                break
        return store

    def test_create_snapshot_happy(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBClusterSnapshot')
        response = handler(store, {
            'DBClusterSnapshotIdentifier': 'test-snap',
            'DBClusterIdentifier': 'test-cluster',
        })
        assert response['DBClusterSnapshot']['DBClusterSnapshotIdentifier'] == 'test-snap'

    def test_create_snapshot_duplicate(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBClusterSnapshot')
        handler(store, {'DBClusterSnapshotIdentifier': 'test-snap', 'DBClusterIdentifier': 'test-cluster'})
        with pytest.raises(DBClusterSnapshotAlreadyExistsException):
            handler(store, {'DBClusterSnapshotIdentifier': 'test-snap', 'DBClusterIdentifier': 'test-cluster'})

    def test_create_snapshot_no_cluster(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBClusterSnapshot')
        with pytest.raises(DBClusterNotFoundException):
            handler(store, {'DBClusterSnapshotIdentifier': 'test-snap', 'DBClusterIdentifier': 'nonexistent'})

    def test_describe_snapshots_list(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBClusterSnapshot')
        handler(store, {'DBClusterSnapshotIdentifier': 's1', 'DBClusterIdentifier': 'test-cluster'})
        handler(store, {'DBClusterSnapshotIdentifier': 's2', 'DBClusterIdentifier': 'test-cluster'})
        desc_handler = _load_handler('DescribeDBClusterSnapshots')
        response = desc_handler(store, {})
        assert len(response['DBClusterSnapshots']) == 2

    def test_describe_snapshot_nonexistent(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('DescribeDBClusterSnapshots')
        with pytest.raises(DBClusterSnapshotNotFoundException):
            handler(store, {'DBClusterSnapshotIdentifier': 'nonexistent'})

    def test_delete_snapshot_happy(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBClusterSnapshot')
        handler(store, {'DBClusterSnapshotIdentifier': 'test-snap', 'DBClusterIdentifier': 'test-cluster'})
        del_handler = _load_handler('DeleteDBClusterSnapshot')
        response = del_handler(store, {'DBClusterSnapshotIdentifier': 'test-snap'})
        assert response['DBClusterSnapshot']['DBClusterSnapshotIdentifier'] == 'test-snap'
        assert store.snapshots('test-snap') is None

    def test_copy_snapshot_happy(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBClusterSnapshot')
        handler(store, {'DBClusterSnapshotIdentifier': 'snap-src', 'DBClusterIdentifier': 'test-cluster'})
        copy_handler = _load_handler('CopyDBClusterSnapshot')
        response = copy_handler(store, {
            'SourceDBClusterSnapshotIdentifier': 'snap-src',
            'TargetDBClusterSnapshotIdentifier': 'snap-dst',
        })
        assert response['DBClusterSnapshot']['DBClusterSnapshotIdentifier'] == 'snap-dst'

    def test_restore_cluster_from_snapshot_happy(self, store_with_cluster):
        store = store_with_cluster
        handler = _load_handler('CreateDBClusterSnapshot')
        handler(store, {'DBClusterSnapshotIdentifier': 'test-snap', 'DBClusterIdentifier': 'test-cluster'})
        restore_handler = _load_handler('RestoreDBClusterFromSnapshot')
        response = restore_handler(store, {
            'DBClusterIdentifier': 'restored-cluster',
            'DBClusterSnapshotIdentifier': 'test-snap',
            'Engine': 'docdb',
        })
        assert response['DBCluster']['DBClusterIdentifier'] == 'restored-cluster'
        assert store.clusters('restored-cluster') is not None


class TestParameterGroupIntegration:
    """DBClusterParameterGroup CRUD tests."""

    @pytest.fixture
    def store(self):
        return DocumentDBStore()

    def test_create_parameter_group_happy(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        response = handler(store, {
            'DBClusterParameterGroupName': 'test-pg',
            'DBParameterGroupFamily': 'docdb5.0',
            'Description': 'Test parameter group',
        })
        assert response['DBClusterParameterGroup']['DBClusterParameterGroupName'] == 'test-pg'

    def test_create_parameter_group_duplicate(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        handler(store, {'DBClusterParameterGroupName': 'test-pg', 'DBParameterGroupFamily': 'docdb5.0', 'Description': 'Test'})
        with pytest.raises(DBParameterGroupAlreadyExistsException):
            handler(store, {'DBClusterParameterGroupName': 'test-pg', 'DBParameterGroupFamily': 'docdb5.0', 'Description': 'Test'})

    def test_describe_parameter_groups_list(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        handler(store, {'DBClusterParameterGroupName': 'pg1', 'DBParameterGroupFamily': 'docdb5.0', 'Description': 'D1'})
        handler(store, {'DBClusterParameterGroupName': 'pg2', 'DBParameterGroupFamily': 'docdb5.0', 'Description': 'D2'})
        desc_handler = _load_handler('DescribeDBClusterParameterGroups')
        response = desc_handler(store, {})
        assert len(response['DBClusterParameterGroups']) == 2

    def test_describe_parameter_group_nonexistent(self, store):
        handler = _load_handler('DescribeDBClusterParameterGroups')
        with pytest.raises(DBClusterParameterGroupNotFoundException):
            handler(store, {'DBClusterParameterGroupName': 'nonexistent'})

    def test_modify_parameter_group_happy(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        handler(store, {'DBClusterParameterGroupName': 'test-pg', 'DBParameterGroupFamily': 'docdb5.0', 'Description': 'Test'})
        mod_handler = _load_handler('ModifyDBClusterParameterGroup')
        response = mod_handler(store, {
            'DBClusterParameterGroupName': 'test-pg',
            'Parameters': [
                {'ParameterName': 'audit_logs', 'ParameterValue': 'enabled', 'ApplyMethod': 'immediate'},
                {'ParameterName': 'ttl_monitor', 'ParameterValue': 'enabled', 'ApplyMethod': 'pending-reboot'},
            ],
        })
        assert response['DBClusterParameterGroupName'] == 'test-pg'
        pg = store.parameter_groups('test-pg')
        assert len(pg.Parameters) == 2

    def test_reset_parameter_group_happy(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        handler(store, {'DBClusterParameterGroupName': 'test-pg', 'DBParameterGroupFamily': 'docdb5.0', 'Description': 'Test'})
        mod_handler = _load_handler('ModifyDBClusterParameterGroup')
        mod_handler(store, {
            'DBClusterParameterGroupName': 'test-pg',
            'Parameters': [
                {'ParameterName': 'audit_logs', 'ParameterValue': 'enabled', 'ApplyMethod': 'immediate'},
            ],
        })
        reset_handler = _load_handler('ResetDBClusterParameterGroup')
        response = reset_handler(store, {
            'DBClusterParameterGroupName': 'test-pg',
            'Parameters': [{'ParameterName': 'audit_logs'}],
        })
        assert response['DBClusterParameterGroupName'] == 'test-pg'
        pg = store.parameter_groups('test-pg')
        assert len(pg.Parameters) == 0

    def test_delete_parameter_group_happy(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        handler(store, {'DBClusterParameterGroupName': 'test-pg', 'DBParameterGroupFamily': 'docdb5.0', 'Description': 'Test'})
        del_handler = _load_handler('DeleteDBClusterParameterGroup')
        response = del_handler(store, {'DBClusterParameterGroupName': 'test-pg'})
        assert response == {}
        assert store.parameter_groups('test-pg') is None
