---
id: "@specs/aws/kafka/docs/bestpractices-kafka-client"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Best practices for Apache Kafka clients"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Best practices for Apache Kafka clients

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/bestpractices-kafka-client
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Best practices for Apache Kafka clients
<a name="bestpractices-kafka-client"></a>

When working with Apache Kafka and Amazon MSK, it's important to correctly configure both the client and server for optimal performance and reliability. This guide provides recommendations of best-practice client-side configuration for Amazon MSK.

For information about Amazon MSK Replicator best practices, see [Best practices](msk-replicator-best-practices.md). For Standard and Express broker best practices, see [Best practices for Standard and Express brokers](bestpractices-intro.md).

**Topics**
+ [Apache Kafka client availability](#bestpractices-kafka-client-client-availability)
+ [Apache Kafka client performance](#bestpractices-kafka-client-performance)
+ [Kafka client monitoring](#bestpractices-kafka-client-monitoring)

## Apache Kafka client availability
<a name="bestpractices-kafka-client-client-availability"></a>

In a distributed system like Apache Kafka, ensuring high availability is crucial for maintaining a reliable and fault-tolerant messaging infrastructure. Brokers will go offline for both planned and unplanned events, such as upgrades, patching, hardware failure, and network issues. A Kafka cluster is tolerant of an offline broker, therefore Kafka clients must also handle broker fail-over gracefully. To ensure high availability of Kafka clients, we recommend these best practices.

**Producer availability**
+ Set `retries` to instruct the producer to retry sending failed messages during broker fail over. We recommend a value of integer max or similar high value for most use cases. Failure to do so will break Kafka’s high availability.
+ Set `delivery.timeout.ms` to specify the upper bound for the total time between sending a message and receiving an acknowledgement from the broker. This should reflect the business requirements of how long a message is valid. Set the time limit high enough to allow for enough retries to complete the failover operation. We recommend a value of 60 seconds or higher for most use cases.
+ Set `request.timeout.ms` to the maximum a single request should wait before a resend is attempted. We recommend a value of 10 seconds or higher for most use cases.
+ Set `retry.backoff.ms` to configure the delay between retries to avoid retry storms and availability impact. We recommend a minimum value of 200ms for most use cases.
+ Set `acks=all` to configure high durability; this should be in line with a server-side config of `RF=3` and `min.isr=2` to ensure all partitions in ISR acknowledge the write. During a single broker offline, this is the `min.isr`, that is `2`.

**Consumer availability**
+ Set `auto.offset.reset` to `latest` initially for new or recreated consumer groups. This avoids the risk of adding cluster load by consuming the entire topic.
+ Set `auto.commit.interval.ms` when using `enable.auto.commit`. We recommend a minimum value of 5 seconds for most use cases to avoid the risk of additional load.
+ Implement exception handling within the consumer's message processing code to handle transient errors, for example, circuit breaker or a sleep with exponential back-off. Failure to do so can result in application crashes, which can cause excessive rebalancing.
+ Set `isolation.level` to control how to read transactional messages:

  We recommend always setting `read_uncommitted` implictly by default. This is missing from some client implementations.

  We recommend a value of `read_uncommitted` when using tiered storage.
+ Set `client.rack` to use a nearest replica read. We recommend setting to the `az id `to minimize network traffic costs and latency. See [Reduce network traffic costs of your Amazon MSK consumers with rack awareness](https://aws.amazon.com/blogs/big-data/reduce-network-traffic-costs-of-your-amazon-msk-consumers-with-rack-awareness/).

**Consumer rebalances**
+ Set `session.timeout.ms` to a value larger than the startup time for an application, including any startup jitter implemented. We recommend a value of 60 seconds for most use cases.
+ Set `heartbeat.interval.ms` to fine-tune how the group coordinator views a consumer as healthy. We recommend a value of 10 seconds for most use cases.
+ Set a shutdown hook in your application to cleanly close the consumer on SIGTERM, rather than relying on session timeouts to identify when a consumer leaves a group. Kstream applications can set `internal.leave.group.on.close` to a value of `true`.
+ Set `group.instance.id` to a distinct value within the consumer group. Ideally a host name, task-id, or pod-id. We recommend always setting this for more deterministic behaviors and better client/server log correlation during troubleshooting.
+ Set `group.initial.rebalance.delay.ms` to a value in line with an average deployment time. This stops continual rebalances during deployment.
+ Set `partition.assignment.strategy` to use sticky assignors. We recommend either `StickyAssignor` or `CooperativeStickyAssignor`.

## Apache Kafka client performance
<a name="bestpractices-kafka-client-performance"></a>

To ensure high performance of Kafka clients, we recommend these best practices.

**Producer performance**
+ Set `linger.ms` to control the amount of time a producer waits for a batch to fill. Smaller batches are computationally expensive for Kafka as they translate to more threads and I/O operations at once. We recommend the following values.

  A minimum value of 5ms for all use cases inc low latency.

  We recommend a higher value of 25ms, for most use cases.

  We recommend against ever using a value of zero in low latency use cases. (A value of zero typically causes latency irrespective because of the IO overhead).
+ Set `batch.size` to control the batch size sent to the cluster. We recommend increasing this to a value of 64KB or 128KB.
+ Set `buffer.memory` when using larger batch sizes. We recommend a value of 64MB for most use cases.
+ Set `send.buffer.bytes` to control the TCP buffer used to receive bytes. We recommend a value of -1 to let the OS manage this buffer when running a producer on a high latency network.
+ Set compression.type to control the compression of batches. We recommend either lz4 or zstd running a producer on a high latency network.

**Consumer performance**
+ Set `fetch.min.bytes` to control the minimum fetch size to be valid to reduce the number of fetches and cluster load. 

  We recommend a minimum value of 32 bytes for all use cases.

  We recommend a higher value of 128 bytes for most use cases.
+ Set fetch.max.wait.ms to determine how long your consumer will wait before fetch.min.bytes is ignored. We recommend a value of 1000ms for most use cases.
+ We recommend the number of consumers be at least equal to the number of partitions for better parallelism and resiliency. In some situations, you may choose to have fewer consumers than the number of partitions for low throughput topics.
+ Set `receive.buffer.bytes` to control the TCP buffer used to receive bytes. We recommend a value of -1 to let the OS manage this buffer when running a consumer on a high latency network.

**Client connections**

Connections lifecycle has a computational and memory cost on a Kafka cluster. Too many connections created at once causes load that may impact the availability of a Kafka cluster. This availability impact can often lead to applications creating even more connections, thus causing a cascading failure, resulting in a full outage. A high number of connections can be achieved when created at a reasonable rate.

We recommend the following mitigations to manage high connection creation rates:
+ Ensure your application deployment mechanism does not restart all producers/consumers at once, but preferably in smaller batches.
+ At the application layer the developer should ensure that a random jitter (random sleep) is performed before creating an admin client, producer client, or consumer client. 
+ At SIGTERM, when closing the connection, a random sleep should be executed to ensure not all Kafka clients are closed at the same time. The random sleep should be within the timeout before SIGKILL occurs.  
**Example A (Java)**  

  ```
  sleepInSeconds(randomNumberBetweenOneAndX);
                          this.kafkaProducer = new KafkaProducer<>(this.props);
  ```  
**Example B (Java)**  

  ```
  Runtime.getRuntime().addShutdownHook(new Thread(() -> {
      sleepInSeconds(randomNumberBetweenOneAndTwentyFive);
      kafkaProducer.close(Duration.ofSeconds(5));
  });
  ```
+ At the application layer, the developer should ensure that clients are created only once per application in a singleton pattern. For example, when using lambda, the client should be created in global scope, and not in the method handler.
+ We recommend connection count is monitored with a goal of being stable. Connection creation/close/shift is normal during deployments and broker failover.

## Kafka client monitoring
<a name="bestpractices-kafka-client-monitoring"></a>

Monitoring Kafka clients is crucial for maintaining the health and efficiency of your Kafka ecosystem. Whether you're a Kafka administrator, developer, or operations team member, enabling client-side metrics is critical for understanding business impact during planned and unplanned events.

We recommend monitoring the following client-side metrics using your preferred metric capture mechanism.

When raising support tickets with AWS, include any abnormal values observed during the incident. Also include a sample of the client application logs detailing errors (not warnings).

**Producer metrics**
+ byte-rate
+ record-send-rate
+ records-per-request-avg
+ acks-latency-avg
+ request-latency-avg
+ request-latency-max
+ record-error-rate
+ record-retry-rate
+ error-rate

**Note**  
Transient errors with retries are not a cause for concern, as this is part of Kafka’s protocol for handling transient issues such as leader fail-over or network retransmits. `record-send-rate` will confirm whether producers are still proceeding with retries.

**Consumer metrics**
+ records-consumed-rate
+ bytes-consumed-rate
+ fetch-rate
+ records-lag-max
+ record-error-rate
+ fetch-error-rate
+ poll-rate
+ rebalance-latency-avg
+ commit-rate

**Note**  
High fetch rates and commit-rates will cause unnecessary load on the cluster. It is optimal to perform requests in larger batches.

**Common metrics**
+ connection-close-rate
+ connection-creation-rate
+ connection-count

**Note**  
High connection creation/termination will cause unnecessary load on the cluster.