"""Neptune in-memory store, data classes, and exceptions."""
import time
import uuid

# ╔══════════════════════════════════════════════════════════════╗
# ║                        EXCEPTIONS                           ║
# ╚══════════════════════════════════════════════════════════════╝

class NeptuneException(Exception):
    """Base exception for Neptune."""
    status_code = 400

class DBClusterNotFoundFault(NeptuneException):
    """DBClusterIdentifier doesn't refer to an existing DB cluster."""
    status_code = 404

class DBClusterSnapshotNotFoundFault(NeptuneException):
    """DBClusterSnapshotIdentifier doesn't refer to an existing DB cluster snapshot."""
    status_code = 404

class DBInstanceNotFoundFault(NeptuneException):
    """DBInstanceIdentifier doesn't refer to an existing DB instance."""
    status_code = 404

class DBParameterGroupNotFoundFault(NeptuneException):
    """DBParameterGroupName doesn't refer to an existing DB parameter group."""
    status_code = 404

class DBSubnetGroupNotFoundFault(NeptuneException):
    """DBSubnetGroupName doesn't refer to an existing DB subnet group."""
    status_code = 404

class DBClusterParameterGroupNotFoundFault(NeptuneException):
    """DBClusterParameterGroupName doesn't refer to an existing DB cluster parameter group."""
    status_code = 404

class DBClusterEndpointNotFoundFault(NeptuneException):
    """DBClusterEndpointIdentifier doesn't refer to an existing endpoint."""
    status_code = 404

class GlobalClusterNotFoundFault(NeptuneException):
    """GlobalClusterIdentifier doesn't refer to an existing global cluster."""
    status_code = 404

class SubscriptionNotFoundFault(NeptuneException):
    """SubscriptionName doesn't refer to an existing event subscription."""
    status_code = 404

class DBClusterAlreadyExistsFault(NeptuneException):
    """A DB cluster with the specified identifier already exists."""
    status_code = 409

class DBClusterSnapshotAlreadyExistsFault(NeptuneException):
    """A DB cluster snapshot with the specified identifier already exists."""
    status_code = 409

class DBInstanceAlreadyExistsFault(NeptuneException):
    """A DB instance with the specified identifier already exists."""
    status_code = 409

class DBParameterGroupAlreadyExistsFault(NeptuneException):
    """A DB parameter group with the specified name already exists."""
    status_code = 409

class DBSubnetGroupAlreadyExistsFault(NeptuneException):
    """A DB subnet group with the specified name already exists."""
    status_code = 409

class DBClusterParameterGroupAlreadyExistsFault(NeptuneException):
    """A DB cluster parameter group with the specified name already exists."""
    status_code = 409

class InvalidDBClusterStateFault(NeptuneException):
    """The DB cluster is not in a valid state."""
    status_code = 400

class InvalidDBInstanceStateFault(NeptuneException):
    """The DB instance is not in a valid state."""
    status_code = 400

class InvalidDBClusterSnapshotStateFault(NeptuneException):
    """The DB cluster snapshot is not in a valid state."""
    status_code = 400

class InvalidParameterValueException(NeptuneException):
    """The parameter value is invalid."""
    status_code = 400

class InvalidSubnet(NeptuneException):
    """The requested subnet is invalid."""
    status_code = 400

class InvalidVPCNetworkStateFault(NeptuneException):
    """The VPC network is in an invalid state."""
    status_code = 400

class SnapshotQuotaExceededFault(NeptuneException):
    """Snapshot quota exceeded."""
    status_code = 400

class DBSubnetQuotaExceededFault(NeptuneException):
    """Subnet quota exceeded."""
    status_code = 400

class InstanceQuotaExceededFault(NeptuneException):
    """Instance quota exceeded."""
    status_code = 400

class StorageQuotaExceededFault(NeptuneException):
    """Storage quota exceeded."""
    status_code = 400

class InsufficientDBClusterCapacityFault(NeptuneException):
    """Insufficient DB cluster capacity."""
    status_code = 400

class InsufficientDBInstanceCapacityFault(NeptuneException):
    """Insufficient DB instance capacity."""
    status_code = 400

class InvalidDBSubnetStateFault(NeptuneException):
    """The DB subnet is not in a valid state."""
    status_code = 400

class InvalidDBSubnetGroupStateFault(NeptuneException):
    """The DB subnet group is not in a valid state."""
    status_code = 400

class DBSubnetGroupDoesNotCoverEnoughAZs(NeptuneException):
    """The DB subnet group doesn't cover enough Availability Zones."""
    status_code = 400


def _find_resource_by_name(store, resource_name):
    """Find a Neptune resource by ARN or identifier."""
    lower_name = resource_name.lower()
    # Check clusters
    for k, v in store.db_clusters.items():
        if lower_name in (k, resource_name):
            return v
    # Check instances
    for k, v in store.db_instances.items():
        if lower_name in (k, resource_name):
            return v
    # Check snapshots
    for k, v in store.db_cluster_snapshots.items():
        if lower_name in (k, resource_name):
            return v
    # Check subnet groups
    for k, v in store.db_subnet_groups.items():
        if lower_name in (k, resource_name):
            return v
    # Check param groups
    for k, v in store.db_cluster_parameter_groups.items():
        if lower_name in (k, resource_name):
            return v
    for k, v in store.db_parameter_groups.items():
        if lower_name in (k, resource_name):
            return v
    return None


# Map common botocore error shapes to our exception classes
ERROR_MAP = {
    'DBClusterNotFoundFault': DBClusterNotFoundFault,
    'DBClusterSnapshotNotFoundFault': DBClusterSnapshotNotFoundFault,
    'DBInstanceNotFoundFault': DBInstanceNotFoundFault,
    'DBParameterGroupNotFoundFault': DBParameterGroupNotFoundFault,
    'DBSubnetGroupNotFoundFault': DBSubnetGroupNotFoundFault,
    'DBClusterParameterGroupNotFoundFault': DBClusterParameterGroupNotFoundFault,
    'DBClusterEndpointNotFoundFault': DBClusterEndpointNotFoundFault,
    'GlobalClusterNotFoundFault': GlobalClusterNotFoundFault,
    'SubscriptionNotFoundFault': SubscriptionNotFoundFault,
    'DBClusterAlreadyExistsFault': DBClusterAlreadyExistsFault,
    'DBClusterSnapshotAlreadyExistsFault': DBClusterSnapshotAlreadyExistsFault,
    'DBInstanceAlreadyExistsFault': DBInstanceAlreadyExistsFault,
    'DBParameterGroupAlreadyExistsFault': DBParameterGroupAlreadyExistsFault,
    'DBSubnetGroupAlreadyExistsFault': DBSubnetGroupAlreadyExistsFault,
    'DBClusterParameterGroupAlreadyExistsFault': DBClusterParameterGroupAlreadyExistsFault,
    'InvalidDBClusterStateFault': InvalidDBClusterStateFault,
    'InvalidDBInstanceStateFault': InvalidDBInstanceStateFault,
    'InvalidDBClusterSnapshotStateFault': InvalidDBClusterSnapshotStateFault,
    'InvalidParameterValueException': InvalidParameterValueException,
    'InvalidSubnet': InvalidSubnet,
    'InvalidVPCNetworkStateFault': InvalidVPCNetworkStateFault,
    'SnapshotQuotaExceededFault': SnapshotQuotaExceededFault,
    'DBSubnetQuotaExceededFault': DBSubnetQuotaExceededFault,
    'InstanceQuotaExceededFault': InstanceQuotaExceededFault,
    'StorageQuotaExceededFault': StorageQuotaExceededFault,
    'InsufficientDBClusterCapacityFault': InsufficientDBClusterCapacityFault,
    'InsufficientDBInstanceCapacityFault': InsufficientDBInstanceCapacityFault,
    'InvalidDBSubnetStateFault': InvalidDBSubnetStateFault,
    'InvalidDBSubnetGroupStateFault': InvalidDBSubnetGroupStateFault,
    'DBSubnetGroupDoesNotCoverEnoughAZs': DBSubnetGroupDoesNotCoverEnoughAZs,
}


# ╔══════════════════════════════════════════════════════════════╗
# ║                     DATA CLASSES                            ║
# ╚══════════════════════════════════════════════════════════════╝

class DBClusterRecord:
    """Represents a Neptune DB cluster."""
    def __init__(self, db_cluster_identifier, engine, **kwargs):
        self.db_cluster_identifier = db_cluster_identifier
        self.db_cluster_identifier_lower = db_cluster_identifier.lower()
        self.engine = engine
        self.status = kwargs.get('status', 'creating')
        self.allocated_storage = kwargs.get('allocated_storage', 1)
        self.availability_zones = kwargs.get('availability_zones', [])
        self.backup_retention_period = kwargs.get('backup_retention_period', 1)
        self.character_set_name = kwargs.get('character_set_name', '')
        self.database_name = kwargs.get('database_name', '')
        self.db_cluster_parameter_group = kwargs.get('db_cluster_parameter_group', '')
        self.db_subnet_group = kwargs.get('db_subnet_group', '')
        self.endpoint = kwargs.get('endpoint', '')
        self.reader_endpoint = kwargs.get('reader_endpoint', '')
        self.engine_version = kwargs.get('engine_version', '')
        self.port = kwargs.get('port', 8182)
        self.master_username = kwargs.get('master_username', '')
        self.preferred_backup_window = kwargs.get('preferred_backup_window', '')
        self.preferred_maintenance_window = kwargs.get('preferred_maintenance_window', '')
        self.replication_source_identifier = kwargs.get('replication_source_identifier', '')
        self.storage_encrypted = kwargs.get('storage_encrypted', False)
        self.kms_key_id = kwargs.get('kms_key_id', '')
        self.db_cluster_resource_id = kwargs.get('db_cluster_resource_id', '')
        self.iam_database_authentication_enabled = kwargs.get('iam_database_authentication_enabled', False)
        self.deletion_protection = kwargs.get('deletion_protection', False)
        self.copy_tags_to_snapshot = kwargs.get('copy_tags_to_snapshot', False)
        self.enable_cloudwatch_logs_exports = kwargs.get('enable_cloudwatch_logs_exports', [])
        self.vpc_security_group_ids = kwargs.get('vpc_security_group_ids', [])
        self.db_cluster_members = kwargs.get('db_cluster_members', [])
        self.associated_roles = kwargs.get('associated_roles', [])
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()
        self.latest_restorable_time = self.created_at

    def to_dict(self):
        return {
            'DBClusterIdentifier': self.db_cluster_identifier,
            'Engine': self.engine,
            'Status': self.status,
            'AllocatedStorage': self.allocated_storage,
            'AvailabilityZones': self.availability_zones,
            'BackupRetentionPeriod': self.backup_retention_period,
            'DatabaseName': self.database_name,
            'DBClusterParameterGroup': self.db_cluster_parameter_group,
            'DBSubnetGroup': self.db_subnet_group,
            'Endpoint': self.endpoint,
            'ReaderEndpoint': self.reader_endpoint,
            'EngineVersion': self.engine_version,
            'Port': self.port,
            'MasterUsername': self.master_username,
            'PreferredBackupWindow': self.preferred_backup_window,
            'PreferredMaintenanceWindow': self.preferred_maintenance_window,
            'StorageEncrypted': self.storage_encrypted,
            'KmsKeyId': self.kms_key_id,
            'DbClusterResourceId': self.db_cluster_resource_id,
            'IAMDatabaseAuthenticationEnabled': self.iam_database_authentication_enabled,
            'DeletionProtection': self.deletion_protection,
            'CopyTagsToSnapshot': self.copy_tags_to_snapshot,
            'EnableCloudwatchLogsExports': self.enable_cloudwatch_logs_exports,
            'VpcSecurityGroups': [{'VpcSecurityGroupId': g} for g in self.vpc_security_group_ids],
            'DBClusterMembers': self.db_cluster_members,
            'AssociatedRoles': self.associated_roles,
            'ClusterCreateTime': self.created_at,
            'LatestRestorableTime': self.latest_restorable_time,
        }


class DBInstanceRecord:
    """Represents a Neptune DB instance."""
    def __init__(self, db_instance_identifier, db_instance_class, engine, db_cluster_identifier, **kwargs):
        self.db_instance_identifier = db_instance_identifier
        self.db_instance_identifier_lower = db_instance_identifier.lower()
        self.db_instance_class = db_instance_class
        self.engine = engine
        self.db_cluster_identifier = db_cluster_identifier
        self.status = kwargs.get('status', 'creating')
        self.allocated_storage = kwargs.get('allocated_storage', 100)
        self.availability_zone = kwargs.get('availability_zone', '')
        self.db_parameter_groups = kwargs.get('db_parameter_groups', [])
        self.db_subnet_group = kwargs.get('db_subnet_group', '')
        self.endpoint_address = kwargs.get('endpoint_address', '')
        self.endpoint_port = kwargs.get('endpoint_port', 8182)
        self.engine_version = kwargs.get('engine_version', '')
        self.master_username = kwargs.get('master_username', '')
        self.preferred_backup_window = kwargs.get('preferred_backup_window', '')
        self.preferred_maintenance_window = kwargs.get('preferred_maintenance_window', '')
        self.publicly_accessible = kwargs.get('publicly_accessible', False)
        self.storage_encrypted = kwargs.get('storage_encrypted', False)
        self.kms_key_id = kwargs.get('kms_key_id', '')
        self.iam_database_authentication_enabled = kwargs.get('iam_database_authentication_enabled', False)
        self.promotion_tier = kwargs.get('promotion_tier', 1)
        self.auto_minor_version_upgrade = kwargs.get('auto_minor_version_upgrade', True)
        self.monitoring_interval = kwargs.get('monitoring_interval', 0)
        self.monitoring_role_arn = kwargs.get('monitoring_role_arn', '')
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()

    def to_dict(self):
        d = {
            'DBInstanceIdentifier': self.db_instance_identifier,
            'DBInstanceClass': self.db_instance_class,
            'Engine': self.engine,
            'DBClusterIdentifier': self.db_cluster_identifier,
            'DBInstanceStatus': self.status,
            'AllocatedStorage': self.allocated_storage,
            'AvailabilityZone': self.availability_zone,
            'DBParameterGroups': self.db_parameter_groups,
            'DBSubnetGroup': {'DBSubnetGroupName': self.db_subnet_group} if self.db_subnet_group else None,
            'Endpoint': {'Address': self.endpoint_address, 'Port': self.endpoint_port} if self.endpoint_address else None,
            'EngineVersion': self.engine_version,
            'MasterUsername': self.master_username,
            'PreferredBackupWindow': self.preferred_backup_window,
            'PreferredMaintenanceWindow': self.preferred_maintenance_window,
            'PubliclyAccessible': self.publicly_accessible,
            'StorageEncrypted': self.storage_encrypted,
            'KmsKeyId': self.kms_key_id,
            'IAMDatabaseAuthenticationEnabled': self.iam_database_authentication_enabled,
            'PromotionTier': self.promotion_tier,
            'AutoMinorVersionUpgrade': self.auto_minor_version_upgrade,
            'MonitoringInterval': self.monitoring_interval,
            'MonitoringRoleArn': self.monitoring_role_arn,
            'InstanceCreateTime': self.created_at,
        }
        return {k: v for k, v in d.items() if v is not None}


class DBClusterParameterGroupRecord:
    """Represents a DB cluster parameter group."""
    def __init__(self, name, family, description, **kwargs):
        self.name = name
        self.name_lower = name.lower()
        self.family = family
        self.description = description
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()

    def to_dict(self):
        return {
            'DBClusterParameterGroupName': self.name,
            'DBParameterGroupFamily': self.family,
            'Description': self.description,
            'DBClusterParameterGroupArn': '',
        }


class DBParameterGroupRecord:
    """Represents a DB parameter group."""
    def __init__(self, name, family, description, **kwargs):
        self.name = name
        self.name_lower = name.lower()
        self.family = family
        self.description = description
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()

    def to_dict(self):
        return {
            'DBParameterGroupName': self.name,
            'DBParameterGroupFamily': self.family,
            'Description': self.description,
            'DBParameterGroupArn': '',
        }


class DBClusterSnapshotRecord:
    """Represents a DB cluster snapshot."""
    def __init__(self, snapshot_id, db_cluster_identifier, **kwargs):
        self.snapshot_id = snapshot_id
        self.snapshot_id_lower = snapshot_id.lower()
        self.db_cluster_identifier = db_cluster_identifier
        self.engine = kwargs.get('engine', 'neptune')
        self.status = kwargs.get('status', 'creating')
        self.snapshot_type = kwargs.get('snapshot_type', 'manual')
        self.allocated_storage = kwargs.get('allocated_storage', 1)
        self.engine_version = kwargs.get('engine_version', '')
        self.port = kwargs.get('port', 8182)
        self.storage_encrypted = kwargs.get('storage_encrypted', False)
        self.kms_key_id = kwargs.get('kms_key_id', '')
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()

    def to_dict(self):
        return {
            'DBClusterSnapshotIdentifier': self.snapshot_id,
            'DBClusterIdentifier': self.db_cluster_identifier,
            'Engine': self.engine,
            'Status': self.status,
            'SnapshotType': self.snapshot_type,
            'AllocatedStorage': self.allocated_storage,
            'EngineVersion': self.engine_version,
            'Port': self.port,
            'StorageEncrypted': self.storage_encrypted,
            'KmsKeyId': self.kms_key_id,
            'SnapshotCreateTime': self.created_at,
        }


class DBSubnetGroupRecord:
    """Represents a DB subnet group."""
    def __init__(self, name, description, subnet_ids, **kwargs):
        self.name = name
        self.name_lower = name.lower()
        self.description = description
        self.subnet_ids = list(subnet_ids)
        self.status = kwargs.get('status', 'Complete')
        self.vpc_id = kwargs.get('vpc_id', '')
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()

    def to_dict(self):
        return {
            'DBSubnetGroupName': self.name,
            'DBSubnetGroupDescription': self.description,
            'VpcId': self.vpc_id,
            'SubnetGroupStatus': self.status,
            'Subnets': [{'SubnetIdentifier': sid} for sid in self.subnet_ids],
            'DBSubnetGroupArn': '',
        }


class DBClusterEndpointRecord:
    """Represents a custom DB cluster endpoint."""
    def __init__(self, endpoint_id, db_cluster_identifier, endpoint_type, **kwargs):
        self.endpoint_id = endpoint_id
        self.endpoint_id_lower = endpoint_id.lower()
        self.db_cluster_identifier = db_cluster_identifier
        self.endpoint_type = endpoint_type  # READER or ANY
        self.status = kwargs.get('status', 'creating')
        self.endpoint = kwargs.get('endpoint', '')
        self.static_members = kwargs.get('static_members', [])
        self.excluded_members = kwargs.get('excluded_members', [])
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()

    def to_dict(self):
        return {
            'DBClusterEndpointIdentifier': self.endpoint_id,
            'DBClusterIdentifier': self.db_cluster_identifier,
            'EndpointType': self.endpoint_type,
            'Status': self.status,
            'Endpoint': self.endpoint,
            'StaticMembers': self.static_members,
            'ExcludedMembers': self.excluded_members,
            'DBClusterEndpointArn': '',
        }


class EventSubscriptionRecord:
    """Represents an event notification subscription."""
    def __init__(self, subscription_name, sns_topic_arn, **kwargs):
        self.subscription_name = subscription_name
        self.subscription_name_lower = subscription_name.lower()
        self.sns_topic_arn = sns_topic_arn
        self.status = kwargs.get('status', 'creating')
        self.source_type = kwargs.get('source_type', '')
        self.source_ids = kwargs.get('source_ids', [])
        self.event_categories = kwargs.get('event_categories', [])
        self.enabled = kwargs.get('enabled', True)
        self.tags = kwargs.get('tags', [])
        self.created_at = time.time()

    def to_dict(self):
        return {
            'EventSubscriptionArn': '',
            'CustSubscriptionId': self.subscription_name,
            'SnsTopicArn': self.sns_topic_arn,
            'Status': self.status,
            'SourceType': self.source_type,
            'SourceIdsList': self.source_ids,
            'EventCategoriesList': self.event_categories,
            'Enabled': self.enabled,
            'SubscriptionCreationTime': self.created_at,
        }


class GlobalClusterRecord:
    """Represents a Neptune global database cluster."""
    def __init__(self, global_cluster_identifier, **kwargs):
        self.global_cluster_identifier = global_cluster_identifier
        self.global_cluster_identifier_lower = global_cluster_identifier.lower()
        self.engine = kwargs.get('engine', 'neptune')
        self.engine_version = kwargs.get('engine_version', '')
        self.status = kwargs.get('status', 'creating')
        self.storage_encrypted = kwargs.get('storage_encrypted', False)
        self.deletion_protection = kwargs.get('deletion_protection', False)
        self.global_cluster_members = kwargs.get('global_cluster_members', [])
        self.created_at = time.time()

    def to_dict(self):
        return {
            'GlobalClusterIdentifier': self.global_cluster_identifier,
            'Engine': self.engine,
            'EngineVersion': self.engine_version,
            'Status': self.status,
            'StorageEncrypted': self.storage_encrypted,
            'DeletionProtection': self.deletion_protection,
            'GlobalClusterMembers': self.global_cluster_members,
            'GlobalClusterArn': '',
        }


# ╔══════════════════════════════════════════════════════════════╗
# ║                          STORE                              ║
# ╚══════════════════════════════════════════════════════════════╝

class NeptuneStore:
    """In-memory store for Neptune resources."""

    def __init__(self):
        self.db_clusters = {}
        self.db_instances = {}
        self.db_cluster_parameter_groups = {}
        self.db_parameter_groups = {}
        self.db_cluster_snapshots = {}
        self.db_subnet_groups = {}
        self.db_cluster_endpoints = {}
        self.event_subscriptions = {}
        self.global_clusters = {}

    # ── DBClusters ──────────────────────────────────────────

    def get_cluster(self, identifier):
        """Get cluster by identifier (case-insensitive)."""
        key = identifier.lower()
        if key not in self.db_clusters:
            raise DBClusterNotFoundFault(f"DBCluster {identifier} not found")
        return self.db_clusters[key]

    def create_cluster(self, db_cluster_identifier, engine, **kwargs):
        key = db_cluster_identifier.lower()
        if key in self.db_clusters:
            raise DBClusterAlreadyExistsFault(f"DBCluster {db_cluster_identifier} already exists")
        cluster = DBClusterRecord(db_cluster_identifier, engine, **kwargs)
        cluster.db_cluster_resource_id = f"cluster-{uuid.uuid4().hex[:16]}"
        self.db_clusters[key] = cluster
        return cluster

    def delete_cluster(self, db_cluster_identifier, skip_final_snapshot=False,
                       final_db_snapshot_identifier=''):
        cluster = self.get_cluster(db_cluster_identifier)
        if cluster.status not in ('available', 'stopped', 'failed'):
            raise InvalidDBClusterStateFault(
                f"DBCluster {db_cluster_identifier} is in {cluster.status} state")
        del self.db_clusters[db_cluster_identifier.lower()]
        return cluster

    def modify_cluster(self, db_cluster_identifier, **updates):
        cluster = self.get_cluster(db_cluster_identifier)
        for k, v in updates.items():
            if v is not None:
                setattr(cluster, k, v)
        return cluster

    def list_clusters(self, db_cluster_identifier=None, max_records=100, marker=None):
        if db_cluster_identifier:
            return [self.get_cluster(db_cluster_identifier)]
        all_clusters = sorted(self.db_clusters.values(),
                              key=lambda c: c.db_cluster_identifier_lower)
        return all_clusters[:max_records]

    # ── DBInstances ─────────────────────────────────────────

    def get_instance(self, identifier):
        key = identifier.lower()
        if key not in self.db_instances:
            raise DBInstanceNotFoundFault(f"DBInstance {identifier} not found")
        return self.db_instances[key]

    def create_instance(self, db_instance_identifier, db_instance_class, engine,
                        db_cluster_identifier, **kwargs):
        key = db_instance_identifier.lower()
        if key in self.db_instances:
            raise DBInstanceAlreadyExistsFault(f"DBInstance {db_instance_identifier} already exists")
        instance = DBInstanceRecord(db_instance_identifier, db_instance_class, engine,
                                    db_cluster_identifier, **kwargs)
        self.db_instances[key] = instance
        # Add to cluster members
        cluster_key = db_cluster_identifier.lower()
        if cluster_key in self.db_clusters:
            cluster = self.db_clusters[cluster_key]
            cluster.db_cluster_members.append({
                'DBInstanceIdentifier': db_instance_identifier,
                'IsClusterWriter': len(cluster.db_cluster_members) == 0,
                'DBClusterParameterGroupStatus': 'in-sync',
                'PromotionTier': kwargs.get('promotion_tier', 1),
            })
        return instance

    def delete_instance(self, db_instance_identifier, skip_final_snapshot=False):
        instance = self.get_instance(db_instance_identifier)
        if instance.status in ('creating', 'deleting'):
            raise InvalidDBInstanceStateFault(
                f"DBInstance {db_instance_identifier} is in {instance.status} state")
        del self.db_instances[db_instance_identifier.lower()]
        return instance

    def modify_instance(self, db_instance_identifier, **updates):
        instance = self.get_instance(db_instance_identifier)
        for k, v in updates.items():
            if v is not None:
                setattr(instance, k, v)
        return instance

    def list_instances(self, db_instance_identifier=None, max_records=100):
        if db_instance_identifier:
            return [self.get_instance(db_instance_identifier)]
        all_instances = sorted(self.db_instances.values(),
                               key=lambda i: i.db_instance_identifier_lower)
        return all_instances[:max_records]

    # ── DBClusterParameterGroups ────────────────────────────

    def get_cluster_param_group(self, name):
        key = name.lower()
        if key not in self.db_cluster_parameter_groups:
            raise DBClusterParameterGroupNotFoundFault(
                f"DBClusterParameterGroup {name} not found")
        return self.db_cluster_parameter_groups[key]

    def create_cluster_param_group(self, name, family, description, **kwargs):
        key = name.lower()
        if key in self.db_cluster_parameter_groups:
            raise DBClusterParameterGroupAlreadyExistsFault(
                f"DBClusterParameterGroup {name} already exists")
        pg = DBClusterParameterGroupRecord(name, family, description, **kwargs)
        self.db_cluster_parameter_groups[key] = pg
        return pg

    def delete_cluster_param_group(self, name):
        pg = self.get_cluster_param_group(name)
        del self.db_cluster_parameter_groups[name.lower()]
        return pg

    def list_cluster_param_groups(self, name=None, max_records=100):
        if name:
            return [self.get_cluster_param_group(name)]
        return sorted(self.db_cluster_parameter_groups.values(),
                      key=lambda p: p.name_lower)[:max_records]

    # ── DBParameterGroups ───────────────────────────────────

    def get_param_group(self, name):
        key = name.lower()
        if key not in self.db_parameter_groups:
            raise DBParameterGroupNotFoundFault(f"DBParameterGroup {name} not found")
        return self.db_parameter_groups[key]

    def create_param_group(self, name, family, description, **kwargs):
        key = name.lower()
        if key in self.db_parameter_groups:
            raise DBParameterGroupAlreadyExistsFault(
                f"DBParameterGroup {name} already exists")
        pg = DBParameterGroupRecord(name, family, description, **kwargs)
        self.db_parameter_groups[key] = pg
        return pg

    def delete_param_group(self, name):
        pg = self.get_param_group(name)
        del self.db_parameter_groups[name.lower()]
        return pg

    def list_param_groups(self, name=None, max_records=100):
        if name:
            return [self.get_param_group(name)]
        return sorted(self.db_parameter_groups.values(),
                      key=lambda p: p.name_lower)[:max_records]

    # ── DBClusterSnapshots ──────────────────────────────────

    def get_snapshot(self, snapshot_id):
        key = snapshot_id.lower()
        if key not in self.db_cluster_snapshots:
            raise DBClusterSnapshotNotFoundFault(
                f"DBClusterSnapshot {snapshot_id} not found")
        return self.db_cluster_snapshots[key]

    def create_snapshot(self, snapshot_id, db_cluster_identifier, **kwargs):
        key = snapshot_id.lower()
        if key in self.db_cluster_snapshots:
            raise DBClusterSnapshotAlreadyExistsFault(
                f"DBClusterSnapshot {snapshot_id} already exists")
        snap = DBClusterSnapshotRecord(snapshot_id, db_cluster_identifier, **kwargs)
        self.db_cluster_snapshots[key] = snap
        return snap

    def delete_snapshot(self, snapshot_id):
        snap = self.get_snapshot(snapshot_id)
        del self.db_cluster_snapshots[snapshot_id.lower()]
        return snap

    def list_snapshots(self, db_cluster_identifier=None, snapshot_type=None, max_records=100):
        snaps = list(self.db_cluster_snapshots.values())
        if db_cluster_identifier:
            lower_id = db_cluster_identifier.lower()
            snaps = [s for s in snaps if s.db_cluster_identifier.lower() == lower_id]
        if snapshot_type:
            snaps = [s for s in snaps if s.snapshot_type == snapshot_type]
        return sorted(snaps, key=lambda s: s.snapshot_id_lower)[:max_records]

    # ── DBSubnetGroups ──────────────────────────────────────

    def get_subnet_group(self, name):
        key = name.lower()
        if key not in self.db_subnet_groups:
            raise DBSubnetGroupNotFoundFault(f"DBSubnetGroup {name} not found")
        return self.db_subnet_groups[key]

    def create_subnet_group(self, name, description, subnet_ids, **kwargs):
        key = name.lower()
        if key in self.db_subnet_groups:
            raise DBSubnetGroupAlreadyExistsFault(f"DBSubnetGroup {name} already exists")
        sg = DBSubnetGroupRecord(name, description, subnet_ids, **kwargs)
        self.db_subnet_groups[key] = sg
        return sg

    def delete_subnet_group(self, name):
        sg = self.get_subnet_group(name)
        del self.db_subnet_groups[name.lower()]
        return sg

    def list_subnet_groups(self, name=None, max_records=100):
        if name:
            return [self.get_subnet_group(name)]
        return sorted(self.db_subnet_groups.values(),
                      key=lambda s: s.name_lower)[:max_records]

    # ── DBClusterEndpoints ──────────────────────────────────

    def get_endpoint(self, endpoint_id):
        key = endpoint_id.lower()
        if key not in self.db_cluster_endpoints:
            raise DBClusterEndpointNotFoundFault(
                f"DBClusterEndpoint {endpoint_id} not found")
        return self.db_cluster_endpoints[key]

    def create_endpoint(self, endpoint_id, db_cluster_identifier, endpoint_type, **kwargs):
        key = endpoint_id.lower()
        if key in self.db_cluster_endpoints:
            raise DBClusterEndpointNotFoundFault(f"DBClusterEndpoint {endpoint_id} already exists")
        ep = DBClusterEndpointRecord(endpoint_id, db_cluster_identifier, endpoint_type, **kwargs)
        self.db_cluster_endpoints[key] = ep
        return ep

    def delete_endpoint(self, endpoint_id):
        ep = self.get_endpoint(endpoint_id)
        del self.db_cluster_endpoints[endpoint_id.lower()]
        return ep

    def list_endpoints(self, db_cluster_identifier=None, max_records=100):
        eps = list(self.db_cluster_endpoints.values())
        if db_cluster_identifier:
            eps = [e for e in eps
                   if e.db_cluster_identifier.lower() == db_cluster_identifier.lower()]
        return sorted(eps, key=lambda e: e.endpoint_id_lower)[:max_records]

    # ── EventSubscriptions ───────────────────────────────────

    def get_subscription(self, subscription_name):
        key = subscription_name.lower()
        if key not in self.event_subscriptions:
            raise SubscriptionNotFoundFault(
                f"EventSubscription {subscription_name} not found")
        return self.event_subscriptions[key]

    def create_subscription(self, subscription_name, sns_topic_arn, **kwargs):
        key = subscription_name.lower()
        if key in self.event_subscriptions:
            raise SubscriptionNotFoundFault(
                f"EventSubscription {subscription_name} already exists")
        sub = EventSubscriptionRecord(subscription_name, sns_topic_arn, **kwargs)
        self.event_subscriptions[key] = sub
        return sub

    def delete_subscription(self, subscription_name):
        sub = self.get_subscription(subscription_name)
        del self.event_subscriptions[subscription_name.lower()]
        return sub

    def list_subscriptions(self, subscription_name=None, max_records=100):
        if subscription_name:
            return [self.get_subscription(subscription_name)]
        return sorted(self.event_subscriptions.values(),
                      key=lambda s: s.subscription_name_lower)[:max_records]

    # ── GlobalClusters ──────────────────────────────────────

    def get_global_cluster(self, global_cluster_identifier):
        key = global_cluster_identifier.lower()
        if key not in self.global_clusters:
            raise GlobalClusterNotFoundFault(
                f"GlobalCluster {global_cluster_identifier} not found")
        return self.global_clusters[key]

    def create_global_cluster(self, global_cluster_identifier, **kwargs):
        key = global_cluster_identifier.lower()
        if key in self.global_clusters:
            raise GlobalClusterNotFoundFault(
                f"GlobalCluster {global_cluster_identifier} already exists")
        gc = GlobalClusterRecord(global_cluster_identifier, **kwargs)
        self.global_clusters[key] = gc
        return gc

    def delete_global_cluster(self, global_cluster_identifier):
        gc = self.get_global_cluster(global_cluster_identifier)
        del self.global_clusters[global_cluster_identifier.lower()]
        return gc

    def list_global_clusters(self, global_cluster_identifier=None, max_records=100):
        if global_cluster_identifier:
            return [self.get_global_cluster(global_cluster_identifier)]
        return sorted(self.global_clusters.values(),
                      key=lambda g: g.global_cluster_identifier_lower)[:max_records]
