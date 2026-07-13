---
id: "@specs/aws/lambda/docs/services-ddb-params"
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
> **spec:id:** @specs/aws/lambda/docs/services-ddb-params
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Lambda parameters for Amazon DynamoDB event source mappings
<a name="services-ddb-params"></a>

All Lambda event source types share the same [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) and [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) API operations. However, only some of the parameters apply to DynamoDB Streams.


| Parameter | Required | Default | Notes | 
| --- | --- | --- | --- | 
| BatchSize | N | 100 | Maximum: 10,000 | 
| BisectBatchOnFunctionError | N | false | none | 
| DestinationConfig | N | N/A | Standard Amazon SQS queue or standard Amazon SNS topic destination for discarded records | 
| Enabled | N | true | none | 
| EventSourceArn | Y | N/A | ARN of the data stream or a stream consumer | 
| FilterCriteria | N | N/A | [Control which events Lambda sends to your function](invocation-eventfiltering.md) | 
| FunctionName | Y | N/A | none | 
| FunctionResponseTypes | N | N/A | To let your function report specific failures in a batch, include the value `ReportBatchItemFailures` in `FunctionResponseTypes`. For more information, see [Configuring partial batch response with DynamoDB and Lambda](services-ddb-batchfailurereporting.md). | 
| MaximumBatchingWindowInSeconds | N | 0 | none | 
| MaximumRecordAgeInSeconds | N | -1 | -1 means infinite: failed records are retried until the record expires. The [data retention limit for DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html#Streams.DataRetention) is 24 hours.<br />Minimum: -1<br />Maximum: 604,800 | 
| MaximumRetryAttempts | N | -1 | -1 means infinite: failed records are retried until the record expires<br />Minimum: 0<br />Maximum: 10,000 | 
| ParallelizationFactor | N | 1 | Maximum: 10 | 
| StartingPosition | Y | N/A | TRIM\_HORIZON or LATEST | 
| TumblingWindowInSeconds | N | N/A | Minimum: 0<br />Maximum: 900 | 