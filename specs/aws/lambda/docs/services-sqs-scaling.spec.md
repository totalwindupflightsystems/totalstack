---
id: "@specs/aws/lambda/docs/services-sqs-scaling"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Scaling behavior"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Scaling behavior

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/services-sqs-scaling
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring scaling behavior for SQS event source mappings
<a name="services-sqs-scaling"></a>

You can control the scaling behavior of your Amazon SQS event source mappings either through maximum concurrency settings or by enabling provisioned mode. These are mutually exclusive options.

By default, Lambda automatically scales event pollers based on message volume. When you enable provisioned mode, you allocate a minimum and maximum number of dedicated polling resources that remain ready to handle expected traffic patterns. This allows you to optimize your event source mapping's performance in two ways:
+ Standard mode (Default): Lambda automatically manages scaling, starting with a small number of pollers and scaling up or down based on workload.
+ Provisioned mode: You configure dedicated polling resources with minimum and maximum limits, enabling 3 times faster scaling and up to 16 times higher processing capacity.

For standard queues, Lambda uses [ long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html#sqs-long-polling) to poll a queue until it becomes active. When messages are available, Lambda starts processing five batches at a time with five concurrent invocations of your function. If messages are still available, Lambda increases the number of processes that are reading batches by up to 300 more concurrent invokes per minute. The maximum number of invokes that an event source mapping can process simultaneously is 1,250. When traffic is low, Lambda scales back the processing to five concurrent invokes, and can optimize to as few as 2 concurrent invokes to reduce the Amazon SQS calls and corresponding costs. However, this optimization is not available when you enable the maximum concurrency setting.

For FIFO queues, Lambda sends messages to your function in the order that it receives them. When you send a message to a FIFO queue, you specify a [message group ID](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html). Amazon SQS ensures that messages in the same group are delivered to Lambda in order. When Lambda reads your messages into batches, each batch may contain messages from more than one message group, but the order of the messages is maintained. If your function returns an error, the function attempts all retries on the affected messages before Lambda receives additional messages from the same group.

When using provisioned mode, each event poller can handle up to 1 MB/sec of throughput, up to 10 concurrent invokes, or up to 10 Amazon SQS polling API calls per second. Lambda scales the number of event pollers between your configured minimum and maximum, quickly adding up to 1,000 concurrency per minute to provide consistent, low-latency processing of your Amazon SQS events. Using provisioned mode incurs additional costs. For detailed pricing, see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/). Each event poller uses [long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html) to your SQS queue with up to 10 polls per second, which incur SQS API requests cost. See [Amazon SQS pricing](https://aws.amazon.com/sqs/pricing/ ) for details. You control scaling and concurrency through these minimum and maximum event poller settings, rather than using the maximum concurrency setting, as these options cannot be used together.

**Note**  
You cannot use the maximum concurrency setting and provisioned mode at the same time. When provisioned mode is enabled, you control the scaling and concurrency of your Amazon SQS event source mapping through the minimum and maximum number of event pollers.

## Configuring maximum concurrency for Amazon SQS event sources
<a name="events-sqs-max-concurrency"></a>

You can use the maximum concurrency setting to control scaling behavior for your SQS event sources. Note that maximum concurrency cannot be used with provisioned mode enabled. The maximum concurrency setting limits the number of concurrent instances of the function that an Amazon SQS event source can invoke. Maximum concurrency is an event source-level setting. If you have multiple Amazon SQS event sources mapped to one function, each event source can have a separate maximum concurrency setting. You can use maximum concurrency to prevent one queue from using all of the function's [reserved concurrency](configuration-concurrency.md) or the rest of the [account's concurrency quota](gettingstarted-limits.md). There is no charge for configuring maximum concurrency on an Amazon SQS event source.

Importantly, maximum concurrency and reserved concurrency are two independent settings. Don't set maximum concurrency higher than the function's reserved concurrency. If you configure maximum concurrency, make sure that your function's reserved concurrency is greater than or equal to the total maximum concurrency for all Amazon SQS event sources on the function. Otherwise, Lambda may throttle your messages.

When your account's concurrency quota is set to the default value of 1,000, an Amazon SQS event source mapping can scale to invoke function instances up to this value, unless you specify a maximum concurrency.

If you receive an increase to your account's default concurrency quota, Lambda may not be able to invoke concurrent functions instances up to your new quota. By default, Lambda can scale to invoke up to 1,250 concurrent function instances for an Amazon SQS event source mapping. If this is insufficient for your use case, contact AWS support to discuss an increase to your account's Amazon SQS event source mapping concurrency.

**Note**  
For FIFO queues, concurrent invocations are capped either by the number of [message group IDs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html) (`messageGroupId`) or the maximum concurrency setting—whichever is lower. For example, if you have six message group IDs and maximum concurrency is set to 10, your function can have a maximum of six concurrent invocations.

You can configure maximum concurrency on new and existing Amazon SQS event source mappings.

**Configure maximum concurrency using the Lambda console**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of a function.

1. Under **Function overview**, choose **SQS**. This opens the **Configuration** tab.

1. Select the Amazon SQS trigger and choose **Edit**.

1. For **Maximum concurrency**, enter a number between 2 and 1,000. To turn off maximum concurrency, leave the box empty.

1. Choose **Save**.

**Configure maximum concurrency using the AWS Command Line Interface (AWS CLI)**  
Use the [update-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html) command with the `--scaling-config` option. Example:

```
aws lambda update-event-source-mapping \
    --uuid {{"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"}} \
    --scaling-config {{'{"MaximumConcurrency":5}'}}
```

To turn off maximum concurrency, enter an empty value for `--scaling-config`:

```
aws lambda update-event-source-mapping \
    --uuid {{"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"}} \
    --scaling-config {{"{}"}}
```

**Configure maximum concurrency using the Lambda API**  
Use the [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) or [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) action with a [ScalingConfig](https://docs.aws.amazon.com/lambda/latest/api/API_ScalingConfig.html) object.