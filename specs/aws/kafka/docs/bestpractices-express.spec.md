---
id: "@specs/aws/kafka/docs/bestpractices-express"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Best practices for Express brokers"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Best practices for Express brokers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/bestpractices-express
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Best practices for Express brokers
<a name="bestpractices-express"></a>

This topic outlines some best practices to follow when using Express brokers. Express brokers come pre-configured for high availability and durability. Your data is distributed across three availability zones by default, replication is always set to 3 and the minimum in-sync replica is always set to 2. However, there are still a few factors to consider in order to optimize your cluster's reliability and performance.

## Client-side considerations
<a name="bestpractices-client-considerations"></a>

Your application's availability and performance depeneds not only on server-side settings but on client settings as well.
+ Configure your clients for high availability. In a distributed system like Apache Kafka, ensuring high availability is crucial for maintaining a reliable and fault-tolerant messaging infrastructure. Brokers will go offline for both planned and unplanned events, for example upgrades, patching, hardware failure, and network issues. A Kafka cluster is tolerant of an offline broker, therefore Kafka clients must also handle broker fail-over gracefully. See the full details in [best practice recommendations for Apache Kafka clients](bestpractices-kafka-client.md).
+ Run performance tests to verify that your client configurations allow you to meet your performance objectives even when we restart brokers under peak load. You can reboot brokers in your cluster from the MSK console or using the MSK APIs.

## Server-side considerations
<a name="bestpractices-server-consideration"></a>

**Topics**
+ [Right-size your cluster: Number of brokers per cluster](#brokers-per-express-cluster)
+ [Monitor CPU usage](#bestpractices-monitor-cpu-express)
+ [Right-size your cluster: Number of partitions per Express broker](#partitions-per-express-broker)
+ [Monitor connection count](#monitor-connection-count)
+ [Reassign partitions](#bestpractices-express-reassign-partitions)

### Right-size your cluster: Number of brokers per cluster
<a name="brokers-per-express-cluster"></a>

Choosing the number of brokers for your Express-based cluster is easy. Each Express broker comes with a defined throughput capacity for ingress and egress. You should use this throughput capacity as the primary means for sizing your cluster (and then consider other factors such as partition and connection count, discussed below). 

For example, if your streaming application needs 45 MBps of data ingress (write) and 90 MBps data egress (read) capacity, you can simply use 3 express.m7g.large brokers to meet your throughput needs. Each express.m7g.large broker will handle 15 MBps of of ingress and 30 MBps egress. See the following table for our recommended throughput limits for each Express broker size. If your throughput exceeds the recommended limits, you may experience degraded performance and you should reduce your traffic or scale your cluster. If your throughput exceeds the recommended limits and reaches the per broker quota, MSK will throttle your client traffic to prevent futher overload.

You can also use our see the [MSK Sizing and Pricing](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fdy7oqpxkwhskb.cloudfront.net%2FMSK_Sizing_Pricing.xlsx&wdOrigin=BROWSELINK) spreadsheet to evaluate multiple scenarios and consider other factors, such as partition count.

The following table lists the recommended maximum throughput per broker for each instance size.


| Instance size | Ingress (MBps) | Egress (MBps) | 
| --- | --- | --- | 
| `express.m7g.large` | 15.6 | 31.2 | 
| `express.m7g.xlarge` | 31.2 | 62.5 | 
| `express.m7g.2xlarge` | 62.5 | 125.0 | 
| `express.m7g.4xlarge` | 124.9 | 249.8 | 
| `express.m7g.8xlarge` | 250.0 | 500.0 | 
| `express.m7g.12xlarge` | 375.0 | 750.0 | 
| `express.m7g.16xlarge` | 500.0 | 1000.0 | 

### Monitor CPU usage
<a name="bestpractices-monitor-cpu-express"></a>

We recommend that you maintain the total CPU utilization for your brokers (defined as CPU User \+ CPU System) under 60%. When you have at least 40% of your cluster's total CPU available, Apache Kafka can redistribute CPU load across brokers in the cluster when necessary. This may be required due to planned or unplanned events. An example of a planned event is a cluster version upgrade during which MSK updates brokers in a cluster by restarting them one at a time. An example of an unplanned event is a hardware failure in a broker or, in the worst case, an AZ failure where all brokers in an AZ are affected. When brokers with partition lead replicas go offline, Apache Kafka reassigns partition leadership to redistribute work to other brokers in the cluster. By following this best practice, you can ensure you have enough CPU headroom in your cluster to tolerate operational events like these.

You can use [Using math expressions with CloudWatch metrics](https://docs.aws.amazon.com///AmazonCloudWatch/latest/monitoring/using-metric-math.html) in the *Amazon CloudWatch User Guide* to create a composite metric that is CPU User \+ CPU System. Set an alarm that gets triggered when the composite metric reaches an average CPU utilization of 60%. When this alarm is triggered, scale the cluster using one of the following options:
+ Option 1: [Update your broker size](msk-update-broker-type.md) to the next larger size. Keep in mind that when you update the broker size in the cluster, Amazon MSK takes brokers offline in a rolling fashion and temporarily reassigns partition leadership to other brokers.
+ Option 2: [Expand your cluster by adding brokers](msk-update-broker-count.md), then reassigning existing partitions using the partition reassignment tool named `kafka-reassign-partitions.sh`.

**Other recommendations**
+ Monitor total CPU utilization per broker as a proxy for load distribution. If brokers have consistently uneven CPU utilization, it might be a sign that load isn't evenly distributed within the cluster. We recommend using [Cruise Control](cruise-control.md) to continuously manage load distribution via partition assignment.
+ Monitor produce and consume latency. Produce and consume latency can increase linearly with CPU utilization.
+ JMX scrape interval: If you enable open monitoring with the Prometheus feature, it is recommended that you use a 60 second or higher scrape interval (`scrape_interval: 60s`) for your Prometheus host configuration (`prometheus.yml`). Lowering the scrape interval can lead to high CPU usage on your cluster.

### Right-size your cluster: Number of partitions per Express broker
<a name="partitions-per-express-broker"></a>

If you have high partition, low throughput use cases where you have higher partition counts, but you aren't sending traffic across all partitions, you can pack more partitions per broker, as long as you have performed sufficient testing and performance testing to validate that your cluster remains healthy with the higher partition count. If the number of partitions per broker exceeds the maxiumum allowed value and your cluster becomes overloaded, you'll be prevented from performing the following operations:
+ Update the cluster configuration
+ Update the cluster to a smaller broker size
+ Associate an AWS Secrets Manager secret with a cluster that has SASL/SCRAM authentication

A cluster overloaded with a high number of partitions can also result in missing Kafka metrics on CloudWatch and on Prometheus scraping.

For guidance on choosing the number of partitions, see [Apache Kafka Supports 200K Partitions Per Cluster](https://blogs.apache.org/kafka/entry/apache-kafka-supports-more-partitions). We also recommend that you perform your own testing to determine the right size for your brokers. For more information about the different broker sizes, see [Amazon MSK broker sizes](broker-instance-sizes.md).

For information about the recommended number of partitions (including leader and follower replicas) for each Express broker, see [Express broker partition quota](limits.md#msk-express-broker-partition-quota). The recommended number of partitions aren't enforced and are a best practice for scenarios where you're sending traffic across all provisioned topic partitions.

### Monitor connection count
<a name="monitor-connection-count"></a>

The client connections to your brokers consume system resources such as memory and CPU. Depending on your authentication mechanism, you should monitor to ensure you are within the applicable limits. To handle retries on failed connections, you can set the `reconnect.backoff.ms` configuration parameter on the client side. For example, if you want a client to retry connections after 1 second, set `reconnect.backoff.ms` to `1000`. For more information about configuring retries, see [Apache Kafka documentation](bestpractices-kafka-client.md#bestpractices-kafka-client-client-availability).


****  

| Dimension | Quota | 
| --- | --- | 
| Maximum TCP connections per broker ([IAM Access control](iam-access-control.md)) | 3000 | 
| Maximum TCP connections per broker (IAM) | 100 per second | 
| Maximum TCP connections per broker (non-IAM) | MSK does not enforce connection limits for non-IAM auth. You should however monitor other metrics such as CPU and memory usage to ensure you do not overload your cluster because of excessive connections. | 

### Reassign partitions
<a name="bestpractices-express-reassign-partitions"></a>

To move partitions to different brokers on the same MSK Provisioned cluster, you can use the partition reassignment tool named `kafka-reassign-partitions.sh`. We recommend that you don't reassign more than 20 partitions in a single `kafka-reassign-partitions` call for safe operations. For example, after you add new brokers to expand a cluster or to move partitions in order to removing brokers, you can rebalance that cluster by reassigning partitions to the new brokers. For information about how to add brokers to an MSK Provisioned cluster, see [Expand the number of brokers in an Amazon MSK cluster](msk-update-broker-count.md). For information about how to remove brokers from an MSK Provisioned cluster, see [Remove a broker from an Amazon MSK cluster](msk-remove-broker.md). For information about the partition reassignment tool, see [Expanding your cluster](https://kafka.apache.org/documentation/#basic_ops_cluster_expansion) in the Apache Kafka documentation.