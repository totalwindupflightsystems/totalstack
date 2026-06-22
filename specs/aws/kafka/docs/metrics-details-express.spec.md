---
id: "@specs/aws/kafka/docs/metrics-details-express"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CloudWatch metrics for Express brokers"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# CloudWatch metrics for Express brokers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/metrics-details-express
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon MSK metrics for monitoring Express brokers with CloudWatch
<a name="metrics-details-express"></a>

Amazon MSK integrates with CloudWatch so that you can collect, view, and analyze CloudWatch metrics for your MSK Express brokers. The metrics that you configure for your MSK Provisioned clusters are automatically collected and pushed to CloudWatch at 1 minute intervals. You can set the monitoring level for an MSK Provisioned cluster to one of the following: `DEFAULT`, `PER_BROKER`, `PER_TOPIC_PER_BROKER`, or `PER_TOPIC_PER_PARTITION`. The tables in the following sections show the metrics that are available starting at each monitoring level.

`DEFAULT`-level metrics are free. Pricing for other metrics is described in the [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) page.

## `DEFAULT` Level monitoring for Express brokers
<a name="express-default-metrics"></a>

The metrics described in the following table are available free of cost at the `DEFAULT` monitoring level.


| Name | When visible | Dimensions | Description | 
| --- | --- | --- | --- | 
| ActiveControllerCount | After the cluster gets to the ACTIVE state. | Cluster Name | Only one controller per cluster should be active at any given time. | 
| BytesInPerSec | After you create a topic. | Cluster Name, Broker ID, Topic | The number of bytes per second received from clients. This metric is available per broker and also per topic. | 
| BytesOutPerSec | After you create a topic. | Cluster Name, Broker ID, Topic | The number of bytes per second sent to clients. This metric is available per broker and also per topic. | 
| ClientConnectionCount | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID, Client Authentication | The number of active authenticated client connections. | 
| ConnectionCount | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of active authenticated, unauthenticated, and inter-broker connections. | 
| CpuIdle | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The percentage of CPU idle time. | 
| CpuSystem | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The percentage of CPU in kernel space. | 
| CpuUser | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The percentage of CPU in user space. | 
| GlobalPartitionCount | After the cluster gets to the ACTIVE state. | Cluster Name | The number of partitions across all topics in the cluster, excluding replicas. Because `GlobalPartitionCount` doesn't include replicas, the sum of the `PartitionCount` values can be higher than `GlobalPartitionCount` if the replication factor for a topic is greater than `1`. | 
| GlobalTopicCount | After the cluster gets to the ACTIVE state. | Cluster Name | Total number of topics across all brokers in the cluster. | 
| EstimatedMaxTimeLag\* | After consumer group consumes from a topic. | Consumer Group, Topic | Time estimate (in seconds) to drain `MaxOffsetLag`. | 
| LeaderCount | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The total number of leaders of partitions per broker, not including replicas. | 
| MaxOffsetLag\* | After consumer group consumes from a topic. | Consumer Group, Topic | The maximum offset lag across all partitions in a topic. | 
| MemoryBuffered | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The size in bytes of buffered memory for the broker. | 
| MemoryCached | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The size in bytes of cached memory for the broker. | 
| MemoryFree | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The size in bytes of memory that is free and available for the broker. | 
| MemoryUsed | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The size in bytes of memory that is in use for the broker. | 
| MessagesInPerSec | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of incoming messages per second for the broker. | 
| NetworkRxDropped | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of dropped receive packages. | 
| NetworkRxErrors | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of network receive errors for the broker. | 
| NetworkRxPackets | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of packets received by the broker. | 
| NetworkTxDropped | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of dropped transmit packages. | 
| NetworkTxErrors | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of network transmit errors for the broker. | 
| NetworkTxPackets | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The number of packets transmitted by the broker. | 
| PartitionCount | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The total number of topic partitions per broker, including replicas. | 
| ProduceTotalTimeMsMean | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The mean produce time in milliseconds. | 
| RequestBytesMean | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | The mean number of request bytes for the broker. | 
| RequestTime | After request throttling is applied. | Cluster Name, Broker ID | The average time in milliseconds spent in broker network and I/O threads to process requests. | 
| RollingEstimatedTimeLagMax\* | After consumer group consumes from a topic. | Consumer Group, Topic | Rolling maximum time estimate (in seconds) to drain the partition offset lag across all partitions in a topic. | 
| StorageUsed | After the cluster gets to the ACTIVE state. | Cluster Name | The total storage used across all partitions in the cluster, excluding replicas. | 
| SumOffsetLag\* | After consumer group consumes from a topic. | Consumer Group, Topic | The aggregated offset lag for all the partitions in a topic. | 
| UserPartitionExists | After the cluster gets to the ACTIVE state. | Cluster Name, Broker ID | Boolean metric that indicates the presence of a user-owned partition on a broker. A value of 1 indicates the presence of partitions on the broker. | 

\* Consumer lag metrics require ASCII-only consumer group names and have specific emission requirements. For more information, see [Monitor consumer lags](consumer-lag.md).

## `PER_BROKER` Level monitoring for Express brokers
<a name="express-per-broker-metrics"></a>

When you set the monitoring level to `PER_BROKER`, you get the metrics described in the following table in addition to all the `DEFAULT` level metrics. You pay for the metrics in the following table, whereas the `DEFAULT` level metrics continue to be free of charge. The metrics in this table have the following dimensions: Cluster Name, Broker ID.


| Name | When visible | Description | 
| --- | --- | --- | 
| ConnectionCloseRate | After the cluster gets to the ACTIVE state. | The number of connections closed per second per listener. This number is aggregated per listener and filtered for the client listeners. | 
| ConnectionCreationRate | After the cluster gets to the ACTIVE state. | The number of new connections established per second per listener. This number is aggregated per listener and filtered for the client listeners. | 
| FetchConsumerLocalTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds that the consumer request is processed at the leader. | 
| FetchConsumerRequestQueueTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds that the consumer request waits in the request queue. | 
| FetchConsumerResponseQueueTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds that the consumer request waits in the response queue. | 
| FetchConsumerResponseSendTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds for the consumer to send a response. | 
| FetchConsumerTotalTimeMsMean | After there's a producer/consumer. | The mean total time in milliseconds that consumers spend on fetching data from the broker. | 
| FetchFollowerLocalTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds that the follower request is processed at the leader. | 
| FetchFollowerRequestQueueTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds that the follower request waits in the request queue. | 
| FetchFollowerResponseQueueTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds that the follower request waits in the response queue. | 
| FetchFollowerResponseSendTimeMsMean | After there's a producer/consumer. | The mean time in milliseconds for the follower to send a response. | 
| FetchFollowerTotalTimeMsMean | After there's a producer/consumer. | The mean total time in milliseconds that followers spend on fetching data from the broker. | 
| FetchThrottleByteRate | After bandwidth throttling is applied. | The number of throttled bytes per second. | 
| FetchThrottleQueueSize | After bandwidth throttling is applied. | The number of messages in the throttle queue. | 
| FetchThrottleTime | After bandwidth throttling is applied. | The average fetch throttle time in milliseconds. | 
| IAMNumberOfConnectionRequests | After the cluster gets to the ACTIVE state. | The number of IAM authentication requests per second. | 
| IAMTooManyConnections | After the cluster gets to the ACTIVE state. | The number of connections attempted beyond 100. `0` means the number of connections is within the limit. If `>0`, the throttle limit is being exceeded and you need to reduce number of connections. | 
| NetworkProcessorAvgIdlePercent | After the cluster gets to the ACTIVE state. | The average percentage of the time the network processors are idle. | 
| ProduceLocalTimeMsMean | After the cluster gets to the ACTIVE state. | The mean time in milliseconds that the request is processed at the leader. | 
| ProduceRequestQueueTimeMsMean | After the cluster gets to the ACTIVE state. | The mean time in milliseconds that request messages spend in the queue. | 
| ProduceResponseQueueTimeMsMean | After the cluster gets to the ACTIVE state. | The mean time in milliseconds that response messages spend in the queue. | 
| ProduceResponseSendTimeMsMean | After the cluster gets to the ACTIVE state. | The mean time in milliseconds spent on sending response messages. | 
| ProduceThrottleByteRate | After bandwidth throttling is applied. | The number of throttled bytes per second. | 
| ProduceThrottleQueueSize | After bandwidth throttling is applied. | The number of messages in the throttle queue. | 
| ProduceThrottleTime | After bandwidth throttling is applied. | The average produce throttle time in milliseconds. | 
| ProduceTotalTimeMsMean | After the cluster gets to the ACTIVE state. | The mean produce time in milliseconds. | 
| ReplicationBytesInPerSec | After you create a topic. | The number of bytes per second received from other brokers. | 
| ReplicationBytesOutPerSec | After you create a topic. | The number of bytes per second sent to other brokers. | 
| RequestExemptFromThrottleTime | After request throttling is applied. | The average time in milliseconds spent in broker network and I/O threads to process requests that are exempt from throttling. | 
| RequestHandlerAvgIdlePercent | After the cluster gets to the ACTIVE state. | The average percentage of the time the request handler threads are idle. | 
| RequestThrottleQueueSize | After request throttling is applied. | The number of messages in the throttle queue. | 
| RequestThrottleTime | After request throttling is applied. | The average request throttle time in milliseconds. | 
| TcpConnections | After the cluster gets to the ACTIVE state. | Shows number of incoming and outgoing TCP segments with the SYN flag set. | 
| TrafficBytes | After the cluster gets to the ACTIVE state. | Shows network traffic in overall bytes between clients (producers and consumers) and brokers. Traffic between brokers isn't reported. | 

## `PER_TOPIC_PER_PARTITION` level monitoring for Express brokers
<a name="express-per-topic-per-partition-metrics"></a>

When you set the monitoring level to `PER_TOPIC_PER_PARTITION`, you get the metrics described in the following table, in addition to all the metrics from the `PER_TOPIC_PER_BROKER`, `PER_BROKER`, and `DEFAULT` levels. Only the `DEFAULT` level metrics are free of charge. The metrics in this table have the following dimensions: Consumer Group, Topic, Partition.


| Name | When visible | Description | 
| --- | --- | --- | 
| EstimatedTimeLag\* | After consumer group consumes from a topic. | Time estimate (in seconds) to drain the partition offset lag. | 
| OffsetLag\* | After consumer group consumes from a topic. | Partition-level consumer lag in number of offsets. | 
| RollingEstimatedTimeLag\* | After consumer group consumes from a topic. | Rolling time estimate (in seconds) to drain the partition offset lag. | 

\* Consumer lag metrics require ASCII-only consumer group names and have specific emission requirements. For more information, see [Monitor consumer lags](consumer-lag.md).

## `PER_TOPIC_PER_BROKER` level monitoring for Express brokers
<a name="express-per-topic-per-broker-metrics"></a>

When you set the monitoring level to `PER_TOPIC_PER_BROKER`, you get the metrics described in the following table, in addition to all the metrics from the `PER_BROKER` and `DEFAULT` levels. Only the `DEFAULT` level metrics are free of charge. The metrics in this table have the following dimensions: Cluster Name, Broker ID, Topic.

**Important**  
The metrics in the following table appear only after their values become nonzero for the first time. For example, to see BytesInPerSec, one or more producers must first send data to the cluster.


| Name | When visible | Description | 
| --- | --- | --- | 
| MessagesInPerSec | After you create a topic. | The number of messages received per second. | 