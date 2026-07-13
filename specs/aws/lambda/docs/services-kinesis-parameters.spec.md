---
id: "@specs/aws/lambda/docs/services-kinesis-parameters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Parameters"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Parameters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/services-kinesis-parameters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Lambda parameters for Amazon Kinesis Data Streams event source mappings
<a name="services-kinesis-parameters"></a>

All Lambda event source mappings share the same [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) and [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) API operations. However, only some of the parameters apply to Kinesis.


| Parameter | Required | Default | Notes | 
| --- | --- | --- | --- | 
| [BatchSize](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-BatchSize) | N | 100 | Maximum: 10,000 | 
| [BisectBatchOnFunctionError](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-BisectBatchOnFunctionError) | N | false |  none | 
| [DestinationConfig](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-DestinationConfig) | N | N/A | Amazon SQS queue or Amazon SNS topic destination for discarded records. For more information, see [Configuring destinations for failed invocations](kinesis-on-failure-destination.md#kinesis-on-failure-destination-console). | 
| [Enabled](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-Enabled) | N | true |  none | 
| [EventSourceArn](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-EventSourceArn) | Y | N/A | ARN of the data stream or a stream consumer | 
| [FunctionName](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-FunctionName) | Y | N/A |  none | 
| [FunctionResponseTypes](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-FunctionResponseTypes) | N |  N/A | To let your function report specific failures in a batch, include the value `ReportBatchItemFailures` in `FunctionResponseTypes`. For more information, see [Configuring partial batch response with Kinesis Data Streams and Lambda](services-kinesis-batchfailurereporting.md). | 
| [MaximumBatchingWindowInSeconds](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-MaximumBatchingWindowInSeconds) | N | 0 |  none | 
| [MaximumRecordAgeInSeconds](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-MaximumRecordAgeInSeconds) | N | -1 | -1 means infinite: Lambda doesn't discard records ([Kinesis Data Streams data retention settings](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html) still apply)<br />Minimum: -1<br />Maximum: 604,800 | 
| [MaximumRetryAttempts](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-MaximumRetryAttempts) | N | -1 | -1 means infinite: failed records are retried until the record expires<br />Minimum: -1<br />Maximum: 10,000 | 
| [ParallelizationFactor](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-ParallelizationFactor) | N | 1 | Maximum: 10 | 
| [StartingPosition](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-StartingPosition) | Y |  N/A | AT\_TIMESTAMP, TRIM\_HORIZON, or LATEST | 
| [StartingPositionTimestamp](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-StartingPositionTimestamp) | N |  N/A | Only valid if StartingPosition is set to AT\_TIMESTAMP. The time from which to start reading, in Unix time seconds | 
| [TumblingWindowInSeconds](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-TumblingWindowInSeconds) | N |  N/A | Minimum: 0<br />Maximum: 900 | 