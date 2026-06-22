---
id: "@specs/aws/kafka/docs/msk-broker-types-express"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Express brokers"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Express brokers

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/msk-broker-types-express
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon MSK Express brokers
<a name="msk-broker-types-express"></a>

Express brokers for MSK Provisioned make Apache Kafka simpler to manage, more cost-effective to run at scale, and more elastic with the low latency you expect. Brokers include pay-as-you-go storage that scales automatically and requires no sizing, provisioning, or proactive monitoring. Depending on the instance size selected, each broker node can provide up to 3x more throughput per broker, scale up to 20x faster, and recover 90% quicker compared to standard Apache Kafka brokers. Express brokers come pre-configured with Amazon MSK’s best practice defaults and enforce client throughput quotas to minimize resource contention between clients and Kafka’s background operations.

Here are some key factors and capabilities to consider when using Express brokers.
+ **No storage management**: Express brokers eliminate the need to [provision or manage any storage resources](msk-storage-management.md). You get elastic, virtually unlimited, pay-as-you-go, and fully managed storage. For high throughput use cases, you do not need to reason about the interactions between compute instances and storage volumes, and the associated throughput bottlenecks. These capabilities simplify cluster management and eliminate storage management operational overhead.
+ **Faster scaling**: Express brokers allow you to scale your cluster and move partitions up to 20x faster than on Standard brokers. This capability is crucial when you need to scale out your cluster to handle upcoming load spikes or scale in your cluster to reduce cost. See the sections on [expanding your cluster](msk-update-broker-count.md), [removing brokers](msk-remove-broker.md), [reassigning partitions](msk-update-broker-type.md), and [setting up LinkedIn’s Cruise Control for rebalancing](cruise-control.md) for more details on scaling your cluster.
+ **Higher throughput**: Express brokers offer up to 3x more throughput per broker than Standard brokers. For example, you can safely write data at up to 500 MBps with each m7g.16xlarge sized Express broker compared to 153.8 MBps on the equivalent Standard broker (both numbers assume sufficient bandwidth allocation towards background operations, such as replication and rebalancing).
+ **Configured for high resilience**: Express brokers automatically offer various best practices to improve your cluster’s resilience. These include guardrails on critical Apache Kafka configurations, throughput quotas, and capacity reservations for background operations and unplanned repairs. These capabilities make it safer and easier to run large scale Apache Kafka applications. See the sections on [Express broker configurations](msk-configuration-express.md) and [Amazon MSK Express broker quota](limits.md#msk-express-quota) for more details.
+ **No Maintenance windows**: There are no maintenance windows for Express brokers. Amazon MSK automatically updates your cluster hardware on an ongoing basis. See [Patching for Express brokers](https://docs.aws.amazon.com/msk/latest/developerguide/patching-impact.html#patching-express-brokers) for more details.

## Additional information about Express brokers
<a name="msk-broker-types-express-notes"></a>
+ Express brokers work with Apache Kafka APIs, but don't yet fully support KStreams API.
+ Express brokers are only available in a 3AZs configuration.
+ Express brokers are only available on select instance sizes. See [Amazon MSK pricing](https://aws.amazon.com/msk/pricing/) for the updated list.
+ Express brokers are supported on the following Apache Kafka versions: 3.6, 3.8, and 3.9.
+ Express brokers can be created with KRaft mode from Apache Kafka version 3.9 onwards.

**See these blogs**  
For more information about MSK Express brokers and to see a real-world example of Express brokers in use, read the following blogs:  
[Introducing Express brokers for Amazon MSK to deliver high throughput and faster scaling for your Kafka clusters](https://aws.amazon.com/blogs/aws/introducing-express-brokers-for-amazon-msk-to-deliver-high-throughput-and-faster-scaling-for-your-kafka-clusters/)
[Express brokers for Amazon MSK: Turbo-charged Kafka scaling with up to 20 times faster performance](https://aws.amazon.com/blogs/big-data/express-brokers-for-amazon-msk-turbo-charged-kafka-scaling-with-up-to-20-times-faster-performance/)  
This blog demonstrates how Express brokers:  
Provide faster throughput, rapid scaling, and improved recovery time from failures
Eliminate storage management complexities