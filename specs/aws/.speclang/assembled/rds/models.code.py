"""RDSStore — local emulator store for Amazon RDS (Relational Database Service).

Core entities: DBInstance, DBCluster, DBSnapshot, DBParameterGroup,
DBSubnetGroup, DBClusterParameterGroup.

Supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server engine types.
"""

import time
import uuid


# ── Exception classes ──────────────────────────────────────────────────

class DBInstanceNotFoundFault(Exception):
    """DBInstanceIdentifier doesn't refer to an existing DB instance."""
    pass

class DBClusterNotFoundFault(Exception):
    """DBClusterIdentifier doesn't refer to an existing DB cluster."""
    pass

class DBSnapshotNotFoundFault(Exception):
    """DBSnapshotIdentifier doesn't refer to an existing DB snapshot."""
    pass

class DBParameterGroupNotFoundFault(Exception):
    """DBParameterGroupName doesn't refer to an existing DB parameter group."""
    pass

class DBSubnetGroupNotFoundFault(Exception):
    """DBSubnetGroupName doesn't refer to an existing DB subnet group."""
    pass

class DBClusterParameterGroupNotFoundFault(Exception):
    """DBClusterParameterGroupName doesn't refer to an existing cluster parameter group."""
    pass

class DBInstanceAlreadyExistsFault(Exception):
    """A DB instance with the specified identifier already exists."""
    pass

class DBClusterAlreadyExistsFault(Exception):
    """A DB cluster with the specified identifier already exists."""
    pass

class DBSnapshotAlreadyExistsFault(Exception):
    """A DB snapshot with the specified identifier already exists."""
    pass

class DBParameterGroupAlreadyExistsFault(Exception):
    """A DB parameter group with the same name already exists."""
    pass

class DBSubnetGroupAlreadyExistsFault(Exception):
    """A DB subnet group with the same name already exists."""
    pass

class InvalidParameterException(Exception):
    """An invalid or out-of-range value was supplied."""
    pass

class ResourceNotFoundException(Exception):
    """The requested resource could not be found."""
    pass

class InvalidParameterCombinationException(Exception):
    """Parameters that must not be used together were used together."""
    pass

class InvalidDBInstanceStateFault(Exception):
    """The DB instance is not in a valid state."""
    pass

class InvalidDBClusterStateFault(Exception):
    """The DB cluster is not in a valid state."""
    pass

class SnapshotQuotaExceededFault(Exception):
    """The request would result in exceeding the allowed number of snapshots."""
    pass


# ── Data classes ────────────────────────────────────────────────────────

class DBInstanceRecord:
    """Record for a single RDS DB instance."""
    def __init__(self, db_instance_identifier, db_instance_class, engine,
                 allocated_storage=20, master_username=None,
                 master_user_password=None, db_name=None, port=None,
                 engine_version=None, license_model=None, iops=None,
                 storage_type='standard', db_subnet_group_name=None,
                 vpc_security_group_ids=None, availability_zone=None,
                 multi_az=False, publicly_accessible=False,
                 auto_minor_version_upgrade=True, backup_retention_period=1,
                 preferred_backup_window=None, preferred_maintenance_window=None,
                 db_parameter_group_name=None, option_group_name=None,
                 copy_tags_to_snapshot=False, monitoring_interval=0,
                 monitoring_role_arn=None, tags=None, **kwargs):
        self.db_instance_identifier = db_instance_identifier
        self.db_instance_class = db_instance_class
        self.engine = engine
        self.allocated_storage = allocated_storage
        self.master_username = master_username
        self.db_name = db_name or db_instance_identifier
        self.port = port or (3306 if 'mysql' in engine.lower() or 'mariadb' in engine.lower()
                             else 5432 if 'postgres' in engine.lower()
                             else 1521 if 'oracle' in engine.lower()
                             else 1433)
        self.engine_version = engine_version
        self.license_model = license_model
        self.iops = iops
        self.storage_type = storage_type
        self.db_subnet_group_name = db_subnet_group_name
        self.vpc_security_group_ids = vpc_security_group_ids or []
        self.availability_zone = availability_zone
        self.multi_az = multi_az
        self.publicly_accessible = publicly_accessible
        self.auto_minor_version_upgrade = auto_minor_version_upgrade
        self.backup_retention_period = backup_retention_period
        self.preferred_backup_window = preferred_backup_window
        self.preferred_maintenance_window = preferred_maintenance_window
        self.db_parameter_group_name = db_parameter_group_name
        self.option_group_name = option_group_name
        self.copy_tags_to_snapshot = copy_tags_to_snapshot
        self.monitoring_interval = monitoring_interval
        self.monitoring_role_arn = monitoring_role_arn
        self.tags = tags or []
        self.db_instance_status = 'available'
        self.endpoint_address = f"{db_instance_identifier}.{_random_hex(12)}.us-east-1.rds.amazonaws.com"
        self.db_instance_arn = f"arn:aws:rds:us-east-1:000000000000:db:{db_instance_identifier}"
        self.instance_create_time = time.time()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            'DBInstanceIdentifier': self.db_instance_identifier,
            'DBInstanceClass': self.db_instance_class,
            'Engine': self.engine,
            'DBInstanceStatus': self.db_instance_status,
            'MasterUsername': self.master_username,
            'DBName': self.db_name,
            'Endpoint': {'Address': self.endpoint_address, 'Port': self.port},
            'AllocatedStorage': self.allocated_storage,
            'InstanceCreateTime': self.instance_create_time,
            'PreferredBackupWindow': self.preferred_backup_window,
            'BackupRetentionPeriod': self.backup_retention_period,
            'DBSecurityGroups': [],
            'VpcSecurityGroups': [{'VpcSecurityGroupId': sg, 'Status': 'active'}
                                  for sg in self.vpc_security_group_ids],
            'DBParameterGroups': [{'DBParameterGroupName': self.db_parameter_group_name,
                                   'ParameterApplyStatus': 'in-sync'}] if self.db_parameter_group_name else [],
            'AvailabilityZone': self.availability_zone,
            'DBSubnetGroup': {'DBSubnetGroupName': self.db_subnet_group_name} if self.db_subnet_group_name else None,
            'PreferredMaintenanceWindow': self.preferred_maintenance_window,
            'MultiAZ': self.multi_az,
            'EngineVersion': self.engine_version,
            'AutoMinorVersionUpgrade': self.auto_minor_version_upgrade,
            'LicenseModel': self.license_model,
            'Iops': self.iops,
            'OptionGroupMemberships': [{'OptionGroupName': self.option_group_name, 'Status': 'in-sync'}]
                                      if self.option_group_name else [],
            'PubliclyAccessible': self.publicly_accessible,
            'StorageType': self.storage_type,
            'DBInstanceArn': self.db_instance_arn,
            'CopyTagsToSnapshot': self.copy_tags_to_snapshot,
            'MonitoringInterval': self.monitoring_interval,
            'MonitoringRoleArn': self.monitoring_role_arn,
            'TagList': self.tags,
        }


class DBClusterRecord:
    """Record for a single RDS DB cluster (Aurora or Multi-AZ)."""
    def __init__(self, db_cluster_identifier, engine, db_cluster_parameter_group_name=None,
                 vpc_security_group_ids=None, db_subnet_group_name=None,
                 database_name=None, master_username=None, master_user_password=None,
                 port=None, engine_version=None, backup_retention_period=1,
                 preferred_backup_window=None, preferred_maintenance_window=None,
                 storage_encrypted=False, kms_key_id=None, tags=None, **kwargs):
        self.db_cluster_identifier = db_cluster_identifier
        self.engine = engine
        self.db_cluster_parameter_group_name = db_cluster_parameter_group_name
        self.vpc_security_group_ids = vpc_security_group_ids or []
        self.db_subnet_group_name = db_subnet_group_name
        self.database_name = database_name
        self.master_username = master_username
        self.port = port or (3306 if 'mysql' in engine.lower() else 5432)
        self.engine_version = engine_version
        self.backup_retention_period = backup_retention_period
        self.preferred_backup_window = preferred_backup_window
        self.preferred_maintenance_window = preferred_maintenance_window
        self.storage_encrypted = storage_encrypted
        self.kms_key_id = kms_key_id
        self.tags = tags or []
        self.status = 'available'
        self.endpoint = f"{db_cluster_identifier}.cluster-{_random_hex(12)}.us-east-1.rds.amazonaws.com"
        self.reader_endpoint = f"{db_cluster_identifier}.cluster-ro-{_random_hex(12)}.us-east-1.rds.amazonaws.com"
        self.db_cluster_arn = f"arn:aws:rds:us-east-1:000000000000:cluster:{db_cluster_identifier}"
        self.cluster_create_time = time.time()
        self.db_cluster_members = []
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            'DBClusterIdentifier': self.db_cluster_identifier,
            'Engine': self.engine,
            'Status': self.status,
            'Endpoint': self.endpoint,
            'ReaderEndpoint': self.reader_endpoint,
            'Port': self.port,
            'MasterUsername': self.master_username,
            'DatabaseName': self.database_name,
            'DBClusterParameterGroup': self.db_cluster_parameter_group_name,
            'DBSubnetGroup': self.db_subnet_group_name,
            'VpcSecurityGroups': [{'VpcSecurityGroupId': sg, 'Status': 'active'}
                                  for sg in self.vpc_security_group_ids],
            'BackupRetentionPeriod': self.backup_retention_period,
            'PreferredBackupWindow': self.preferred_backup_window,
            'PreferredMaintenanceWindow': self.preferred_maintenance_window,
            'StorageEncrypted': self.storage_encrypted,
            'KmsKeyId': self.kms_key_id,
            'DBClusterArn': self.db_cluster_arn,
            'ClusterCreateTime': self.cluster_create_time,
            'DBClusterMembers': self.db_cluster_members,
            'EngineVersion': self.engine_version,
            'TagList': self.tags,
        }


class DBSnapshotRecord:
    """Record for a DB snapshot."""
    def __init__(self, db_snapshot_identifier, db_instance_identifier,
                 engine, snapshot_type='manual', tags=None, **kwargs):
        self.db_snapshot_identifier = db_snapshot_identifier
        self.db_instance_identifier = db_instance_identifier
        self.engine = engine
        self.snapshot_type = snapshot_type
        self.tags = tags or []
        self.status = 'available'
        self.snapshot_create_time = time.time()
        self.allocated_storage = kwargs.get('allocated_storage', 20)
        self.port = kwargs.get('port', 3306)
        self.availability_zone = kwargs.get('availability_zone', 'us-east-1a')
        self.db_snapshot_arn = f"arn:aws:rds:us-east-1:000000000000:snapshot:{db_snapshot_identifier}"
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            'DBSnapshotIdentifier': self.db_snapshot_identifier,
            'DBInstanceIdentifier': self.db_instance_identifier,
            'Engine': self.engine,
            'SnapshotType': self.snapshot_type,
            'Status': self.status,
            'SnapshotCreateTime': self.snapshot_create_time,
            'AllocatedStorage': self.allocated_storage,
            'Port': self.port,
            'AvailabilityZone': self.availability_zone,
            'DBSnapshotArn': self.db_snapshot_arn,
            'TagList': self.tags,
        }


class DBParameterGroupRecord:
    """Record for a DB parameter group."""
    def __init__(self, db_parameter_group_name, db_parameter_group_family,
                 description, tags=None, **kwargs):
        self.db_parameter_group_name = db_parameter_group_name
        self.db_parameter_group_family = db_parameter_group_family
        self.description = description
        self.tags = tags or []
        self.db_parameter_group_arn = f"arn:aws:rds:us-east-1:000000000000:pg:{db_parameter_group_name}"
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            'DBParameterGroupName': self.db_parameter_group_name,
            'DBParameterGroupFamily': self.db_parameter_group_family,
            'Description': self.description,
            'DBParameterGroupArn': self.db_parameter_group_arn,
        }


class DBSubnetGroupRecord:
    """Record for a DB subnet group."""
    def __init__(self, db_subnet_group_name, db_subnet_group_description,
                 subnet_ids, tags=None, **kwargs):
        self.db_subnet_group_name = db_subnet_group_name
        self.db_subnet_group_description = db_subnet_group_description
        self.subnet_ids = subnet_ids or []
        self.tags = tags or []
        self.subnet_group_status = 'Complete'
        self.vpc_id = kwargs.get('vpc_id', 'vpc-default')
        self.db_subnet_group_arn = f"arn:aws:rds:us-east-1:000000000000:subgrp:{db_subnet_group_name}"
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            'DBSubnetGroupName': self.db_subnet_group_name,
            'DBSubnetGroupDescription': self.db_subnet_group_description,
            'VpcId': self.vpc_id,
            'SubnetGroupStatus': self.subnet_group_status,
            'Subnets': [{'SubnetIdentifier': sid} for sid in self.subnet_ids],
            'DBSubnetGroupArn': self.db_subnet_group_arn,
        }


class DBClusterParameterGroupRecord:
    """Record for a DB cluster parameter group."""
    def __init__(self, db_cluster_parameter_group_name,
                 db_parameter_group_family, description, tags=None, **kwargs):
        self.db_cluster_parameter_group_name = db_cluster_parameter_group_name
        self.db_parameter_group_family = db_parameter_group_family
        self.description = description
        self.tags = tags or []
        self.db_cluster_parameter_group_arn = (
            f"arn:aws:rds:us-east-1:000000000000:cluster-pg:{db_cluster_parameter_group_name}")
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            'DBClusterParameterGroupName': self.db_cluster_parameter_group_name,
            'DBParameterGroupFamily': self.db_parameter_group_family,
            'Description': self.description,
            'DBClusterParameterGroupArn': self.db_cluster_parameter_group_arn,
        }


# ── Helpers ─────────────────────────────────────────────────────────────

def _random_hex(n):
    return uuid.uuid4().hex[:n]

def _generate_resource_id():
    return f"rds-{uuid.uuid4().hex[:17]}"


# ── RDS Store ───────────────────────────────────────────────────────────

class RDSStore:
    """In-memory store for RDS resources."""

    MAX_SNAPSHOTS = 50

    def __init__(self):
        self._instances: dict[str, DBInstanceRecord] = {}
        self._clusters: dict[str, DBClusterRecord] = {}
        self._snapshots: dict[str, DBSnapshotRecord] = {}
        self._param_groups: dict[str, DBParameterGroupRecord] = {}
        self._subnet_groups: dict[str, DBSubnetGroupRecord] = {}
        self._cluster_param_groups: dict[str, DBClusterParameterGroupRecord] = {}

    # ── DB Instance operations ──────────────────────────────────────

    def create_db_instance(self, db_instance_identifier, db_instance_class,
                           engine, **kwargs):
        if db_instance_identifier in self._instances:
            raise DBInstanceAlreadyExistsFault(
                f"DB instance {db_instance_identifier} already exists")
        record = DBInstanceRecord(
            db_instance_identifier=db_instance_identifier,
            db_instance_class=db_instance_class,
            engine=engine,
            **kwargs)
        self._instances[db_instance_identifier] = record
        return record.to_dict()

    def describe_db_instances(self, db_instance_identifier=None):
        if db_instance_identifier:
            if db_instance_identifier not in self._instances:
                raise DBInstanceNotFoundFault(
                    f"DBInstance {db_instance_identifier} not found")
            return self._instances[db_instance_identifier].to_dict()
        return [r.to_dict() for r in self._instances.values()]

    def modify_db_instance(self, db_instance_identifier, **kwargs):
        if db_instance_identifier not in self._instances:
            raise DBInstanceNotFoundFault(
                f"DBInstance {db_instance_identifier} not found")
        record = self._instances[db_instance_identifier]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record.to_dict()

    def delete_db_instance(self, db_instance_identifier,
                           skip_final_snapshot=False,
                           final_db_snapshot_identifier=None):
        if db_instance_identifier not in self._instances:
            raise DBInstanceNotFoundFault(
                f"DBInstance {db_instance_identifier} not found")
        record = self._instances[db_instance_identifier]
        if not skip_final_snapshot and final_db_snapshot_identifier:
            self.create_db_snapshot(
                db_snapshot_identifier=final_db_snapshot_identifier,
                db_instance_identifier=db_instance_identifier,
                engine=record.engine)
        del self._instances[db_instance_identifier]
        return record.to_dict()

    def reboot_db_instance(self, db_instance_identifier, force_failover=False):
        if db_instance_identifier not in self._instances:
            raise DBInstanceNotFoundFault(
                f"DBInstance {db_instance_identifier} not found")
        record = self._instances[db_instance_identifier]
        record.db_instance_status = 'rebooting'
        return record.to_dict()

    # ── DB Cluster operations ───────────────────────────────────────

    def create_db_cluster(self, db_cluster_identifier, engine, **kwargs):
        if db_cluster_identifier in self._clusters:
            raise DBClusterAlreadyExistsFault(
                f"DB cluster {db_cluster_identifier} already exists")
        record = DBClusterRecord(
            db_cluster_identifier=db_cluster_identifier,
            engine=engine,
            **kwargs)
        self._clusters[db_cluster_identifier] = record
        return record.to_dict()

    def describe_db_clusters(self, db_cluster_identifier=None):
        if db_cluster_identifier:
            if db_cluster_identifier not in self._clusters:
                raise DBClusterNotFoundFault(
                    f"DBCluster {db_cluster_identifier} not found")
            return self._clusters[db_cluster_identifier].to_dict()
        return [r.to_dict() for r in self._clusters.values()]

    def modify_db_cluster(self, db_cluster_identifier, **kwargs):
        if db_cluster_identifier not in self._clusters:
            raise DBClusterNotFoundFault(
                f"DBCluster {db_cluster_identifier} not found")
        record = self._clusters[db_cluster_identifier]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record.to_dict()

    def delete_db_cluster(self, db_cluster_identifier,
                          skip_final_snapshot=False,
                          final_db_snapshot_identifier=None):
        if db_cluster_identifier not in self._clusters:
            raise DBClusterNotFoundFault(
                f"DBCluster {db_cluster_identifier} not found")
        record = self._clusters[db_cluster_identifier]
        if not skip_final_snapshot and final_db_snapshot_identifier:
            self.create_db_snapshot(
                db_snapshot_identifier=final_db_snapshot_identifier,
                db_instance_identifier=db_cluster_identifier,
                engine=record.engine)
        del self._clusters[db_cluster_identifier]
        return record.to_dict()

    # ── DB Snapshot operations ──────────────────────────────────────

    def create_db_snapshot(self, db_snapshot_identifier,
                           db_instance_identifier, engine='mysql', **kwargs):
        if db_snapshot_identifier in self._snapshots:
            raise DBSnapshotAlreadyExistsFault(
                f"DBSnapshot {db_snapshot_identifier} already exists")
        if len(self._snapshots) >= self.MAX_SNAPSHOTS:
            raise SnapshotQuotaExceededFault(
                f"Maximum number of snapshots ({self.MAX_SNAPSHOTS}) exceeded")
        record = DBSnapshotRecord(
            db_snapshot_identifier=db_snapshot_identifier,
            db_instance_identifier=db_instance_identifier,
            engine=engine,
            **kwargs)
        self._snapshots[db_snapshot_identifier] = record
        return record.to_dict()

    def describe_db_snapshots(self, db_snapshot_identifier=None,
                               db_instance_identifier=None,
                               snapshot_type=None):
        results = list(self._snapshots.values())
        if db_snapshot_identifier:
            results = [r for r in results
                       if r.db_snapshot_identifier == db_snapshot_identifier]
            if not results:
                raise DBSnapshotNotFoundFault(
                    f"DBSnapshot {db_snapshot_identifier} not found")
        if db_instance_identifier:
            results = [r for r in results
                       if r.db_instance_identifier == db_instance_identifier]
        if snapshot_type:
            results = [r for r in results
                       if r.snapshot_type == snapshot_type]
        return [r.to_dict() for r in results]

    def delete_db_snapshot(self, db_snapshot_identifier):
        if db_snapshot_identifier not in self._snapshots:
            raise DBSnapshotNotFoundFault(
                f"DBSnapshot {db_snapshot_identifier} not found")
        record = self._snapshots[db_snapshot_identifier]
        del self._snapshots[db_snapshot_identifier]
        return record.to_dict()

    # ── DB Parameter Group operations ───────────────────────────────

    def create_db_parameter_group(self, db_parameter_group_name,
                                   db_parameter_group_family, description,
                                   **kwargs):
        if db_parameter_group_name in self._param_groups:
            raise DBParameterGroupAlreadyExistsFault(
                f"DBParameterGroup {db_parameter_group_name} already exists")
        record = DBParameterGroupRecord(
            db_parameter_group_name=db_parameter_group_name,
            db_parameter_group_family=db_parameter_group_family,
            description=description,
            **kwargs)
        self._param_groups[db_parameter_group_name] = record
        return record.to_dict()

    def describe_db_parameter_groups(self, db_parameter_group_name=None):
        if db_parameter_group_name:
            if db_parameter_group_name not in self._param_groups:
                raise DBParameterGroupNotFoundFault(
                    f"DBParameterGroup {db_parameter_group_name} not found")
            return self._param_groups[db_parameter_group_name].to_dict()
        return [r.to_dict() for r in self._param_groups.values()]

    def modify_db_parameter_group(self, db_parameter_group_name, parameters):
        if db_parameter_group_name not in self._param_groups:
            raise DBParameterGroupNotFoundFault(
                f"DBParameterGroup {db_parameter_group_name} not found")
        return {'DBParameterGroupName': db_parameter_group_name}

    def delete_db_parameter_group(self, db_parameter_group_name):
        if db_parameter_group_name not in self._param_groups:
            raise DBParameterGroupNotFoundFault(
                f"DBParameterGroup {db_parameter_group_name} not found")
        del self._param_groups[db_parameter_group_name]
        return {}

    # ── DB Subnet Group operations ──────────────────────────────────

    def create_db_subnet_group(self, db_subnet_group_name,
                                db_subnet_group_description,
                                subnet_ids, **kwargs):
        if db_subnet_group_name in self._subnet_groups:
            raise DBSubnetGroupAlreadyExistsFault(
                f"DBSubnetGroup {db_subnet_group_name} already exists")
        record = DBSubnetGroupRecord(
            db_subnet_group_name=db_subnet_group_name,
            db_subnet_group_description=db_subnet_group_description,
            subnet_ids=subnet_ids,
            **kwargs)
        self._subnet_groups[db_subnet_group_name] = record
        return record.to_dict()

    def describe_db_subnet_groups(self, db_subnet_group_name=None):
        if db_subnet_group_name:
            if db_subnet_group_name not in self._subnet_groups:
                raise DBSubnetGroupNotFoundFault(
                    f"DBSubnetGroup {db_subnet_group_name} not found")
            return self._subnet_groups[db_subnet_group_name].to_dict()
        return [r.to_dict() for r in self._subnet_groups.values()]

    def delete_db_subnet_group(self, db_subnet_group_name):
        if db_subnet_group_name not in self._subnet_groups:
            raise DBSubnetGroupNotFoundFault(
                f"DBSubnetGroup {db_subnet_group_name} not found")
        del self._subnet_groups[db_subnet_group_name]
        return {}

    # ── DB Cluster Parameter Group operations ───────────────────────

    def create_db_cluster_parameter_group(self, db_cluster_parameter_group_name,
                                           db_parameter_group_family,
                                           description, **kwargs):
        if db_cluster_parameter_group_name in self._cluster_param_groups:
            raise DBParameterGroupAlreadyExistsFault(
                f"DBClusterParameterGroup {db_cluster_parameter_group_name} already exists")
        record = DBClusterParameterGroupRecord(
            db_cluster_parameter_group_name=db_cluster_parameter_group_name,
            db_parameter_group_family=db_parameter_group_family,
            description=description,
            **kwargs)
        self._cluster_param_groups[db_cluster_parameter_group_name] = record
        return record.to_dict()

    def describe_db_cluster_parameter_groups(self,
                                              db_cluster_parameter_group_name=None):
        if db_cluster_parameter_group_name:
            if db_cluster_parameter_group_name not in self._cluster_param_groups:
                raise DBClusterParameterGroupNotFoundFault(
                    f"DBClusterParameterGroup {db_cluster_parameter_group_name} not found")
            return self._cluster_param_groups[db_cluster_parameter_group_name].to_dict()
        return [r.to_dict() for r in self._cluster_param_groups.values()]

    def delete_db_cluster_parameter_group(self, db_cluster_parameter_group_name):
        if db_cluster_parameter_group_name not in self._cluster_param_groups:
            raise DBClusterParameterGroupNotFoundFault(
                f"DBClusterParameterGroup {db_cluster_parameter_group_name} not found")
        del self._cluster_param_groups[db_cluster_parameter_group_name]
        return {}

    # ── Tag operations ──────────────────────────────────────────────

    def add_tags_to_resource(self, resource_name, tags):
        """Add tags to an RDS resource (instance, cluster, snapshot, etc.)."""
        for coll_name, coll in [
            ('db', self._instances),
            ('cluster', self._clusters),
            ('snapshot', self._snapshots),
        ]:
            if resource_name in coll:
                record = coll[resource_name]
                existing_keys = {t.get('Key') for t in record.tags}
                for tag in tags:
                    if tag.get('Key') not in existing_keys:
                        record.tags.append(tag)
                return {}
        raise ResourceNotFoundException(
            f"Resource {resource_name} not found")

    def remove_tags_from_resource(self, resource_name, tag_keys):
        """Remove tags from an RDS resource."""
        for coll_name, coll in [
            ('db', self._instances),
            ('cluster', self._clusters),
            ('snapshot', self._snapshots),
        ]:
            if resource_name in coll:
                record = coll[resource_name]
                record.tags = [t for t in record.tags
                               if t.get('Key') not in tag_keys]
                return {}
        raise ResourceNotFoundException(
            f"Resource {resource_name} not found")

    def list_tags_for_resource(self, resource_name):
        """List tags for an RDS resource."""
        for coll_name, coll in [
            ('db', self._instances),
            ('cluster', self._clusters),
            ('snapshot', self._snapshots),
        ]:
            if resource_name in coll:
                return {'TagList': coll[resource_name].tags}
        raise ResourceNotFoundException(
            f"Resource {resource_name} not found")
