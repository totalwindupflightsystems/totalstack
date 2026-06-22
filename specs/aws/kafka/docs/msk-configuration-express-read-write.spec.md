---
id: "@specs/aws/kafka/docs/msk-configuration-express-read-write"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Custom read/write access configurations"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Custom read/write access configurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-configuration-express-read-write
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Custom MSK Express broker configurations (Read/Write access)
<a name="msk-configuration-express-read-write"></a>

You can update read/write broker configurations either by using Amazon MSK’s [update configuration feature](msk-update-cluster-config.md) or using Apache Kafka’s AlterConfig API. Apache Kafka broker configurations are either static or dynamic. Static configurations require a broker restart for the configuration to be applied, while dynamic configurations do not need a broker restart. For more information about configuration properties and update modes, see [Updating broker configs](https://kafka.apache.org/documentation/#dynamicbrokerconfigs).

**Topics**
+ [Static configurations on MSK Express brokers](#msk-configuration-express-static-configuration)
+ [Dynamic configurations on Express Brokers](#msk-configuration-express-dynamic-configuration)
+ [Topic-level configurations on Express Brokers](#msk-configuration-express-topic-configuration)

## Static configurations on MSK Express brokers
<a name="msk-configuration-express-static-configuration"></a>

You can use Amazon MSK to create a custom MSK configuration file to set the following static properties. Amazon MSK sets and manages all other properties that you do not set. You can create and update static configuration files from the MSK console or using the [configurations command](msk-configuration-operations-create.md).


| Property | Description | Default Value | 
| --- | --- | --- | 
| allow.everyone.if.no.acl.found | If you want to set this property to false, first make sure you define Apache Kafka ACLs for your cluster. If you set this property to false and you don't first define Apache Kafka ACLs, you lose access to the cluster. If that happens, you can update the configuration again and set this property to true to regain access to the cluster. | true | 
| auto.create.topics.enable | Enables autocreation of a topic on the server. | false | 
| compression.type | Specify the final compression type for a given topic. This configuration accepts the standard compression codecs: gzip, snappy, lz4, zstd.<br />This configuration additionally accepts `uncompressed`, which is equivalent to no compression; and `producer`, which means retain the original compression codec set by the producer. | Apache Kafka Default | 
| connections.max.idle.ms | Idle connections timeout in milliseconds. The server socket processor threads close the connections that are idle for more than the value that you set for this property. | Apache Kafka Default | 
| delete.topic.enable | Enables the delete topic operation. If you turn off this setting, you can't delete a topic through the admin tool. | Apache Kafka Default | 
| group.initial.rebalance.delay.ms |  Amount of time the group coordinator waits for more data consumers to join a new group before the group coordinator performs the first rebalance. A longer delay means potentially fewer rebalances, but this increases the time until processing begins. | Apache Kafka Default | 
| group.max.session.timeout.ms | Maximum session timeout for registered consumers. Longer timeouts give consumers more time to process messages between heartbeats at the cost of a longer time to detect failures. | Apache Kafka Default | 
| leader.imbalance.per.broker.percentage | The ratio of leader imbalance allowed per broker. The controller triggers a leader balance if it exceeds this value per broker. This value is specified in percentage. | Apache Kafka Default | 
| log.cleanup.policy | The default cleanup policy for segments beyond the retention window. A comma-separated list of valid policies. Valid policies are delete and compact. For tiered storage-enabled clusters, valid policy is delete only. | Apache Kafka Default | 
| log.message.timestamp.after.max.ms | The allowable timestamp difference between the message timestamp and the broker's timestamp. The message timestamp can be later than or equal to the broker's timestamp, with the maximum allowable difference determined by the value set in this configuration.<br />If `log.message.timestamp.type=CreateTime`, the message will be rejected if the difference in timestamps exceeds this specified threshold. This configuration is ignored if `log.message.timestamp.type=LogAppendTime`. | 86400000 (24 \* 60 \* 60 \* 1000 ms, that is, 1 day) | 
| log.message.timestamp.before.max.ms | The allowable timestamp difference between the broker's timestamp and the message timestamp. The message timestamp can be earlier than or equal to the broker's timestamp, with the maximum allowable difference determined by the value set in this configuration.<br />If `log.message.timestamp.type=CreateTime`, the message will be rejected if the difference in timestamps exceeds this specified threshold. This configuration is ignored if `log.message.timestamp.type=LogAppendTime`. | 86400000 (24 \* 60 \* 60 \* 1000 ms, that is, 1 day) | 
| log.message.timestamp.type | Specifies if the timestamp in the message is the message creation time or the log append time. The allowed values are CreateTime and LogAppendTime. | Apache Kafka Default | 
| log.retention.bytes | Maximum size of the log before deleting it. | Apache Kafka Default | 
| log.retention.ms | Number of milliseconds to keep a log file before deleting it. | Apache Kafka Default | 
| max.connections.per.ip | The maximum number of connections allowed from each IP address. This can be set to 0 if there are overrides configured using the max.connections.per.ip.overrides property. New connections from the IP address are dropped if the limit is reached. | Apache Kafka Default | 
| max.incremental.fetch.session.cache.slots | Maximum number of incremental fetch sessions that are maintained. | Apache Kafka Default | 
| message.max.bytes | Largest record batch size that Kafka allows. If you increase this value and there are consumers older than 0.10.2, you must also increase the fetch size of the consumers so that they can fetch record batches this large.<br />The latest message format version always groups messages into batches for efficiency. Previous message format versions don't group uncompressed records into batches, and in such a case, this limit only applies to a single record. You can set this value per topic with the topic level `max.message.bytes` config. | Apache Kafka Default | 
| num.partitions | Default number of partitions per topic. | 1 | 
| offsets.retention.minutes | After a consumer group loses all its consumers (that is, it becomes empty) its offsets are kept for this retention period before getting discarded. For standalone consumers (that is, those that use manual assignment), offsets expire after the time of the last commit plus this retention period. | Apache Kafka Default | 
| replica.fetch.max.bytes | Number of bytes of messages to attempt to fetch for each partition. This is not an absolute maximum. If the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch is returned to ensure progress. The message.max.bytes (broker config) or max.message.bytes (topic config) defines the maximum record batch size that the broker accepts. | Apache Kafka Default | 
| replica.selector.class | The fully-qualified class name that implements ReplicaSelector. The broker uses this value to find the preferred read replica. If you want to allow consumers to fetch from the closest replica, set this property to `org.apache.kafka.common.replica.RackAwareReplicaSelector`. | Apache Kafka Default | 
| socket.receive.buffer.bytes | The SO\_RCVBUF buffer of the socket sever sockets. If the value is -1, the OS default is used. | 102400 | 
| socket.request.max.bytes | Maximum number of bytes in a socket request. | 104857600 | 
| socket.send.buffer.bytes | The SO\_SNDBUF buffer of the socket sever sockets. If the value is -1, the OS default is used. | 102400 | 
| transaction.max.timeout.ms | Maximum timeout for transactions. If the requested transaction time of a client exceeds this value, the broker returns an error in InitProducerIdRequest. This prevents a client from too large of a timeout, and this can stall consumers that read from topics included in the transaction. | Apache Kafka Default | 
| transactional.id.expiration.ms | The time in milliseconds that the transaction coordinator waits to receive any transaction status updates for the current transaction before the coordinator expires its transactional ID. This setting also influences producer ID expiration because it causes producer IDs to expire when this time elapses after the last write with the given producer ID. Producer IDs might expire sooner if the last write from the producer ID is deleted because of the retention settings for the topic. The minimum value for this property is 1 millisecond. | Apache Kafka Default | 

## Dynamic configurations on Express Brokers
<a name="msk-configuration-express-dynamic-configuration"></a>

You can use Apache Kafka AlterConfig API or the Kafka-configs.sh tool to edit the following dynamic configurations. Amazon MSK sets and manages all other properties that you do not set. You can dynamically set cluster-level and broker-level configuration properties that don't require a broker restart.


| Property | Description | Default value | 
| --- | --- | --- | 
| advertised.listeners | Listeners to publish for clients to use, if different than the `listeners` config property. In IaaS environments, this may need to be different from the interface to which the broker binds. If this is not set, the value for listeners will be used. Unlike listeners, it is not valid to advertise the 0.0.0.0 meta-address.<br />Also unlike `listeners`, there can be duplicated ports in this property, so that one listener can be configured to advertise another listener's address. This can be useful in some cases where external load balancers are used.<br />This property is set at a per-broker level. | null | 
| compression.type | The final compression type for a given topic. You can set this property to the standard compression codecs (`gzip`, `snappy`, `lz4`, and `zstd`). It additionally accepts `uncompressed`. This value is equivalent to no compression. If you set the value to `producer`, it means retain the original compression codec that the producer sets. | Apache Kafka Default | 
| log.cleaner.delete.retention.ms | The amount of time to retain delete tombstone markers for log compacted topics. This setting also gives a bound on the time in which a consumer must complete a read if they begin from offset 0 to ensure that they get a valid snapshot of the final stage. Else, delete tombstones might be collected before they complete their scan. | 86400000 (24 \* 60 \* 60 \* 1000 ms, that is, 1 day), Apache Kafka Default | 
| log.cleaner.min.compaction.lag.ms | The minimum time a message will remain uncompacted in the log. This setting is only applicable for logs that are being compacted. | 0, Apache Kafka Default | 
| log.cleaner.max.compaction.lag.ms | The maximum time a message will remain ineligible for compaction in the log. This setting is only applicable for logs that are being compacted. This configuration would be bounded in the range of [7 days, Long.Max]. | 9223372036854775807, Apache Kafka Default | 
| log.cleanup.policy | The default cleanup policy for segments beyond the retention window. A comma-separated list of valid policies. Valid policies are `delete` and `compact`. For tiered storage-enabled clusters, valid policy is `delete` only. | Apache Kafka Default | 
| log.message.timestamp.after.max.ms | The allowable timestamp difference between the message timestamp and the broker's timestamp. The message timestamp can be later than or equal to the broker's timestamp, with the maximum allowable difference determined by the value set in this configuration. If `log.message.timestamp.type=CreateTime`, the message will be rejected if the difference in timestamps exceeds this specified threshold. This configuration is ignored if `log.message.timestamp.type=LogAppendTime`. | 86400000 (24 \* 60 \* 60 \* 1000 ms, that is, 1 day) | 
| log.message.timestamp.before.max.ms | The allowable timestamp difference between the broker's timestamp and the message timestamp. The message timestamp can be earlier than or equal to the broker's timestamp, with the maximum allowable difference determined by the value set in this configuration. If `log.message.timestamp.type=CreateTime`, the message will be rejected if the difference in timestamps exceeds this specified threshold. This configuration is ignored if `log.message.timestamp.type=LogAppendTime`. | 86400000 (24 \* 60 \* 60 \* 1000 ms, that is, 1 day) | 
| log.message.timestamp.type | Specifies if the timestamp in the message is the message creation time or the log append time. The allowed values are `CreateTime` and `LogAppendTime`. | Apache Kafka Default | 
| log.retention.bytes | Maximum size of the log before deleting it. | Apache Kafka Default | 
| log.retention.ms | Number of milliseconds to keep a log file before deleting it. | Apache Kafka Default | 
| max.connection.creation.rate | The maximum connection creation rate allowed in the broker at any time. | Apache Kafka Default | 
| max.connections | The maximum number of connections allowed in the broker at any time. This limit is applied in addition to any per-ip limits configured using `max.connections.per.ip`. | Apache Kafka Default | 
| max.connections.per.ip | The maximum number of connections allowed from each ip address. This can be set to `0` if there are overrides configured using max.connections.per.ip.overrides property. New connections from the ip address are dropped if the limit is reached. | Apache Kafka Default | 
| max.connections.per.ip.overrides | A comma-separated list of per-ip or hostname overrides to the default maximum number of connections. An example value is `hostName:100,127.0.0.1:200` | Apache Kafka Default | 
| message.max.bytes | Largest record batch size that Kafka allows. If you increase this value and there are consumers older than 0.10.2, you must also increase the fetch size of the consumers so that they can fetch record batches this large. The latest message format version always groups messages into batches for efficiency. Previous message format versions don't group uncompressed records into batches, and in such a case, this limit only applies to a single record. You can set this value per topic with the topic level `max.message.bytes` config. | Apache Kafka Default | 
| producer.id.expiration.ms | The time in ms that a topic partition leader will wait before expiring producer IDs. Producer IDs will not expire while a transaction associated to them is still ongoing. Note that producer IDs may expire sooner if the last write from the producer ID is deleted due to the topic's retention settings. Setting this value the same or higher than `delivery.timeout.ms` can help prevent expiration during retries and protect against message duplication, but the default should be reasonable for most use cases. | Apache Kafka Default | 

## Topic-level configurations on Express Brokers
<a name="msk-configuration-express-topic-configuration"></a>

You can use Apache Kafka commands to set or modify topic-level configuration properties for new and existing topics. If you can't give any topic-level, configuration, Amazon MSK uses the broker default. As with broker-level configurations, Amazon MSK protects some of the topic-level configuration properties from change. Examples include replication factor, `min.insync.replicas` and `unclean.leader.election.enable`. If you try to create a topic with a replication factor value other than `3`, Amazon MSK will create the topic with a replication factor of `3` by default. For more information on topic-level configuration properties and examples on how to set them, see [Topic-Level Configs](https://kafka.apache.org/documentation/#topicconfigs) in the Apache Kafka documentation.


| Property | Description | 
| --- | --- | 
| cleanup.policy | This config designates the retention policy to use on log segments. The "delete" policy (which is the default) will discard old segments when their retention time or size limit has been reached. The "compact" policy will enable log compaction, which retains the latest value for each key. It is also possible to specify both policies in a comma-separated list (for example, "delete,compact"). In this case, old segments will be discarded per the retention time and size configuration, while retained segments will be compacted. Compaction on Express brokers is triggered after the data in a partition reaches 256 MB. | 
| compression.type | Specify the final compression type for a given topic. This configuration accepts the standard compression codecs (`gzip`, `snappy`, `lz4`, `zstd`). It additionally accepts `uncompressed` which is equivalent to no compression; and `producer` which means retain the original compression codec set by the producer. | 
| delete.retention.ms | The amount of time to retain delete tombstone markers for log compacted topics. This setting also gives a bound on the time in which a consumer must complete a read if they begin from offset 0 to ensure that they get a valid snapshot of the final stage. Else, delete tombstones might be collected before they complete their scan.<br />The default value for this setting is 86400000 (24 \* 60 \* 60 \* 1000 ms, that is, 1 day), Apache Kafka Default | 
| max.message.bytes | The largest record batch size allowed by Kafka (after compression, if compression is enabled). If this is increased and there are consumers older than `0.10.2`, the consumers' fetch size must also be increased so that they can fetch record batches this large. In the latest message format version, records are always grouped into batches for efficiency. In previous message format versions, uncompressed records are not grouped into batches and this limit only applies to a single record in that case. This can be set per topic with the topic level `max.message.bytes config`. | 
| message.timestamp.after.max.ms | This configuration sets the allowable timestamp difference between the message timestamp and the broker's timestamp. The message timestamp can be later than or equal to the broker's timestamp, with the maximum allowable difference determined by the value set in this configuration. If `message.timestamp.type=CreateTime`, the message will be rejected if the difference in timestamps exceeds this specified threshold. This configuration is ignored if `message.timestamp.type=LogAppendTime`. | 
| message.timestamp.before.max.ms | This configuration sets the allowable timestamp difference between the broker's timestamp and the message timestamp. The message timestamp can be earlier than or equal to the broker's timestamp, with the maximum allowable difference determined by the value set in this configuration. If `message.timestamp.type=CreateTime`, the message will be rejected if the difference in timestamps exceeds this specified threshold. This configuration is ignored if `message.timestamp.type=LogAppendTime`. | 
| message.timestamp.type | Define whether the timestamp in the message is message create time or log append time. The value should be either `CreateTime` or `LogAppendTime` | 
| min.compaction.lag.ms | The minimum time a message will remain uncompacted in the log. This setting is only applicable for logs that are being compacted.<br />The default value for this setting is 0, Apache Kafka Default | 
| max.compaction.lag.ms | The maximum time a message will remain ineligible for compaction in the log. This setting is only applicable for logs that are being compacted. This configuration would be bounded in the range of [7 days, Long.Max].<br />The default value for this setting is 9223372036854775807, Apache Kafka Default. | 
| retention.bytes | This configuration controls the maximum size a partition (which consists of log segments) can grow to before we will discard old log segments to free up space if we are using the "delete" retention policy. By default there is no size limit only a time limit. Since this limit is enforced at the partition level, multiply it by the number of partitions to compute the topic retention in bytes. Additionally, `retention.bytes configuration` operates independently of `segment.ms` and `segment.bytes` configurations. Moreover, it triggers the rolling of new segment if the `retention.bytes` is configured to zero. | 
| retention.ms | This configuration controls the maximum time we will retain a log before we will discard old log segments to free up space if we are using the "delete" retention policy. This represents an SLA on how soon consumers must read their data. If set to `-1`, no time limit is applied. Additionally, `retention.ms` configuration operates independently of `segment.ms` and `segment.bytes` configurations. Moreover, it triggers the rolling of new segment if the `retention.ms` condition is satisfied. | 