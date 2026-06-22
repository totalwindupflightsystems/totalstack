---
id: "@specs/aws/kafka/docs/msk-default-configuration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Default Amazon MSK configuration"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Default Amazon MSK configuration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-default-configuration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Default Amazon MSK configuration
<a name="msk-default-configuration"></a>

When you create an MSK cluster and don't specify a custom MSK configuration, Amazon MSK creates and uses a default configuration with the values shown in the following table. For properties that aren't in this table, Amazon MSK uses the defaults associated with your version of Apache Kafka. For a list of these default values, see [Apache Kafka Configuration](https://kafka.apache.org/documentation/#configuration). 


| Name | Description | Default value for non-tiered storage cluster | Default value for tiered storage-enabled cluster | 
| --- | --- | --- | --- | 
| allow.everyone.if.no.acl.found | If no resource patterns match a specific resource, the resource has no associated ACLs. In this case, if you set this property to true, all users can access the resource, not just the super users. | true | true | 
| auto.create.topics.enable | Enables autocreation of a topic on the server. | false | false | 
| auto.leader.rebalance.enable | Enables auto leader balancing. A background thread checks and initiates leader balance at regular intervals, if necessary. | true | true | 
| default.replication.factor | Default replication factors for automatically created topics. | 3 for clusters in 3 Availability Zones, and 2 for clusters in 2 Availability Zones. | 3 for clusters in 3 Availability Zones, and 2 for clusters in 2 Availability Zones. | 
| local.retention.bytes | The maximum size of local log segments for a partition before it deletes the old segments. If you don't set this value, the value in log.retention.bytes is used. The effective value should always be less than or equal to the log.retention.bytes value. The default value of -2 indicates that there is no limit on local retention. This corresponds to the retention.ms/bytes setting of -1. The properties local.retention.ms and local.retention.bytes are similar to log.retention as they are used to determine how long the log segments should remain in local storage. Existing log.retention.\* configurations are retention configurations for the topic partition. This includes both local and remote storage. Valid values: integers in [-2; \+Inf] | -2 for unlimited | -2 for unlimited | 
| local.retention.ms | The number of milliseconds to retain the local log segment before deletion. If you don't set this value, Amazon MSK uses the value in log.retention.ms. The effective value should always be less than or equal to the log.retention.bytes value. The default value of -2 indicates that there is no limit on local retention. This corresponds to the retention.ms/bytes setting of -1.The values local.retention.ms and local.retention.bytes are similar to log.retention. MSK uses this configuration to determine how long the log segments should remain in local storage. Existing log.retention.\* configurations are retention configurations for the topic partition. This includes both local and remote storage. Valid values are integers greater than 0. | -2 for unlimited | -2 for unlimited | 
| log.message.timestamp.difference.max.ms | This configuration is deprecated in Kafka 3.6.0. Two configurations, log.message.timestamp.before.max.ms and log.message.timestamp.after.max.ms, have been added. The maximum difference allowed between the timestamp when a broker receives a message and the timestamp specified in the message. If log.message.timestamp.type=CreateTime, a message will be rejected if the difference in timestamp exceeds this threshold. This configuration is ignored if log.message.timestamp.type=LogAppendTime. The maximum timestamp difference allowed should be no greater than log.retention.ms to avoid unnecessarily frequent log rolling. | 9223372036854775807 | 86400000 for Kafka 2.8.2.tiered and Kafka 3.7.x tiered. | 
| log.segment.bytes | The maximum size of a single log file. | 1073741824 | 134217728 | 
| min.insync.replicas | When a producer sets the value of acks (acknowledgement producer gets from Kafka broker) to `"all"` (or `"-1"`), the value in min.insync.replicas specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful. If this value doesn't meet this minimum, the producer raises an exception (either NotEnoughReplicas or NotEnoughReplicasAfterAppend).<br />When you use the values in min.insync.replicas and acks together, you can enforce greater durability guarantees. For example, you might create a topic with a replication factor of 3, set min.insync.replicas to 2, and produce with acks of `"all"`. This ensures that the producer raises an exception if a majority of replicas don't receive a write. | 2 for clusters in 3 Availability Zones, and 1 for clusters in 2 Availability Zones. | 2 for clusters in 3 Availability Zones, and 1 for clusters in 2 Availability Zones. | 
| num.io.threads | Number of threads that the server uses to produce requests, which may include disk I/O. | 8 | max(8, vCPUs) where vCPUs depends on the instance size of broker | 
| num.network.threads | Number of threads that the server uses to receive requests from the network and send responses to the network. | 5 | max(5, vCPUs / 2) where vCPUs depends on the instance size of broker | 
| num.partitions | Default number of log partitions per topic. | 1 | 1 | 
| num.replica.fetchers | Number of fetcher threads used to replicate messages from a source broker.If you increase this value, you can increase the degree of I/O parallelism in the follower broker. | 2 | max(2, vCPUs / 4) where vCPUs depends on the instance size of broker | 
| remote.log.msk.disable.policy | Used with remote.storage.enable to disable tiered storage. Set this policy to Delete, to indicate that data in tiered storage is deleted when you set remote.storage.enable to false. | N/A | None | 
| remote.log.reader.threads | Remote log reader thread pool size, which is used in scheduling tasks to fetch data from remote storage. | N/A | max(10, vCPUs \* 0.67) where vCPUs depends on the instance size of broker | 
| remote.storage.enable | Enables tiered (remote) storage for a topic if set to true. Disables topic level tiered storage if set to false and remote.log.msk.disable.policy is set to Delete. When you disable tiered storage, you delete data from remote storage. When you disable tiered storage for a topic, you can't enable it again. | false | false | 
| replica.lag.time.max.ms | If a follower hasn't sent any fetch requests or hasn't consumed up to the leader's log end offset for at least this number of milliseconds, the leader removes the follower from the ISR. | 30000 | 30000 | 
| retention.ms | Mandatory field. Minimum time is 3 days. There is no default because the setting is mandatory.<br />Amazon MSK uses the retention.ms value with local.retention.ms to determine when data moves from local to tiered storage. The local.retention.ms value specifies when to move data from local to tiered storage. The retention.ms value specifies when to remove data from tiered storage (that is, removed from the cluster). Valid values: integers in [-1; \+Inf] | Minimum 259,200,000 milliseconds (3 days). -1 for infinite retention. | Minimum 259,200,000 milliseconds (3 days). -1 for infinite retention. | 
| socket.receive.buffer.bytes | The SO\_RCVBUF buffer of the socket sever sockets. If the value is -1, the OS default is used. | 102400 | 102400 | 
| socket.request.max.bytes | Maximum number of bytes in a socket request. | 104857600 | 104857600 | 
| socket.send.buffer.bytes | The SO\_SNDBUF buffer of the socket sever sockets. If the value is -1, the OS default is used. | 102400 | 102400 | 
| unclean.leader.election.enable | Indicates if you want replicas not in the ISR set to serve as leader as a last resort, even though this might result in data loss. | true | false | 
| zookeeper.session.timeout.ms | The Apache ZooKeeper session timeout in milliseconds. | 18000 | 18000 | 
| zookeeper.set.acl | The set client to use secure ACLs. | false | false | 

For information about how to specify custom configuration values, see [Custom Amazon MSK configurations](msk-configuration-properties.md).