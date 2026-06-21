"""Integration tests for Neptune — real NeptuneStore with generated handlers."""
import importlib.util
import os
import time as _time
import types
import uuid as _uuid

import pytest

# ═══════════════════════════════════════════════════════════════
# Dynamic loader utilities (greenfield service pattern)
# ═══════════════════════════════════════════════════════════════

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'neptune')

# Load the models module first
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py')
)
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
NeptuneStore = models_mod.NeptuneStore
DBClusterNotFoundFault = models_mod.DBClusterNotFoundFault
DBClusterSnapshotNotFoundFault = models_mod.DBClusterSnapshotNotFoundFault
DBInstanceNotFoundFault = models_mod.DBInstanceNotFoundFault
DBParameterGroupNotFoundFault = models_mod.DBParameterGroupNotFoundFault
DBSubnetGroupNotFoundFault = models_mod.DBSubnetGroupNotFoundFault
DBClusterParameterGroupNotFoundFault = models_mod.DBClusterParameterGroupNotFoundFault
DBClusterAlreadyExistsFault = models_mod.DBClusterAlreadyExistsFault
DBClusterSnapshotAlreadyExistsFault = models_mod.DBClusterSnapshotAlreadyExistsFault
DBInstanceAlreadyExistsFault = models_mod.DBInstanceAlreadyExistsFault
DBParameterGroupAlreadyExistsFault = models_mod.DBParameterGroupAlreadyExistsFault
DBSubnetGroupAlreadyExistsFault = models_mod.DBSubnetGroupAlreadyExistsFault
DBClusterParameterGroupAlreadyExistsFault = models_mod.DBClusterParameterGroupAlreadyExistsFault
InvalidParameterValueException = models_mod.InvalidParameterValueException
InvalidDBClusterStateFault = models_mod.InvalidDBClusterStateFault
InvalidDBInstanceStateFault = models_mod.InvalidDBInstanceStateFault
DBSubnetGroupDoesNotCoverEnoughAZs = models_mod.DBSubnetGroupDoesNotCoverEnoughAZs


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file, injecting exceptions and stdlib."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    if not os.path.exists(path):
        pytest.skip(f"Handler file not found: {path}")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.DBClusterNotFoundFault = DBClusterNotFoundFault
    mod.DBClusterSnapshotNotFoundFault = DBClusterSnapshotNotFoundFault
    mod.DBInstanceNotFoundFault = DBInstanceNotFoundFault
    mod.DBParameterGroupNotFoundFault = DBParameterGroupNotFoundFault
    mod.DBSubnetGroupNotFoundFault = DBSubnetGroupNotFoundFault
    mod.DBClusterParameterGroupNotFoundFault = DBClusterParameterGroupNotFoundFault
    mod.DBClusterAlreadyExistsFault = DBClusterAlreadyExistsFault
    mod.DBClusterSnapshotAlreadyExistsFault = DBClusterSnapshotAlreadyExistsFault
    mod.DBInstanceAlreadyExistsFault = DBInstanceAlreadyExistsFault
    mod.DBParameterGroupAlreadyExistsFault = DBParameterGroupAlreadyExistsFault
    mod.DBSubnetGroupAlreadyExistsFault = DBSubnetGroupAlreadyExistsFault
    mod.DBClusterParameterGroupAlreadyExistsFault = DBClusterParameterGroupAlreadyExistsFault
    mod.InvalidParameterValueException = InvalidParameterValueException
    mod.InvalidDBClusterStateFault = InvalidDBClusterStateFault
    mod.InvalidDBInstanceStateFault = InvalidDBInstanceStateFault
    mod.DBSubnetGroupDoesNotCoverEnoughAZs = DBSubnetGroupDoesNotCoverEnoughAZs
    mod.time = _time
    mod.uuid = _uuid
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)

    # Find the handler function — exclude stdlib injects, lambdas, exceptions
    skip_names = {
        'time', 'uuid', '<lambda>',
        'DBClusterNotFoundFault', 'DBClusterSnapshotNotFoundFault',
        'DBInstanceNotFoundFault', 'DBParameterGroupNotFoundFault',
        'DBSubnetGroupNotFoundFault', 'DBClusterParameterGroupNotFoundFault',
        'DBClusterAlreadyExistsFault', 'DBClusterSnapshotAlreadyExistsFault',
        'DBInstanceAlreadyExistsFault', 'DBParameterGroupAlreadyExistsFault',
        'DBSubnetGroupAlreadyExistsFault', 'DBClusterParameterGroupAlreadyExistsFault',
        'InvalidParameterValueException', 'InvalidDBClusterStateFault',
        'InvalidDBInstanceStateFault', 'DBSubnetGroupDoesNotCoverEnoughAZs',
    }
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    if handler is None:
        raise RuntimeError(f"No handler function found in {op_name}.code.py")
    return handler


def _load_module(op_name, globals_inject=None):
    """Load a generated .code.py module (for multi-function files)."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.DBClusterNotFoundFault = DBClusterNotFoundFault
    mod.DBClusterSnapshotNotFoundFault = DBClusterSnapshotNotFoundFault
    mod.DBInstanceNotFoundFault = DBInstanceNotFoundFault
    mod.DBParameterGroupNotFoundFault = DBParameterGroupNotFoundFault
    mod.DBSubnetGroupNotFoundFault = DBSubnetGroupNotFoundFault
    mod.DBClusterParameterGroupNotFoundFault = DBClusterParameterGroupNotFoundFault
    mod.DBClusterAlreadyExistsFault = DBClusterAlreadyExistsFault
    mod.DBClusterSnapshotAlreadyExistsFault = DBClusterSnapshotAlreadyExistsFault
    mod.DBInstanceAlreadyExistsFault = DBInstanceAlreadyExistsFault
    mod.DBParameterGroupAlreadyExistsFault = DBParameterGroupAlreadyExistsFault
    mod.DBSubnetGroupAlreadyExistsFault = DBSubnetGroupAlreadyExistsFault
    mod.DBClusterParameterGroupAlreadyExistsFault = DBClusterParameterGroupAlreadyExistsFault
    mod.InvalidParameterValueException = InvalidParameterValueException
    mod.InvalidDBClusterStateFault = InvalidDBClusterStateFault
    mod.InvalidDBInstanceStateFault = InvalidDBInstanceStateFault
    mod.DBSubnetGroupDoesNotCoverEnoughAZs = DBSubnetGroupDoesNotCoverEnoughAZs
    mod.time = _time
    mod.uuid = _uuid
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    return mod


# ═══════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════

@pytest.fixture
def store():
    return NeptuneStore()


@pytest.fixture
def cluster(store):
    """Create a test cluster for instance/snapshot-dependent tests."""
    handler = _load_handler('CreateDBCluster')
    response = handler(store, {
        'DBClusterIdentifier': 'test-cluster',
        'Engine': 'neptune',
        'MasterUsername': 'admin',
        'MasterUserPassword': 'password123',
    })
    return response


@pytest.fixture
def instance(store, cluster):
    """Create a test instance."""
    handler = _load_handler('CreateDBInstance')
    response = handler(store, {
        'DBInstanceIdentifier': 'test-instance',
        'DBInstanceClass': 'db.r5.large',
        'Engine': 'neptune',
        'DBClusterIdentifier': 'test-cluster',
    })
    return response


# ═══════════════════════════════════════════════════════════════
# DBCluster Tests
# ═══════════════════════════════════════════════════════════════

class TestCreateDBCluster:
    def test_create_cluster_happy_path(self, store):
        handler = _load_handler('CreateDBCluster')
        response = handler(store, {
            'DBClusterIdentifier': 'my-cluster',
            'Engine': 'neptune',
            'MasterUsername': 'admin',
            'MasterUserPassword': 'password123',
        })
        assert response is not None
        assert 'DBCluster' in response
        assert response['DBCluster']['DBClusterIdentifier'] == 'my-cluster'
        assert response['DBCluster']['Engine'] == 'neptune'
        assert response['DBCluster']['Status'] == 'available'

    def test_create_cluster_missing_id(self, store):
        handler = _load_handler('CreateDBCluster')
        with pytest.raises(InvalidParameterValueException):
            handler(store, {'Engine': 'neptune'})

    def test_create_cluster_duplicate(self, store):
        handler = _load_handler('CreateDBCluster')
        handler(store, {'DBClusterIdentifier': 'dup-cluster', 'Engine': 'neptune'})
        with pytest.raises(DBClusterAlreadyExistsFault):
            handler(store, {'DBClusterIdentifier': 'dup-cluster', 'Engine': 'neptune'})


class TestDeleteDBCluster:
    def test_delete_cluster_happy_path(self, store, cluster):
        handler = _load_handler('DeleteDBCluster')
        response = handler(store, {'DBClusterIdentifier': 'test-cluster'})
        assert 'DBCluster' in response
        # Verify gone
        with pytest.raises(DBClusterNotFoundFault):
            store.get_cluster('test-cluster')

    def test_delete_nonexistent_cluster(self, store):
        handler = _load_handler('DeleteDBCluster')
        with pytest.raises(DBClusterNotFoundFault):
            handler(store, {'DBClusterIdentifier': 'no-such-cluster'})


class TestModifyDBCluster:
    def test_modify_cluster_happy_path(self, store, cluster):
        handler = _load_handler('ModifyDBCluster')
        response = handler(store, {
            'DBClusterIdentifier': 'test-cluster',
            'BackupRetentionPeriod': 7,
            'DeletionProtection': True,
        })
        assert 'DBCluster' in response
        c = store.get_cluster('test-cluster')
        assert c.backup_retention_period == 7
        assert c.deletion_protection is True

    def test_modify_nonexistent_cluster(self, store):
        handler = _load_handler('ModifyDBCluster')
        with pytest.raises(DBClusterNotFoundFault):
            handler(store, {'DBClusterIdentifier': 'no-such-cluster'})


class TestDescribeDBClusters:
    def test_describe_all(self, store, cluster):
        handler = _load_handler('DescribeDBClusters')
        response = handler(store, {})
        assert 'DBClusters' in response
        assert len(response['DBClusters']) >= 1

    def test_describe_specific(self, store, cluster):
        handler = _load_handler('DescribeDBClusters')
        response = handler(store, {'DBClusterIdentifier': 'test-cluster'})
        assert len(response['DBClusters']) == 1
        assert response['DBClusters'][0]['DBClusterIdentifier'] == 'test-cluster'


# ═══════════════════════════════════════════════════════════════
# DBInstance Tests
# ═══════════════════════════════════════════════════════════════

class TestCreateDBInstance:
    def test_create_instance_happy_path(self, store, cluster):
        handler = _load_handler('CreateDBInstance')
        response = handler(store, {
            'DBInstanceIdentifier': 'my-instance',
            'DBInstanceClass': 'db.r5.large',
            'Engine': 'neptune',
            'DBClusterIdentifier': 'test-cluster',
        })
        assert response is not None
        assert 'DBInstance' in response
        assert response['DBInstance']['DBInstanceIdentifier'] == 'my-instance'

    def test_create_instance_missing_id(self, store):
        handler = _load_handler('CreateDBInstance')
        with pytest.raises(InvalidParameterValueException):
            handler(store, {'DBInstanceClass': 'db.r5.large', 'Engine': 'neptune'})

    def test_create_instance_duplicate(self, store, instance):
        handler = _load_handler('CreateDBInstance')
        with pytest.raises(DBInstanceAlreadyExistsFault):
            handler(store, {
                'DBInstanceIdentifier': 'test-instance',
                'DBInstanceClass': 'db.r5.large',
                'Engine': 'neptune',
                'DBClusterIdentifier': 'test-cluster',
            })


class TestDeleteDBInstance:
    def test_delete_instance_happy_path(self, store, instance):
        handler = _load_handler('DeleteDBInstance')
        response = handler(store, {'DBInstanceIdentifier': 'test-instance'})
        assert 'DBInstance' in response
        with pytest.raises(DBInstanceNotFoundFault):
            store.get_instance('test-instance')

    def test_delete_nonexistent_instance(self, store):
        handler = _load_handler('DeleteDBInstance')
        with pytest.raises(DBInstanceNotFoundFault):
            handler(store, {'DBInstanceIdentifier': 'no-such'})


class TestDescribeDBInstances:
    def test_describe_all(self, store, instance):
        handler = _load_handler('DescribeDBInstances')
        response = handler(store, {})
        assert 'DBInstances' in response
        assert len(response['DBInstances']) >= 1

    def test_describe_specific(self, store, instance):
        handler = _load_handler('DescribeDBInstances')
        response = handler(store, {'DBInstanceIdentifier': 'test-instance'})
        assert len(response['DBInstances']) == 1


# ═══════════════════════════════════════════════════════════════
# DBClusterParameterGroup Tests
# ═══════════════════════════════════════════════════════════════

class TestCreateDBClusterParameterGroup:
    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        response = handler(store, {
            'DBClusterParameterGroupName': 'my-cpg',
            'DBParameterGroupFamily': 'neptune1.3',
            'Description': 'Test cluster param group',
        })
        assert response is not None
        assert 'DBClusterParameterGroup' in response

    def test_create_missing_name(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        with pytest.raises(InvalidParameterValueException):
            handler(store, {'DBParameterGroupFamily': 'neptune1.3', 'Description': 'x'})

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBClusterParameterGroup')
        handler(store, {
            'DBClusterParameterGroupName': 'dup-cpg',
            'DBParameterGroupFamily': 'neptune1.3',
            'Description': 'Test',
        })
        with pytest.raises(DBClusterParameterGroupAlreadyExistsFault):
            handler(store, {
                'DBClusterParameterGroupName': 'dup-cpg',
                'DBParameterGroupFamily': 'neptune1.3',
                'Description': 'Test',
            })


class TestDeleteDBClusterParameterGroup:
    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBClusterParameterGroup')
        create(store, {
            'DBClusterParameterGroupName': 'del-me',
            'DBParameterGroupFamily': 'neptune1.3',
            'Description': 'To delete',
        })
        handler = _load_handler('DeleteDBClusterParameterGroup')
        handler(store, {'DBClusterParameterGroupName': 'del-me'})
        with pytest.raises(DBClusterParameterGroupNotFoundFault):
            store.get_cluster_param_group('del-me')

    def test_delete_nonexistent(self, store):
        handler = _load_handler('DeleteDBClusterParameterGroup')
        with pytest.raises(DBClusterParameterGroupNotFoundFault):
            handler(store, {'DBClusterParameterGroupName': 'no-such'})


# ═══════════════════════════════════════════════════════════════
# DBParameterGroup Tests
# ═══════════════════════════════════════════════════════════════

class TestCreateDBParameterGroup:
    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBParameterGroup')
        response = handler(store, {
            'DBParameterGroupName': 'my-pg',
            'DBParameterGroupFamily': 'neptune1.3',
            'Description': 'Test param group',
        })
        assert response is not None

    def test_create_missing_family(self, store):
        handler = _load_handler('CreateDBParameterGroup')
        with pytest.raises(InvalidParameterValueException):
            handler(store, {'DBParameterGroupName': 'test', 'Description': 'x'})

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBParameterGroup')
        handler(store, {
            'DBParameterGroupName': 'dup-pg',
            'DBParameterGroupFamily': 'neptune1.3',
            'Description': 'Test',
        })
        with pytest.raises(DBParameterGroupAlreadyExistsFault):
            handler(store, {
                'DBParameterGroupName': 'dup-pg',
                'DBParameterGroupFamily': 'neptune1.3',
                'Description': 'Test',
            })


class TestDeleteDBParameterGroup:
    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBParameterGroup')
        create(store, {
            'DBParameterGroupName': 'del-pg',
            'DBParameterGroupFamily': 'neptune1.3',
            'Description': 'Delete me',
        })
        handler = _load_handler('DeleteDBParameterGroup')
        handler(store, {'DBParameterGroupName': 'del-pg'})
        with pytest.raises(DBParameterGroupNotFoundFault):
            store.get_param_group('del-pg')


# ═══════════════════════════════════════════════════════════════
# DBClusterSnapshot Tests
# ═══════════════════════════════════════════════════════════════

class TestCreateDBClusterSnapshot:
    def test_create_happy_path(self, store, cluster):
        handler = _load_handler('CreateDBClusterSnapshot')
        response = handler(store, {
            'DBClusterSnapshotIdentifier': 'my-snap',
            'DBClusterIdentifier': 'test-cluster',
        })
        assert response is not None
        assert 'DBClusterSnapshot' in response
        assert response['DBClusterSnapshot']['DBClusterSnapshotIdentifier'] == 'my-snap'

    def test_create_missing_cluster(self, store):
        handler = _load_handler('CreateDBClusterSnapshot')
        with pytest.raises(DBClusterNotFoundFault):
            handler(store, {
                'DBClusterSnapshotIdentifier': 'snap',
                'DBClusterIdentifier': 'no-cluster',
            })

    def test_create_duplicate(self, store, cluster):
        handler = _load_handler('CreateDBClusterSnapshot')
        handler(store, {
            'DBClusterSnapshotIdentifier': 'dup-snap',
            'DBClusterIdentifier': 'test-cluster',
        })
        with pytest.raises(DBClusterSnapshotAlreadyExistsFault):
            handler(store, {
                'DBClusterSnapshotIdentifier': 'dup-snap',
                'DBClusterIdentifier': 'test-cluster',
            })


class TestDeleteDBClusterSnapshot:
    def test_delete_happy_path(self, store, cluster):
        create = _load_handler('CreateDBClusterSnapshot')
        create(store, {
            'DBClusterSnapshotIdentifier': 'del-snap',
            'DBClusterIdentifier': 'test-cluster',
        })
        handler = _load_handler('DeleteDBClusterSnapshot')
        response = handler(store, {'DBClusterSnapshotIdentifier': 'del-snap'})
        assert 'DBClusterSnapshot' in response

    def test_delete_nonexistent(self, store):
        handler = _load_handler('DeleteDBClusterSnapshot')
        with pytest.raises(DBClusterSnapshotNotFoundFault):
            handler(store, {'DBClusterSnapshotIdentifier': 'no-such-snap'})


class TestDescribeDBClusterSnapshots:
    def test_describe_by_cluster(self, store, cluster):
        create = _load_handler('CreateDBClusterSnapshot')
        create(store, {
            'DBClusterSnapshotIdentifier': 'snap1',
            'DBClusterIdentifier': 'test-cluster',
        })
        handler = _load_handler('DescribeDBClusterSnapshots')
        response = handler(store, {'DBClusterIdentifier': 'test-cluster'})
        assert len(response['DBClusterSnapshots']) >= 1


# ═══════════════════════════════════════════════════════════════
# DBSubnetGroup Tests
# ═══════════════════════════════════════════════════════════════

class TestCreateDBSubnetGroup:
    def test_create_happy_path(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        response = handler(store, {
            'DBSubnetGroupName': 'my-subnet',
            'DBSubnetGroupDescription': 'Test subnet group',
            'SubnetIds': ['subnet-abc123', 'subnet-def456'],
        })
        assert response is not None
        assert 'DBSubnetGroup' in response

    def test_create_insufficient_subnets(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        with pytest.raises(DBSubnetGroupDoesNotCoverEnoughAZs):
            handler(store, {
                'DBSubnetGroupName': 'bad-subnet',
                'DBSubnetGroupDescription': 'Only one subnet',
                'SubnetIds': ['subnet-abc123'],
            })

    def test_create_duplicate(self, store):
        handler = _load_handler('CreateDBSubnetGroup')
        handler(store, {
            'DBSubnetGroupName': 'dup-sg',
            'DBSubnetGroupDescription': 'Test',
            'SubnetIds': ['subnet-a', 'subnet-b'],
        })
        with pytest.raises(DBSubnetGroupAlreadyExistsFault):
            handler(store, {
                'DBSubnetGroupName': 'dup-sg',
                'DBSubnetGroupDescription': 'Test',
                'SubnetIds': ['subnet-a', 'subnet-b'],
            })


class TestDeleteDBSubnetGroup:
    def test_delete_happy_path(self, store):
        create = _load_handler('CreateDBSubnetGroup')
        create(store, {
            'DBSubnetGroupName': 'del-sg',
            'DBSubnetGroupDescription': 'Delete me',
            'SubnetIds': ['subnet-a', 'subnet-b'],
        })
        handler = _load_handler('DeleteDBSubnetGroup')
        handler(store, {'DBSubnetGroupName': 'del-sg'})
        with pytest.raises(DBSubnetGroupNotFoundFault):
            store.get_subnet_group('del-sg')


# ═══════════════════════════════════════════════════════════════
# Tag Tests
# ═══════════════════════════════════════════════════════════════

class TestTagOperations:
    def test_add_and_list_tags(self, store, cluster):
        # Load AddTagsToResource as module to get helper
        tag_mod = _load_module('AddTagsToResource')
        _finder = tag_mod._find_resource_by_name

        rmt_mod = _load_module('RemoveTagsFromResource', {'_find_resource_by_name': _finder})
        lst_mod = _load_module('ListTagsForResource', {'_find_resource_by_name': _finder})

        # Add tags
        tag_mod.add_tags_to_resource(store, {
            'ResourceName': 'test-cluster',
            'Tags': [{'Key': 'Env', 'Value': 'test'}, {'Key': 'Owner', 'Value': 'team'}],
        })

        # List tags
        response = lst_mod.list_tags_for_resource(store, {'ResourceName': 'test-cluster'})
        tag_list = response['TagList']
        assert len(tag_list) == 2
        keys = {t['Key'] for t in tag_list}
        assert 'Env' in keys
        assert 'Owner' in keys

        # Remove one tag
        rmt_mod.remove_tags_from_resource(store, {
            'ResourceName': 'test-cluster',
            'TagKeys': ['Env'],
        })
        response2 = lst_mod.list_tags_for_resource(store, {'ResourceName': 'test-cluster'})
        assert len(response2['TagList']) == 1
        assert response2['TagList'][0]['Key'] == 'Owner'


# ═══════════════════════════════════════════════════════════════
# DescribeDBEngineVersions Tests
# ═══════════════════════════════════════════════════════════════

class TestDescribeDBEngineVersions:
    def test_describe_all(self, store):
        handler = _load_handler('DescribeDBEngineVersions')
        response = handler(store, {})
        assert 'DBEngineVersions' in response
        assert len(response['DBEngineVersions']) >= 1

    def test_describe_specific(self, store):
        handler = _load_handler('DescribeDBEngineVersions')
        response = handler(store, {'EngineVersion': '1.4.0.0'})
        assert len(response['DBEngineVersions']) == 1
        assert response['DBEngineVersions'][0]['EngineVersion'] == '1.4.0.0'
