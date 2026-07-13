---
id: "@specs/aws/lambda/update_event_source_mapping"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateEventSourceMapping"
---

# UpdateEventSourceMapping

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_event_source_mapping
> **spec:implements:** @kind:operation UpdateEventSourceMapping
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2015-03-31/event-source-mappings/{UUID}
> **@ref:** specs/aws/lambda/docs/API_UpdateEventSourceMapping.spec.md

Updates an event source mapping. You can change the function that Lambda invokes, or pause invocation and resume later from the same location. For details about how to configure different event sources, see the following topics. Amazon DynamoDB Streams Amazon Kinesis Amazon SQS Amazon MQ and RabbitMQ Amazon MSK Apache Kafka Amazon DocumentDB The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka): BisectBatchOnFunctionError – If the function returns an error, split the batch in two and retry. MaximumRecordAgeInSeconds – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires MaximumRetryAttempts – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires. OnFailure – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see Adding a destination . The following option is available only for DynamoDB and Kinesis event sources: ParallelizationFactor – Process multiple batches from each shard concurrently. For information about which configuration parameters apply to each event source, see the following topics. Amazon DynamoDB Streams Amazon Kinesis Amazon SQS Amazon MQ and RabbitMQ Amazon MSK Apache Kafka Amazon DocumentDB

## Input Shape: UpdateEventSourceMappingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AmazonManagedKafkaEventSourceConfig | Any  # complex shape |  |  |
| BatchSize | Any  # complex shape |  | The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lamb |
| BisectBatchOnFunctionError | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch |
| DestinationConfig | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destina |
| DocumentDBEventSourceConfig | Any  # complex shape |  | Specific configuration settings for a DocumentDB event source. |
| Enabled | Any  # complex shape |  | When true, the event source mapping is active. When false, Lambda pauses polling and invocation. Default: True |
| FilterCriteria | Any  # complex shape |  | An object that defines the filter criteria that determine whether Lambda should process an event. For more information,  |
| FunctionName | Any  # complex shape |  | The name or ARN of the Lambda function. Name formats Function name – MyFunction . Function ARN – arn:aws:lambda:us-west- |
| FunctionResponseTypes | list[Any  # complex shape] |  | (Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums |
| KMSKeyArn | Any  # complex shape |  | The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's filter crit |
| LoggingConfig | Any  # complex shape |  |  |
| MaximumBatchingWindowInSeconds | Any  # complex shape |  | The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can confi |
| MaximumRecordAgeInSeconds | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The |
| MaximumRetryAttempts | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of ret |
| MetricsConfig | Any  # complex shape |  | The metrics configuration for your event source. For more information, see Event source mapping metrics . |
| ParallelizationFactor | Any  # complex shape |  | (Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently. |
| ProvisionedPollerConfig | Any  # complex shape |  | (Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. Fo |
| ScalingConfig | Any  # complex shape |  | (Amazon SQS only) The scaling configuration for the event source. For more information, see Configuring maximum concurre |
| SelfManagedKafkaEventSourceConfig | Any  # complex shape |  |  |
| SourceAccessConfigurations | Any  # complex shape |  | An array of authentication protocols or VPC components required to secure your event source. |
| TumblingWindowInSeconds | Any  # complex shape |  | (Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams even |
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
- **ResourceInUseException**: The operation conflicts with the resource's availability. For example, you tried to update an event source mapping in the CREATING state, or you tried to delete an event source mapping currently UPDAT
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def update_event_source_mapping(store, request: dict) -> dict:
    """Updates an event source mapping. You can change the function that Lambda invokes, or pause invocation and resume later from the same location. For details about how to configure different event source"""
    uuid = request.get("UUID", "").strip() if isinstance(request.get("UUID"), str) else request.get("UUID")
    if not uuid:
        raise ValidationException("UUID is required")

    resource = store.event_source_mappings(uuid)
    if not resource:
        raise ResourceNotFoundException(f"Resource uuid not found")

    # Update mutable fields
    if "FunctionName" in request:
        resource["FunctionName"] = function_name
    if "Enabled" in request:
        resource["Enabled"] = enabled
    if "BatchSize" in request:
        resource["BatchSize"] = batch_size
    if "FilterCriteria" in request:
        resource["FilterCriteria"] = filter_criteria
    if "MaximumBatchingWindowInSeconds" in request:
        resource["MaximumBatchingWindowInSeconds"] = maximum_batching_window_in_seconds
    if "DestinationConfig" in request:
        resource["DestinationConfig"] = destination_config
    if "MaximumRecordAgeInSeconds" in request:
        resource["MaximumRecordAgeInSeconds"] = maximum_record_age_in_seconds
    if "BisectBatchOnFunctionError" in request:
        resource["BisectBatchOnFunctionError"] = bisect_batch_on_function_error
    if "MaximumRetryAttempts" in request:
        resource["MaximumRetryAttempts"] = maximum_retry_attempts
    if "ParallelizationFactor" in request:
        resource["ParallelizationFactor"] = parallelization_factor
    if "SourceAccessConfigurations" in request:
        resource["SourceAccessConfigurations"] = source_access_configurations
    if "TumblingWindowInSeconds" in request:
        resource["TumblingWindowInSeconds"] = tumbling_window_in_seconds
    if "FunctionResponseTypes" in request:
        resource["FunctionResponseTypes"] = function_response_types
    if "ScalingConfig" in request:
        resource["ScalingConfig"] = scaling_config
    if "AmazonManagedKafkaEventSourceConfig" in request:
        resource["AmazonManagedKafkaEventSourceConfig"] = amazon_managed_kafka_event_source_config
    if "SelfManagedKafkaEventSourceConfig" in request:
        resource["SelfManagedKafkaEventSourceConfig"] = self_managed_kafka_event_source_config
    if "DocumentDBEventSourceConfig" in request:
        resource["DocumentDBEventSourceConfig"] = document_db_event_source_config
    if "KMSKeyArn" in request:
        resource["KMSKeyArn"] = kms_key_arn
    if "MetricsConfig" in request:
        resource["MetricsConfig"] = metrics_config
    if "LoggingConfig" in request:
        resource["LoggingConfig"] = logging_config
    if "ProvisionedPollerConfig" in request:
        resource["ProvisionedPollerConfig"] = provisioned_poller_config

    store.event_source_mappings(uuid, resource)
    return resource
```
