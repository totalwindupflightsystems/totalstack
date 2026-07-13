---
id: "@specs/aws/lambda/docs/kafka-scaling-modes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Event poller scaling"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Event poller scaling

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/kafka-scaling-modes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Apache Kafka event poller scaling modes in Lambda
<a name="kafka-scaling-modes"></a>

You can choose between two modes of event poller scaling for Amazon MSK and self-managed Apache Kafka event source mappings:
+ [On-demand mode (default)](#kafka-default-mode)
+ [Provisioned mode](#kafka-provisioned-mode)

## On-demand mode (default)
<a name="kafka-default-mode"></a>

When you initially create the Kafka event source, Lambda allocates a default number of event pollers to process all partitions in the Kafka topic. Lambda automatically scales up or down the number of [event pollers](invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode) based on message load.

In one-minute intervals, Lambda evaluates the offset lag of all the partitions in the topic. If the offset lag is too high, the partition is receiving messages faster than Lambda can process them. If necessary, Lambda adds or removes event pollers from the topic. This autoscaling process of adding or removing event pollers occurs within three minutes of evaluation.

If your target Lambda function is throttled, Lambda reduces the number of event pollers. This action reduces the workload on the function by reducing the number of messages that event pollers can retrieve and send to the function.

## Provisioned mode
<a name="kafka-provisioned-mode"></a>

For workloads where you need to fine-tune the throughput of your event source mapping, you can use provisioned mode. In provisioned mode, you define minimum and maximum limits for the amount of provisioned event pollers. These provisioned event pollers are dedicated to your event source mapping, and can handle unexpected message spikes through responsive autoscaling. We recommend that you use provisioned mode for Kafka workloads that have strict performance requirements.

In Lambda, an event poller is a compute unit with throughput capabilities that vary by event source type. For Amazon MSK and self-managed Apache Kafka, each event poller can handle up to 5 MB/sec of throughput or up to 5 concurrent invocations. For example, if your event source produces an average payload of 1 MB and the average duration of your function is 1 second, a single Kafka event poller can support 5 MB/sec throughput and 5 concurrent Lambda invocations (assuming no payload transformation). For Amazon SQS, each event poller can handle up to 1 MB/sec of throughput or up to 10 concurrent invocations. Using provisioned mode incurs additional costs based on your event poller usage. For pricing details, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

**Note**  
When using provisioned mode, you don't need to create AWS PrivateLink VPC endpoints or grant the associated permissions as part of your network configuration.

In provisioned mode, the range of accepted values for the minimum number of event pollers (`MinimumPollers`) is between 1 and 200, inclusive. The range of accepted values for the maximum number of event pollers (`MaximumPollers`) is between 1 and 2,000, inclusive. `MaximumPollers` must be greater than or equal to `MinimumPollers`. In addition, to maintain ordered processing within partitions, Lambda caps the `MaximumPollers` to the number of partitions in the topic.

For more details about choosing appropriate values for minimum and maximum event pollers, see [Best practices](#kafka-provisioned-mode-bp).

You can configure provisioned mode for your Kafka event source mapping using the console or the Lambda API.

**To configure provisioned mode for an existing event source mapping (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the function with the event source mapping you want to configure provisioned mode for.

1. Choose **Configuration**, then choose **Triggers**.

1. Choose the event source mapping that you want to configure provisioned mode for, then choose **Edit**.

1. Under **Provisioned mode**, select **Configure**.
   + For **Minimum event pollers**, enter a value between 1 and 200. If you don't specify a value, Lambda chooses a default value of 1.
   + For **Maximum event pollers**, enter a value between 1 and 2,000. This value must be greater than or equal to your value for **Minimum event pollers**. If you don't specify a value, Lambda chooses a default value of 200.

1. Choose **Save**.

You can configure provisioned mode programmatically using the [ProvisionedPollerConfig](https://docs.aws.amazon.com/lambda/latest/api/API_ProvisionedPollerConfig.html) object in your [ EventSourceMappingConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_EventSourceMappingConfiguration.html). For example, the following [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) CLI command configures a `MinimumPollers` value of 5, and a `MaximumPollers` value of 100.

```
aws lambda update-event-source-mapping \
    --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --provisioned-poller-config '{"MinimumPollers": 5, "MaximumPollers": 100}'
```

After configuring provisioned mode, you can observe the usage of event pollers for your workload by monitoring the `ProvisionedPollers` metric. For more information, see [Event source mapping metrics](monitoring-metrics-types.md#event-source-mapping-metrics).

To disable provisioned mode and return to default (on-demand) mode, you can use the following [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) CLI command:

```
aws lambda update-event-source-mapping \
    --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --provisioned-poller-config '{}'
```

## Advanced error handling and performance features
<a name="services-kafka-advanced-features"></a>

For Kafka event source mappings with provisioned mode enabled, you can configure additional features to improve error handling and performance:
+ [Retry configurations](kafka-retry-configurations.md) – Control how Lambda handles failed records with maximum retry attempts, record age limits, batch splitting, and partial batch responses.
+ [Kafka on-failure destinations](kafka-on-failure-destination.md) – Send failed records to a Kafka topic for later processing or analysis.

## Best practices and considerations when using provisioned mode
<a name="kafka-provisioned-mode-bp"></a>

The optimal configuration of minimum and maximum event pollers for your event source mapping depends on your application's performance requirements. We recommend that you start with the default minimum event pollers to baseline the performance profile. Adjust your configuration based on observed message processing patterns and your desired performance profile.

For workloads with spiky traffic and strict performance needs, increase the minimum event pollers to handle sudden surges in messages. To determine the minimum event pollers required, consider your workload's messages per second and average payload size, and use the throughput capacity of a single event poller (up to 5 MBps) as a reference.

To maintain ordered processing within a partition, Lambda limits the maximum event pollers to the number of partitions in the topic. Additionally, the maximum event pollers your event source mapping can scale to depends on the function's concurrency settings.

When activating provisioned mode, update your network settings to remove AWS PrivateLink VPC endpoints and associated permissions.

## Cost Optimization for Provisioned mode
<a name="kafka-cost-optimization"></a>

### Provisioned mode pricing
<a name="kafka-provisioned-pricing"></a>

Provisioned mode is charged based on the provisioned minimum event pollers, and the event pollers consumed during autoscaling. Charges are calculated using a billing unit called Event Poller Unit (EPU). You pay for the number and duration of EPUs used, measured in Event-Poller-Unit-hours. You can use Provisioned mode with either a single ESM for performance-sensitive applications or you can group multiple ESMs within the same VPC to share EPU capacity and costs. We will deep dive on two capabilities that help you optimize your Provisioned mode costs. For pricing details, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

### Enhanced EPU Utilization
<a name="kafka-enhanced-epu-utilization"></a>

Each EPU supports up to 20 MB/s throughput capacity for event polling and supports a default of 10 event pollers. When you create a Provisioned mode for Kafka ESM by setting minimum and maximum pollers, it uses minimum poller number to provision EPUs based on default of 10 event pollers per EPU. However, each event poller can independently scale to support up to 5 MB/s of throughput capacity, which may require lower density of event pollers on a specific EPU and can trigger scaling of EPUs. The number of event pollers allocated on an EPU depends on the compute capacity consumed by each event poller. This approach of enhanced EPU utilization allows event pollers with varying throughput requirements to utilize EPU capacity effectively, reducing costs for all ESMs.

### ESM grouping
<a name="kafka-esm-grouping-cost"></a>

To optimize your Provisioned mode costs further, you can group multiple Kafka ESMs to share EPU capacity. With ESM grouping and enhanced EPU Utilization, you can reduce your Provisioned mode costs up to 90% for low-throughput workloads compared to running in single ESM mode. All ESMs that require less than 1 EPU capacity will benefit from ESM grouping. Such ESMs typically require few minimum event pollers to support their throughput needs. This capability will allow you to adopt Provisioned mode for all your Kafka workloads, and benefit from features like schema validation, filtering of Avro/Protobuf events, low-latency invocations, and enhanced error handling that only available in Provisioned mode.

When you configure the `PollerGroupName` parameter with the same value for multiple ESMs within the same Amazon VPC, those ESMs share EPU resources instead of each requiring dedicated EPU capacity. You can group up to 100 ESMs per poller group and aggregate maximum pollers across all ESMs in a group cannot exceed 2000.

#### To configure ESM grouping (console)
<a name="kafka-esm-grouping-console-cost"></a>

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose your function.

1. Choose **Configuration**, and then choose **Triggers**.

1. When creating a new Kafka event source mapping, or editing an existing one, select **Configure** under **Provisioned mode**.

1. For **Minimum event pollers**, enter a value between 1 and 200.

1. For **Maximum event pollers**, enter a value between 1 and 2,000.

1. For **Poller group name**, enter an identifier for the group. Use the same name for other ESMs you want to group together.

1. Choose **Save**.

#### To configure ESM grouping (AWS CLI)
<a name="kafka-esm-grouping-cli-cost"></a>

The following example creates an ESM with a poller group named `production-app-group`:

```
aws lambda create-event-source-mapping \
  --function-name myFunction1 \
  --event-source-arn arn:aws:kafka:us-east-1:123456789012:cluster/MyCluster/abcd1234 \
  --topics topic1 \
  --starting-position LATEST \
  --provisioned-poller-config '{
    "MinimumPollers": 1, 
    "MaximumPollers": 10, 
    "PollerGroupName": "production-app-group"
  }'
```

To add another ESM to the same group (sharing EPU capacity), use the same PollerGroupName:

```
aws lambda create-event-source-mapping \
  --function-name myFunction2 \
  --event-source-arn arn:aws:kafka:us-east-1:123456789012:cluster/MyCluster/abcd1234 \
  --topics topic2 \
  --starting-position LATEST \
  --provisioned-poller-config '{
    "MinimumPollers": 1, 
    "MaximumPollers": 10, 
    "PollerGroupName": "production-app-group"
  }'
```

**Note**  
You can update the `PollerGroupName` to move an ESM to a different group, or remove an ESM from a group by passing an empty string ("") for `PollerGroupName`:

```
# Move ESM to a different group
aws lambda update-event-source-mapping \
  --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
  --provisioned-poller-config '{
    "MinimumPollers": 1, 
    "MaximumPollers": 10, 
    "PollerGroupName": "new-group-name"
  }'

# Remove ESM from group (use dedicated resources)
aws lambda update-event-source-mapping \
  --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
  --provisioned-poller-config '{
    "MinimumPollers": 1, 
    "MaximumPollers": 10, 
    "PollerGroupName": ""
  }'
```

#### Grouping strategy considerations
<a name="kafka-grouping-strategy-considerations"></a>
+ **Application boundary** – Group ESMs that belong to the same applications or services for better cost allocation and management. Consider using naming conventions like `app-name-environment` (e.g., `order-processor-prod`).
+ **Traffic pattern** – Avoid grouping ESMs with high throughput and spiky traffic pattern, as this may lead to resource contention.
+ **Blast radius** – Consider the impact if the shared infrastructure experiences issues. All ESMs in the same group are affected by shared resource limitations. For mission-critical workloads, you may want to use separate groups or dedicated ESMs.

#### Cost optimization example
<a name="kafka-cost-optimization-example"></a>

Consider a scenario where you have 10 ESMs, each configured with 1 event poller and throughput under 2 MB/s:

**Without grouping:**
+ Each ESM requires its own EPU
+ Total EPUs needed: 10
+ Cost per EPU: $0.185/hour in US East (N. Virginia)
+ Monthly EPU cost (720 hours): 10 × 720 × $0.185 = $1,332

**With grouping:**
+ All 10 ESMs share EPU capacity
+ 10 event pollers fit in 1 EPU (with new 10 poller per EPU support)
+ Total EPUs needed: 1
+ Monthly EPU cost (720 hours): 1 × 720 × $0.185 = $133.20
+ **Cost savings: 90%** ($1,198.80 savings per month)