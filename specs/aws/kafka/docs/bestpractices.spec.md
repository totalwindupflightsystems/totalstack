---
id: "@specs/aws/kafka/docs/bestpractices"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Best practices for Standard brokers"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Best practices for Standard brokers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/bestpractices
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Best practices for Standard brokers
<a name="bestpractices"></a>

This topic outlines some best practices to follow when using Amazon MSK. For information about Amazon MSK Replicator best practices, see [Best practices](msk-replicator-best-practices.md).

## Client-side considerations
<a name="bestpractices-client-side-considerations"></a>

Your application's availability and performance depends not only on server-side settings but on client settings as well.
+ Configure your clients for high availability. In a distributed system like Apache Kafka, ensuring high availability is crucial for maintaining a reliable and fault-tolerant messaging infrastructure. Brokers will go offline for both planned and unplanned events, for example upgrades, patching, hardware failure, and network issues. A Kafka cluster is tolerant of an offline broker, therefore Kafka clients must also handle broker fail-over gracefully. See the full details on [Best practices for Apache Kafka clients](bestpractices-kafka-client.md).
+ Ensure client connection strings include at least one broker from each availability zone. Having multiple brokers in a client's connection string allows for failover when a specific broker is offline for an update. For information about how to get a connection string with multiple brokers, see [Get the bootstrap brokers for an Amazon MSK cluster](msk-get-bootstrap-brokers.md).
+ Run performance tests to verify that your client configurations allow you to meet your performance objectives.

## Server-side considerations
<a name="standard-server-side-considerations"></a>

### Right-size your cluster: Number of partitions per Standard broker
<a name="partitions-per-broker"></a>

The following table shows the recommended number of partitions (including leader and follower replicas) per Standard broker. The recommended number of partitions are not enforced and are a best practice for scenarios where you are sending traffic across all provisioned topic partitions.


| Broker size | Recommended number of partitions (including leader and follower replicas) per broker | Maximum number of partitions that support update operations | 
| --- | --- | --- | 
| kafka.t3.small | 300 | 300 | 
| kafka.m5.large or kafka.m5.xlarge | 1000 | 1500 | 
| kafka.m5.2xlarge | 2000 | 3000 | 
| kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, or kafka.m5.24xlarge | 4000 | 6000 | 
| kafka.m7g.large or kafka.m7g.xlarge | 1000 | 1500 | 
| kafka.m7g.2xlarge | 2000 | 3000 | 
| kafka.m7g.4xlarge, kafka.m7g.8xlarge, kafka.m7g.12xlarge, or kafka.m7g.16xlarge | 4000 | 6000 | 

If you have high partition, low throughput use cases where you have higher partition counts, but you are not sending traffic across all partitions, you can pack more partitions per broker, as long as you have performed sufficient testing and performance testing to validate that your cluster remains healthy with the higher partition count. If the number of partitions per broker exceeds the maximum allowed value and your cluster becomes overloaded, you will be prevented from performing the following operations:
+ Update the cluster configuration
+ Update the cluster to a smaller broker size
+ Associate an AWS Secrets Manager secret with a cluster that has SASL/SCRAM authentication

A high number of partitions can also result in missing Kafka metrics on CloudWatch and on Prometheus scraping.

For guidance on choosing the number of partitions, see [Apache Kafka Supports 200K Partitions Per Cluster](https://blogs.apache.org/kafka/entry/apache-kafka-supports-more-partitions). We also recommend that you perform your own testing to determine the right size for your brokers. For more information about the different broker sizes, see [Amazon MSK broker types](broker-instance-types.md). 

### Right-size your cluster: Number of Standard brokers per cluster
<a name="brokers-per-cluster"></a>

To determine the right number of Standard brokers for your MSK Provisioned cluster and understand costs, see the [MSK Sizing and Pricing](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fdy7oqpxkwhskb.cloudfront.net%2FMSK_Sizing_Pricing.xlsx&wdOrigin=BROWSELINK) spreadsheet. This spreadsheet provides an estimate for sizing an MSK Provisioned cluster and the associated costs of Amazon MSK compared to a similar, self-managed, EC2-based Apache Kafka cluster. For more information about the input parameters in the spreadsheet, hover over the parameter descriptions. Estimates provided by this sheet are conservative and provide a starting point for a new MSK Provisioned cluster. Cluster performance, size, and costs are dependent on your use case and we recommend that you verify them with actual testing.

To understand how the underlying infrastructure affects Apache Kafka performance, see [Best practices for right-sizing your Apache Kafka clusters to optimize performance and cost](https://aws.amazon.com/blogs/big-data/best-practices-for-right-sizing-your-apache-kafka-clusters-to-optimize-performance-and-cost/) in the AWS Big Data Blog. The blog post provides information about how to size your clusters to meet your throughput, availability, and latency requirements. It also provides answers to questions, such as when you should scale *up* versus scale *out*, and guidance about how to continuously verify the size of your production clusters. For information about tiered storage based clusters, see [Best practices for running production workloads using Amazon MSK tiered storage](https://aws.amazon.com/blogs/big-data/best-practices-for-running-production-workloads-using-amazon-msk-tiered-storage/).

### Optimize cluster throughput for m5.4xl, m7g.4xl or larger instances
<a name="optimize-broker-threads"></a>

When using m5.4xl, m7g.4xl, or larger instances, you can optimize the MSK Provisioned cluster throughput by tuning the num.io.threads and num.network.threads configurations.

Num.io.threads is the number of threads that a Standard broker uses for processing requests. Adding more threads, up to the number of CPU cores supported for the instance size, can help improve cluster throughput.

Num.network.threads is the number of threads the Standard broker uses for receiving all incoming requests and returning responses. Network threads place incoming requests on a request queue for processing by io.threads. Setting num.network.threads to half the number of CPU cores supported for the instance size allows for full usage of the new instance size.

**Important**  
Do not increase num.network.threads without first increasing num.io.threads as this can lead to congestion related to queue saturation.

The following table describes the recommended settings for each instance size.


| Instance size | Recommended value for num.io.threads | Recommended value for num.network.threads | 
| --- | --- | --- | 
| m5.4xl | 16 | 8 | 
| m5.8xl | 32 | 16 | 
| m5.12xl | 48 | 24 | 
| m5.16xl | 64 | 32 | 
| m5.24xl | 96 | 48 | 
| m7g.4xlarge | 16 | 8 | 
| m7g.8xlarge | 32 | 16 | 
| m7g.12xlarge | 48 | 24 | 
| m7g.16xlarge | 64 | 32 | 

### Use latest Kafka AdminClient to avoid topic ID mismatch issue
<a name="topic-id-mismatch"></a>

The ID of a topic is lost (Error: does not match the topic Id for partition) when you use a Kafka AdminClient version lower than 2.8.0 with the flag `--zookeeper` to increase or reassign topic partitions for an MSK Provisioned cluster using Kafka version 2.8.0 or higher. Note that the `--zookeeper` flag is deprecated in Kafka 2.5 and is removed starting with Kafka 3.0. See [Upgrading to 2.5.0 from any version 0.8.x through 2.4.x](https://kafka.apache.org/documentation.html#upgrade_2_5_0).

To prevent topic ID mismatch, use a Kafka client version 2.8.0 or higher for Kafka admin operations. Alternatively, clients 2.5 and higher can use the `--bootstrap-servers` flag instead of the `--zookeeper` flag.

### Build highly available clusters
<a name="ensure-high-availability"></a>

Use the following recommendations so that your MSK Provisioned clusters can be highly available during an update (such as when you're updating the broker size or Apache Kafka version, for example) or when Amazon MSK is replacing a broker.
+ Set up a three-AZ cluster.
+ Ensure that the replication factor (RF) is at least 3. Note that a RF of 1 can lead to offline partitions during a rolling update; and a RF of 2 may lead to data loss.
+ Set minimum in-sync replicas (minISR) to at most RF - 1. A minISR that is equal to the RF can prevent producing to the cluster during a rolling update. A minISR of 2 allows three-way replicated topics to be available when one replica is offline.

### Monitor CPU usage
<a name="bestpractices-monitor-cpu"></a>

Amazon MSK strongly recommends that you maintain the CPU utilization for your brokers (defined as `CPU User + CPU System`) under 60%. This ensures that your cluster retains sufficient CPU headroom to handle operational events, such as broker failures, patching, and rolling upgrades.

Apache Kafka can redistribute CPU load across brokers in the cluster when necessary. For example, when Amazon MSK detects and recovers from a broker fault, it performs automatic maintenance, such as patching. Similarly, when a user requests a broker-size change or version upgrade, Amazon MSK initiates rolling workflows that take one broker offline at a time. When brokers with lead partitions go offline, Apache Kafka reassigns partition leadership to redistribute work to other brokers in the cluster. By following this best practice, you ensure sufficient CPU headroom to tolerate these operational events.

**Note**  
While monitoring CPU utilization, be aware that total CPU usage includes more than `CPU User` and `CPU System`. Other categories, such as `iowait`, `irq`, `softirq`, and `steal`, also contribute to overall CPU activity. Consequently, CPU Idle *isn't always equal* to `100% - CPU User - CPU System`.

You can use [Amazon CloudWatch metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) to create a composite metric (`CPU User + CPU System`), and set an alarm to trigger when the average usage exceeds 60%. When triggered, consider scaling the cluster using one of the following options:
+ Option 1 (recommended): [Update your broker size](https://docs.aws.amazon.com//msk/latest/developerguide/msk-update-broker-type.html) to the next larger size. For example, if the current size is `kafka.m5.large`, update the cluster to use `kafka.m5.xlarge`. Keep in mind that when you update the broker size in the cluster, Amazon MSK takes brokers offline in a rolling fashion and temporarily reassigns partition leadership to other brokers. A size update typically takes 10-15 minutes per broker.
+ Option 2: If there are topics with all messages ingested from producers that use round-robin writes (in other words, messages aren't keyed and ordering isn't important to consumers), [expand your cluster](https://docs.aws.amazon.com//msk/latest/developerguide/msk-update-broker-count.html) by adding brokers. Also add partitions to existing topics with the highest throughput. Next, use `kafka-topics.sh --describe` to ensure that newly added partitions are assigned to the new brokers. The main benefit of this option compared to the previous one is that you can manage resources and costs more granularly. Additionally, you can use this option if CPU load significantly exceeds 60% because this form of scaling doesn't typically result in increased load on existing brokers.
+ Option 3: Expand your MSK Provisioned cluster by adding brokers, then reassign existing partitions by using the partition reassignment tool named `kafka-reassign-partitions.sh`. However, if you use this option, the cluster will need to spend resources to replicate data from broker to broker after partitions are reassigned. Compared to the two previous options, this can significantly increase the load on the cluster at first. As a result, Amazon MSK doesn't recommend using this option when CPU utilization is above 70% because replication causes additional CPU load and network traffic. Amazon MSK only recommends using this option if the two previous options aren't feasible.

Other recommendations: 
+ Monitor total CPU utilization per broker as a proxy for load distribution. If brokers have consistently uneven CPU utilization it might be a sign that load isn't evenly distributed within the cluster. We recommend using [Cruise Control](https://docs.aws.amazon.com//msk/latest/developerguide/cruise-control.html) to continuously manage load distribution via partition assignment.
+ Monitor produce and consume latency. Produce and consume latency can increase linearly with CPU utilization.
+ **JMX scrape interval**: If you enable open monitoring with the [Prometheus feature](https://docs.aws.amazon.com/msk/latest/developerguide/open-monitoring.html), it is recommended that you use a 60 second or higher scrape interval (scrape\_interval: 60s) for your Prometheus host configuration (prometheus.yml). Lowering the scrape interval can lead to high CPU usage on your cluster. 

### Monitor disk space
<a name="bestpractices-monitor-disk-space"></a>

To avoid running out of disk space for messages, create a CloudWatch alarm that watches the `KafkaDataLogsDiskUsed` metric. When the value of this metric reaches or exceeds 85%, perform one or more of the following actions:
+ Use [Automatic scaling for Amazon MSK clusters](msk-autoexpand.md). You can also manually increase broker storage as described in [Manual scaling for Standard brokers](manually-expand-storage.md).
+ Reduce the message retention period or log size. For information on how to do that, see [Adjust data retention parameters](#bestpractices-retention-period).
+ Delete unused topics.

For information on how to set up and use alarms, see [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html). For a full list of Amazon MSK metrics, see [Monitor an Amazon MSK Provisioned cluster](monitoring.md).

### Adjust data retention parameters
<a name="bestpractices-retention-period"></a>

Consuming messages doesn't remove them from the log. To free up disk space regularly, you can explicitly specify a retention time period, which is how long messages stay in the log. You can also specify a retention log size. When either the retention time period or the retention log size are reached, Apache Kafka starts removing inactive segments from the log.

To specify a retention policy at the cluster level, set one or more of the following parameters: `log.retention.hours`, `log.retention.minutes`, `log.retention.ms`, or `log.retention.bytes`. For more information, see [Custom Amazon MSK configurations](msk-configuration-properties.md).

You can also specify retention parameters at the topic level:
+ To specify a retention time period per topic, use the following command.

  ```
  kafka-configs.sh --bootstrap-server $bs --alter --entity-type topics --entity-name {{TopicName}} --add-config retention.ms={{DesiredRetentionTimePeriod}}
  ```
+ To specify a retention log size per topic, use the following command.

  ```
  kafka-configs.sh --bootstrap-server $bs --alter --entity-type topics --entity-name {{TopicName}} --add-config retention.bytes={{DesiredRetentionLogSize}}
  ```

The retention parameters that you specify at the topic level take precedence over cluster-level parameters.

### Speeding up log recovery after unclean shutdown
<a name="bestpractices-log-recovery-thread"></a>

After an unclean shutdown, a broker can take a while to restart as it does log recovery. By default, Kafka only uses a single thread per log directory to perform this recovery. For example, if you have thousands of partitions, log recovery can take hours to complete. To speed up log recovery, it's recommended to increase the number of threads using configuration property [https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html). You can set it to the number of CPU cores.

### Monitor Apache Kafka memory
<a name="bestpractices-monitor-memory"></a>

We recommend that you monitor the memory that Apache Kafka uses. Otherwise, the cluster may become unavailable.

To determine how much memory Apache Kafka uses, you can monitor the `HeapMemoryAfterGC` metric. `HeapMemoryAfterGC` is the percentage of total heap memory that is in use after garbage collection. We recommend that you create a CloudWatch alarm that takes action when `HeapMemoryAfterGC` increases above 60%. 

The steps that you can take to decrease memory usage vary. They depend on the way that you configure Apache Kafka. For example, if you use transactional message delivery, you can decrease the `transactional.id.expiration.ms` value in your Apache Kafka configuration from `604800000` ms to `86400000` ms (from 7 days to 1 day). This decreases the memory footprint of each transaction.

### Don't add non-MSK brokers
<a name="bestpractices-non-msk-brokers"></a>

For ZooKeeper-based MSK Provisioned clusters, if you use Apache ZooKeeper commands to add brokers, these brokers don't get added to your MSK Provisioned cluster, and your Apache ZooKeeper will contain incorrect information about the cluster. This might result in data loss. For supported MSK Provisioned cluster operations, see [Amazon MSK key features and concepts](operations.md).

### Enable in-transit encryption
<a name="bestpractices-enable-in-transit-encryption"></a>

For information about encryption in transit and how to enable it, see [Amazon MSK encryption in transit](msk-encryption.md#msk-encryption-in-transit).

### Reassign partitions
<a name="bestpractices-balance-cluster"></a>

To move partitions to different brokers on the same MSK Provisioned cluster, you can use the partition reassignment tool named `kafka-reassign-partitions.sh`. We recommend that you don't reassign more than 10 partitions in a single `kafka-reassign-partitions` call for safe operations. For example, after you add new brokers to expand a cluster or to move partitions in order to removing brokers, you can rebalance that cluster by reassigning partitions to the new brokers. For information about how to add brokers to an MSK Provisioned cluster, see [Expand the number of brokers in an Amazon MSK cluster](msk-update-broker-count.md). For information about how to remove brokers from an MSK Provisioned cluster, see [Remove a broker from an Amazon MSK cluster](msk-remove-broker.md). For information about the partition reassignment tool, see [Expanding your cluster](https://kafka.apache.org/documentation/#basic_ops_cluster_expansion) in the Apache Kafka documentation.