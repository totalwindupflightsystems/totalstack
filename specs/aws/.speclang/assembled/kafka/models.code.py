"""Kafka (MSK — Managed Streaming for Apache Kafka) — TotalStack store.

Entities: Cluster, Topic (per cluster), Configuration.
"""

import time as _time


# ==================== Exception Classes ====================

class NotFoundException(Exception):
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(message)


class BadRequestException(Exception):
    def __init__(self, message="Bad request"):
        self.message = message
        super().__init__(message)


class InternalServerErrorException(Exception):
    def __init__(self, message="Internal server error"):
        self.message = message
        super().__init__(message)


class ForbiddenException(Exception):
    def __init__(self, message="Forbidden"):
        self.message = message
        super().__init__(message)


class ConflictException(Exception):
    def __init__(self, message="Conflict"):
        self.message = message
        super().__init__(message)


class UnauthorizedException(Exception):
    def __init__(self, message="Unauthorized"):
        self.message = message
        super().__init__(message)


class ServiceUnavailableException(Exception):
    def __init__(self, message="Service unavailable"):
        self.message = message
        super().__init__(message)


class TooManyRequestsException(Exception):
    def __init__(self, message="Too many requests"):
        self.message = message
        super().__init__(message)


class TopicExistsException(Exception):
    def __init__(self, message="Topic already exists"):
        self.message = message
        super().__init__(message)


# ==================== Record Classes ====================

class BrokerNodeGroupInfo:
    def __init__(self, ClientSubnets=None, InstanceType=None,
                 SecurityGroups=None, BrokerAZDistribution=None,
                 StorageInfo=None):
        self.ClientSubnets = ClientSubnets or []
        self.InstanceType = InstanceType or "kafka.m5.large"
        self.SecurityGroups = SecurityGroups or []
        self.BrokerAZDistribution = BrokerAZDistribution or "DEFAULT"
        self.StorageInfo = StorageInfo or {}


class ClusterRecord:
    def __init__(self, ClusterName, BrokerNodeGroupInfo=None,
                 KafkaVersion=None, NumberOfBrokerNodes=1,
                 EncryptionInfo=None, EnhancedMonitoring=None,
                 OpenMonitoring=None, LoggingInfo=None,
                 ClientAuthentication=None, ConfigurationInfo=None,
                 Tags=None, Arn=None, Status="CREATING",
                 ClusterArn=None, CreatedAt=None,
                 BootstrapBrokerStringTls=None,
                 ZookeeperConnectString=None,
                 CurrentBrokerSoftwareInfo=None):
        self.ClusterName = ClusterName
        self.BrokerNodeGroupInfo = BrokerNodeGroupInfo or _BrokerNodeGroupInfo()
        if isinstance(self.BrokerNodeGroupInfo, dict):
            self.BrokerNodeGroupInfo = _BrokerNodeGroupInfo(**self.BrokerNodeGroupInfo)
        self.KafkaVersion = KafkaVersion or "3.6.0"
        self.NumberOfBrokerNodes = NumberOfBrokerNodes
        self.EncryptionInfo = EncryptionInfo or {}
        self.EnhancedMonitoring = EnhancedMonitoring or "DEFAULT"
        self.OpenMonitoring = OpenMonitoring or {}
        self.LoggingInfo = LoggingInfo or {}
        self.ClientAuthentication = ClientAuthentication or {}
        self.ConfigurationInfo = ConfigurationInfo or {}
        self.Tags = Tags or {}
        self.Arn = Arn or ClusterArn
        self.ClusterArn = ClusterArn or Arn
        self.Status = Status
        self.CreatedAt = CreatedAt or _time.time()
        self.BootstrapBrokerStringTls = BootstrapBrokerStringTls
        self.ZookeeperConnectString = ZookeeperConnectString
        self.CurrentBrokerSoftwareInfo = CurrentBrokerSoftwareInfo or {}

    def to_dict(self):
        return {
            "ClusterName": self.ClusterName,
            "ClusterArn": self.ClusterArn,
            "Arn": self.Arn,
            "Status": self.Status,
            "KafkaVersion": self.KafkaVersion,
            "NumberOfBrokerNodes": self.NumberOfBrokerNodes,
            "EnhancedMonitoring": self.EnhancedMonitoring,
            "CreatedAt": self.CreatedAt,
            "BootstrapBrokerStringTls": self.BootstrapBrokerStringTls,
            "ZookeeperConnectString": self.ZookeeperConnectString,
            "Tags": self.Tags,
        }


class TopicRecord:
    def __init__(self, TopicName, NumPartitions=1,
                 ReplicationFactor=3, ConfigEntries=None,
                 Arn=None, Status="ACTIVE"):
        self.TopicName = TopicName
        self.NumPartitions = NumPartitions
        self.ReplicationFactor = ReplicationFactor
        self.ConfigEntries = ConfigEntries or {}
        self.Arn = Arn or f"arn:aws:kafka:us-east-1:000000000000:topic/{TopicName}"
        self.Status = Status

    def to_dict(self):
        return {
            "TopicName": self.TopicName,
            "NumPartitions": self.NumPartitions,
            "ReplicationFactor": self.ReplicationFactor,
            "Status": self.Status,
        }


class ConfigurationRecord:
    def __init__(self, Name, ServerProperties=None,
                 KafkaVersions=None, Description=None,
                 Arn=None, Revision=1, LatestRevision=None,
                 State="ACTIVE", CreatedAt=None):
        self.Name = Name
        self.ServerProperties = ServerProperties or ""
        self.KafkaVersions = KafkaVersions or ["3.6.0"]
        self.Description = Description or ""
        self.Arn = Arn or f"arn:aws:kafka:us-east-1:000000000000:configuration/{Name}"
        self.Revision = Revision
        self.LatestRevision = LatestRevision or Revision
        self.State = State
        self.CreatedAt = CreatedAt or _time.time()

    def to_dict(self):
        return {
            "Name": self.Name,
            "Arn": self.Arn,
            "Description": self.Description,
            "ServerProperties": self.ServerProperties,
            "KafkaVersions": self.KafkaVersions,
            "LatestRevision": self.LatestRevision,
            "Revision": self.Revision,
            "State": self.State,
        }


# Aliases to avoid parameter shadowing in __init__
_BrokerNodeGroupInfo = BrokerNodeGroupInfo


# ==================== Kafka Store ====================

class KafkaStore:
    def __init__(self):
        self._clusters: dict[str, ClusterRecord] = {}
        self._topics: dict[str, dict[str, TopicRecord]] = {}  # cluster_arn → {name: record}
        self._configurations: dict[str, ConfigurationRecord] = {}
        self._tags: dict[str, dict] = {}
        self._arn_counter = 0

    def _gen_arn(self, prefix, name):
        self._arn_counter += 1
        return f"arn:aws:kafka:us-east-1:000000000000:{prefix}/{name}-{self._arn_counter}"

    # ---- Cluster accessor ----
    def clusters(self, arn=None):
        if arn is not None:
            return self._clusters.get(arn)
        return list(self._clusters.values())

    # ---- Cluster CRUD ----
    def create_cluster(self, **kwargs):
        name = kwargs.get("ClusterName")
        arn = self._gen_arn("cluster", name)
        record = ClusterRecord(**kwargs)
        record.Arn = arn
        record.ClusterArn = arn
        record.BootstrapBrokerStringTls = f"b-1.{name}.kafka.us-east-1.amazonaws.com:9094"
        record.ZookeeperConnectString = f"z-1.{name}.kafka.us-east-1.amazonaws.com:2181"
        self._clusters[arn] = record
        self._topics.setdefault(arn, {})
        # Tags
        tags_raw = kwargs.get("Tags")
        if tags_raw:
            self._tags[arn] = self._convert_tags(tags_raw)
        return record.to_dict()

    def get_cluster(self, ClusterArn):
        r = self._clusters.get(ClusterArn)
        if not r:
            raise NotFoundException(f"Cluster {ClusterArn} not found")
        result = r.to_dict()
        result["Tags"] = self._tags.get(ClusterArn, {})
        return result

    def list_clusters(self, **kwargs):
        return [r.to_dict() for r in self._clusters.values()]

    def delete_cluster(self, ClusterArn):
        r = self._clusters.pop(ClusterArn, None)
        if not r:
            raise NotFoundException(f"Cluster {ClusterArn} not found")
        self._topics.pop(ClusterArn, None)
        self._tags.pop(ClusterArn, None)
        return {}

    def get_bootstrap_brokers(self, ClusterArn):
        r = self._clusters.get(ClusterArn)
        if not r:
            raise NotFoundException(f"Cluster {ClusterArn} not found")
        return {"BootstrapBrokerStringTls": r.BootstrapBrokerStringTls}

    # ---- Topic CRUD ----
    def create_topic(self, ClusterArn, **kwargs):
        if ClusterArn not in self._clusters:
            raise NotFoundException(f"Cluster {ClusterArn} not found")
        name = kwargs.get("TopicName")
        if name in self._topics[ClusterArn]:
            raise TopicExistsException(f"Topic {name} already exists")
        record = TopicRecord(**kwargs)
        self._topics[ClusterArn][name] = record
        return record.to_dict()

    def describe_topic(self, ClusterArn, TopicName):
        r = self._topics.get(ClusterArn, {}).get(TopicName)
        if not r:
            raise NotFoundException(f"Topic {TopicName} not found")
        return r.to_dict()

    def list_topics(self, ClusterArn, **kwargs):
        if ClusterArn not in self._clusters:
            raise NotFoundException(f"Cluster {ClusterArn} not found")
        return [t.to_dict() for t in self._topics[ClusterArn].values()]

    def delete_topic(self, ClusterArn, TopicName):
        r = self._topics.get(ClusterArn, {}).pop(TopicName, None)
        if not r:
            raise NotFoundException(f"Topic {TopicName} not found")
        return {}

    def update_topic(self, ClusterArn, TopicName, **kwargs):
        r = self._topics.get(ClusterArn, {}).get(TopicName)
        if not r:
            raise NotFoundException(f"Topic {TopicName} not found")
        for k, v in kwargs.items():
            if hasattr(r, k):
                setattr(r, k, v)
        return r.to_dict()

    # ---- Configuration CRUD ----
    def create_configuration(self, **kwargs):
        name = kwargs.get("Name")
        arn = self._gen_arn("configuration", name)
        record = ConfigurationRecord(**kwargs)
        record.Arn = arn
        self._configurations[arn] = record
        return record.to_dict()

    def describe_configuration(self, Arn):
        r = self._configurations.get(Arn)
        if not r:
            raise NotFoundException(f"Configuration {Arn} not found")
        return r.to_dict()

    def list_configurations(self, **kwargs):
        return [c.to_dict() for c in self._configurations.values()]

    def delete_configuration(self, Arn):
        r = self._configurations.pop(Arn, None)
        if not r:
            raise NotFoundException(f"Configuration {Arn} not found")
        return {}

    def update_configuration(self, Arn, **kwargs):
        r = self._configurations.get(Arn)
        if not r:
            raise NotFoundException(f"Configuration {Arn} not found")
        for k, v in kwargs.items():
            if hasattr(r, k) and k != "Arn":
                setattr(r, k, v)
        r.Revision += 1
        r.LatestRevision = r.Revision
        return r.to_dict()

    # ---- Tag helpers ----
    def _convert_tags(self, tags):
        if tags is None:
            return {}
        if isinstance(tags, dict):
            return dict(tags)
        tag_dict = {}
        for t in tags:
            tag_dict[t.get("key", t.get("Key", ""))] = t.get(
                "value", t.get("Value", ""))
        return tag_dict

    # ---- Tag operations ----
    def list_tags_for_resource(self, ResourceArn):
        if ResourceArn not in self._tags and ResourceArn not in self._clusters:
            raise NotFoundException(f"Resource {ResourceArn} not found")
        return {"Tags": self._tags.get(ResourceArn, {})}

    def tag_resource(self, ResourceArn, Tags):
        if ResourceArn not in self._clusters:
            raise NotFoundException(f"Resource {ResourceArn} not found")
        existing = self._tags.get(ResourceArn, {})
        existing.update(self._convert_tags(Tags))
        self._tags[ResourceArn] = existing
        return {}

    def untag_resource(self, ResourceArn, TagKeys):
        if ResourceArn not in self._clusters:
            raise NotFoundException(f"Resource {ResourceArn} not found")
        existing = self._tags.get(ResourceArn, {})
        for k in TagKeys:
            existing.pop(k, None)
        self._tags[ResourceArn] = existing
        return {}
