"""DocumentDB store — MongoDB wire-protocol compatible document database.

Entities:
- DBCluster: The main cluster resource (engine=docdb, storage, networking)
- DBInstance: Individual instances within a cluster (compute nodes)
- DBSubnetGroup: Subnet configuration for VPC networking
- DBClusterSnapshot: Point-in-time snapshots of a cluster
- DBClusterParameterGroup: Configuration parameter groups
"""

import uuid
import time
from collections import defaultdict


# =============================================================================
# Exception Classes
# =============================================================================

class InvalidParameterException(Exception):
    """Invalid parameter value."""
    pass


class ResourceNotFoundException(Exception):
    """Resource not found."""
    pass


class DBClusterNotFoundException(ResourceNotFoundException):
    """Cluster not found."""
    pass


class DBInstanceNotFoundException(ResourceNotFoundException):
    """Instance not found."""
    pass


class DBSubnetGroupNotFoundException(ResourceNotFoundException):
    """Subnet group not found."""
    pass


class DBClusterSnapshotNotFoundException(ResourceNotFoundException):
    """Snapshot not found."""
    pass


class DBClusterParameterGroupNotFoundException(ResourceNotFoundException):
    """Parameter group not found."""
    pass


class DBClusterAlreadyExistsException(Exception):
    """Cluster with this identifier already exists."""
    pass


class DBInstanceAlreadyExistsException(Exception):
    """Instance with this identifier already exists."""
    pass


class DBSubnetGroupAlreadyExistsException(Exception):
    """Subnet group with this name already exists."""
    pass


class DBClusterSnapshotAlreadyExistsException(Exception):
    """Snapshot with this identifier already exists."""
    pass


class DBParameterGroupAlreadyExistsException(Exception):
    """Parameter group with this name already exists."""
    pass


class InvalidDBClusterStateException(Exception):
    """Cluster is in an invalid state for this operation."""
    pass


class InvalidDBInstanceStateException(Exception):
    """Instance is in an invalid state for this operation."""
    pass


class SnapshotQuotaExceededException(Exception):
    """Snapshot quota exceeded."""
    pass


class DBParameterGroupQuotaExceededException(Exception):
    """Parameter group quota exceeded."""
    pass


class InternalServerException(Exception):
    """Internal server error."""
    pass


# =============================================================================
# Record Classes
# =============================================================================

class ClusterRecord:
    """Record for a DocumentDB cluster."""

    def __init__(self, DBClusterIdentifier, Engine, **kwargs):
        self.DBClusterIdentifier = DBClusterIdentifier
        self.Engine = Engine
        self.Status = kwargs.get('Status', 'available')
        self.DBClusterArn = kwargs.get('DBClusterArn', f'arn:aws:rds:us-east-1:000000000000:cluster:{DBClusterIdentifier}')
        self.DBClusterResourceId = kwargs.get('DBClusterResourceId', f'cluster-{str(uuid.uuid4())[:22]}')
        self.Endpoint = kwargs.get('Endpoint', f'{DBClusterIdentifier}.cluster-docdb.us-east-1.docdb.amazonaws.com')
        self.ReaderEndpoint = kwargs.get('ReaderEndpoint', f'{DBClusterIdentifier}.cluster-ro-docdb.us-east-1.docdb.amazonaws.com')
        self.Port = kwargs.get('Port', 27017)
        self.MasterUsername = kwargs.get('MasterUsername', 'admin')
        self.PreferredBackupWindow = kwargs.get('PreferredBackupWindow', '02:00-03:00')
        self.PreferredMaintenanceWindow = kwargs.get('PreferredMaintenanceWindow', 'sun:05:00-sun:06:00')
        self.BackupRetentionPeriod = kwargs.get('BackupRetentionPeriod', 1)
        self.DBClusterMembers = kwargs.get('DBClusterMembers', [])
        self.VpcSecurityGroups = kwargs.get('VpcSecurityGroups', [])
        self.AvailabilityZones = kwargs.get('AvailabilityZones', [])
        self.DBSubnetGroup = kwargs.get('DBSubnetGroup', 'default')
        self.EarliestRestorableTime = kwargs.get('EarliestRestorableTime', None)
        self.LatestRestorableTime = kwargs.get('LatestRestorableTime', None)
        self.StorageEncrypted = kwargs.get('StorageEncrypted', False)
        self.DeletionProtection = kwargs.get('DeletionProtection', False)
        self.ClusterCreateTime = kwargs.get('ClusterCreateTime', time.time())
        self.EnabledCloudwatchLogsExports = kwargs.get('EnabledCloudwatchLogsExports', [])
        self.DBClusterParameterGroup = kwargs.get('DBClusterParameterGroup', 'default.docdb5.0')

    def to_dict(self):
        return self.__dict__


class InstanceRecord:
    """Record for a DocumentDB instance."""

    def __init__(self, DBInstanceIdentifier, DBClusterIdentifier, DBInstanceClass, Engine, **kwargs):
        self.DBInstanceIdentifier = DBInstanceIdentifier
        self.DBClusterIdentifier = DBClusterIdentifier
        self.DBInstanceClass = DBInstanceClass
        self.Engine = Engine
        self.DBInstanceStatus = kwargs.get('DBInstanceStatus', 'available')
        self.DBInstanceArn = kwargs.get('DBInstanceArn', f'arn:aws:rds:us-east-1:000000000000:db:{DBInstanceIdentifier}')
        self.Endpoint = kwargs.get('Endpoint', {'Address': f'{DBInstanceIdentifier}.docdb.us-east-1.docdb.amazonaws.com', 'Port': 27017})
        self.AvailabilityZone = kwargs.get('AvailabilityZone', 'us-east-1a')
        self.PreferredBackupWindow = kwargs.get('PreferredBackupWindow', '02:00-03:00')
        self.PreferredMaintenanceWindow = kwargs.get('PreferredMaintenanceWindow', 'sun:05:00-sun:06:00')
        self.StorageEncrypted = kwargs.get('StorageEncrypted', False)
        self.CACertificateIdentifier = kwargs.get('CACertificateIdentifier', 'rds-ca-2019')
        self.PromotionTier = kwargs.get('PromotionTier', 1)
        self.AutoMinorVersionUpgrade = kwargs.get('AutoMinorVersionUpgrade', True)
        self.CopyTagsToSnapshot = kwargs.get('CopyTagsToSnapshot', False)
        self.PubliclyAccessible = kwargs.get('PubliclyAccessible', False)
        self.InstanceCreateTime = kwargs.get('InstanceCreateTime', time.time())

    def to_dict(self):
        return self.__dict__


class SubnetGroupRecord:
    """Record for a DocumentDB subnet group."""

    def __init__(self, DBSubnetGroupName, DBSubnetGroupDescription, SubnetIds, **kwargs):
        self.DBSubnetGroupName = DBSubnetGroupName
        self.DBSubnetGroupDescription = DBSubnetGroupDescription
        self.SubnetIds = SubnetIds
        self.Subnets = kwargs.get('Subnets', [{'SubnetIdentifier': sid} for sid in SubnetIds])
        self.DBSubnetGroupArn = kwargs.get('DBSubnetGroupArn', f'arn:aws:rds:us-east-1:000000000000:subgrp:{DBSubnetGroupName}')
        self.VpcId = kwargs.get('VpcId', 'vpc-default')
        self.SubnetGroupStatus = kwargs.get('SubnetGroupStatus', 'Complete')

    def to_dict(self):
        return self.__dict__


class SnapshotRecord:
    """Record for a DocumentDB cluster snapshot."""

    def __init__(self, DBClusterSnapshotIdentifier, DBClusterIdentifier, **kwargs):
        self.DBClusterSnapshotIdentifier = DBClusterSnapshotIdentifier
        self.DBClusterIdentifier = DBClusterIdentifier
        self.DBClusterSnapshotArn = kwargs.get('DBClusterSnapshotArn', f'arn:aws:rds:us-east-1:000000000000:cluster-snapshot:{DBClusterSnapshotIdentifier}')
        self.SnapshotType = kwargs.get('SnapshotType', 'manual')
        self.Engine = kwargs.get('Engine', 'docdb')
        self.EngineVersion = kwargs.get('EngineVersion', '5.0.0')
        self.Status = kwargs.get('Status', 'available')
        self.PercentProgress = kwargs.get('PercentProgress', 100)
        self.ClusterCreateTime = kwargs.get('ClusterCreateTime', time.time())
        self.SnapshotCreateTime = kwargs.get('SnapshotCreateTime', time.time())
        self.Port = kwargs.get('Port', 27017)
        self.AvailabilityZones = kwargs.get('AvailabilityZones', [])
        self.VpcId = kwargs.get('VpcId', 'vpc-default')
        self.StorageEncrypted = kwargs.get('StorageEncrypted', False)
        self.MasterUsername = kwargs.get('MasterUsername', 'admin')

    def to_dict(self):
        return self.__dict__


class ParameterGroupRecord:
    """Record for a DocumentDB cluster parameter group."""

    def __init__(self, DBClusterParameterGroupName, DBParameterGroupFamily, Description, **kwargs):
        self.DBClusterParameterGroupName = DBClusterParameterGroupName
        self.DBParameterGroupFamily = DBParameterGroupFamily
        self.Description = Description
        self.DBClusterParameterGroupArn = kwargs.get('DBClusterParameterGroupArn', f'arn:aws:rds:us-east-1:000000000000:cluster-pg:{DBClusterParameterGroupName}')
        self.Parameters = kwargs.get('Parameters', [])

    def to_dict(self):
        return self.__dict__


# =============================================================================
# DocumentDB Store
# =============================================================================

class DocumentDBStore:
    """In-memory store for DocumentDB resources.

    All internal storage uses _prefixed dicts. Public accessors are methods
    so generated handlers can call store.clusters(id) as a method.
    """

    def __init__(self):
        self._clusters: dict[str, ClusterRecord] = {}
        self._instances: dict[str, InstanceRecord] = {}
        self._subnet_groups: dict[str, SubnetGroupRecord] = {}
        self._snapshots: dict[str, SnapshotRecord] = {}
        self._parameter_groups: dict[str, ParameterGroupRecord] = {}

    # ---- Cluster accessors ----

    def clusters(self, DBClusterIdentifier=None):
        if DBClusterIdentifier is not None:
            return self._clusters.get(DBClusterIdentifier)
        return list(self._clusters.values())

    # ---- Instance accessors ----

    def instances(self, DBInstanceIdentifier=None):
        if DBInstanceIdentifier is not None:
            return self._instances.get(DBInstanceIdentifier)
        return list(self._instances.values())

    # ---- Subnet group accessors ----

    def subnet_groups(self, DBSubnetGroupName=None):
        if DBSubnetGroupName is not None:
            return self._subnet_groups.get(DBSubnetGroupName)
        return list(self._subnet_groups.values())

    # ---- Snapshot accessors ----

    def snapshots(self, DBClusterSnapshotIdentifier=None):
        if DBClusterSnapshotIdentifier is not None:
            return self._snapshots.get(DBClusterSnapshotIdentifier)
        return list(self._snapshots.values())

    # ---- Parameter group accessors ----

    def parameter_groups(self, DBClusterParameterGroupName=None):
        if DBClusterParameterGroupName is not None:
            return self._parameter_groups.get(DBClusterParameterGroupName)
        return list(self._parameter_groups.values())

    # ===== Cluster CRUD =====

    def create_cluster(self, DBClusterIdentifier, Engine, **kwargs):
        if DBClusterIdentifier in self._clusters:
            raise DBClusterAlreadyExistsException(f"Cluster {DBClusterIdentifier} already exists")
        record = ClusterRecord(DBClusterIdentifier, Engine, **kwargs)
        self._clusters[DBClusterIdentifier] = record
        return {'DBCluster': record.to_dict()}

    def describe_clusters(self, DBClusterIdentifier=None, **kwargs):
        if DBClusterIdentifier:
            record = self._clusters.get(DBClusterIdentifier)
            if not record:
                raise DBClusterNotFoundException(f"Cluster {DBClusterIdentifier} not found")
            return {'DBClusters': [record.to_dict()]}
        return {'DBClusters': [r.to_dict() for r in self._clusters.values()]}

    def modify_cluster(self, DBClusterIdentifier, **kwargs):
        record = self._clusters.get(DBClusterIdentifier)
        if not record:
            raise DBClusterNotFoundException(f"Cluster {DBClusterIdentifier} not found")
        for key, value in kwargs.items():
            if hasattr(record, key):
                setattr(record, key, value)
        return {'DBCluster': record.to_dict()}

    def delete_cluster(self, DBClusterIdentifier, **kwargs):
        record = self._clusters.get(DBClusterIdentifier)
        if not record:
            raise DBClusterNotFoundException(f"Cluster {DBClusterIdentifier} not found")
        if record.DeletionProtection:
            raise InvalidDBClusterStateException("Cannot delete cluster with deletion protection enabled")
        del self._clusters[DBClusterIdentifier]
        return {'DBCluster': record.to_dict()}

    def start_cluster(self, DBClusterIdentifier):
        record = self._clusters.get(DBClusterIdentifier)
        if not record:
            raise DBClusterNotFoundException(f"Cluster {DBClusterIdentifier} not found")
        record.Status = 'available'
        return {'DBCluster': record.to_dict()}

    def stop_cluster(self, DBClusterIdentifier):
        record = self._clusters.get(DBClusterIdentifier)
        if not record:
            raise DBClusterNotFoundException(f"Cluster {DBClusterIdentifier} not found")
        record.Status = 'stopped'
        return {'DBCluster': record.to_dict()}

    # ===== Instance CRUD =====

    def create_instance(self, DBInstanceIdentifier, DBClusterIdentifier, DBInstanceClass, Engine, **kwargs):
        if DBInstanceIdentifier in self._instances:
            raise DBInstanceAlreadyExistsException(f"Instance {DBInstanceIdentifier} already exists")
        if DBClusterIdentifier not in self._clusters:
            raise DBClusterNotFoundException(f"Cluster {DBClusterIdentifier} not found")
        record = InstanceRecord(DBInstanceIdentifier, DBClusterIdentifier, DBInstanceClass, Engine, **kwargs)
        self._instances[DBInstanceIdentifier] = record
        return {'DBInstance': record.to_dict()}

    def describe_instances(self, DBInstanceIdentifier=None, **kwargs):
        if DBInstanceIdentifier:
            record = self._instances.get(DBInstanceIdentifier)
            if not record:
                raise DBInstanceNotFoundException(f"Instance {DBInstanceIdentifier} not found")
            return {'DBInstances': [record.to_dict()]}
        return {'DBInstances': [r.to_dict() for r in self._instances.values()]}

    def modify_instance(self, DBInstanceIdentifier, **kwargs):
        record = self._instances.get(DBInstanceIdentifier)
        if not record:
            raise DBInstanceNotFoundException(f"Instance {DBInstanceIdentifier} not found")
        for key, value in kwargs.items():
            if hasattr(record, key):
                setattr(record, key, value)
        return {'DBInstance': record.to_dict()}

    def delete_instance(self, DBInstanceIdentifier):
        record = self._instances.get(DBInstanceIdentifier)
        if not record:
            raise DBInstanceNotFoundException(f"Instance {DBInstanceIdentifier} not found")
        del self._instances[DBInstanceIdentifier]
        return {'DBInstance': record.to_dict()}

    def reboot_instance(self, DBInstanceIdentifier):
        record = self._instances.get(DBInstanceIdentifier)
        if not record:
            raise DBInstanceNotFoundException(f"Instance {DBInstanceIdentifier} not found")
        record.DBInstanceStatus = 'rebooting'
        return {'DBInstance': record.to_dict()}

    # ===== Subnet Group CRUD =====

    def create_subnet_group(self, DBSubnetGroupName, DBSubnetGroupDescription, SubnetIds, **kwargs):
        if DBSubnetGroupName in self._subnet_groups:
            raise DBSubnetGroupAlreadyExistsException(f"Subnet group {DBSubnetGroupName} already exists")
        record = SubnetGroupRecord(DBSubnetGroupName, DBSubnetGroupDescription, SubnetIds, **kwargs)
        self._subnet_groups[DBSubnetGroupName] = record
        return {'DBSubnetGroup': record.to_dict()}

    def describe_subnet_groups(self, DBSubnetGroupName=None, **kwargs):
        if DBSubnetGroupName:
            record = self._subnet_groups.get(DBSubnetGroupName)
            if not record:
                raise DBSubnetGroupNotFoundException(f"Subnet group {DBSubnetGroupName} not found")
            return {'DBSubnetGroups': [record.to_dict()]}
        return {'DBSubnetGroups': [r.to_dict() for r in self._subnet_groups.values()]}

    def modify_subnet_group(self, DBSubnetGroupName, **kwargs):
        record = self._subnet_groups.get(DBSubnetGroupName)
        if not record:
            raise DBSubnetGroupNotFoundException(f"Subnet group {DBSubnetGroupName} not found")
        for key, value in kwargs.items():
            if hasattr(record, key):
                setattr(record, key, value)
        return {'DBSubnetGroup': record.to_dict()}

    def delete_subnet_group(self, DBSubnetGroupName):
        record = self._subnet_groups.get(DBSubnetGroupName)
        if not record:
            raise DBSubnetGroupNotFoundException(f"Subnet group {DBSubnetGroupName} not found")
        del self._subnet_groups[DBSubnetGroupName]
        return {}

    # ===== Snapshot CRUD =====

    def create_snapshot(self, DBClusterSnapshotIdentifier, DBClusterIdentifier, **kwargs):
        if DBClusterSnapshotIdentifier in self._snapshots:
            raise DBClusterSnapshotAlreadyExistsException(f"Snapshot {DBClusterSnapshotIdentifier} already exists")
        if DBClusterIdentifier not in self._clusters:
            raise DBClusterNotFoundException(f"Cluster {DBClusterIdentifier} not found")
        record = SnapshotRecord(DBClusterSnapshotIdentifier, DBClusterIdentifier, **kwargs)
        self._snapshots[DBClusterSnapshotIdentifier] = record
        return {'DBClusterSnapshot': record.to_dict()}

    def describe_snapshots(self, DBClusterSnapshotIdentifier=None, DBClusterIdentifier=None, **kwargs):
        if DBClusterSnapshotIdentifier:
            record = self._snapshots.get(DBClusterSnapshotIdentifier)
            if not record:
                raise DBClusterSnapshotNotFoundException(f"Snapshot {DBClusterSnapshotIdentifier} not found")
            return {'DBClusterSnapshots': [record.to_dict()]}
        results = list(self._snapshots.values())
        if DBClusterIdentifier:
            results = [r for r in results if r.DBClusterIdentifier == DBClusterIdentifier]
        return {'DBClusterSnapshots': [r.to_dict() for r in results]}

    def delete_snapshot(self, DBClusterSnapshotIdentifier):
        record = self._snapshots.get(DBClusterSnapshotIdentifier)
        if not record:
            raise DBClusterSnapshotNotFoundException(f"Snapshot {DBClusterSnapshotIdentifier} not found")
        del self._snapshots[DBClusterSnapshotIdentifier]
        return {'DBClusterSnapshot': record.to_dict()}

    def copy_snapshot(self, SourceDBClusterSnapshotIdentifier, TargetDBClusterSnapshotIdentifier, **kwargs):
        if TargetDBClusterSnapshotIdentifier in self._snapshots:
            raise DBClusterSnapshotAlreadyExistsException(f"Snapshot {TargetDBClusterSnapshotIdentifier} already exists")
        source = self._snapshots.get(SourceDBClusterSnapshotIdentifier)
        if not source:
            raise DBClusterSnapshotNotFoundException(f"Snapshot {SourceDBClusterSnapshotIdentifier} not found")
        record = SnapshotRecord(
            TargetDBClusterSnapshotIdentifier,
            source.DBClusterIdentifier,
            Engine=source.Engine,
            EngineVersion=source.EngineVersion,
            Port=source.Port,
            AvailabilityZones=source.AvailabilityZones,
            VpcId=source.VpcId,
            StorageEncrypted=source.StorageEncrypted,
            MasterUsername=source.MasterUsername,
            SnapshotType='manual',
            **kwargs,
        )
        self._snapshots[TargetDBClusterSnapshotIdentifier] = record
        return {'DBClusterSnapshot': record.to_dict()}

    def restore_cluster_from_snapshot(self, DBClusterIdentifier, DBClusterSnapshotIdentifier, Engine, **kwargs):
        if DBClusterIdentifier in self._clusters:
            raise DBClusterAlreadyExistsException(f"Cluster {DBClusterIdentifier} already exists")
        snapshot = self._snapshots.get(DBClusterSnapshotIdentifier)
        if not snapshot:
            raise DBClusterSnapshotNotFoundException(f"Snapshot {DBClusterSnapshotIdentifier} not found")
        record = ClusterRecord(
            DBClusterIdentifier=DBClusterIdentifier,
            Engine=Engine,
            EngineVersion=snapshot.EngineVersion,
            Port=snapshot.Port,
            AvailabilityZones=snapshot.AvailabilityZones,
            StorageEncrypted=snapshot.StorageEncrypted,
            MasterUsername=snapshot.MasterUsername,
            **kwargs,
        )
        self._clusters[DBClusterIdentifier] = record
        return {'DBCluster': record.to_dict()}

    # ===== Parameter Group CRUD =====

    def create_parameter_group(self, DBClusterParameterGroupName, DBParameterGroupFamily, Description, **kwargs):
        if DBClusterParameterGroupName in self._parameter_groups:
            raise DBParameterGroupAlreadyExistsException(f"Parameter group {DBClusterParameterGroupName} already exists")
        record = ParameterGroupRecord(DBClusterParameterGroupName, DBParameterGroupFamily, Description, **kwargs)
        self._parameter_groups[DBClusterParameterGroupName] = record
        return {'DBClusterParameterGroup': record.to_dict()}

    def describe_parameter_groups(self, DBClusterParameterGroupName=None, **kwargs):
        if DBClusterParameterGroupName:
            record = self._parameter_groups.get(DBClusterParameterGroupName)
            if not record:
                raise DBClusterParameterGroupNotFoundException(f"Parameter group {DBClusterParameterGroupName} not found")
            return {'DBClusterParameterGroups': [record.to_dict()]}
        return {'DBClusterParameterGroups': [r.to_dict() for r in self._parameter_groups.values()]}

    def modify_parameter_group(self, DBClusterParameterGroupName, Parameters, **kwargs):
        record = self._parameter_groups.get(DBClusterParameterGroupName)
        if not record:
            raise DBClusterParameterGroupNotFoundException(f"Parameter group {DBClusterParameterGroupName} not found")
        # Merge parameters
        existing = {p.get('ParameterName'): p for p in record.Parameters}
        for param in Parameters:
            name = param.get('ParameterName')
            if name:
                existing[name] = param
        record.Parameters = list(existing.values())
        return {'DBClusterParameterGroupName': DBClusterParameterGroupName}

    def delete_parameter_group(self, DBClusterParameterGroupName):
        record = self._parameter_groups.get(DBClusterParameterGroupName)
        if not record:
            raise DBClusterParameterGroupNotFoundException(f"Parameter group {DBClusterParameterGroupName} not found")
        del self._parameter_groups[DBClusterParameterGroupName]
        return {}

    def reset_parameter_group(self, DBClusterParameterGroupName, Parameters=None, **kwargs):
        record = self._parameter_groups.get(DBClusterParameterGroupName)
        if not record:
            raise DBClusterParameterGroupNotFoundException(f"Parameter group {DBClusterParameterGroupName} not found")
        if Parameters:
            # Reset only specific parameters (remove them so defaults apply)
            names = {p.get('ParameterName') for p in Parameters if p.get('ParameterName')}
            record.Parameters = [p for p in record.Parameters if p.get('ParameterName') not in names]
        else:
            record.Parameters = []
        return {'DBClusterParameterGroupName': DBClusterParameterGroupName}
