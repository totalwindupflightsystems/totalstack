---
id: "@specs/aws/lambda/get_event_source_mapping"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetEventSourceMapping"
---

# GetEventSourceMapping

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_event_source_mapping
> **spec:implements:** @kind:operation GetEventSourceMapping
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/event-source-mappings/{UUID}
> **@ref:** specs/aws/lambda/docs/API_GetEventSourceMapping.spec.md

Returns details about an event source mapping. You can get the identifier of a mapping from the output of ListEventSourceMappings .

## Input Shape: GetEventSourceMappingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| UUID | str | ✓ | The identifier of the event source mapping. |

## Output Shape: EventSourceMappingConfiguration

- **AmazonManagedKafkaEventSourceConfig** (Any  # complex shape): Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.
- **BatchSize** (Any  # complex shape): The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lamb
- **BisectBatchOnFunctionError** (Any  # complex shape): (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch
- **DestinationConfig** (Any  # complex shape): (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destina
- **DocumentDBEventSourceConfig** (Any  # complex shape): Specific configuration settings for a DocumentDB event source.
- **EventSourceArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the event source.
- **EventSourceMappingArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the event source mapping.
- **FilterCriteria** (Any  # complex shape): An object that defines the filter criteria that determine whether Lambda should process an event. For more information, 
- **FilterCriteriaError** (Any  # complex shape): An object that contains details about an error related to filter criteria encryption.
- **FunctionArn** (Any  # complex shape): The ARN of the Lambda function.
- **FunctionResponseTypes** (list[Any  # complex shape]): (Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums
- **KMSKeyArn** (Any  # complex shape): The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's filter crit
- **LastModified** (str  # ISO8601): The date that the event source mapping was last updated or that its state changed.
- **LastProcessingResult** (str): The result of the event source mapping's last processing attempt.
- **LoggingConfig** (Any  # complex shape): (Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, 
- **MaximumBatchingWindowInSeconds** (Any  # complex shape): The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can confi
- **MaximumRecordAgeInSeconds** (Any  # complex shape): (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The
- **MaximumRetryAttempts** (Any  # complex shape): (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of ret
- **MetricsConfig** (Any  # complex shape): The metrics configuration for your event source. For more information, see Event source mapping metrics .
- **ParallelizationFactor** (Any  # complex shape): (Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 
- **ProvisionedPollerConfig** (Any  # complex shape): (Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. Fo
- **Queues** (Any  # complex shape): (Amazon MQ) The name of the Amazon MQ broker destination queue to consume.
- **ScalingConfig** (Any  # complex shape): (Amazon SQS only) The scaling configuration for the event source. For more information, see Configuring maximum concurre
- **SelfManagedEventSource** (Any  # complex shape): The self-managed Apache Kafka cluster for your event source.
- **SelfManagedKafkaEventSourceConfig** (Any  # complex shape): Specific configuration settings for a self-managed Apache Kafka event source.
- **SourceAccessConfigurations** (Any  # complex shape): An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.
- **StartingPosition** (Any  # complex shape): The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sourc
- **StartingPositionTimestamp** (str  # ISO8601): With StartingPosition set to AT_TIMESTAMP , the time from which to start reading. StartingPositionTimestamp cannot be in
- **State** (str): The state of the event source mapping. It can be one of the following: Creating , Enabling , Enabled , Disabling , Disab
- **StateTransitionReason** (str): Indicates whether a user or Lambda made the last change to the event source mapping.
- **Topics** (Any  # complex shape): The name of the Kafka topic.
- **TumblingWindowInSeconds** (Any  # complex shape): (Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams even
- **UUID** (str): The identifier of the event source mapping.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_event_source_mapping(store, request: dict) -> dict:
    """Returns details about an event source mapping. You can get the identifier of a mapping from the output of ListEventSourceMappings ."""
    uuid = request.get("UUID", "").strip() if isinstance(request.get("UUID"), str) else request.get("UUID")
    if not uuid:
        raise ValidationException("UUID is required")

    resource = store.event_source_mappings(uuid)
    if not resource:
        raise ResourceNotFoundException(f"Resource uuid not found")
    return {"UUID": uuid, **resource}
```
