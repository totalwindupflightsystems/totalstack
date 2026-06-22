"""Redshift emulator store — clusters, parameter groups, snapshots, subnet groups, subscriptions."""
import uuid

# ─── Exceptions ───────────────────────────────────────────────────────────────

class ClusterNotFoundFault(Exception):
    pass

class ClusterAlreadyExistsFault(Exception):
    pass

class InvalidClusterStateFault(Exception):
    pass

class ClusterParameterGroupNotFoundFault(Exception):
    pass

class ClusterParameterGroupAlreadyExistsFault(Exception):
    pass

class ClusterParameterGroupQuotaExceededFault(Exception):
    pass

class InvalidClusterParameterGroupStateFault(Exception):
    pass

class ClusterSnapshotNotFoundFault(Exception):
    pass

class ClusterSnapshotAlreadyExistsFault(Exception):
    pass

class InvalidClusterSnapshotStateFault(Exception):
    pass

class ClusterSubnetGroupNotFoundFault(Exception):
    pass

class ClusterSubnetGroupAlreadyExistsFault(Exception):
    pass

class InvalidClusterSubnetGroupStateFault(Exception):
    pass

class ClusterSubnetQuotaExceededFault(Exception):
    pass

class InvalidClusterSubnetStateFault(Exception):
    pass

class SubscriptionNotFoundFault(Exception):
    pass

class SubscriptionAlreadyExistFault(Exception):
    pass

class EventSubscriptionQuotaExceededFault(Exception):
    pass

class SubscriptionCategoryNotFoundFault(Exception):
    pass

class SubscriptionEventIdNotFoundFault(Exception):
    pass

class SubscriptionSeverityNotFoundFault(Exception):
    pass

class SnapshotCopyAlreadyDisabledFault(Exception):
    pass


# ─── Record Classes ───────────────────────────────────────────────────────────

class ClusterRecord:
    def __init__(self, ClusterIdentifier, NodeType, MasterUsername,
                 ClusterType="single-node", DBName="dev",
                 MasterUserPassword=None, Port=None, ClusterParameterGroupName=None,
                 ClusterSubnetGroupName=None, ClusterVersion=None,
                 AllowVersionUpgrade=None, NumberOfNodes=None,
                 PubliclyAccessible=None, Encrypted=None, KmsKeyId=None,
                 EnhancedVpcRouting=None, AdditionalInfo=None,
                 IamRoles=None, Tags=None, VpcSecurityGroupIds=None,
                 AvailabilityZone=None, PreferredMaintenanceWindow=None,
                 AutomatedSnapshotRetentionPeriod=None, ManualSnapshotRetentionPeriod=None,
                 ClusterSecurityGroups=None, ElasticIp=None,
                 HsmClientCertificateIdentifier=None, HsmConfigurationIdentifier=None,
                 MaintenanceTrackName=None, SnapshotScheduleIdentifier=None,
                 AvailabilityZoneRelocation=None, AquaConfigurationStatus=None,
                 DefaultIamRoleArn=None, LoadSampleData=None, ManageMasterPassword=None,
                 MasterPasswordSecretKmsKeyId=None, IpAddressType=None, MultiAZ=None,
                 ExtraComputeForAutomaticOptimization=None, RedshiftIdcApplicationArn=None,
                 CatalogName=None):
        self.ClusterIdentifier = ClusterIdentifier
        self.NodeType = NodeType
        self.MasterUsername = MasterUsername
        self.ClusterType = ClusterType or "single-node"
        self.DBName = DBName or "dev"
        self.MasterUserPassword = MasterUserPassword
        self.Port = Port or 5439
        self.ClusterParameterGroupName = ClusterParameterGroupName
        self.ClusterSubnetGroupName = ClusterSubnetGroupName
        self.ClusterVersion = ClusterVersion or "1.0"
        self.AllowVersionUpgrade = AllowVersionUpgrade
        self.NumberOfNodes = NumberOfNodes or (1 if ClusterType == "single-node" else 2)
        self.PubliclyAccessible = PubliclyAccessible
        self.Encrypted = Encrypted
        self.KmsKeyId = KmsKeyId
        self.EnhancedVpcRouting = EnhancedVpcRouting
        self.AdditionalInfo = AdditionalInfo
        self.IamRoles = IamRoles or []
        self.Tags = Tags or []
        self.VpcSecurityGroupIds = VpcSecurityGroupIds or []
        self.AvailabilityZone = AvailabilityZone
        self.PreferredMaintenanceWindow = PreferredMaintenanceWindow
        self.AutomatedSnapshotRetentionPeriod = AutomatedSnapshotRetentionPeriod or 1
        self.ManualSnapshotRetentionPeriod = ManualSnapshotRetentionPeriod
        self.ClusterSecurityGroups = ClusterSecurityGroups or []
        self.ElasticIp = ElasticIp
        self.HsmClientCertificateIdentifier = HsmClientCertificateIdentifier
        self.HsmConfigurationIdentifier = HsmConfigurationIdentifier
        self.MaintenanceTrackName = MaintenanceTrackName
        self.SnapshotScheduleIdentifier = SnapshotScheduleIdentifier
        self.AvailabilityZoneRelocation = AvailabilityZoneRelocation
        self.AquaConfigurationStatus = AquaConfigurationStatus
        self.DefaultIamRoleArn = DefaultIamRoleArn
        self.LoadSampleData = LoadSampleData
        self.ManageMasterPassword = ManageMasterPassword
        self.MasterPasswordSecretKmsKeyId = MasterPasswordSecretKmsKeyId
        self.IpAddressType = IpAddressType
        self.MultiAZ = MultiAZ
        self.ExtraComputeForAutomaticOptimization = ExtraComputeForAutomaticOptimization
        self.RedshiftIdcApplicationArn = RedshiftIdcApplicationArn
        self.CatalogName = CatalogName
        # Synthetic fields
        self.ClusterStatus = "available"
        self.ClusterCreateTime = None
        self.Endpoint = None
        self.ClusterRevisionNumber = "1.0"
        self.ClusterPublicKey = None
        self.ClusterNodes = []
        self.Encrypted = Encrypted or False

    def to_dict(self):
        return {
            "ClusterIdentifier": self.ClusterIdentifier,
            "NodeType": self.NodeType,
            "ClusterStatus": self.ClusterStatus,
            "MasterUsername": self.MasterUsername,
            "DBName": self.DBName,
            "ClusterType": self.ClusterType,
            "ClusterVersion": self.ClusterVersion,
            "NumberOfNodes": self.NumberOfNodes,
            "Port": self.Port,
            "PubliclyAccessible": self.PubliclyAccessible,
            "Encrypted": self.Encrypted,
            "KmsKeyId": self.KmsKeyId,
            "EnhancedVpcRouting": self.EnhancedVpcRouting,
            "Tags": self.Tags,
            "IamRoles": self.IamRoles,
            "AvailabilityZone": self.AvailabilityZone,
            "PreferredMaintenanceWindow": self.PreferredMaintenanceWindow,
            "AutomatedSnapshotRetentionPeriod": self.AutomatedSnapshotRetentionPeriod,
            "ManualSnapshotRetentionPeriod": self.ManualSnapshotRetentionPeriod,
            "AllowVersionUpgrade": self.AllowVersionUpgrade,
            "ClusterParameterGroups": [{"ParameterGroupName": self.ClusterParameterGroupName, "ParameterApplyStatus": "in-sync"}] if self.ClusterParameterGroupName else [],
            "ClusterSubnetGroupName": self.ClusterSubnetGroupName,
            "VpcSecurityGroups": self.VpcSecurityGroupIds,
            "ClusterSecurityGroups": self.ClusterSecurityGroups,
            "MaintenanceTrackName": self.MaintenanceTrackName,
            "MultiAZ": self.MultiAZ,
            "IpAddressType": self.IpAddressType,
        }


class ClusterParameterGroupRecord:
    def __init__(self, ParameterGroupName, ParameterGroupFamily, Description, Tags=None):
        self.ParameterGroupName = ParameterGroupName
        self.ParameterGroupFamily = ParameterGroupFamily
        self.Description = Description
        self.Tags = Tags or []
        self.Parameters = {}

    def to_dict(self):
        return {
            "ParameterGroupName": self.ParameterGroupName,
            "ParameterGroupFamily": self.ParameterGroupFamily,
            "Description": self.Description,
            "Tags": self.Tags,
        }


class ClusterSnapshotRecord:
    def __init__(self, SnapshotIdentifier, ClusterIdentifier, SnapshotType="manual",
                 ManualSnapshotRetentionPeriod=None, Tags=None):
        self.SnapshotIdentifier = SnapshotIdentifier
        self.ClusterIdentifier = ClusterIdentifier
        self.SnapshotType = SnapshotType
        self.ManualSnapshotRetentionPeriod = ManualSnapshotRetentionPeriod
        self.Tags = Tags or []
        self.Status = "available"
        self.Port = 5439

    def to_dict(self):
        return {
            "SnapshotIdentifier": self.SnapshotIdentifier,
            "ClusterIdentifier": self.ClusterIdentifier,
            "SnapshotType": self.SnapshotType,
            "Status": self.Status,
            "Tags": self.Tags,
            "Port": self.Port,
        }


class ClusterSubnetGroupRecord:
    def __init__(self, ClusterSubnetGroupName, Description, SubnetIds, Tags=None, VpcId=None):
        self.ClusterSubnetGroupName = ClusterSubnetGroupName
        self.Description = Description
        self.SubnetIds = SubnetIds
        self.Tags = Tags or []
        self.VpcId = VpcId or "vpc-default"
        self.SubnetGroupStatus = "Complete"

    def to_dict(self):
        return {
            "ClusterSubnetGroupName": self.ClusterSubnetGroupName,
            "Description": self.Description,
            "Subnets": [{"SubnetIdentifier": sid, "SubnetAvailabilityZone": {"Name": "us-east-1a"}, "SubnetStatus": "Active"} for sid in self.SubnetIds],
            "SubnetGroupStatus": self.SubnetGroupStatus,
            "VpcId": self.VpcId,
            "Tags": self.Tags,
        }


class EventSubscriptionRecord:
    def __init__(self, SubscriptionName, SnsTopicArn, SourceType=None, SourceIds=None,
                 EventCategories=None, Severity=None, Enabled=True, Tags=None):
        self.SubscriptionName = SubscriptionName
        self.SnsTopicArn = SnsTopicArn
        self.SourceType = SourceType
        self.SourceIds = SourceIds or []
        self.EventCategories = EventCategories or []
        self.Severity = Severity
        self.Enabled = Enabled if Enabled is not None else True
        self.Tags = Tags or []
        self.CustSubscriptionId = str(uuid.uuid4())
        self.Status = "active"

    def to_dict(self):
        return {
            "CustSubscriptionId": self.CustSubscriptionId,
            "SubscriptionName": self.SubscriptionName,
            "SnsTopicArn": self.SnsTopicArn,
            "SourceType": self.SourceType,
            "SourceIds": self.SourceIds,
            "EventCategoriesList": self.EventCategories,
            "Severity": self.Severity,
            "Enabled": self.Enabled,
            "Status": self.Status,
            "Tags": self.Tags,
        }


# ─── RedshiftStore ────────────────────────────────────────────────────────────

class RedshiftStore:
    def __init__(self):
        self._clusters = {}
        self._parameter_groups = {}
        self._snapshots = {}
        self._subnet_groups = {}
        self._subscriptions = {}

    # ── Clusters ──────────────────────────────────────────────────────────

    def clusters(self, name=None):
        if name is not None:
            return self._clusters.get(name)
        return list(self._clusters.values())

    def create_cluster(self, ClusterIdentifier, NodeType, MasterUsername, **kwargs):
        if ClusterIdentifier in self._clusters:
            raise ClusterAlreadyExistsFault(f"Cluster {ClusterIdentifier} already exists")
        record = ClusterRecord(ClusterIdentifier, NodeType, MasterUsername, **kwargs)
        self._clusters[ClusterIdentifier] = record
        return record

    def describe_clusters(self, ClusterIdentifier=None, Marker=None, MaxRecords=None, **_kw):
        if ClusterIdentifier:
            record = self._clusters.get(ClusterIdentifier)
            if not record:
                raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
            return {"Clusters": [record.to_dict()]}
        all_clusters = list(self._clusters.values())
        return {"Clusters": [r.to_dict() for r in all_clusters], "Marker": None}

    def modify_cluster(self, ClusterIdentifier, **kwargs):
        record = self._clusters.get(ClusterIdentifier)
        if not record:
            raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
        if "NewClusterIdentifier" in kwargs:
            new_name = kwargs.pop("NewClusterIdentifier")
            record.ClusterIdentifier = new_name
            self._clusters[new_name] = record
            del self._clusters[ClusterIdentifier]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record

    def delete_cluster(self, ClusterIdentifier, SkipFinalClusterSnapshot=None,
                       FinalClusterSnapshotIdentifier=None,
                       FinalClusterSnapshotRetentionPeriod=None):
        record = self._clusters.get(ClusterIdentifier)
        if not record:
            raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
        if SkipFinalClusterSnapshot:
            pass  # skip creating final snapshot
        elif FinalClusterSnapshotIdentifier:
            self._snapshots[FinalClusterSnapshotIdentifier] = ClusterSnapshotRecord(
                FinalClusterSnapshotIdentifier, ClusterIdentifier, SnapshotType="manual",
                ManualSnapshotRetentionPeriod=FinalClusterSnapshotRetentionPeriod)
        del self._clusters[ClusterIdentifier]
        return record

    def pause_cluster(self, ClusterIdentifier):
        record = self._clusters.get(ClusterIdentifier)
        if not record:
            raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
        record.ClusterStatus = "paused"
        return record

    def resume_cluster(self, ClusterIdentifier):
        record = self._clusters.get(ClusterIdentifier)
        if not record:
            raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
        record.ClusterStatus = "available"
        return record

    def reboot_cluster(self, ClusterIdentifier):
        record = self._clusters.get(ClusterIdentifier)
        if not record:
            raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
        record.ClusterStatus = "rebooting"
        return record

    def resize_cluster(self, ClusterIdentifier, ClusterType=None, NodeType=None,
                       NumberOfNodes=None, **_kw):
        record = self._clusters.get(ClusterIdentifier)
        if not record:
            raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
        if ClusterType:
            record.ClusterType = ClusterType
        if NodeType:
            record.NodeType = NodeType
        if NumberOfNodes is not None:
            record.NumberOfNodes = NumberOfNodes
        return record

    # ── Parameter Groups ──────────────────────────────────────────────────

    def parameter_groups(self, name=None):
        if name is not None:
            return self._parameter_groups.get(name)
        return list(self._parameter_groups.values())

    def create_cluster_parameter_group(self, ParameterGroupName, ParameterGroupFamily,
                                       Description, Tags=None):
        if ParameterGroupName in self._parameter_groups:
            raise ClusterParameterGroupAlreadyExistsFault(
                f"Parameter group {ParameterGroupName} already exists")
        record = ClusterParameterGroupRecord(
            ParameterGroupName, ParameterGroupFamily, Description, Tags=Tags)
        self._parameter_groups[ParameterGroupName] = record
        return record

    def describe_cluster_parameter_groups(self, ParameterGroupName=None, **_kw):
        if ParameterGroupName:
            record = self._parameter_groups.get(ParameterGroupName)
            if not record:
                raise ClusterParameterGroupNotFoundFault(
                    f"Parameter group {ParameterGroupName} not found")
            return {"ParameterGroups": [record.to_dict()]}
        all_pgs = list(self._parameter_groups.values())
        return {"ParameterGroups": [r.to_dict() for r in all_pgs], "Marker": None}

    def modify_cluster_parameter_group(self, ParameterGroupName, Parameters):
        record = self._parameter_groups.get(ParameterGroupName)
        if not record:
            raise ClusterParameterGroupNotFoundFault(
                f"Parameter group {ParameterGroupName} not found")
        if isinstance(Parameters, list):
            for p in Parameters:
                if isinstance(p, dict):
                    name = p.get("ParameterName")
                    value = p.get("ParameterValue")
                    if name:
                        record.Parameters[name] = value
        return {
            "ParameterGroupName": ParameterGroupName,
            "ParameterGroupStatus": "in-sync"
        }

    def delete_cluster_parameter_group(self, ParameterGroupName):
        if ParameterGroupName not in self._parameter_groups:
            raise ClusterParameterGroupNotFoundFault(
                f"Parameter group {ParameterGroupName} not found")
        del self._parameter_groups[ParameterGroupName]

    def reset_cluster_parameter_group(self, ParameterGroupName, Parameters=None,
                                      ResetAllParameters=None, **_kw):
        record = self._parameter_groups.get(ParameterGroupName)
        if not record:
            raise ClusterParameterGroupNotFoundFault(
                f"Parameter group {ParameterGroupName} not found")
        if ResetAllParameters:
            record.Parameters = {}
        elif Parameters and isinstance(Parameters, list):
            for p in Parameters:
                if isinstance(p, dict) and "ParameterName" in p:
                    name = p["ParameterName"]
                    if name in record.Parameters:
                        del record.Parameters[name]
        return {
            "ParameterGroupName": ParameterGroupName,
            "ParameterGroupStatus": "in-sync"
        }

    # ── Snapshots ─────────────────────────────────────────────────────────

    def snapshots(self, name=None):
        if name is not None:
            return self._snapshots.get(name)
        return list(self._snapshots.values())

    def create_cluster_snapshot(self, SnapshotIdentifier, ClusterIdentifier,
                                ManualSnapshotRetentionPeriod=None, Tags=None):
        if ClusterIdentifier not in self._clusters:
            raise ClusterNotFoundFault(f"Cluster {ClusterIdentifier} not found")
        if SnapshotIdentifier in self._snapshots:
            raise ClusterSnapshotAlreadyExistsFault(
                f"Snapshot {SnapshotIdentifier} already exists")
        record = ClusterSnapshotRecord(
            SnapshotIdentifier, ClusterIdentifier,
            ManualSnapshotRetentionPeriod=ManualSnapshotRetentionPeriod, Tags=Tags)
        self._snapshots[SnapshotIdentifier] = record
        return record

    def describe_cluster_snapshots(self, SnapshotIdentifier=None,
                                   ClusterIdentifier=None, **_kw):
        results = list(self._snapshots.values())
        if SnapshotIdentifier:
            record = self._snapshots.get(SnapshotIdentifier)
            if not record:
                raise ClusterSnapshotNotFoundFault(
                    f"Snapshot {SnapshotIdentifier} not found")
            results = [record]
        elif ClusterIdentifier:
            results = [s for s in results if s.ClusterIdentifier == ClusterIdentifier]
        return {"Snapshots": [r.to_dict() for r in results], "Marker": None}

    def delete_cluster_snapshot(self, SnapshotIdentifier, **_kw):
        if SnapshotIdentifier not in self._snapshots:
            raise ClusterSnapshotNotFoundFault(
                f"Snapshot {SnapshotIdentifier} not found")
        record = self._snapshots.pop(SnapshotIdentifier)
        return record

    def copy_cluster_snapshot(self, SourceSnapshotIdentifier,
                              TargetSnapshotIdentifier,
                              ManualSnapshotRetentionPeriod=None, **_kw):
        if SourceSnapshotIdentifier not in self._snapshots:
            raise ClusterSnapshotNotFoundFault(
                f"Snapshot {SourceSnapshotIdentifier} not found")
        source = self._snapshots[SourceSnapshotIdentifier]
        new_rec = ClusterSnapshotRecord(
            TargetSnapshotIdentifier, source.ClusterIdentifier,
            SnapshotType="manual",
            ManualSnapshotRetentionPeriod=ManualSnapshotRetentionPeriod)
        self._snapshots[TargetSnapshotIdentifier] = new_rec
        return new_rec

    # ── Subnet Groups ─────────────────────────────────────────────────────

    def subnet_groups(self, name=None):
        if name is not None:
            return self._subnet_groups.get(name)
        return list(self._subnet_groups.values())

    def create_cluster_subnet_group(self, ClusterSubnetGroupName, Description,
                                    SubnetIds, Tags=None):
        if ClusterSubnetGroupName in self._subnet_groups:
            raise ClusterSubnetGroupAlreadyExistsFault(
                f"Subnet group {ClusterSubnetGroupName} already exists")
        record = ClusterSubnetGroupRecord(
            ClusterSubnetGroupName, Description, SubnetIds, Tags=Tags)
        self._subnet_groups[ClusterSubnetGroupName] = record
        return record

    def describe_cluster_subnet_groups(self, ClusterSubnetGroupName=None, **_kw):
        if ClusterSubnetGroupName:
            record = self._subnet_groups.get(ClusterSubnetGroupName)
            if not record:
                raise ClusterSubnetGroupNotFoundFault(
                    f"Subnet group {ClusterSubnetGroupName} not found")
            return {"ClusterSubnetGroups": [record.to_dict()]}
        all_sgs = list(self._subnet_groups.values())
        return {"ClusterSubnetGroups": [r.to_dict() for r in all_sgs], "Marker": None}

    def modify_cluster_subnet_group(self, ClusterSubnetGroupName, SubnetIds,
                                    Description=None):
        record = self._subnet_groups.get(ClusterSubnetGroupName)
        if not record:
            raise ClusterSubnetGroupNotFoundFault(
                f"Subnet group {ClusterSubnetGroupName} not found")
        record.SubnetIds = SubnetIds
        if Description:
            record.Description = Description
        return record

    def delete_cluster_subnet_group(self, ClusterSubnetGroupName):
        if ClusterSubnetGroupName not in self._subnet_groups:
            raise ClusterSubnetGroupNotFoundFault(
                f"Subnet group {ClusterSubnetGroupName} not found")
        del self._subnet_groups[ClusterSubnetGroupName]

    # ── Event Subscriptions ───────────────────────────────────────────────

    def subscriptions(self, name=None):
        if name is not None:
            return self._subscriptions.get(name)
        return list(self._subscriptions.values())

    def create_event_subscription(self, SubscriptionName, SnsTopicArn, **kwargs):
        if SubscriptionName in self._subscriptions:
            raise SubscriptionAlreadyExistFault(
                f"Subscription {SubscriptionName} already exists")
        record = EventSubscriptionRecord(SubscriptionName, SnsTopicArn, **kwargs)
        self._subscriptions[SubscriptionName] = record
        return record

    def describe_event_subscriptions(self, SubscriptionName=None, **_kw):
        if SubscriptionName:
            record = self._subscriptions.get(SubscriptionName)
            if not record:
                raise SubscriptionNotFoundFault(
                    f"Subscription {SubscriptionName} not found")
            return {"EventSubscriptionsList": [record.to_dict()]}
        all_subs = list(self._subscriptions.values())
        return {"EventSubscriptionsList": [r.to_dict() for r in all_subs], "Marker": None}

    def modify_event_subscription(self, SubscriptionName, **kwargs):
        record = self._subscriptions.get(SubscriptionName)
        if not record:
            raise SubscriptionNotFoundFault(
                f"Subscription {SubscriptionName} not found")
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record

    def delete_event_subscription(self, SubscriptionName):
        if SubscriptionName not in self._subscriptions:
            raise SubscriptionNotFoundFault(
                f"Subscription {SubscriptionName} not found")
        del self._subscriptions[SubscriptionName]
