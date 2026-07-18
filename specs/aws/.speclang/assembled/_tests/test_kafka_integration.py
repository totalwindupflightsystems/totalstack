"""Integration test for Kafka (MSK) — real store with generated handlers."""
import os
import types
import importlib.util

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'kafka')

# Load models.code.py
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

KafkaStore = models_mod.KafkaStore
ClusterRecord = models_mod.ClusterRecord
TopicRecord = models_mod.TopicRecord
ConfigurationRecord = models_mod.ConfigurationRecord
NotFoundException = models_mod.NotFoundException
BadRequestException = models_mod.BadRequestException
InternalServerErrorException = models_mod.InternalServerErrorException
ConflictException = models_mod.ConflictException
TopicExistsException = models_mod.TopicExistsException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exceptions
    mod.NotFoundException = NotFoundException
    mod.BadRequestException = BadRequestException
    mod.InternalServerErrorException = InternalServerErrorException
    mod.ConflictException = ConflictException
    mod.TopicExistsException = TopicExistsException
    mod.ForbiddenException = models_mod.ForbiddenException
    mod.UnauthorizedException = models_mod.UnauthorizedException
    mod.ServiceUnavailableException = models_mod.ServiceUnavailableException
    mod.TooManyRequestsException = models_mod.TooManyRequestsException
    # Inject records
    mod.ClusterRecord = ClusterRecord
    mod.TopicRecord = TopicRecord
    mod.ConfigurationRecord = ConfigurationRecord
    # Inject stdlib
    mod.time = __import__('time')
    mod.uuid = __import__('uuid')
    spec.loader.exec_module(mod)
    skip_names = {'NotFoundException', 'BadRequestException',
                  'InternalServerErrorException', 'ConflictException',
                  'TopicExistsException', 'ForbiddenException',
                  'UnauthorizedException', 'ServiceUnavailableException',
                  'TooManyRequestsException', 'ClusterRecord',
                  'TopicRecord', 'ConfigurationRecord', 'time', 'uuid'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestKafkaCluster:
    """Cluster CRUD operations."""

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KafkaStore()
        return self._store

    def _create_cluster(self):
        h = _load_handler('CreateCluster')
        return h(self.store, {
            "ClusterName": "test-cluster",
            "BrokerNodeGroupInfo": {
                "ClientSubnets": ["subnet-abc"],
                "InstanceType": "kafka.m5.large",
                "SecurityGroups": ["sg-123"],
            },
            "KafkaVersion": "3.6.0",
            "NumberOfBrokerNodes": 3,
        })

    def test_create_cluster_happy(self):
        resp = self._create_cluster()
        assert resp is not None
        assert "ClusterArn" in resp
        assert resp["ClusterName"] == "test-cluster"

    def test_create_cluster_v2(self):
        h = _load_handler('CreateClusterV2')
        resp = h(self.store, {
            "ClusterName": "v2-cluster",
            "BrokerNodeGroupInfo": {
                "ClientSubnets": ["subnet-abc"],
                "InstanceType": "kafka.m5.large",
            },
            "KafkaVersion": "3.6.0",
            "NumberOfBrokerNodes": 1,
        })
        assert "ClusterArn" in resp

    def test_describe_cluster_happy(self):
        resp = self._create_cluster()
        h = _load_handler('DescribeCluster')
        info = h(self.store, {"ClusterArn": resp["ClusterArn"]})
        assert info["ClusterName"] == "test-cluster"
        assert info["Status"] == "CREATING"

    def test_describe_cluster_nonexistent(self):
        h = _load_handler('DescribeCluster')
        try:
            h(self.store, {"ClusterArn": "arn:aws:kafka:us-east-1:000000000000:cluster/nonexistent"})
            raise AssertionError("Expected NotFoundException")
        except NotFoundException:
            pass

    def test_list_clusters(self):
        self._create_cluster()
        h = _load_handler('CreateCluster')(self.store, {
            "ClusterName": "cluster-2",
            "BrokerNodeGroupInfo": {
                "ClientSubnets": ["subnet-abc"],
            },
            "KafkaVersion": "3.6.0",
            "NumberOfBrokerNodes": 1,
        })
        h = _load_handler('ListClusters')
        resp = h(self.store, {})
        assert "ClusterInfoList" in resp
        assert len(resp["ClusterInfoList"]) == 2

    def test_delete_cluster_happy(self):
        resp = self._create_cluster()
        arn = resp["ClusterArn"]
        h = _load_handler('DeleteCluster')
        resp2 = h(self.store, {"ClusterArn": arn})
        assert resp2 == {}
        # Verify deleted
        try:
            _load_handler('DescribeCluster')(self.store, {"ClusterArn": arn})
            raise AssertionError("Expected NotFoundException")
        except NotFoundException:
            pass

    def test_delete_cluster_nonexistent(self):
        h = _load_handler('DeleteCluster')
        try:
            h(self.store, {"ClusterArn": "arn:nonexistent"})
            raise AssertionError("Expected NotFoundException")
        except NotFoundException:
            pass

    def test_get_bootstrap_brokers(self):
        resp = self._create_cluster()
        h = _load_handler('GetBootstrapBrokers')
        brokers = h(self.store, {"ClusterArn": resp["ClusterArn"]})
        assert "BootstrapBrokerStringTls" in brokers


class TestKafkaTopics:
    """Topic CRUD within a cluster."""

    _store = None
    _cluster_arn = None

    @property
    def store(self):
        if self._store is None:
            s = KafkaStore()
            h = _load_handler('CreateCluster')
            resp = h(s, {
                "ClusterName": "topic-cluster",
                "BrokerNodeGroupInfo": {
                    "ClientSubnets": ["subnet-abc"],
                },
                "KafkaVersion": "3.6.0",
                "NumberOfBrokerNodes": 1,
            })
            TestKafkaTopics._store = s
            TestKafkaTopics._cluster_arn = resp["ClusterArn"]
        return self._store

    def test_create_topic_happy(self):
        h = _load_handler('CreateTopic')
        resp = h(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "my-topic",
            "NumPartitions": 3,
            "ReplicationFactor": 3,
        })
        assert resp["TopicName"] == "my-topic"

    def test_create_duplicate_topic(self):
        h = _load_handler('CreateTopic')
        h(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "dup-topic",
            "NumPartitions": 1,
            "ReplicationFactor": 3,
        })
        try:
            h(self.store, {
                "ClusterArn": self._cluster_arn,
                "TopicName": "dup-topic",
                "NumPartitions": 1,
                "ReplicationFactor": 3,
            })
            raise AssertionError("Expected TopicExistsException")
        except TopicExistsException:
            pass

    def test_describe_topic_happy(self):
        h = _load_handler('CreateTopic')(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "desc-topic",
            "NumPartitions": 1,
            "ReplicationFactor": 3,
        })
        h = _load_handler('DescribeTopic')
        resp = h(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "desc-topic",
        })
        assert resp["TopicName"] == "desc-topic"

    def test_describe_topic_nonexistent(self):
        h = _load_handler('DescribeTopic')
        try:
            h(self.store, {
                "ClusterArn": self._cluster_arn,
                "TopicName": "nonexistent",
            })
            raise AssertionError("Expected NotFoundException")
        except NotFoundException:
            pass

    def test_list_topics(self):
        for i in range(3):
            _load_handler('CreateTopic')(self.store, {
                "ClusterArn": self._cluster_arn,
                "TopicName": f"topic-{i}",
                "NumPartitions": 1,
                "ReplicationFactor": 3,
            })
        h = _load_handler('ListTopics')
        resp = h(self.store, {"ClusterArn": self._cluster_arn})
        assert len(resp["TopicInfoList"]) >= 3

    def test_delete_topic(self):
        _load_handler('CreateTopic')(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "delete-me",
            "NumPartitions": 1,
            "ReplicationFactor": 3,
        })
        h = _load_handler('DeleteTopic')
        resp = h(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "delete-me",
        })
        assert resp == {}
        # Verify
        try:
            _load_handler('DescribeTopic')(self.store, {
                "ClusterArn": self._cluster_arn,
                "TopicName": "delete-me",
            })
            raise AssertionError("Expected NotFoundException")
        except NotFoundException:
            pass

    def test_update_topic(self):
        _load_handler('CreateTopic')(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "update-me",
            "NumPartitions": 1,
            "ReplicationFactor": 3,
        })
        h = _load_handler('UpdateTopic')
        resp = h(self.store, {
            "ClusterArn": self._cluster_arn,
            "TopicName": "update-me",
            "NumPartitions": 6,
        })
        assert resp["NumPartitions"] == 6


class TestKafkaConfiguration:
    """Configuration CRUD."""

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = KafkaStore()
        return self._store

    def test_create_configuration_happy(self):
        h = _load_handler('CreateConfiguration')
        resp = h(self.store, {
            "Name": "my-config",
            "ServerProperties": "auto.create.topics.enable=true",
            "KafkaVersions": ["3.6.0"],
        })
        assert resp["Name"] == "my-config"
        assert "Arn" in resp

    def test_describe_configuration_happy(self):
        h = _load_handler('CreateConfiguration')
        resp = h(self.store, {
            "Name": "desc-config",
            "ServerProperties": "ssl.enabled=true",
            "KafkaVersions": ["3.6.0"],
        })
        h = _load_handler('DescribeConfiguration')
        info = h(self.store, {"Arn": resp["Arn"]})
        assert info["Name"] == "desc-config"

    def test_describe_configuration_nonexistent(self):
        h = _load_handler('DescribeConfiguration')
        try:
            h(self.store, {"Arn": "arn:nonexistent"})
            raise AssertionError("Expected NotFoundException")
        except NotFoundException:
            pass

    def test_list_configurations(self):
        for i in range(2):
            _load_handler('CreateConfiguration')(self.store, {
                "Name": f"config-{i}",
                "ServerProperties": "prop=val",
            })
        h = _load_handler('ListConfigurations')
        resp = h(self.store, {})
        assert len(resp["Configurations"]) == 2

    def test_delete_configuration(self):
        resp = _load_handler('CreateConfiguration')(self.store, {
            "Name": "delete-config",
            "ServerProperties": "",
        })
        h = _load_handler('DeleteConfiguration')
        resp2 = h(self.store, {"Arn": resp["Arn"]})
        assert resp2 == {}
        try:
            _load_handler('DescribeConfiguration')(self.store, {"Arn": resp["Arn"]})
            raise AssertionError("Expected NotFoundException")
        except NotFoundException:
            pass

    def test_update_configuration(self):
        resp = _load_handler('CreateConfiguration')(self.store, {
            "Name": "update-config",
            "ServerProperties": "old=val",
        })
        h = _load_handler('UpdateConfiguration')
        resp2 = h(self.store, {
            "Arn": resp["Arn"],
            "ServerProperties": "new=val",
            "Description": "updated",
        })
        assert resp2["ServerProperties"] == "new=val"
        assert resp2["Description"] == "updated"
        assert resp2["LatestRevision"]["Revision"] > resp["Revision"]


class TestKafkaTags:
    """Tag operations on clusters."""

    _store = None
    _cluster_arn = None

    @property
    def store(self):
        if self._store is None:
            s = KafkaStore()
            h = _load_handler('CreateCluster')
            resp = h(s, {
                "ClusterName": "tag-cluster",
                "BrokerNodeGroupInfo": {"ClientSubnets": ["subnet-abc"]},
                "KafkaVersion": "3.6.0",
                "NumberOfBrokerNodes": 1,
                "Tags": {"env": "test"},
            })
            TestKafkaTags._store = s
            TestKafkaTags._cluster_arn = resp["ClusterArn"]
        return self._store

    def test_list_tags(self):
        h = _load_handler('ListTagsForResource')
        resp = h(self.store, {"ResourceArn": self._cluster_arn})
        assert resp["Tags"]["env"] == "test"

    def test_tag_resource(self):
        h = _load_handler('TagResource')
        resp = h(self.store, {
            "ResourceArn": self._cluster_arn,
            "Tags": {"team": "platform"},
        })
        assert resp == {}
        resp2 = _load_handler('ListTagsForResource')(self.store, {"ResourceArn": self._cluster_arn})
        assert resp2["Tags"]["team"] == "platform"

    def test_untag_resource(self):
        _load_handler('TagResource')(self.store, {
            "ResourceArn": self._cluster_arn,
            "Tags": {"temp": "remove"},
        })
        h = _load_handler('UntagResource')
        h(self.store, {
            "ResourceArn": self._cluster_arn,
            "TagKeys": ["temp"],
        })
        resp = _load_handler('ListTagsForResource')(self.store, {"ResourceArn": self._cluster_arn})
        assert "temp" not in resp["Tags"]
        assert resp["Tags"]["env"] == "test"
