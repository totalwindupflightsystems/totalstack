---
id: "@specs/aws/kafka/docs/troubleshooting-offlinebroker-clientfailover"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Broker offline and client failover"
status: active
depends_on:
  - "@specs/aws/kafka/meta"
---

# Broker offline and client failover

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kafka/docs/troubleshooting-offlinebroker-clientfailover
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Broker offline and client failover
<a name="troubleshooting-offlinebroker-clientfailover"></a>

Kafka allows for an offline broker; a single offline broker in a healthy and balanced cluster following best practices will not see impact or cause failure to produce or consume. This is because another broker will take over partition leadership and because the Kafka client lib will automatically fail-over and start sending requests to the new leader brokers. 

**Client server contract**  
This results in a shared contract between the client library and server-side behavior; the server must successfully assign one or more new leaders and the client must change brokers to send requests to the new leaders in a timely manner.

Kafka uses exceptions to control this flow:

**An example procedure**

1. Broker A enters an offline state.

1. Kafka client receives an exception (typically network disconnect or not\_leader\_for\_partition).

1. These exceptions trigger the Kafka client to update its metadata so that it knows about the latest leaders. 

1. Kafka client resumes sending requests to the new partition leaders on other brokers.

This process typically takes less than 2 seconds with the vended Java client and default configurations. The client side errors are verbose and repetitive but not cause for concern, as denoted by the “WARN” level.

**Example: Exception 1**  
`10:05:25.306 [kafka-producer-network-thread | producer-1] WARN o.a.k.c.producer.internals.Sender - [Producer clientId=producer-1] Got error produce response with correlation id 864845 on topic-partition msk-test-topic-1-0, retrying (2147483646 attempts left). Error: NETWORK_EXCEPTION. Error Message: Disconnected from node 2`

**Example: Exception 2**  
`10:05:25.306 [kafka-producer-network-thread | producer-1] WARN o.a.k.c.producer.internals.Sender - [Producer clientId=producer-1] Received invalid metadata error in produce request on partition msk-test-topic-1-41 due to org.apache.kafka.common.errors.NotLeaderOrFollowerException: For requests intended only for the leader, this error indicates that the broker is not the current leader. For requests intended for any replica, this error indicates that the broker is not a replica of the topic partition.. Going to request metadata update now"`

Kafka clients will automatically resolve these errors typically within 1 second and at most 3 seconds. This presents as produce/consume latency at p99 in client side metrics (typically high milliseconds in the 100’s). Any longer than this typically indicates an issue with client configuration or server-side controller load. Please see the troubleshooting section.

A successful fail-over can be verified by checking the `BytesInPerSec` and `LeaderCount` metrics increase on other brokers which proves that the traffic and leadership moved as expected. You will also observe an increase in the `UnderReplicatedPartitions` metric, which is expected when replicas are offline with the shutdown broker.

**Troubleshooting**  
The above flow can be disrupted by breaking the client-server contract. The most common reasons for issue include:
+ Misconfiguration or incorrect usage of Kafka client libs.
+ Unexpected default behaviours and bugs with 3rd party client libs.
+ Overloaded controller resulting in slower partition leader assignment.
+ New controller is being elected resulting in slower partition leader assignment.

In order to ensure correct behaviour to handle leadership fail-over, we recommend:
+ Server side [best practices](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html) must be followed to ensure that the controller broker is scaled appropriately to avoid slow leadership assignment.
+ Client libraries must have retries enabled to ensure that client handles the failover.
+ Client libraries must have retry.backoff.ms configured (default 100) to avoid connection/request storms.
+ Client libraries must set request.timeout.ms and delivery.timeout.ms to values inline with the applications’ SLA. Higher values will result in slower fail-over for certain failure types.
+ Client libraries must ensure that bootstrap.servers contains at least 3 random brokers to avoid an availability impact on initial discovery.
+ Some client libraries are lower level than others and expect the application developer to implement retry logic and exception handling themselves. Please refer to client lib specific documentation for example usage, and ensure that correct reconnect/retry logic is followed.
+ We recommend monitoring client side latency for produces, successful request count, and error count for non-retryable errors.
+ We have observed that older 3rd party golang and ruby libraries remain verbose during an entire broker offline time period despite produces and consume requests being unaffected. We recommend you always monitor your business level metrics besides request metrics for success and errors to determine if there is real impact vs noise in your logs.
+ Customers should not alarm on transient exceptions for network/not\_leader as they are normal, non-impacting, and expected as part of the kafka protocol.
+ Customers should not alarm on UnderReplicatedPartitions as they are normal, non-impacting, and expected during a single offline broker.