"""MemoryDB Store — durable Redis-compatible in-memory database.

Entities: Cluster, ACL, User, ParameterGroup, SubnetGroup, Snapshot.
All store methods accept CamelCase field names as kwargs matching AWS API.
"""



# ── Exception classes ──────────────────────────────────────────────

class MemoryDBException(Exception):
    """Base exception for MemoryDB."""


class ClusterAlreadyExistsFault(MemoryDBException):
    """Cluster already exists."""


class ClusterNotFoundFault(MemoryDBException):
    """Cluster not found."""


class ClusterQuotaForCustomerExceededFault(MemoryDBException):
    """Cluster quota exceeded."""


class ACLAlreadyExistsFault(MemoryDBException):
    """ACL already exists."""


class ACLNotFoundFault(MemoryDBException):
    """ACL not found."""


class ACLQuotaExceededFault(MemoryDBException):
    """ACL quota exceeded."""


class UserAlreadyExistsFault(MemoryDBException):
    """User already exists."""


class UserNotFoundFault(MemoryDBException):
    """User not found."""


class UserQuotaExceededFault(MemoryDBException):
    """User quota exceeded."""


class ParameterGroupAlreadyExistsFault(MemoryDBException):
    """Parameter group already exists."""


class ParameterGroupNotFoundFault(MemoryDBException):
    """Parameter group not found."""


class ParameterGroupQuotaExceededFault(MemoryDBException):
    """Parameter group quota exceeded."""


class SubnetGroupAlreadyExistsFault(MemoryDBException):
    """Subnet group already exists."""


class SubnetGroupNotFoundFault(MemoryDBException):
    """Subnet group not found."""


class SubnetGroupQuotaExceededFault(MemoryDBException):
    """Subnet group quota exceeded."""


class SnapshotAlreadyExistsFault(MemoryDBException):
    """Snapshot already exists."""


class SnapshotNotFoundFault(MemoryDBException):
    """Snapshot not found."""


class SnapshotQuotaExceededFault(MemoryDBException):
    """Snapshot quota exceeded."""


class InvalidParameterCombinationException(MemoryDBException):
    """Invalid parameter combination."""


class InvalidParameterValueException(MemoryDBException):
    """Invalid parameter value."""


class InvalidClusterStateFault(MemoryDBException):
    """Invalid cluster state for operation."""


class InvalidACLStateFault(MemoryDBException):
    """Invalid ACL state for operation."""


class InvalidUserStateFault(MemoryDBException):
    """Invalid user state for operation."""


class TagNotFoundFault(MemoryDBException):
    """Tag not found."""


# ── Record classes ─────────────────────────────────────────────────

class ClusterRecord:
    def __init__(self, ClusterName, NodeType, ACLName, EngineVersion=None,
                 Description=None, MaintenanceWindow=None,
                 Port=None, ParameterGroupName=None,
                 SecurityGroupIds=None, SnapshotArns=None,
                 SnapshotName=None, SnapshotRetentionLimit=None,
                 SnapshotWindow=None, SnsTopicArn=None,
                 SubnetGroupName=None, TLSEnabled=None,
                 KmsKeyId=None, NumShards=None, NumReplicasPerShard=None,
                 Tags=None, MultiRegionClusterName=None,
                 DataTiering=None, **kwargs):
        self.ClusterName = ClusterName
        self.NodeType = NodeType
        self.ACLName = ACLName
        self.EngineVersion = EngineVersion or "7.0"
        self.Description = Description or ""
        self.MaintenanceWindow = MaintenanceWindow or "sun:05:00-sun:09:00"
        self.Port = Port or 6379
        self.ParameterGroupName = ParameterGroupName or "default.memorydb-redis7"
        self.SubnetGroupName = SubnetGroupName or "default"
        self.SecurityGroupIds = SecurityGroupIds or []
        self.TLSEnabled = TLSEnabled if TLSEnabled is not None else True
        self.NumShards = NumShards or 1
        self.NumReplicasPerShard = NumReplicasPerShard or 1
        self.Status = "creating"
        self.ARN = f"arn:aws:memorydb:us-east-1:000000000000:cluster/{ClusterName}"
        self.SubnetGroup = "default"

    def to_dict(self):
        return {
            "Name": self.ClusterName,
            "Description": self.Description,
            "Status": self.Status,
            "NumberOfShards": self.NumShards,
            "ARN": self.ARN,
            "EngineVersion": self.EngineVersion,
            "NodeType": self.NodeType,
            "MaintenanceWindow": self.MaintenanceWindow,
            "Port": self.Port,
            "ParameterGroupName": self.ParameterGroupName,
            "SubnetGroupName": self.SubnetGroupName,
            "TLSEnabled": self.TLSEnabled,
        }


class ACLRecord:
    def __init__(self, ACLName, UserNames=None, Tags=None, **kwargs):
        self.ACLName = ACLName
        self.UserNames = UserNames or []
        self.Status = "active"
        self.ARN = f"arn:aws:memorydb:us-east-1:000000000000:acl/{ACLName}"

    def to_dict(self):
        return {
            "Name": self.ACLName,
            "Status": self.Status,
            "UserNames": list(self.UserNames),
            "ARN": self.ARN,
        }


class UserRecord:
    def __init__(self, UserName, AuthenticationMode, AccessString=None,
                 Tags=None, **kwargs):
        self.UserName = UserName
        self.AuthenticationMode = AuthenticationMode or {}
        self.AccessString = AccessString or "on ~* +@all"
        self.Status = "active"
        self.ARN = f"arn:aws:memorydb:us-east-1:000000000000:user/{UserName}"

    def to_dict(self):
        return {
            "Name": self.UserName,
            "Status": self.Status,
            "AccessString": self.AccessString,
            "Authentication": self.AuthenticationMode,
            "ARN": self.ARN,
        }


class ParameterGroupRecord:
    def __init__(self, ParameterGroupName, Family, Description=None,
                 Parameters=None, Tags=None, **kwargs):
        self.ParameterGroupName = ParameterGroupName
        self.Family = Family
        self.Description = Description or ""
        self.Parameters = Parameters or {}
        self.ARN = f"arn:aws:memorydb:us-east-1:000000000000:parametergroup/{ParameterGroupName}"

    def to_dict(self):
        return {
            "Name": self.ParameterGroupName,
            "Family": self.Family,
            "Description": self.Description,
            "ARN": self.ARN,
        }


class SubnetGroupRecord:
    def __init__(self, SubnetGroupName, SubnetIds, Description=None,
                 Tags=None, **kwargs):
        self.SubnetGroupName = SubnetGroupName
        self.SubnetIds = SubnetIds or ["subnet-default"]
        self.Description = Description or ""
        self.ARN = f"arn:aws:memorydb:us-east-1:000000000000:subnetgroup/{SubnetGroupName}"

    def to_dict(self):
        return {
            "Name": self.SubnetGroupName,
            "Description": self.Description,
            "Subnets": [{"Identifier": s} for s in self.SubnetIds],
            "ARN": self.ARN,
        }


class SnapshotRecord:
    def __init__(self, SnapshotName, ClusterName, KmsKeyId=None,
                 Tags=None, **kwargs):
        self.SnapshotName = SnapshotName
        self.ClusterName = ClusterName
        self.KmsKeyId = KmsKeyId
        self.Status = "creating"
        self.ARN = f"arn:aws:memorydb:us-east-1:000000000000:snapshot/{SnapshotName}"

    def to_dict(self):
        return {
            "Name": self.SnapshotName,
            "ClusterName": self.ClusterName,
            "Status": self.Status,
            "ARN": self.ARN,
        }


# ── Store ───────────────────────────────────────────────────────────

class MemoryDBStore:
    def __init__(self):
        self._clusters: dict[str, ClusterRecord] = {}
        self._acls: dict[str, ACLRecord] = {}
        self._users: dict[str, UserRecord] = {}
        self._parameter_groups: dict[str, ParameterGroupRecord] = {}
        self._subnet_groups: dict[str, SubnetGroupRecord] = {}
        self._snapshots: dict[str, SnapshotRecord] = {}
        self._tags: dict[str, dict] = {}

    # ── Cluster methods ──────────────────────────────────────────

    def create_cluster(self, ClusterName, NodeType, ACLName, **kwargs):
        if ClusterName in self._clusters:
            raise ClusterAlreadyExistsFault(f"Cluster '{ClusterName}' already exists")
        record = ClusterRecord(ClusterName=ClusterName, NodeType=NodeType,
                               ACLName=ACLName, **kwargs)
        tags = kwargs.get("Tags")
        if tags and isinstance(tags, list):
            self._tags[record.ARN] = {t["Key"]: t["Value"] for t in tags if "Key" in t}
        self._clusters[ClusterName] = record
        return record.to_dict()

    def describe_clusters(self, ClusterName=None, **kwargs):
        if ClusterName:
            if ClusterName not in self._clusters:
                raise ClusterNotFoundFault(f"Cluster '{ClusterName}' not found")
            return {"Clusters": [self._clusters[ClusterName].to_dict()]}
        return {"Clusters": [c.to_dict() for c in self._clusters.values()]}

    def delete_cluster(self, ClusterName, **kwargs):
        if ClusterName not in self._clusters:
            raise ClusterNotFoundFault(f"Cluster '{ClusterName}' not found")
        record = self._clusters.pop(ClusterName)
        return record.to_dict()

    def update_cluster(self, ClusterName, **kwargs):
        if ClusterName not in self._clusters:
            raise ClusterNotFoundFault(f"Cluster '{ClusterName}' not found")
        record = self._clusters[ClusterName]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record.to_dict()

    # ── ACL methods ──────────────────────────────────────────────

    def create_acl(self, ACLName, **kwargs):
        if ACLName in self._acls:
            raise ACLAlreadyExistsFault(f"ACL '{ACLName}' already exists")
        record = ACLRecord(ACLName=ACLName, **kwargs)
        self._acls[ACLName] = record
        return record.to_dict()

    def describe_acls(self, ACLName=None, **kwargs):
        if ACLName:
            if ACLName not in self._acls:
                raise ACLNotFoundFault(f"ACL '{ACLName}' not found")
            return {"ACLs": [self._acls[ACLName].to_dict()]}
        return {"ACLs": [a.to_dict() for a in self._acls.values()]}

    def delete_acl(self, ACLName, **kwargs):
        if ACLName not in self._acls:
            raise ACLNotFoundFault(f"ACL '{ACLName}' not found")
        record = self._acls.pop(ACLName)
        return record.to_dict()

    def update_acl(self, ACLName, **kwargs):
        if ACLName not in self._acls:
            raise ACLNotFoundFault(f"ACL '{ACLName}' not found")
        record = self._acls[ACLName]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record.to_dict()

    # ── User methods ─────────────────────────────────────────────

    def create_user(self, UserName, AuthenticationMode, **kwargs):
        if UserName in self._users:
            raise UserAlreadyExistsFault(f"User '{UserName}' already exists")
        record = UserRecord(UserName=UserName,
                            AuthenticationMode=AuthenticationMode, **kwargs)
        self._users[UserName] = record
        return record.to_dict()

    def describe_users(self, UserName=None, **kwargs):
        if UserName:
            if UserName not in self._users:
                raise UserNotFoundFault(f"User '{UserName}' not found")
            return {"Users": [self._users[UserName].to_dict()]}
        return {"Users": [u.to_dict() for u in self._users.values()]}

    def delete_user(self, UserName, **kwargs):
        if UserName not in self._users:
            raise UserNotFoundFault(f"User '{UserName}' not found")
        record = self._users.pop(UserName)
        return record.to_dict()

    def update_user(self, UserName, **kwargs):
        if UserName not in self._users:
            raise UserNotFoundFault(f"User '{UserName}' not found")
        record = self._users[UserName]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record.to_dict()

    # ── ParameterGroup methods ───────────────────────────────────

    def create_parameter_group(self, ParameterGroupName, Family, **kwargs):
        if ParameterGroupName in self._parameter_groups:
            raise ParameterGroupAlreadyExistsFault(
                f"ParameterGroup '{ParameterGroupName}' already exists")
        record = ParameterGroupRecord(
            ParameterGroupName=ParameterGroupName, Family=Family, **kwargs)
        self._parameter_groups[ParameterGroupName] = record
        return record.to_dict()

    def describe_parameter_groups(self, ParameterGroupName=None, **kwargs):
        if ParameterGroupName:
            if ParameterGroupName not in self._parameter_groups:
                raise ParameterGroupNotFoundFault(
                    f"ParameterGroup '{ParameterGroupName}' not found")
            return {"ParameterGroups": [
                self._parameter_groups[ParameterGroupName].to_dict()]}
        return {"ParameterGroups": [p.to_dict()
                for p in self._parameter_groups.values()]}

    def delete_parameter_group(self, ParameterGroupName, **kwargs):
        if ParameterGroupName not in self._parameter_groups:
            raise ParameterGroupNotFoundFault(
                f"ParameterGroup '{ParameterGroupName}' not found")
        record = self._parameter_groups.pop(ParameterGroupName)
        return record.to_dict()

    def update_parameter_group(self, ParameterGroupName, **kwargs):
        if ParameterGroupName not in self._parameter_groups:
            raise ParameterGroupNotFoundFault(
                f"ParameterGroup '{ParameterGroupName}' not found")
        record = self._parameter_groups[ParameterGroupName]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record.to_dict()

    def reset_parameter_group(self, ParameterGroupName, **kwargs):
        if ParameterGroupName not in self._parameter_groups:
            raise ParameterGroupNotFoundFault(
                f"ParameterGroup '{ParameterGroupName}' not found")
        record = self._parameter_groups[ParameterGroupName]
        record.Parameters = {}
        return record.to_dict()

    # ── SubnetGroup methods ──────────────────────────────────────

    def create_subnet_group(self, SubnetGroupName, SubnetIds, **kwargs):
        if SubnetGroupName in self._subnet_groups:
            raise SubnetGroupAlreadyExistsFault(
                f"SubnetGroup '{SubnetGroupName}' already exists")
        record = SubnetGroupRecord(SubnetGroupName=SubnetGroupName,
                                   SubnetIds=SubnetIds, **kwargs)
        self._subnet_groups[SubnetGroupName] = record
        return record.to_dict()

    def describe_subnet_groups(self, SubnetGroupName=None, **kwargs):
        if SubnetGroupName:
            if SubnetGroupName not in self._subnet_groups:
                raise SubnetGroupNotFoundFault(
                    f"SubnetGroup '{SubnetGroupName}' not found")
            return {"SubnetGroups": [
                self._subnet_groups[SubnetGroupName].to_dict()]}
        return {"SubnetGroups": [s.to_dict()
                for s in self._subnet_groups.values()]}

    def delete_subnet_group(self, SubnetGroupName, **kwargs):
        if SubnetGroupName not in self._subnet_groups:
            raise SubnetGroupNotFoundFault(
                f"SubnetGroup '{SubnetGroupName}' not found")
        record = self._subnet_groups.pop(SubnetGroupName)
        return record.to_dict()

    def update_subnet_group(self, SubnetGroupName, **kwargs):
        if SubnetGroupName not in self._subnet_groups:
            raise SubnetGroupNotFoundFault(
                f"SubnetGroup '{SubnetGroupName}' not found")
        record = self._subnet_groups[SubnetGroupName]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record.to_dict()

    # ── Snapshot methods ─────────────────────────────────────────

    def create_snapshot(self, SnapshotName, ClusterName, **kwargs):
        if SnapshotName in self._snapshots:
            raise SnapshotAlreadyExistsFault(
                f"Snapshot '{SnapshotName}' already exists")
        if ClusterName not in self._clusters:
            raise ClusterNotFoundFault(
                f"Cluster '{ClusterName}' not found")
        record = SnapshotRecord(SnapshotName=SnapshotName,
                                ClusterName=ClusterName, **kwargs)
        self._snapshots[SnapshotName] = record
        return record.to_dict()

    def describe_snapshots(self, SnapshotName=None, **kwargs):
        if SnapshotName:
            if SnapshotName not in self._snapshots:
                raise SnapshotNotFoundFault(
                    f"Snapshot '{SnapshotName}' not found")
            return {"Snapshots": [self._snapshots[SnapshotName].to_dict()]}
        return {"Snapshots": [s.to_dict() for s in self._snapshots.values()]}

    def delete_snapshot(self, SnapshotName, **kwargs):
        if SnapshotName not in self._snapshots:
            raise SnapshotNotFoundFault(
                f"Snapshot '{SnapshotName}' not found")
        record = self._snapshots.pop(SnapshotName)
        return record.to_dict()

    # ── Tag methods ──────────────────────────────────────────────

    def tag_resource(self, ResourceArn, Tags, **kwargs):
        if ResourceArn not in self._tags:
            self._tags[ResourceArn] = {}
        for t in Tags:
            self._tags[ResourceArn][t["Key"]] = t["Value"]
        return {"TagList": [
            {"Key": k, "Value": v} for k, v in self._tags[ResourceArn].items()]}

    def untag_resource(self, ResourceArn, TagKeys, **kwargs):
        if ResourceArn in self._tags:
            for k in TagKeys:
                self._tags[ResourceArn].pop(k, None)
        return {"TagList": [
            {"Key": k, "Value": v}
            for k, v in self._tags.get(ResourceArn, {}).items()]}

    def list_tags(self, ResourceArn, **kwargs):
        return {"TagList": [
            {"Key": k, "Value": v}
            for k, v in self._tags.get(ResourceArn, {}).items()]}
