---
id: "@specs/aws/lambda/docs/services-mq-params"
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
> **spec:id:** @specs/aws/lambda/docs/services-mq-params
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Event source mapping parameters
<a name="services-mq-params"></a>

All Lambda event source types share the same [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) and [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) API operations. However, only some of the parameters apply to Amazon MQ and RabbitMQ.


| Parameter | Required | Default | Notes | 
| --- | --- | --- | --- | 
| BatchSize | N | 100 | Maximum: 10,000 | 
| Enabled | N | true | none | 
| FunctionName | Y | N/A  | none | 
| FilterCriteria | N | N/A  | [Control which events Lambda sends to your function](invocation-eventfiltering.md) | 
| MaximumBatchingWindowInSeconds | N | 500 ms | [Batching behavior](invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching) | 
| Queues | N | N/A | The name of the Amazon MQ broker destination queue to consume. | 
| SourceAccessConfigurations | N | N/A  | For ActiveMQ, BASIC\_AUTH credentials. For RabbitMQ, can contain both BASIC\_AUTH credentials and VIRTUAL\_HOST information. | 