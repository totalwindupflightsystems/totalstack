"""Integration tests for ElastiCache — real store objects.

Tests against the generated handlers and store model.
Greenfield service — no LocalStack provider exists. Uses importlib dynamic loading.
"""
import pytest
import os
import sys
import importlib.util
import types

# Paths
ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'elasticache')

# --- Load models.code.py dynamically ---
models_spec = importlib.util.spec_from_file_location(
    'models',
    os.path.join(SERVICE_DIR, 'models.code.py')
)
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
ElastiCacheStore = models_mod.ElastiCacheStore
ElastiCacheException = models_mod.ElastiCacheException
InvalidParameterValueException = models_mod.InvalidParameterValueException
CacheClusterNotFoundFault = models_mod.CacheClusterNotFoundFault
CacheClusterAlreadyExistsFault = models_mod.CacheClusterAlreadyExistsFault
ReplicationGroupNotFoundFault = models_mod.ReplicationGroupNotFoundFault
ReplicationGroupAlreadyExistsFault = models_mod.ReplicationGroupAlreadyExistsFault
CacheParameterGroupNotFoundFault = models_mod.CacheParameterGroupNotFoundFault
CacheParameterGroupAlreadyExistsFault = models_mod.CacheParameterGroupAlreadyExistsFault
CacheSubnetGroupNotFoundFault = models_mod.CacheSubnetGroupNotFoundFault
CacheSubnetGroupAlreadyExistsFault = models_mod.CacheSubnetGroupAlreadyExistsFault
SnapshotNotFoundFault = models_mod.SnapshotNotFoundFault
SnapshotAlreadyExistsFault = models_mod.SnapshotAlreadyExistsFault
UserNotFoundFault = models_mod.UserNotFoundFault
UserAlreadyExistsFault = models_mod.UserAlreadyExistsFault
UserGroupNotFoundFault = models_mod.UserGroupNotFoundFault
UserGroupAlreadyExistsFault = models_mod.UserGroupAlreadyExistsFault

# --- Helper: load a single-handler .code.py file ---
def _load_handler(op_name):
    """Load a generated .code.py handler — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes (generated code references them without imports)
    mod.InvalidParameterValueException = InvalidParameterValueException
    mod.CacheClusterNotFoundFault = CacheClusterNotFoundFault
    mod.CacheClusterAlreadyExistsFault = CacheClusterAlreadyExistsFault
    mod.ReplicationGroupNotFoundFault = ReplicationGroupNotFoundFault
    mod.ReplicationGroupAlreadyExistsFault = ReplicationGroupAlreadyExistsFault
    mod.CacheParameterGroupNotFoundFault = CacheParameterGroupNotFoundFault
    mod.CacheParameterGroupAlreadyExistsFault = CacheParameterGroupAlreadyExistsFault
    mod.CacheSubnetGroupNotFoundFault = CacheSubnetGroupNotFoundFault
    mod.CacheSubnetGroupAlreadyExistsFault = CacheSubnetGroupAlreadyExistsFault
    mod.SnapshotNotFoundFault = SnapshotNotFoundFault
    mod.SnapshotAlreadyExistsFault = SnapshotAlreadyExistsFault
    mod.UserNotFoundFault = UserNotFoundFault
    mod.UserAlreadyExistsFault = UserAlreadyExistsFault
    mod.UserGroupNotFoundFault = UserGroupNotFoundFault
    mod.UserGroupAlreadyExistsFault = UserGroupAlreadyExistsFault
    mod.InvalidCacheClusterStateFault = models_mod.InvalidCacheClusterStateFault
    mod.InvalidReplicationGroupStateFault = models_mod.InvalidReplicationGroupStateFault
    mod.InvalidCacheParameterGroupStateFault = models_mod.InvalidCacheParameterGroupStateFault
    mod.InvalidUserStateFault = models_mod.InvalidUserStateFault
    mod.InvalidUserGroupStateFault = models_mod.InvalidUserGroupStateFault
    mod.InvalidSnapshotStateFault = models_mod.InvalidSnapshotStateFault
    mod.TagQuotaPerResourceExceeded = models_mod.TagQuotaPerResourceExceeded
    mod.CacheSubnetQuotaExceededFault = models_mod.CacheSubnetQuotaExceededFault
    mod.CacheSubnetGroupQuotaExceededFault = models_mod.CacheSubnetGroupQuotaExceededFault
    mod.CacheParameterGroupQuotaExceededFault = models_mod.CacheParameterGroupQuotaExceededFault
    mod.CacheSubnetGroupInUse = models_mod.CacheSubnetGroupInUse
    mod.SnapshotFeatureNotSupportedFault = models_mod.SnapshotFeatureNotSupportedFault
    mod.SnapshotQuotaExceededFault = models_mod.SnapshotQuotaExceededFault
    mod.InvalidParameterCombinationException = models_mod.InvalidParameterCombinationException
    mod.UserQuotaExceededFault = models_mod.UserQuotaExceededFault
    mod.DuplicateUserNameFault = models_mod.DuplicateUserNameFault
    mod.DefaultUserRequired = models_mod.DefaultUserRequired
    mod.ServiceLinkedRoleNotFoundFault = models_mod.ServiceLinkedRoleNotFoundFault
    mod.InvalidSubnet = models_mod.InvalidSubnet
    mod.SubnetInUse = models_mod.SubnetInUse
    mod.SubnetNotAllowedFault = models_mod.SubnetNotAllowedFault
    mod.NodeQuotaForClusterExceeded = models_mod.NodeQuotaForClusterExceeded
    mod.InsufficientCacheClusterCapacityFault = models_mod.InsufficientCacheClusterCapacityFault
    mod.InvalidCacheSecurityGroupStateFault = models_mod.CacheSecurityGroupNotFoundFault  # reuse
    mod.ElastiCacheException = ElastiCacheException
    spec.loader.exec_module(mod)
    # Find the handler function
    for v in mod.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_'):
            return v
    raise RuntimeError(f"No handler function found in {op_name}")


# ==================== Cache Cluster Tests ====================

class TestCacheCluster:
    """CRUD tests for Cache Clusters."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_create_happy_path(self, store):
        """Create a cache cluster with valid params."""
        create_handler = _load_handler('CreateCacheCluster')
        response = create_handler(store, {
            'CacheClusterId': 'test-cluster-1',
            'Engine': 'redis',
            'CacheNodeType': 'cache.t2.micro',
            'NumCacheNodes': 1,
        })
        assert response['CacheClusterId'] == 'test-cluster-1'
        assert response['Status'] == 'available'
        assert 'test-cluster-1' in store.cache_clusters

    def test_create_missing_required(self, store):
        """Create without CacheClusterId raises InvalidParameterValueException."""
        create_handler = _load_handler('CreateCacheCluster')
        with pytest.raises(InvalidParameterValueException):
            create_handler(store, {})

    def test_create_duplicate(self, store):
        """Creating duplicate CacheClusterId raises CacheClusterAlreadyExistsFault."""
        create_handler = _load_handler('CreateCacheCluster')
        create_handler(store, {'CacheClusterId': 'test-cluster-1'})
        with pytest.raises(CacheClusterAlreadyExistsFault):
            create_handler(store, {'CacheClusterId': 'test-cluster-1'})

    def test_describe_specific(self, store):
        """Describe a specific cache cluster."""
        create_handler = _load_handler('CreateCacheCluster')
        desc_handler = _load_handler('DescribeCacheClusters')
        create_handler(store, {'CacheClusterId': 'test-cluster-1'})
        response = desc_handler(store, {'CacheClusterId': 'test-cluster-1'})
        assert 'CacheClusters' in response
        assert len(response['CacheClusters']) == 1
        assert response['CacheClusters'][0]['CacheClusterId'] == 'test-cluster-1'

    def test_describe_nonexistent(self, store):
        """Describe nonexistent cache cluster raises CacheClusterNotFoundFault."""
        desc_handler = _load_handler('DescribeCacheClusters')
        with pytest.raises(CacheClusterNotFoundFault):
            desc_handler(store, {'CacheClusterId': 'nonexistent'})

    def test_describe_all(self, store):
        """Describe all cache clusters when no ID specified."""
        create_handler = _load_handler('CreateCacheCluster')
        desc_handler = _load_handler('DescribeCacheClusters')
        create_handler(store, {'CacheClusterId': 'c1'})
        create_handler(store, {'CacheClusterId': 'c2'})
        response = desc_handler(store, {})
        assert len(response['CacheClusters']) == 2

    def test_delete_happy_path(self, store):
        """Delete an existing cache cluster."""
        create_handler = _load_handler('CreateCacheCluster')
        delete_handler = _load_handler('DeleteCacheCluster')
        create_handler(store, {'CacheClusterId': 'test-cluster-1'})
        delete_handler(store, {'CacheClusterId': 'test-cluster-1'})
        assert 'test-cluster-1' not in store.cache_clusters

    def test_delete_nonexistent(self, store):
        """Delete nonexistent cache cluster raises CacheClusterNotFoundFault."""
        delete_handler = _load_handler('DeleteCacheCluster')
        with pytest.raises(CacheClusterNotFoundFault):
            delete_handler(store, {'CacheClusterId': 'nonexistent'})

    def test_modify_happy_path(self, store):
        """Modify a cache cluster."""
        create_handler = _load_handler('CreateCacheCluster')
        modify_handler = _load_handler('ModifyCacheCluster')
        create_handler(store, {'CacheClusterId': 'test-cluster-1'})
        response = modify_handler(store, {
            'CacheClusterId': 'test-cluster-1',
            'CacheNodeType': 'cache.m5.large',
            'NumCacheNodes': 3,
        })
        assert response['CacheNodeType'] == 'cache.m5.large'
        assert response['NumCacheNodes'] == 3

    def test_reboot_happy_path(self, store):
        """Reboot cache cluster nodes."""
        create_handler = _load_handler('CreateCacheCluster')
        reboot_handler = _load_handler('RebootCacheCluster')
        create_handler(store, {'CacheClusterId': 'test-cluster-1'})
        response = reboot_handler(store, {
            'CacheClusterId': 'test-cluster-1',
            'CacheNodeIdsToReboot': ['0001'],
        })
        assert response['Status'] == 'rebooting cache cluster nodes'


# ==================== Replication Group Tests ====================

class TestReplicationGroup:
    """CRUD tests for Replication Groups."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_create_happy_path(self, store):
        """Create a replication group."""
        create_handler = _load_handler('CreateReplicationGroup')
        response = create_handler(store, {
            'ReplicationGroupId': 'test-rg-1',
            'ReplicationGroupDescription': 'Test replication group',
        })
        assert response['ReplicationGroupId'] == 'test-rg-1'
        assert 'test-rg-1' in store.replication_groups

    def test_create_duplicate(self, store):
        """Creating duplicate replication group raises error."""
        create_handler = _load_handler('CreateReplicationGroup')
        create_handler(store, {
            'ReplicationGroupId': 'test-rg-1',
            'ReplicationGroupDescription': 'Test',
        })
        with pytest.raises(ReplicationGroupAlreadyExistsFault):
            create_handler(store, {
                'ReplicationGroupId': 'test-rg-1',
                'ReplicationGroupDescription': 'Test',
            })

    def test_describe_specific(self, store):
        """Describe a specific replication group."""
        create_handler = _load_handler('CreateReplicationGroup')
        desc_handler = _load_handler('DescribeReplicationGroups')
        create_handler(store, {
            'ReplicationGroupId': 'test-rg-1',
            'ReplicationGroupDescription': 'Test',
        })
        response = desc_handler(store, {'ReplicationGroupId': 'test-rg-1'})
        assert len(response['ReplicationGroups']) == 1

    def test_delete_happy_path(self, store):
        """Delete a replication group."""
        create_handler = _load_handler('CreateReplicationGroup')
        delete_handler = _load_handler('DeleteReplicationGroup')
        create_handler(store, {
            'ReplicationGroupId': 'test-rg-1',
            'ReplicationGroupDescription': 'Test',
        })
        delete_handler(store, {'ReplicationGroupId': 'test-rg-1'})
        assert 'test-rg-1' not in store.replication_groups

    def test_modify_happy_path(self, store):
        """Modify a replication group."""
        create_handler = _load_handler('CreateReplicationGroup')
        modify_handler = _load_handler('ModifyReplicationGroup')
        create_handler(store, {
            'ReplicationGroupId': 'test-rg-1',
            'ReplicationGroupDescription': 'Test',
        })
        response = modify_handler(store, {
            'ReplicationGroupId': 'test-rg-1',
            'ReplicationGroupDescription': 'Updated description',
        })
        assert response['ReplicationGroupDescription'] == 'Updated description'


# ==================== Parameter Group Tests ====================

class TestParameterGroup:
    """CRUD tests for Cache Parameter Groups."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_create_happy_path(self, store):
        create_handler = _load_handler('CreateCacheParameterGroup')
        response = create_handler(store, {
            'CacheParameterGroupName': 'test-pg',
            'CacheParameterGroupFamily': 'redis7',
            'Description': 'Test PG',
        })
        assert response['CacheParameterGroupName'] == 'test-pg'
        assert 'test-pg' in store.parameter_groups

    def test_create_duplicate(self, store):
        create_handler = _load_handler('CreateCacheParameterGroup')
        create_handler(store, {
            'CacheParameterGroupName': 'test-pg',
            'CacheParameterGroupFamily': 'redis7',
            'Description': 'Test',
        })
        with pytest.raises(CacheParameterGroupAlreadyExistsFault):
            create_handler(store, {
                'CacheParameterGroupName': 'test-pg',
                'CacheParameterGroupFamily': 'redis7',
                'Description': 'Test',
            })

    def test_delete_happy_path(self, store):
        create_handler = _load_handler('CreateCacheParameterGroup')
        delete_handler = _load_handler('DeleteCacheParameterGroup')
        create_handler(store, {
            'CacheParameterGroupName': 'test-pg',
            'CacheParameterGroupFamily': 'redis7',
            'Description': 'Test',
        })
        delete_handler(store, {'CacheParameterGroupName': 'test-pg'})
        assert 'test-pg' not in store.parameter_groups


# ==================== Subnet Group Tests ====================

class TestSubnetGroup:
    """CRUD tests for Cache Subnet Groups."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_create_happy_path(self, store):
        create_handler = _load_handler('CreateCacheSubnetGroup')
        response = create_handler(store, {
            'CacheSubnetGroupName': 'test-sg',
            'CacheSubnetGroupDescription': 'Test SG',
            'SubnetIds': ['subnet-abc123'],
        })
        assert response['CacheSubnetGroupName'] == 'test-sg'
        assert 'test-sg' in store.subnet_groups

    def test_create_duplicate(self, store):
        create_handler = _load_handler('CreateCacheSubnetGroup')
        create_handler(store, {
            'CacheSubnetGroupName': 'test-sg',
            'CacheSubnetGroupDescription': 'Test',
            'SubnetIds': ['subnet-abc123'],
        })
        with pytest.raises(CacheSubnetGroupAlreadyExistsFault):
            create_handler(store, {
                'CacheSubnetGroupName': 'test-sg',
                'CacheSubnetGroupDescription': 'Test',
                'SubnetIds': ['subnet-abc123'],
            })


# ==================== Snapshot Tests ====================

class TestSnapshot:
    """CRUD tests for Snapshots."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_create_happy_path(self, store):
        create_handler = _load_handler('CreateSnapshot')
        response = create_handler(store, {'SnapshotName': 'test-snap'})
        assert response['SnapshotName'] == 'test-snap'

    def test_create_duplicate(self, store):
        create_handler = _load_handler('CreateSnapshot')
        create_handler(store, {'SnapshotName': 'test-snap'})
        with pytest.raises(SnapshotAlreadyExistsFault):
            create_handler(store, {'SnapshotName': 'test-snap'})

    def test_copy_happy_path(self, store):
        create_handler = _load_handler('CreateSnapshot')
        copy_handler = _load_handler('CopySnapshot')
        create_handler(store, {'SnapshotName': 'snap-src'})
        response = copy_handler(store, {
            'SourceSnapshotName': 'snap-src',
            'TargetSnapshotName': 'snap-dst',
        })
        assert 'Snapshot' in response
        assert response['Snapshot']['SnapshotName'] == 'snap-dst'


# ==================== Tags Tests ====================

class TestTags:
    """Tests for tag operations."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_add_tags(self, store):
        add_handler = _load_handler('AddTagsToResource')
        list_handler = _load_handler('ListTagsForResource')
        add_handler(store, {
            'ResourceName': 'arn:aws:elasticache:us-east-1:123456789012:cluster:test',
            'Tags': [{'Key': 'env', 'Value': 'test'}, {'Key': 'team', 'Value': 'backend'}],
        })
        response = list_handler(store, {
            'ResourceName': 'arn:aws:elasticache:us-east-1:123456789012:cluster:test',
        })
        assert len(response['TagList']) == 2

    def test_remove_tags(self, store):
        add_handler = _load_handler('AddTagsToResource')
        remove_handler = _load_handler('RemoveTagsFromResource')
        list_handler = _load_handler('ListTagsForResource')
        add_handler(store, {
            'ResourceName': 'arn:test',
            'Tags': [{'Key': 'env', 'Value': 'test'}, {'Key': 'team', 'Value': 'backend'}],
        })
        remove_handler(store, {
            'ResourceName': 'arn:test',
            'TagKeys': ['team'],
        })
        response = list_handler(store, {'ResourceName': 'arn:test'})
        assert len(response['TagList']) == 1
        assert response['TagList'][0]['Key'] == 'env'


# ==================== User Tests ====================

class TestUser:
    """CRUD tests for Users."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_create_happy_path(self, store):
        create_handler = _load_handler('CreateUser')
        response = create_handler(store, {
            'UserId': 'user-1',
            'UserName': 'testuser',
            'Engine': 'redis',
            'AccessString': 'on ~* +@all',
        })
        assert response['UserId'] == 'user-1'
        assert 'user-1' in store.users

    def test_create_duplicate(self, store):
        create_handler = _load_handler('CreateUser')
        create_handler(store, {
            'UserId': 'user-1', 'UserName': 'testuser',
            'Engine': 'redis', 'AccessString': 'on ~* +@all',
        })
        with pytest.raises(UserAlreadyExistsFault):
            create_handler(store, {
                'UserId': 'user-1', 'UserName': 'testuser2',
                'Engine': 'redis', 'AccessString': 'on ~* +@all',
            })


# ==================== User Group Tests ====================

class TestUserGroup:
    """CRUD tests for User Groups."""

    @pytest.fixture
    def store(self):
        return ElastiCacheStore()

    def test_create_happy_path(self, store):
        create_handler = _load_handler('CreateUserGroup')
        response = create_handler(store, {
            'UserGroupId': 'ug-1',
            'Engine': 'redis',
        })
        assert response['UserGroupId'] == 'ug-1'

    def test_create_duplicate(self, store):
        create_handler = _load_handler('CreateUserGroup')
        create_handler(store, {'UserGroupId': 'ug-1', 'Engine': 'redis'})
        with pytest.raises(UserGroupAlreadyExistsFault):
            create_handler(store, {'UserGroupId': 'ug-1', 'Engine': 'redis'})


# ==================== Engine Versions Test ====================

class TestEngineVersions:
    """Test engine version listing."""

    def test_describe_engine_versions(self):
        store = ElastiCacheStore()
        handler = _load_handler('DescribeCacheEngineVersions')
        response = handler(store, {})
        assert 'CacheEngineVersions' in response
        assert len(response['CacheEngineVersions']) > 0
        engines = {v['Engine'] for v in response['CacheEngineVersions']}
        assert 'redis' in engines
