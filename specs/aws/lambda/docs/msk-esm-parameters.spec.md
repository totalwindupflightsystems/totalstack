---
id: "@specs/aws/lambda/docs/msk-esm-parameters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuration parameters"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Configuration parameters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/msk-esm-parameters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# All Amazon MSK event source configuration parameters in Lambda
<a name="msk-esm-parameters"></a>

All Lambda event source types share the same [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) and [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) API operations. However, only some of the parameters apply to Amazon MSK, as shown in the following table.


| Parameter | Required | Default | Notes | 
| --- | --- | --- | --- | 
| AmazonManagedKafkaEventSourceConfig | N | Contains the ConsumerGroupId field, which defaults to a unique value. | Can set only on Create | 
| BatchSize | N | 100 | Maximum: 10,000 | 
| DestinationConfig | N | N/A | [Capturing discarded batches for Amazon MSK and self-managed Apache Kafka event sources](kafka-on-failure.md) | 
| Enabled | N | True |  | 
| BisectBatchOnFunctionError | N | False | [Configuring error handling controls for Kafka event sources](kafka-retry-configurations.md) | 
| FunctionResponseTypes | N | N/A | [Configuring error handling controls for Kafka event sources](kafka-retry-configurations.md) | 
| MaximumRecordAgeInSeconds | N | -1 (infinite) | [Configuring error handling controls for Kafka event sources](kafka-retry-configurations.md) | 
| MaximumRetryAttempts | N | -1 (infinite) | [Configuring error handling controls for Kafka event sources](kafka-retry-configurations.md) | 
| EventSourceArn | Y | N/A | Can set only on Create | 
| FilterCriteria | N | N/A | [Control which events Lambda sends to your function](invocation-eventfiltering.md) | 
| FunctionName | Y | N/A |  | 
| KMSKeyArn | N | N/A | [Encryption of filter criteria](invocation-eventfiltering.md#filter-criteria-encryption) | 
| MaximumBatchingWindowInSeconds | N | 500 ms | [Batching behavior](invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching) | 
| ProvisionedPollersConfig | N | `MinimumPollers`: default value of 1 if not specified<br />`MaximumPollers`: default value of 200 if not specified<br />`PollerGroupName`: N/A | [Provisioned mode](kafka-scaling-modes.md#kafka-provisioned-mode) | 
| SourceAccessConfigurations | N | No credentials | SASL/SCRAM or CLIENT\_CERTIFICATE\_TLS\_AUTH (MutualTLS) authentication credentials for your event source | 
| StartingPosition | Y | N/A | AT\_TIMESTAMP, TRIM\_HORIZON, or LATEST<br />Can set only on Create | 
| StartingPositionTimestamp | N | N/A | Required if StartingPosition is set to AT\_TIMESTAMP | 
| Tags | N | N/A | [Using tags on event source mappings](tags-esm.md) | 
| Topics | Y | N/A | Kafka topic name<br />Can set only on Create | 

**Note**  
When you specify a `PollerGroupName`, multiple ESMs within the same Amazon VPC can share Event Poller Unit (EPU) capacity. You can use this option to optimize Provisioned mode costs for your ESMs. Requirements for ESM grouping:  
ESMs must be within the same Amazon VPC
Maximum of 100 ESMs per poller group
Aggregate maximum pollers across all ESMs in a group cannot exceed 2000
You can update the `PollerGroupName` to move an ESM to a different group, or remove an ESM from a group by setting `PollerGroupName` to an empty string ("").