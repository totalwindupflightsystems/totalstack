---
id: "@specs/aws/lambda/docs/monitoring-metrics-types"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Metric types"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Metric types

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/monitoring-metrics-types
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Types of metrics for Lambda functions
<a name="monitoring-metrics-types"></a>

This section describes the types of Lambda metrics available in the CloudWatch console.

**Topics**
+ [Invocation metrics](#invocation-metrics)
+ [Deployment metrics](#deployment-metrics)
+ [Performance metrics](#performance-metrics)
+ [Concurrency metrics](#concurrency-metrics)
+ [Asynchronous invocation metrics](#async-invocation-metrics)
+ [Event source mapping metrics](#event-source-mapping-metrics)

## Invocation metrics
<a name="invocation-metrics"></a>

Invocation metrics are binary indicators of the outcome of a Lambda function invocation. View these metrics with the `Sum` statistic. For example, if the function returns an error, then Lambda sends the `Errors` metric with a value of 1. To get a count of the number of function errors that occurred each minute, view the `Sum` of the `Errors` metric with a period of 1 minute.
+ `Invocations` – The number of times that your function code is invoked, including successful invocations and invocations that result in a function error. Invocations aren't recorded if the invocation request is throttled or otherwise results in an invocation error. The value of `Invocations` equals the number of requests billed.
+ `Errors` – The number of invocations that result in a function error. Function errors include exceptions that your code throws and exceptions that the Lambda runtime throws. The runtime returns errors for issues such as timeouts and configuration errors. To calculate the error rate, divide the value of `Errors` by the value of `Invocations`. Note that the timestamp on an error metric reflects when the function was invoked, not when the error occurred.
+ `DeadLetterErrors` – For [asynchronous invocation](invocation-async.md), the number of times that Lambda attempts to send an event to a dead-letter queue (DLQ) but fails. Dead-letter errors can occur due to incorrectly set resources or size limits.
+ `DestinationDeliveryFailures` – For asynchronous invocation and supported [event source mappings](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html), the number of times that Lambda attempts to send an event to a [destination](invocation-async-retain-records.md#invocation-async-destinations) but fails. For event source mappings, Lambda supports destinations for stream sources (DynamoDB and Kinesis). Delivery errors can occur due to permissions errors, incorrectly configured resources, or size limits. Errors can also occur if the destination you have configured is an unsupported type such as an Amazon SQS FIFO queue or an Amazon SNS FIFO topic.
+ `Throttles` – The number of invocation requests that are throttled. When all function instances are processing requests and no concurrency is available to scale up, Lambda rejects additional requests with a `TooManyRequestsException` error. Throttled requests and other invocation errors don't count as either `Invocations` or `Errors`.
**Note**  
With [Lambda Managed Instances](lambda-managed-instances.md), Lambda provides granular throttle metrics that identify the specific constraint causing the throttle. When a throttle occurs on the execution environment, exactly one of the following sub-metrics is emitted with a value of 1, while the remaining three are emitted with a value of 0. The `Throttles` metric is always emitted alongside these sub-metrics.  
`CPUThrottles` – Invocations throttled due to CPU exhaustion on the execution environment.
`MemoryThrottles` – Invocations throttled due to memory exhaustion on the execution environment.
`DiskThrottles` – Invocations throttled due to disk exhaustion on the execution environment.
`ConcurrencyThrottles` – Invocations throttled when the execution environment concurrency limit is reached.
+ `OversizedRecordCount` – For Amazon DocumentDB event sources, the number of events your function receives from your change stream that are over 6 MB in size. Lambda drops the message and emits this metric.
+ `ProvisionedConcurrencyInvocations` – The number of times that your function code is invoked using [provisioned concurrency](provisioned-concurrency.md).
+ `ProvisionedConcurrencySpilloverInvocations` – The number of times that your function code is invoked using standard concurrency when all provisioned concurrency is in use.
+ `RecursiveInvocationsDropped` – The number of times that Lambda has stopped invocation of your function because it has detected that your function is part of an infinite recursive loop. Recursive loop detection monitors how many times a function is invoked as part of a chain of requests by tracking metadata added by supported AWS SDKs. By default, if your function is invoked as part of a chain of requests approximately 16 times, Lambda drops the next invocation. If you disable recursive loop detection, this metric is not emitted. For more information about this feature, see [Use Lambda recursive loop detection to prevent infinite loops](invocation-recursion.md).

## Deployment metrics
<a name="deployment-metrics"></a>

Deployment metrics provide information about Lambda function deployment events and related validation processes.
+ `SignatureValidationErrors` – The number of times a code package deployment has occurred with signature validation failures when the code signing configuration policy is set to `Warn`. This metric is emitted when the expiry, mismatch, or revocation checks fail but the deployment is still allowed due to the `Warn` policy setting. For more information about code signing, see [Using code signing to verify code integrity with Lambda](configuration-codesigning.md).

## Performance metrics
<a name="performance-metrics"></a>

Performance metrics provide performance details about a single function invocation. For example, the `Duration` metric indicates the amount of time in milliseconds that your function spends processing an event. To get a sense of how fast your function processes events, view these metrics with the `Average` or `Max` statistic.
+ `Duration` – The amount of time that your function code spends processing an event. The billed duration for an invocation is the value of `Duration` rounded up to the nearest millisecond. `Duration` does not include cold start time.
+ `PostRuntimeExtensionsDuration` – The cumulative amount of time that the runtime spends running code for extensions after the function code has completed.
+ `IteratorAge` – For DynamoDB, Kinesis, and Amazon DocumentDB event sources, the age of the last record in the event in milliseconds. This metric measures the time between when a stream receives the record and when the event source mapping sends the event to the function.
+ `OffsetLag` – For self-managed Apache Kafka and Amazon Managed Streaming for Apache Kafka (Amazon MSK) event sources, the difference in offset between the last record written to a topic and the last record that your function's consumer group processed. Though a Kafka topic can have multiple partitions, this metric measures the offset lag at the topic level.

`Duration` also supports percentile (`p`) statistics. Use percentiles to exclude outlier values that skew `Average` and `Maximum` statistics. For example, the `p95` statistic shows the maximum duration of 95 percent of invocations, excluding the slowest 5 percent. For more information, see [Percentiles](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Percentiles) in the *Amazon CloudWatch User Guide*.

## Concurrency metrics
<a name="concurrency-metrics"></a>

Lambda reports concurrency metrics as an aggregate count of the number of instances processing events across a function, version, alias, or AWS Region. To see how close you are to hitting [concurrency limits](lambda-concurrency.md#concurrency-quotas), view these metrics with the `Max` statistic.
+ `ConcurrentExecutions` – The number of function instances that are processing events. If this number reaches your [concurrent executions quota](gettingstarted-limits.md#compute-and-storage) for the Region, or the [reserved concurrency](configuration-concurrency.md) limit on the function, then Lambda throttles additional invocation requests.
+ `ProvisionedConcurrentExecutions` – The number of function instances that are processing events using [provisioned concurrency](provisioned-concurrency.md). For each invocation of an alias or version with provisioned concurrency, Lambda emits the current count. If your function is inactive or not receiving requests, Lambda doesn't emit this metric.
+ `ProvisionedConcurrencyUtilization` – For a version or alias, the value of `ProvisionedConcurrentExecutions` divided by the total amount of provisioned concurrency configured. For example, if you configure a provisioned concurrency of 10 for your function, and your `ProvisionedConcurrentExecutions` is 7, then your `ProvisionedConcurrencyUtilization` is 0.7.

  If your function is inactive or not receiving requests, Lambda doesn't emit this metric because it is based on `ProvisionedConcurrentExecutions`. Keep this in mind if you use `ProvisionedConcurrencyUtilization` as the basis for CloudWatch alarms.
+ `UnreservedConcurrentExecutions` – For a Region, the number of events that functions without reserved concurrency are processing.
+ `ClaimedAccountConcurrency` – For a Region, the amount of concurrency that is unavailable for on-demand invocations. `ClaimedAccountConcurrency` is equal to `UnreservedConcurrentExecutions` plus the amount of allocated concurrency (i.e. the total reserved concurrency plus total provisioned concurrency). For more information, see [Working with the `ClaimedAccountConcurrency` metric](monitoring-concurrency.md#claimed-account-concurrency).

## Asynchronous invocation metrics
<a name="async-invocation-metrics"></a>

Asynchronous invocation metrics provide details about asynchronous invocations from event sources and direct invocations. You can set thresholds and alarms to notify you of certain changes. For example, when there's an undesired increase in the number of events queued for processing (`AsyncEventsReceived`). Or, when an event has been waiting a long time to be processed (`AsyncEventAge`).
+ `AsyncEventsReceived` – The number of events that Lambda successfully queues for processing. This metric provides insight into the number of events that a Lambda function receives. Monitor this metric and set alarms for thresholds to check for issues. For example, to detect an undesirable number of events sent to Lambda, and to quickly diagnose issues resulting from incorrect trigger or function configurations. Mismatches between `AsyncEventsReceived` and `Invocations` can indicate a disparity in processing, events being dropped, or a potential queue backlog.
+ `AsyncEventAge` – The time between when Lambda successfully queues the event and when the function is invoked. The value of this metric increases when events are being retried due to invocation failures or throttling. Monitor this metric and set alarms for thresholds on different statistics for when a queue buildup occurs. To troubleshoot an increase in this metric, look at the `Errors` metric to identify function errors and the `Throttles` metric to identify concurrency issues.
+ `AsyncEventsDropped` – The number of events that are dropped without successfully executing the function. If you configure a dead-letter queue (DLQ) or `OnFailure` destination, then events are sent there before they're dropped. Events are dropped for various reasons. For example, events can exceed the maximum event age or exhaust the maximum retry attempts, or reserved concurrency might be set to 0. To troubleshoot why events are dropped, look at the `Errors` metric to identify function errors and the `Throttles` metric to identify concurrency issues.

## Event source mapping metrics
<a name="event-source-mapping-metrics"></a>

Event source mapping metrics provide insights into the processing behavior of your event source mapping.

Currently, event source mapping metrics are available for Amazon SQS, Kinesis, DynamoDB, Amazon MSK and self-managed Apache Kafka event sources.

For event source mapping with metrics config, you can also check all the ESM related metrics in the **Monitor** tab from the page Console **Lambda** > **Additional resources** > **event source mappings** now.

**To enable metrics or an event source mapping (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the function you want to enable metrics for.

1. Choose **Configuration**, then choose **Triggers**.

1. Choose the event source mapping that you want to enable metrics for, then choose **Edit**.

1. Under **Event source mapping configuration**, choose ** Enable metrics** or select from the **Metrics** dropdown list.

1. Choose **Save**.

Alternatively, you can enable metrics for your event source mapping programmatically using the [ EventSourceMappingMetricsConfig](https://docs.aws.amazon.com/lambda/latest/api/API_EventSourceMappingMetricsConfig.html) object in your [EventSourceMappingConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_EventSourceMappingConfiguration.html). For example, the following [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) CLI command enables metrics for an event source mapping:

```
aws lambda update-event-source-mapping \
    --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --metrics-config Metrics=EventCount
```

There are 3 metric goups: `EventCount`, `ErrorCount` and `KafkaMetrics`, and each group has multi metrics. Not every metric is available for each event source. The following table summarizes the supported metrics for each type of event source.

You must opt-in the metric group to receive metrics related metrics. for example set EventCount in metrics config to have: (`PolledEventCount`, `FilteredOutEventCount`, `InvokedEventCount`, `FailedInvokeEventCount`, `DroppedEventCount`, `OnFailureDestinationDeliveredEventCount`, and `DeletedEventCount`). 


| Event source mapping metric | Metric group | Amazon SQS | Kinesis and DynamoDB streams | Amazon MSK and self-managed Apache Kafka | 
| --- | --- | --- | --- | --- | 
| `PolledEventCount` | `EventCount` | Yes | Yes | Yes | 
| `FilteredOutEventCount` | `EventCount` | Yes | Yes | Yes | 
| `InvokedEventCount` | `EventCount` | Yes | Yes | Yes | 
| `FailedInvokeEventCount` | `EventCount` | Yes | Yes | Yes | 
| `DroppedEventCount` | `EventCount` | No | Yes | Yes | 
| `OnFailureDestinationDeliveredEventCount` | `EventCount` | No | Yes | Yes | 
| `DeletedEventCount` | `EventCount` | Yes | No | No | 
| `CommittedEventCount` | `EventCount` | No | No | Yes | 
| `PollingErrorCount` | `ErrorCount` | No | No | Yes | 
| `InvokeErrorCount` | `ErrorCount` | No | No | Yes | 
| `OnFailureDestinationDeliveryErrorCount` | `ErrorCount` | No | No | Yes | 
| `SchemaRegistryErrorCount` | `ErrorCount` | No | No | Yes | 
| `CommitErrorCount` | `ErrorCount` | No | No | Yes | 
| `MaxOffsetLag` | `KafkaMetrics` | No | No | Yes | 
| `SumOffsetLag` | `KafkaMetrics` | No | No | Yes | 

In addition, if your event source mapping is in [ provisioned mode](invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode), Lambda provides the following metric:
+ `ProvisionedPollers` – For event source mappings in provisioned mode, the number of event pollers that are actively running. View this metric using the `MAX` math.
+ (Amazon MSK and self-managed Apache Kafka event sources only) `EventPollerUnit` – For event source mappings in provisioned mode, the number of event poller units that are actively running. View this metric using the `SUM` math.
+ (Amazon MSK and self-managed Apache Kafka event sources) `EventPollerThroughputInBytes` – For event source mappings in provisioned mode, the total record size of event pollers polled from the event source. It can tell you the current polling throughput. View this metric using the `SUM` math.

Here is more detail about each of the metric:
+ `PolledEventCount` – The number of events that Lambda reads successfully from the event source. If Lambda polls for events but receives an empty poll (no new records), Lambda emits a 0 value for this metric. Use this metric to detect whether your event source mapping is correctly polling for new events.
+ `FilteredOutEventCount` – For event source mapping with a [filter criteria](invocation-eventfiltering.md), the number of events filtered out by that filter criteria. Use this metric to detect whether your event source mapping is properly filtering out events. For events that match the filter criteria, Lambda emits a 0 metric.
+ `InvokedEventCount` – The number of events that invoked your Lambda function. Use this metric to verify that events are properly invoking your function. If an event results in a function error or throttling, `InvokedEventCount` may count multiple times for the same polled event due to automatic retries.
**Warning**  
Lambda event source mappings process each event at least once, and duplicate processing of records can occur. Because of this, events may be counted multiple times in metrics that involve event counts.
+ `FailedInvokeEventCount` – The number of events that Lambda tried to invoke your function with, but failed. Invocations can fail due to reasons such as network configuration issues, incorrect permissions, or a deleted Lambda function, version, or alias. If your event source mapping has [ partial batch responses](services-sqs-errorhandling.md#services-sqs-batchfailurereporting) enabled, `FailedInvokeEventCount` includes any event with a non-empty `BatchItemFailures` in the response.
**Note**  
The timestamp for the `FailedInvokeEventCount` metric represents the end of the function invocation. This behavior differs from other Lambda invocation error metrics, which are timestamped at the start of the function invocation.
+ `DroppedEventCount` – The number of events that Lambda dropped due to expiry or retry exhaustion. Specifically, this is the number of records that exceed your configured values for `MaximumRecordAgeInSeconds` or `MaximumRetryAttempts`. Importantly, this doesn't include the number of records that expire due to exceeding your event source's retention settings. Dropped events also excludes events that you send to an [ on-failure destination](invocation-async-retain-records.md). Use this metric to detect an increasing backlog of events.
+ `OnFailureDestinationDeliveredEventCount` – For event source mappings with an [on-failure destination](invocation-async-retain-records.md) configured, the number of events sent to that destination. Use this metric to monitor for function errors related to invocations from this event source. If delivery to the destination fails, Lambda handles metrics as follows:
  + Lambda doesn't emit the `OnFailureDestinationDeliveredEventCount` metric.
  + For the `DestinationDeliveryFailures` metric, Lambda emits a 1.
  + For the `DroppedEventCount` metric, Lambda emits a number equal to the number of events that failed delivery.
+ `DeletedEventCount` – The number of events that Lambda successfully deletes after processing. If Lambda tries to delete an event but fails, Lambda emits a 0 metric. Use this metric to ensure that successfully processed events are deleted from your event source.
+ `CommittedEventCount` – The number of events that Lambda successfully committed after processing. It's a sum of the deltas of last and current committted offset from each partition in the Kafka event source mapping.
+ `PollingErrorCount` – The number of errors that Lambda failed to poll requests from event source. Lambda only emits this metric data when error happened.
+ `InvokeErrorCount` – The number of errors that Lambda failed to invoke your function. Notice the invocation is records in batch. The number is on batch level, not on record count level. Lambda only emits this metric data when error happened.
+ `SchemaRegistryErrorCount` – The number of errors that Lambda failed to fetch the schema or deserialize with the scheme. Lambda only emits this metric data when error happened.
+ `CommitErrorCount` – The number of errors that Lambda failed to commit to Kafka cluster. Lambda only emits this metric data when error happened.
+ `MaxOffsetLag` – The max of offset lags (difference between latest and committed offsets) accross all partitions in the event source mapping.
+ `SumOffsetLag` – The sum of the offset lags across all partitions in the event source mapping.

If your event source mapping is disabled, you won't receive event source mapping metrics. You may also see missing metrics if CloudWatch or Lambda is experiencing degraded availability.