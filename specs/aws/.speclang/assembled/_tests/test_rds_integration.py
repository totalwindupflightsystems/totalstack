"""Integration test for RDS — real RDSStore with generated handler code."""
import os
import types
import importlib.util

import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'rds')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out all needed names
RDSStore = models_mod.RDSStore
DBInstanceRecord = models_mod.DBInstanceRecord
DBClusterRecord = models_mod.DBClusterRecord
DBSnapshotRecord = models_mod.DBSnapshotRecord
DBParameterGroupRecord = models_mod.DBParameterGroupRecord
DBSubnetGroupRecord = models_mod.DBSubnetGroupRecord
DBClusterParameterGroupRecord = models_mod.DBClusterParameterGroupRecord
DBInstanceNotFoundFault = models_mod.DBInstanceNotFoundFault
DBClusterNotFoundFault = models_mod.DBClusterNotFoundFault
DBSnapshotNotFoundFault = models_mod.DBSnapshotNotFoundFault
DBParameterGroupNotFoundFault = models_mod.DBParameterGroupNotFoundFault
DBSubnetGroupNotFoundFault = models_mod.DBSubnetGroupNotFoundFault
DBClusterParameterGroupNotFoundFault = models_mod.DBClusterParameterGroupNotFoundFault
DBInstanceAlreadyExistsFault = models_mod.DBInstanceAlreadyExistsFault
DBClusterAlreadyExistsFault = models_mod.DBClusterAlreadyExistsFault
DBSnapshotAlreadyExistsFault = models_mod.DBSnapshotAlreadyExistsFault
DBParameterGroupAlreadyExistsFault = models_mod.DBParameterGroupAlreadyExistsFault
DBSubnetGroupAlreadyExistsFault = models_mod.DBSubnetGroupAlreadyExistsFault
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
InvalidParameterCombinationException = models_mod.InvalidParameterCombinationException
InvalidDBInstanceStateFault = models_mod.InvalidDBInstanceStateFault
InvalidDBClusterStateFault = models_mod.InvalidDBClusterStateFault
SnapshotQuotaExceededFault = models_mod.SnapshotQuotaExceededFault


def _load_handler(op_name):
    """Load a generated .code.py handler — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.DBInstanceNotFoundFault = DBInstanceNotFoundFault
    mod.DBClusterNotFoundFault = DBClusterNotFoundFault
    mod.DBSnapshotNotFoundFault = DBSnapshotNotFoundFault
    mod.DBParameterGroupNotFoundFault = DBParameterGroupNotFoundFault
    mod.DBSubnetGroupNotFoundFault = DBSubnetGroupNotFoundFault
    mod.DBClusterParameterGroupNotFoundFault = DBClusterParameterGroupNotFoundFault
    mod.DBInstanceAlreadyExistsFault = DBInstanceAlreadyExistsFault
    mod.DBClusterAlreadyExistsFault = DBClusterAlreadyExistsFault
    mod.DBSnapshotAlreadyExistsFault = DBSnapshotAlreadyExistsFault
    mod.DBParameterGroupAlreadyExistsFault = DBParameterGroupAlreadyExistsFault
    mod.DBSubnetGroupAlreadyExistsFault = DBSubnetGroupAlreadyExistsFault
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.InvalidParameterCombinationException = InvalidParameterCombinationException
    mod.InvalidDBInstanceStateFault = InvalidDBInstanceStateFault
    mod.InvalidDBClusterStateFault = InvalidDBClusterStateFault
    mod.SnapshotQuotaExceededFault = SnapshotQuotaExceededFault
    spec.loader.exec_module(mod)
    # Discover handler function — skip __name__ starting with _ and skip <lambda>
    skip_names = {'<lambda>', 'dataclass', 'time', 'uuid'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler found in {op_name}.code.py")


# ── DB Instance Tests ──────────────────────────────────────────────────

class TestDBInstance:
    @pytest.fixture
    def store(self):
        return RDSStore()

    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBInstance')
        response = handler(store, {
            'DBInstanceIdentifier': 'test-db-1',
            'DBInstanceClass': 'db.t3.micro',
            'Engine': 'mysql',
            'MasterUsername': 'admin',
            'MasterUserPassword': 'password123',
            'AllocatedStorage': 20,
        })
        assert response is not None
        assert response['DBInstanceIdentifier'] == 'test-db-1'
        assert response['Engine'] == 'mysql'
        assert response['DBInstanceStatus'] == 'available'
        assert 'Endpoint' in response

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBInstance')
        req = {
            'DBInstanceIdentifier': 'test-db-1',
            'DBInstanceClass': 'db.t3.micro',
            'Engine': 'mysql',
        }
        handler(store, req)
        with pytest.raises(DBInstanceAlreadyExistsFault):
            handler(store, req)

    def test_describe_single(self, store):
        create = _load_handler('CreateDBInstance')
        create(store, {
            'DBInstanceIdentifier': 'test-db-1',
            'DBInstanceClass': 'db.t3.micro',
            'Engine': 'mysql',
        })
        describe = _load_handler('DescribeDBInstances')
        response = describe(store, {'DBInstanceIdentifier': 'test-db-1'})
        assert 'DBInstances' in response
        assert len(response['DBInstances']) == 1
        assert response['DBInstances'][0]['DBInstanceIdentifier'] == 'test-db-1'

    def test_describe_all(self, store):
        create = _load_handler('CreateDBInstance')
        create(store, {
            'DBInstanceIdentifier': 'db-a',
            'DBInstanceClass': 'db.t3.micro',
            'Engine': 'mysql',
        })
        create(store, {
            'DBInstanceIdentifier': 'db-b',
            'DBInstanceClass': 'db.t3.small',
            'Engine': 'postgres',
        })
        describe = _load_handler('DescribeDBInstances')
        response = describe(store, {})
        assert len(response['DBInstances']) == 2

    def test_describe_nonexistent(self, store):
        describe = _load_handler('DescribeDBInstances')
        with pytest.raises(DBInstanceNotFoundFault):
            describe(store, {'DBInstanceIdentifier': 'nonexistent'})

    def test_modify_happy_path(self, store):
        create = _load_handler('CreateDBInstance')
        create(store, {
            'DBInstanceIdentifier': 'test-db-1',
            'DBInstanceClass': 'db.t3.micro',
            'Engine': 'mysql',
        })
        modify = _load_handler('ModifyDBInstance')
        response = modify(store, {
            'DBInstanceIdentifier': 'test-db-1',
            'DBInstanceClass': 'db.t3.small',
        })
        assert response['DBInstanceIdentifier'] == 'test-db-1'

    def test_modify_nonexistent(self, store):
        modify = _load_handler('ModifyDBInstance')
        with pytest.raises(DBInstanceNotFoundFault):
            modify(store, {'DBInstanceIdentifier': 'nonexistent'})

    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBInstance')
        create(store, {
            'DBInstanceIdentifier': 'test-db-1',
            'DBInstanceClass': 'db.t3.micro',
            'Engine': 'mysql',
        })
        delete = _load_handler('DeleteDBInstance')
        response = delete(store, {
            'DBInstanceIdentifier': 'test-db-1',
            'SkipFinalSnapshot': True,
        })
        assert response['DBInstanceIdentifier'] == 'test-db-1'
        # Verify it's gone
        describe = _load_handler('DescribeDBInstances')
        with pytest.raises(DBInstanceNotFoundFault):
            describe(store, {'DBInstanceIdentifier': 'test-db-1'})

    def test_delete_nonexistent(self, store):
        delete = _load_handler('DeleteDBInstance')
        with pytest.raises(DBInstanceNotFoundFault):
            delete(store, {'DBInstanceIdentifier': 'nonexistent'})

    def test_reboot_happy_path(self, store):
        create = _load_handler('CreateDBInstance')
        create(store, {
            'DBInstanceIdentifier': 'test-db-1',
            'DBInstanceClass': 'db.t3.micro',
            'Engine': 'mysql',
        })
        reboot = _load_handler('RebootDBInstance')
        response = reboot(store, {'DBInstanceIdentifier': 'test-db-1'})
        assert response['DBInstanceIdentifier'] == 'test-db-1'


# ── DB Cluster Tests ───────────────────────────────────────────────────

class TestDBCluster:
    @pytest.fixture
    def store(self):
        return RDSStore()

    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBCluster')
        response = handler(store, {
            'DBClusterIdentifier': 'test-cluster-1',
            'Engine': 'aurora-mysql',
            'MasterUsername': 'admin',
            'MasterUserPassword': 'password123',
        })
        assert response['DBClusterIdentifier'] == 'test-cluster-1'
        assert response['Engine'] == 'aurora-mysql'
        assert response['Status'] == 'available'

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBCluster')
        req = {
            'DBClusterIdentifier': 'test-cluster-1',
            'Engine': 'aurora-mysql',
        }
        handler(store, req)
        with pytest.raises(DBClusterAlreadyExistsFault):
            handler(store, req)

    def test_describe_single(self, store):
        create = _load_handler('CreateDBCluster')
        create(store, {
            'DBClusterIdentifier': 'test-cluster-1',
            'Engine': 'aurora-mysql',
        })
        describe = _load_handler('DescribeDBClusters')
        response = describe(store, {'DBClusterIdentifier': 'test-cluster-1'})
        assert len(response['DBClusters']) == 1

    def test_describe_nonexistent(self, store):
        describe = _load_handler('DescribeDBClusters')
        with pytest.raises(DBClusterNotFoundFault):
            describe(store, {'DBClusterIdentifier': 'nonexistent'})

    def test_modify_happy_path(self, store):
        create = _load_handler('CreateDBCluster')
        create(store, {
            'DBClusterIdentifier': 'test-cluster-1',
            'Engine': 'aurora-mysql',
        })
        modify = _load_handler('ModifyDBCluster')
        response = modify(store, {
            'DBClusterIdentifier': 'test-cluster-1',
            'BackupRetentionPeriod': 7,
        })
        assert response['DBClusterIdentifier'] == 'test-cluster-1'

    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBCluster')
        create(store, {
            'DBClusterIdentifier': 'test-cluster-1',
            'Engine': 'aurora-mysql',
        })
        delete = _load_handler('DeleteDBCluster')
        response = delete(store, {
            'DBClusterIdentifier': 'test-cluster-1',
            'SkipFinalSnapshot': True,
        })
        assert response['DBClusterIdentifier'] == 'test-cluster-1'
        # Verify gone
        describe = _load_handler('DescribeDBClusters')
        with pytest.raises(DBClusterNotFoundFault):
            describe(store, {'DBClusterIdentifier': 'test-cluster-1'})


# ── DB Snapshot Tests ──────────────────────────────────────────────────

class TestDBSnapshot:
    @pytest.fixture
    def store(self):
        s = RDSStore()
        # Create an instance to snapshot
        s.create_db_instance(
            db_instance_identifier='test-db-1',
            db_instance_class='db.t3.micro',
            engine='mysql')
        return s

    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBSnapshot')
        response = handler(store, {
            'DBSnapshotIdentifier': 'test-snap-1',
            'DBInstanceIdentifier': 'test-db-1',
        })
        assert response['DBSnapshotIdentifier'] == 'test-snap-1'
        assert response['Status'] == 'available'

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBSnapshot')
        req = {
            'DBSnapshotIdentifier': 'test-snap-1',
            'DBInstanceIdentifier': 'test-db-1',
        }
        handler(store, req)
        with pytest.raises(DBSnapshotAlreadyExistsFault):
            handler(store, req)

    def test_describe(self, store):
        create = _load_handler('CreateDBSnapshot')
        create(store, {
            'DBSnapshotIdentifier': 'test-snap-1',
            'DBInstanceIdentifier': 'test-db-1',
        })
        describe = _load_handler('DescribeDBSnapshots')
        response = describe(store, {})
        assert len(response['DBSnapshots']) >= 1

    def test_describe_nonexistent(self, store):
        describe = _load_handler('DescribeDBSnapshots')
        with pytest.raises(DBSnapshotNotFoundFault):
            describe(store, {'DBSnapshotIdentifier': 'nonexistent'})

    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBSnapshot')
        create(store, {
            'DBSnapshotIdentifier': 'test-snap-1',
            'DBInstanceIdentifier': 'test-db-1',
        })
        delete = _load_handler('DeleteDBSnapshot')
        delete(store, {'DBSnapshotIdentifier': 'test-snap-1'})
        # Verify gone
        describe = _load_handler('DescribeDBSnapshots')
        with pytest.raises(DBSnapshotNotFoundFault):
            describe(store, {'DBSnapshotIdentifier': 'test-snap-1'})


# ── DB Parameter Group Tests ──────────────────────────────────────────

class TestDBParameterGroup:
    @pytest.fixture
    def store(self):
        return RDSStore()

    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBParameterGroup')
        response = handler(store, {
            'DBParameterGroupName': 'test-pg-1',
            'DBParameterGroupFamily': 'mysql8.0',
            'Description': 'Test parameter group',
        })
        assert response['DBParameterGroupName'] == 'test-pg-1'

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBParameterGroup')
        req = {
            'DBParameterGroupName': 'test-pg-1',
            'DBParameterGroupFamily': 'mysql8.0',
            'Description': 'Test',
        }
        handler(store, req)
        with pytest.raises(DBParameterGroupAlreadyExistsFault):
            handler(store, req)

    def test_describe(self, store):
        create = _load_handler('CreateDBParameterGroup')
        create(store, {
            'DBParameterGroupName': 'test-pg-1',
            'DBParameterGroupFamily': 'mysql8.0',
            'Description': 'Test',
        })
        describe = _load_handler('DescribeDBParameterGroups')
        response = describe(store, {})
        assert len(response['DBParameterGroups']) >= 1

    def test_describe_nonexistent(self, store):
        describe = _load_handler('DescribeDBParameterGroups')
        with pytest.raises(DBParameterGroupNotFoundFault):
            describe(store, {'DBParameterGroupName': 'nonexistent'})

    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBParameterGroup')
        create(store, {
            'DBParameterGroupName': 'test-pg-1',
            'DBParameterGroupFamily': 'mysql8.0',
            'Description': 'Test',
        })
        delete = _load_handler('DeleteDBParameterGroup')
        delete(store, {'DBParameterGroupName': 'test-pg-1'})
        describe = _load_handler('DescribeDBParameterGroups')
        with pytest.raises(DBParameterGroupNotFoundFault):
            describe(store, {'DBParameterGroupName': 'test-pg-1'})


# ── DB Subnet Group Tests ──────────────────────────────────────────────

class TestDBSubnetGroup:
    @pytest.fixture
    def store(self):
        return RDSStore()

    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        response = handler(store, {
            'DBSubnetGroupName': 'test-sg-1',
            'DBSubnetGroupDescription': 'Test subnet group',
            'SubnetIds': ['subnet-abc123', 'subnet-def456'],
        })
        assert response['DBSubnetGroupName'] == 'test-sg-1'

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        req = {
            'DBSubnetGroupName': 'test-sg-1',
            'DBSubnetGroupDescription': 'Test',
            'SubnetIds': ['subnet-abc123'],
        }
        handler(store, req)
        with pytest.raises(DBSubnetGroupAlreadyExistsFault):
            handler(store, req)

    def test_describe(self, store):
        create = _load_handler('CreateDBSubnetGroup')
        create(store, {
            'DBSubnetGroupName': 'test-sg-1',
            'DBSubnetGroupDescription': 'Test',
            'SubnetIds': ['subnet-abc123'],
        })
        describe = _load_handler('DescribeDBSubnetGroups')
        response = describe(store, {})
        assert len(response['DBSubnetGroups']) >= 1

    def test_describe_nonexistent(self, store):
        describe = _load_handler('DescribeDBSubnetGroups')
        with pytest.raises(DBSubnetGroupNotFoundFault):
            describe(store, {'DBSubnetGroupName': 'nonexistent'})

    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBSubnetGroup')
        create(store, {
            'DBSubnetGroupName': 'test-sg-1',
            'DBSubnetGroupDescription': 'Test',
            'SubnetIds': ['subnet-abc123'],
        })
        delete = _load_handler('DeleteDBSubnetGroup')
        delete(store, {'DBSubnetGroupName': 'test-sg-1'})
        describe = _load_handler('DescribeDBSubnetGroups')
        with pytest.raises(DBSubnetGroupNotFoundFault):
            describe(store, {'DBSubnetGroupName': 'test-sg-1'})


# ── DB Cluster Parameter Group Tests ───────────────────────────────────

class TestDBClusterParameterGroup:
    @pytest.fixture
    def store(self):
        return RDSStore()

    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        response = handler(store, {
            'DBClusterParameterGroupName': 'test-cpg-1',
            'DBParameterGroupFamily': 'aurora-mysql8.0',
            'Description': 'Test cluster parameter group',
        })
        assert response['DBClusterParameterGroupName'] == 'test-cpg-1'

    def test_describe_nonexistent(self, store):
        describe = _load_handler('DescribeDBClusterParameterGroups')
        with pytest.raises(DBClusterParameterGroupNotFoundFault):
            describe(store, {'DBClusterParameterGroupName': 'nonexistent'})

    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBClusterParameterGroup')
        create(store, {
            'DBClusterParameterGroupName': 'test-cpg-1',
            'DBParameterGroupFamily': 'aurora-mysql8.0',
            'Description': 'Test',
        })
        delete = _load_handler('DeleteDBClusterParameterGroup')
        delete(store, {'DBClusterParameterGroupName': 'test-cpg-1'})


# ── Tag Tests ──────────────────────────────────────────────────────────

class TestTags:
    @pytest.fixture
    def store(self):
        s = RDSStore()
        s.create_db_instance(
            db_instance_identifier='test-db-1',
            db_instance_class='db.t3.micro',
            engine='mysql')
        return s

    def test_add_tags(self, store):
        handler = _load_handler('AddTagsToResource')
        handler(store, {
            'ResourceName': 'test-db-1',
            'Tags': [{'Key': 'env', 'Value': 'test'}],
        })
        list_handler = _load_handler('ListTagsForResource')
        response = list_handler(store, {'ResourceName': 'test-db-1'})
        assert len(response['TagList']) >= 1

    def test_remove_tags(self, store):
        add = _load_handler('AddTagsToResource')
        add(store, {
            'ResourceName': 'test-db-1',
            'Tags': [{'Key': 'env', 'Value': 'test'}],
        })
        remove = _load_handler('RemoveTagsFromResource')
        remove(store, {
            'ResourceName': 'test-db-1',
            'TagKeys': ['env'],
        })
        list_handler = _load_handler('ListTagsForResource')
        response = list_handler(store, {'ResourceName': 'test-db-1'})
        assert len(response['TagList']) == 0

    def test_list_nonexistent(self, store):
        list_handler = _load_handler('ListTagsForResource')
        with pytest.raises(ResourceNotFoundException):
            list_handler(store, {'ResourceName': 'nonexistent'})
