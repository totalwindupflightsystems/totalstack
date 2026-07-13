---
id: "@specs/aws/lambda/docs/with-kafka-low-latency"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Low latency Apache Kafka"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Low latency Apache Kafka

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/with-kafka-low-latency
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Low latency processing for Kafka event sources
<a name="with-kafka-low-latency"></a>

AWS Lambda natively supports low latency event processing for applications that require consistent end-to-end latencies of less than 100 milliseconds. This page provides configuration details and recommendations to enable low latency workflows.

## Enable low latency processing
<a name="enable-low-latency"></a>

To enable low latency processing on a Kafka event source mapping, the following basic configuration is required: 
+ Enable provisioned mode. For more information, see [Provisioned mode](kafka-scaling-modes.md#kafka-provisioned-mode).
+ Set the event source mapping's `MaximumBatchingWindowInSeconds` parameter to 0. For more information, see [Batching behavior](invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching).

## Fine-tuning your low latency Kafka ESM
<a name="recommendations-low-latency"></a>

Consider the following recommendations to optimize your Kafka event source mapping for low latency:

### Provisioned mode configuration
<a name="recommendations-pollers"></a>

In provisioned mode for Kafka event source mapping, Lambda allows you to fine-tune the throughput of your event source mapping by configuring a minimum and maximum number of resources called **event pollers**. An event poller (or **a poller**) represents a compute resource that underpins an event source mapping in the provisioned mode, and allocates up to 5 MB/s throughput. Each event poller supports up to 5 concurrent Lambda invocations.

To determine the optimal poller configuration for your application, consider your peak ingestion rate and processing requirements. Let's look at a simplified example:

With a batch size of 20 records and an average target function duration of 50ms, each poller can handle 2,000 records per second subject to 5 MB/s limit. This is calculated as: (20 records × 1000ms/50ms) × 5 concurrent Lambda invocations. Therefore, if your desired peak ingestion rate is 20,000 records per second, you would need at least 10 event pollers.

**Note**  
We recommend to provision additional event pollers as buffer to avoid consistently operating at maximum capacity.

Provisioned mode automatically scales your event pollers based on traffic patterns within configured minimum and maximum **event pollers** which can trigger rebalance, and therefore, introduce additional latency. You can disable auto-scaling by configuring same value for minimum and maximum **event poller**.

### Additional considerations
<a name="additional-considerations-low-latency"></a>

Some of the additional considerations include:
+ Cold starts from the invocation of your Lambda target function can potentially increase end-to-end latency. To reduce this risk, consider enabling [provisioned concurrency](provisioned-concurrency.md) or [SnapStart](snapstart.md) on your event source mapping's target function. Additionally, optimize your function's memory allocation to ensure consistent and optimal executions.
+ When `MaximumBatchingWindowInSeconds` is set to 0, Lambda will immediately process any available records without waiting to fill the complete batch size. For example, if your batch size is set to 1,000 records but only 100 records are available, Lambda will process those 100 records immediately rather than waiting for the full 1,000 records to accumulate.

**Important**  
The optimal configuration for low latency processing varies significantly based on your specific workload. We strongly recommend testing different configurations with your actual workload to determine the best settings for your use case. 