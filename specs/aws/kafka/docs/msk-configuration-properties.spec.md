---
id: "@specs/aws/kafka/docs/msk-configuration-properties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Custom Amazon MSK configurations"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Custom Amazon MSK configurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-properties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Custom Amazon MSK configurations
<a name="msk-configuration-properties"></a>

You can use Amazon MSK to create a custom MSK configuration where you set the following Apache Kafka configuration properties. Properties that you don't set explicitly get the values they have in [Default Amazon MSK configuration](msk-default-configuration.md). For more information about configuration properties, see [Apache Kafka Configuration](https://kafka.apache.org/documentation/#configuration).


| Name | Description | 
| --- | --- | 
| allow.everyone.if.no.acl.found | If you want to set this property tofalse, first make sure you define Apache Kafka ACLs for your cluster. If you set this property to falseand you don't first define Apache Kafka ACLs, you lose access to the cluster. If that happens, you can update the configuration again and set this property to true to regain access to the cluster. | 
| auto.create.topics.enable | Enables topic auto-creation on the server. | 
| compression.type | The final compression type for a given topic. You can set this property to the standard compression codecs (gzip, snappy, lz4, and zstd). It additionally accepts uncompressed. This value is equivalent to no compression. If you set the value to producer, it means retain the original compression codec that the producer sets. | 
| connections.max.idle.ms | Idle connections timeout in milliseconds. The server socket processor threads close the connections that are idle for more than the value that you set for this property. | 
| default.replication.factor | The default replication factor for automatically created topics. | 
| delete.topic.enable | Enables the delete topic operation. If you turn off this setting, you can't delete a topic through the admin tool. | 
| group.initial.rebalance.delay.ms | Amount of time the group coordinator waits for more data consumers to join a new group before the group coordinator performs the first rebalance. A longer delay means potentially fewer rebalances, but this increases the time until processing begins. | 
| group.max.session.timeout.ms | Maximum session timeout for registered consumers. Longer timeouts give consumers more time to process messages between heartbeats at the cost of a longer time to detect failures. | 
| group.min.session.timeout.ms | Minimum session timeout for registered consumers. Shorter timeouts result in quicker failure detection at the cost of more frequent consumer heartbeats. This can overwhelm broker resources. | 
| leader.imbalance.per.broker.percentage | The ratio of leader imbalance allowed per broker. The controller triggers a leader balance if it exceeds this value per broker. This value is specified in percentage. | 
| log.cleaner.delete.retention.ms | Amount of time that you want Apache Kafka to retain deleted records. The minimum value is 0. | 
| log.cleaner.min.cleanable.ratio | This configuration property can have values between 0 and 1. This value determines how frequently the log compactor attempts to clean the log (if log compaction is enabled). By default, Apache Kafka avoids cleaning a log if more than 50% of the log has been compacted. This ratio bounds the maximum space that  the log wastes with duplicates (at 50%, this means at most 50% of the log could be duplicates). A higher ratio means fewer, more efficient cleanings, but more wasted space in the log. | 
| log.cleanup.policy | The default cleanup policy for segments beyond the retention window. A comma-separated list of valid policies. Valid policies are delete and compact. For Tiered Storage enabled clusters, valid policy is delete only. | 
| log.flush.interval.messages | Number of messages that accumulate on a log partition before messages are flushed to disk. | 
| log.flush.interval.ms | Maximum time in milliseconds that a message in any topic remains in memory before flushed to disk. If you don't set this value, the value in log.flush.scheduler.interval.ms is used. The minimum value is 0. | 
| log.message.timestamp.difference.max.ms | This configuration is deprecated in Kafka 3.6.0. Two configurations, log.message.timestamp.before.max.ms and log.message.timestamp.after.max.ms, have been added. The maximum time difference between the timestamp when a broker receives a message and the timestamp specified in the message. If log.message.timestamp.type=CreateTime, a message is rejected if the difference in timestamp exceeds this threshold. This configuration is ignored if log.message.timestamp.type=LogAppendTime. | 
| log.message.timestamp.type | Specifies if the timestamp in the message is the message creation time or the log append time. The allowed values are CreateTime and LogAppendTime. | 
| log.retention.bytes | Maximum size of the log before deleting it. | 
| log.retention.hours | Number of hours to keep a log file before deleting it, tertiary to the log.retention.ms property. | 
| log.retention.minutes | Number of minutes to keep a log file before deleting it, secondary to log.retention.ms property. If you don't set this value, the value in log.retention.hours is used. | 
| log.retention.ms | Number of milliseconds to keep a log file before deleting it (in milliseconds), If not set, the value in log.retention.minutes is used. | 
| log.roll.ms | Maximum time before a new log segment is rolled out (in milliseconds). If you don't set this property, the value in log.roll.hours is used. The minimum possible value for this property is 1. | 
| log.segment.bytes | Maximum size of a single log file. | 
| max.incremental.fetch.session.cache.slots | Maximum number of incremental fetch sessions that are maintained. | 
| message.max.bytes | Largest record batch size that Kafka allows. If you increase this value and there are consumers older than 0.10.2, you must also increase the fetch size of the consumers so that they can fetch record batches this large.<br />The latest message format version always groups messages into batches for efficiency. Previous message format versions don't group uncompressed records into batches, and in such a case, this limit only applies to a single record.<br />You can set this value per topic with the topic level max.message.bytes config. | 
| min.insync.replicas | When a producer sets acks to `"all"` (or `"-1"`), the value in min.insync.replicas specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful. If this minimum cannot be met, the producer raises an exception (either NotEnoughReplicas or NotEnoughReplicasAfterAppend).<br />You can use values in min.insync.replicas and acks to enforce greater durability guarantees. For example, you might create a topic with a replication factor of 3, set min.insync.replicas to 2, and produce with acks of `"all"`. This ensures that the producer raises an exception if a majority of replicas don't receive a write. | 
| num.io.threads | The number of threads that the server uses for processing requests, which may include disk I/O. | 
| num.network.threads | The number of threads that the server uses to receive requests from the network and send responses to it. | 
| num.partitions | Default number of log partitions per topic. | 
| num.recovery.threads.per.data.dir | The number of threads per data directory to be used to recover logs at startup and and to flush them at shutdown. | 
| num.replica.fetchers | The number of fetcher threads used to replicate messages from a source broker. If you increase this value, you can increase the degree of I/O parallelism in the follower broker. | 
| offsets.retention.minutes | After a consumer group loses all its consumers (that is, it becomes empty) its offsets are kept for this retention period before getting discarded. For standalone consumers (that is,those that use manual assignment), offsets expire after the time of the last commit plus this retention period. | 
| offsets.topic.replication.factor | The replication factor for the offsets topic. Set this value higher to ensure availability. Internal topic creation fails until the cluster size meets this replication factor requirement. | 
| replica.fetch.max.bytes | Number of bytes of messages to attempt to fetch for each partition. This is not an absolute maximum. If the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch is returned to ensure progress. The message.max.bytes (broker config) or max.message.bytes (topic config) defines the maximum record batch size that the broker accepts. | 
| replica.fetch.response.max.bytes | The maximum number of bytes expected for the entire fetch response. Records are fetched in batches, and if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure progress. This isn't an absolute maximum. The message.max.bytes (broker config) or max.message.bytes (topic config) properties specify the maximum record batch size that the broker accepts. | 
| replica.lag.time.max.ms | If a follower hasn't sent any fetch requests or hasn't consumed up to the leader's log end offset for at least this number of milliseconds, the leader removes the follower from the ISR.MinValue: 10000<br />MaxValue = 30000 | 
| replica.selector.class | The fully-qualified class name that implements ReplicaSelector. The broker uses this value to find the preferred read replica. If you use Apache Kafka version 2.4.1 or higher, and want to allow consumers to fetch from the closest replica, set this property to org.apache.kafka.common.replica.RackAwareReplicaSelector. For more information, see [Apache Kafka version 2.4.1 (use 2.4.1.1 instead)](supported-kafka-versions.md#2.4.1). | 
| replica.socket.receive.buffer.bytes | The socket receive buffer for network requests. | 
| socket.receive.buffer.bytes | The SO\_RCVBUF buffer of the socket server sockets. The minimum value that you can set for this property is -1. If the value is -1, Amazon MSK uses the OS default. | 
| socket.request.max.bytes | The maximum number of bytes in a socket request. | 
| socket.send.buffer.bytes | The SO\_SNDBUF buffer of the socket server sockets. The minimum value that you can set for this property is -1. If the value is -1, Amazon MSK uses the OS default. | 
| transaction.max.timeout.ms | Maximum timeout for transactions. If the requested transaction time of a client exceeds this value, the broker returns an error in InitProducerIdRequest. This prevents a client from too large of a timeout, and this can stall consumers that read from topics included in the transaction. | 
| transaction.state.log.min.isr | Overridden min.insync.replicas configuration for the transaction topic. | 
| transaction.state.log.replication.factor | The replication factor for the transaction topic. Set this property to a higher value to increase availability. Internal topic creation fails until the cluster size meets this replication factor requirement. | 
| transactional.id.expiration.ms | The time in milliseconds that the transaction coordinator waits to receive any transaction status updates for the current transaction before the coordinator expires its transactional ID. This setting also influences producer ID expiration because it causes producer IDs expire when this time elapses after the last write with the given producer ID. Producer IDs might expire sooner if the last write from the producer ID is deleted because of the  retention settings for the topic. The minimum value for this property is 1 millisecond. | 
| unclean.leader.election.enable | Indicates if replicas not in the ISR set should serve as leader as a last resort, even though this might result in data loss. | 
| zookeeper.connection.timeout.ms | ZooKeeper mode clusters. Maximum time that the client waits to establish a connection to ZooKeeper. If you don't set this value, the value in zookeeper.session.timeout.ms is used.<br />MinValue = 6000<br />MaxValue (inclusive) = 18000<br />We recommend that you set this value to 10,000 on T3.small to avoid cluster downtime. | 
| zookeeper.session.timeout.ms | ZooKeeper mode clusters. The Apache ZooKeeper session timeout in milliseconds.<br />MinValue = 6000<br />MaxValue (inclusive) = 18000 | 

To learn how you can create a custom MSK configuration, list all configurations, or describe them, see [Broker configuration operations](msk-configuration-operations.md). To create an MSK cluster with a custom MSK configuration, or to update a cluster with a new custom configuration, see [Amazon MSK key features and concepts](operations.md).

When you update your existing MSK cluster with a custom MSK configuration, Amazon MSK does rolling restarts when necessary, and uses best practices to minimize customer downtime. For example, after Amazon MSK restarts each broker, Amazon MSK tries to let the broker catch up on data that the broker might have missed during the configuration update before it moves to the next broker.

## Dynamic Amazon MSK configuration
<a name="msk-dynamic-confinguration"></a>

In addition to the configuration properties that Amazon MSK provides, you can dynamically set cluster-level and broker-level configuration properties that don't require a broker restart. You can dynamically set some configuration properties. These are the properties not marked as read-only in the table under [Broker Configs](https://kafka.apache.org/documentation/#brokerconfigs) in the Apache Kafka documentation. For information on dynamic configuration and example commands, see [Updating Broker Configs](https://kafka.apache.org/documentation/#dynamicbrokerconfigs) in the Apache Kafka documentation.

**Note**  
You can set the `advertised.listeners` property, but not the `listeners` property.

## Topic-level Amazon MSK configuration
<a name="msk-topic-confinguration"></a>

You can use Apache Kafka commands to set or modify topic-level configuration properties for new and existing topics. For more information on topic-level configuration properties and examples on how to set them, see [Topic-Level Configs](https://kafka.apache.org/documentation/#topicconfigs) in the Apache Kafka documentation.