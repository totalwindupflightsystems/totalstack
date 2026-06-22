"""Amazon MQ store, records, and exception classes.

Core entities:
  - Broker: managed ActiveMQ/RabbitMQ instance
  - Configuration: broker configuration definition
  - User: broker-level user account

Operations (20 of 20 core):
  Create/Describe/Delete/List/Update/RebootBroker
  Create/Describe/Delete/List/UpdateConfiguration, DescribeConfigurationRevision
  Create/Describe/Delete/List/UpdateUser
  CreateTags, DeleteTags, ListTags
"""
import uuid
import time as _time
from collections import defaultdict


# ---------------------------------------------------------------------------
# Exception classes
# ---------------------------------------------------------------------------

class BadRequestException(Exception):
    pass

class UnauthorizedException(Exception):
    pass

class InternalServerErrorException(Exception):
    pass

class ConflictException(Exception):
    pass

class ForbiddenException(Exception):
    pass

class NotFoundException(Exception):
    pass


# ---------------------------------------------------------------------------
# Record classes
# ---------------------------------------------------------------------------

class BrokerRecord:
    def __init__(self, BrokerName, EngineType, DeploymentMode=None,
                 HostInstanceType=None, AuthenticationStrategy="SIMPLE",
                 AutoMinorVersionUpgrade=True, Configuration=None,
                 CreatorRequestId=None, EncryptionOptions=None,
                 EngineVersion=None, LdapServerMetadata=None, Logs=None,
                 MaintenanceWindowStartTime=None, PubliclyAccessible=False,
                 SecurityGroups=None, StorageType=None, SubnetIds=None,
                 Tags=None, Users=None, DataReplicationMode=None,
                 DataReplicationPrimaryBrokerArn=None):
        self.BrokerId = str(uuid.uuid4())
        self.BrokerArn = f"arn:aws:mq:us-east-1:000000000000:broker:{self.BrokerId}"
        self.BrokerName = BrokerName
        self.EngineType = EngineType
        self.DeploymentMode = DeploymentMode
        self.HostInstanceType = HostInstanceType or "mq.t3.micro"
        self.AuthenticationStrategy = AuthenticationStrategy
        self.AutoMinorVersionUpgrade = AutoMinorVersionUpgrade
        self.Configuration = Configuration
        self.EncryptionOptions = EncryptionOptions or {}
        self.EngineVersion = EngineVersion or ""
        self.Logs = Logs or {}
        self.MaintenanceWindowStartTime = MaintenanceWindowStartTime or {}
        self.PubliclyAccessible = PubliclyAccessible
        self.SecurityGroups = SecurityGroups or []
        self.StorageType = StorageType or "efs"
        self.SubnetIds = SubnetIds or []
        self.BrokerState = "RUNNING"
        self.Created = _time.time()
        self.PendingEngineVersion = EngineVersion or ""
        self._tags = {}
        if Tags:
            for k, v in (Tags if isinstance(Tags, dict) else {}).items():
                self._tags[k] = v


class ConfigurationRecord:
    def __init__(self, Name, EngineType, EngineVersion,
                 AuthenticationStrategy="SIMPLE", Description=None, Tags=None):
        self.Id = str(uuid.uuid4())
        self.Arn = f"arn:aws:mq:us-east-1:000000000000:configuration:{self.Id}"
        self.Name = Name
        self.EngineType = EngineType
        self.EngineVersion = EngineVersion
        self.AuthenticationStrategy = AuthenticationStrategy
        self.Description = Description or ""
        self.LatestRevision = 1
        self.Created = _time.time()
        self.Revisions = {1: {"revision": 1, "description": Description or "", "data": ""}}
        self._tags = {}
        if Tags:
            for k, v in (Tags if isinstance(Tags, dict) else {}).items():
                self._tags[k] = v


class UserRecord:
    def __init__(self, Username, Password, ConsoleAccess=False,
                 Groups=None, ReplicationUser=False):
        self.Username = Username
        self.Password = Password
        self.ConsoleAccess = ConsoleAccess
        self.Groups = Groups or []
        self.ReplicationUser = ReplicationUser
        self.Pending = {}


# ---------------------------------------------------------------------------
# Store
# ---------------------------------------------------------------------------

class MqStore:
    def __init__(self):
        self._brokers: dict[str, BrokerRecord] = {}
        self._configurations: dict[str, ConfigurationRecord] = {}
        self._users: dict[str, dict[str, UserRecord]] = defaultdict(dict)

    # -- Broker operations --

    def create_broker(self, **kwargs):
        BrokerName = kwargs.get("BrokerName")
        if not BrokerName:
            raise BadRequestException("BrokerName is required")
        # Check duplicate
        for b in self._brokers.values():
            if b.BrokerName == BrokerName:
                raise ConflictException(f"Broker '{BrokerName}' already exists")
        rec = BrokerRecord(**kwargs)
        self._brokers[rec.BrokerId] = rec
        return {"BrokerId": rec.BrokerId, "BrokerArn": rec.BrokerArn}

    def describe_broker(self, BrokerId):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        rec = self._brokers[BrokerId]
        return {
            "BrokerId": rec.BrokerId,
            "BrokerArn": rec.BrokerArn,
            "BrokerName": rec.BrokerName,
            "EngineType": rec.EngineType,
            "BrokerState": rec.BrokerState,
            "Created": rec.Created,
            "DeploymentMode": rec.DeploymentMode,
            "HostInstanceType": rec.HostInstanceType,
            "PubliclyAccessible": rec.PubliclyAccessible,
            "AutoMinorVersionUpgrade": rec.AutoMinorVersionUpgrade,
            "Tags": rec._tags,
        }

    def delete_broker(self, BrokerId):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        rec = self._brokers.pop(BrokerId)
        self._users.pop(rec.BrokerId, None)
        return {"BrokerId": BrokerId}

    def list_brokers(self, MaxResults=None, NextToken=None):
        brokers = list(self._brokers.values())
        if MaxResults:
            brokers = brokers[:MaxResults]
        summaries = []
        for b in brokers:
            summaries.append({
                "BrokerId": b.BrokerId,
                "BrokerName": b.BrokerName,
                "BrokerState": b.BrokerState,
                "EngineType": b.EngineType,
                "HostInstanceType": b.HostInstanceType,
                "DeploymentMode": b.DeploymentMode,
            })
        return {"BrokerSummaries": summaries}

    def update_broker(self, BrokerId, **kwargs):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        rec = self._brokers[BrokerId]
        for key, value in kwargs.items():
            if value is not None and hasattr(rec, key):
                setattr(rec, key, value)
        return {"BrokerId": BrokerId, "Configuration": rec.Configuration}

    def reboot_broker(self, BrokerId):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        self._brokers[BrokerId].BrokerState = "REBOOT_IN_PROGRESS"
        return {"BrokerId": BrokerId}

    # -- Configuration operations --

    def create_configuration(self, **kwargs):
        Name = kwargs.get("Name")
        if not Name:
            raise BadRequestException("Name is required")
        for c in self._configurations.values():
            if c.Name == Name:
                raise ConflictException(f"Configuration '{Name}' already exists")
        rec = ConfigurationRecord(**kwargs)
        self._configurations[rec.Id] = rec
        return {
            "Id": rec.Id,
            "Arn": rec.Arn,
            "Name": rec.Name,
            "LatestRevision": {"Revision": rec.LatestRevision, "Created": rec.Created},
        }

    def describe_configuration(self, ConfigurationId):
        if ConfigurationId not in self._configurations:
            raise NotFoundException(f"Configuration '{ConfigurationId}' not found")
        rec = self._configurations[ConfigurationId]
        return {
            "Id": rec.Id,
            "Arn": rec.Arn,
            "Name": rec.Name,
            "EngineType": rec.EngineType,
            "EngineVersion": rec.EngineVersion,
            "LatestRevision": {"Revision": rec.LatestRevision, "Created": rec.Created},
            "Description": rec.Description,
            "Tags": rec._tags,
        }

    def delete_configuration(self, ConfigurationId):
        if ConfigurationId not in self._configurations:
            raise NotFoundException(f"Configuration '{ConfigurationId}' not found")
        del self._configurations[ConfigurationId]
        return {"Id": ConfigurationId}

    def list_configurations(self, MaxResults=None, NextToken=None):
        configs = list(self._configurations.values())
        if MaxResults:
            configs = configs[:MaxResults]
        summaries = []
        for c in configs:
            summaries.append({
                "Id": c.Id,
                "Arn": c.Arn,
                "Name": c.Name,
                "EngineType": c.EngineType,
                "EngineVersion": c.EngineVersion,
            })
        return {"Configurations": summaries}

    def update_configuration(self, ConfigurationId, Data, Description=None):
        if ConfigurationId not in self._configurations:
            raise NotFoundException(f"Configuration '{ConfigurationId}' not found")
        rec = self._configurations[ConfigurationId]
        rec.LatestRevision += 1
        rev_num = rec.LatestRevision
        rec.Revisions[rev_num] = {
            "revision": rev_num,
            "description": Description or "",
            "data": Data,
        }
        if Description is not None:
            rec.Description = Description
        return {
            "Id": ConfigurationId,
            "Name": rec.Name,
            "LatestRevision": {"Revision": rev_num, "Created": _time.time()},
        }

    def describe_configuration_revision(self, ConfigurationId, ConfigurationRevision):
        if ConfigurationId not in self._configurations:
            raise NotFoundException(f"Configuration '{ConfigurationId}' not found")
        rec = self._configurations[ConfigurationId]
        rev = rec.Revisions.get(ConfigurationRevision)
        if rev is None:
            raise NotFoundException(
                f"Revision '{ConfigurationRevision}' not found for '{ConfigurationId}'")
        return {
            "ConfigurationId": ConfigurationId,
            "Id": rec.Id,
            "Revision": rev["revision"],
            "Description": rev["description"],
            "Data": rev["data"],
        }

    # -- User operations --

    def create_user(self, BrokerId, Username, Password=None, ConsoleAccess=False,
                    Groups=None, ReplicationUser=False):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        if Username in self._users.get(BrokerId, {}):
            raise ConflictException(
                f"User '{Username}' already exists on broker '{BrokerId}'")
        rec = UserRecord(
            Username=Username, Password=Password or "",
            ConsoleAccess=ConsoleAccess, Groups=Groups,
            ReplicationUser=ReplicationUser)
        self._users[BrokerId][Username] = rec
        return {}

    def describe_user(self, BrokerId, Username):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        if Username not in self._users.get(BrokerId, {}):
            raise NotFoundException(
                f"User '{Username}' not found on broker '{BrokerId}'")
        rec = self._users[BrokerId][Username]
        return {
            "Username": rec.Username,
            "ConsoleAccess": rec.ConsoleAccess,
            "Groups": rec.Groups,
            "Pending": rec.Pending,
        }

    def delete_user(self, BrokerId, Username):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        users = self._users.get(BrokerId, {})
        if Username not in users:
            raise NotFoundException(
                f"User '{Username}' not found on broker '{BrokerId}'")
        del users[Username]
        return {}

    def list_users(self, BrokerId, MaxResults=None, NextToken=None):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        users = list(self._users.get(BrokerId, {}).values())
        if MaxResults:
            users = users[:MaxResults]
        summaries = []
        for u in users:
            summaries.append({
                "Username": u.Username,
                "ConsoleAccess": u.ConsoleAccess,
                "Groups": u.Groups,
                "Pending": u.Pending,
            })
        return {"Users": summaries}

    def update_user(self, BrokerId, Username, ConsoleAccess=None, Groups=None,
                    Password=None, ReplicationUser=None):
        if BrokerId not in self._brokers:
            raise NotFoundException(f"Broker '{BrokerId}' not found")
        users = self._users.get(BrokerId, {})
        if Username not in users:
            raise NotFoundException(
                f"User '{Username}' not found on broker '{BrokerId}'")
        rec = users[Username]
        if ConsoleAccess is not None:
            rec.ConsoleAccess = ConsoleAccess
        if Groups is not None:
            rec.Groups = Groups
        if Password is not None:
            rec.Password = Password
        if ReplicationUser is not None:
            rec.ReplicationUser = ReplicationUser
        return {}

    # -- Tag operations --

    def create_tags(self, ResourceArn, Tags):
        rec = self._find_by_arn(ResourceArn)
        for k, v in (Tags if isinstance(Tags, dict) else {}).items():
            rec._tags[k] = v
        return {}

    def delete_tags(self, ResourceArn, TagKeys):
        rec = self._find_by_arn(ResourceArn)
        for key in TagKeys:
            rec._tags.pop(key, None)
        return {}

    def list_tags(self, ResourceArn):
        rec = self._find_by_arn(ResourceArn)
        return {"Tags": dict(rec._tags)}

    # -- Helpers --

    def _find_by_arn(self, arn):
        for b in self._brokers.values():
            if b.BrokerArn == arn:
                return b
        for c in self._configurations.values():
            if c.Arn == arn:
                return c
        raise NotFoundException(f"Resource not found: {arn}")
