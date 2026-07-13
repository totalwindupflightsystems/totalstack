---
id: "@specs/aws/lambda/create_event_source_mapping"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_CreateEventSourceMapping"
---

# CreateEventSourceMapping

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/create_event_source_mapping
> **spec:implements:** @kind:operation CreateEventSourceMapping
> **AWS Protocol:** rest-json
> **HTTP:** POST /2015-03-31/event-source-mappings
> **@ref:** specs/aws/lambda/docs/API_CreateEventSourceMapping.spec.md

Creates a mapping between an event source and an Lambda function. Lambda reads items from the event source and invokes the function. For details about how to configure different event sources, see the following topics. Amazon DynamoDB Streams Amazon Kinesis Amazon SQS Amazon MQ and RabbitMQ Amazon MSK Apache Kafka Amazon DocumentDB The following error handling options are available for stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka): BisectBatchOnFunctionError – If the function returns an error, split the batch in two and retry. MaximumRecordAgeInSeconds – Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires MaximumRetryAttempts – Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires. OnFailure – Send discarded records to an Amazon SQS queue, Amazon SNS topic, Kafka topic, or Amazon S3 bucket. For more information, see Adding a destination . The following option is available only for DynamoDB and Kinesis event sources: ParallelizationFactor – Process multiple batches from each shard concurrently. For information about which configuration parameters apply to each event source, see the following topics. Amazon DynamoDB Streams Amazon Kinesis Amazon SQS Amazon MQ and RabbitMQ Amazon MSK Apache Kafka Amazon DocumentDB

## Input Shape: CreateEventSourceMappingRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AmazonManagedKafkaEventSourceConfig | Any  # complex shape |  | Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source. |
| BatchSize | Any  # complex shape |  | The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lamb |
| BisectBatchOnFunctionError | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch |
| DestinationConfig | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destina |
| DocumentDBEventSourceConfig | Any  # complex shape |  | Specific configuration settings for a DocumentDB event source. |
| Enabled | Any  # complex shape |  | When true, the event source mapping is active. When false, Lambda pauses polling and invocation. Default: True |
| EventSourceArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the event source. Amazon Kinesis – The ARN of the data stream or a stream consumer. Am |
| FilterCriteria | Any  # complex shape |  | An object that defines the filter criteria that determine whether Lambda should process an event. For more information,  |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – MyFunction . Function ARN – arn:aws:lambda:us-west- |
| FunctionResponseTypes | list[Any  # complex shape] |  | (Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums |
| KMSKeyArn | Any  # complex shape |  | The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's filter crit |
| LoggingConfig | Any  # complex shape |  | (Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information,  |
| MaximumBatchingWindowInSeconds | Any  # complex shape |  | The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can confi |
| MaximumRecordAgeInSeconds | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The |
| MaximumRetryAttempts | Any  # complex shape |  | (Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of ret |
| MetricsConfig | Any  # complex shape |  | The metrics configuration for your event source. For more information, see Event source mapping metrics . |
| ParallelizationFactor | Any  # complex shape |  | (Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently. |
| ProvisionedPollerConfig | Any  # complex shape |  | (Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. Fo |
| Queues | Any  # complex shape |  | (MQ) The name of the Amazon MQ broker destination queue to consume. |
| ScalingConfig | Any  # complex shape |  | (Amazon SQS only) The scaling configuration for the event source. For more information, see Configuring maximum concurre |
| SelfManagedEventSource | Any  # complex shape |  | The self-managed Apache Kafka cluster to receive records from. |
| SelfManagedKafkaEventSourceConfig | Any  # complex shape |  | Specific configuration settings for a self-managed Apache Kafka event source. |
| SourceAccessConfigurations | Any  # complex shape |  | An array of authentication protocols or VPC components required to secure your event source. |
| StartingPosition | Any  # complex shape |  | The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sourc |
| StartingPositionTimestamp | str  # ISO8601 |  | With StartingPosition set to AT_TIMESTAMP , the time from which to start reading. StartingPositionTimestamp cannot be in |
| Tags | Any  # complex shape |  | A list of tags to apply to the event source mapping. |
| Topics | Any  # complex shape |  | The name of the Kafka topic. |
| TumblingWindowInSeconds | Any  # complex shape |  | (Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams even |

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
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def create_event_source_mapping(store, request: dict) -> dict:
    """Creates a mapping between an event source and an Lambda function. Lambda reads items from the event source and invokes the function. For details about how to configure different event sources, see the"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    if store.event_source_mappings(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "EventSourceArn": event_source_arn,
        "FunctionName": function_name,
        "Enabled": enabled,
        "BatchSize": batch_size,
        "FilterCriteria": filter_criteria,
        "MaximumBatchingWindowInSeconds": maximum_batching_window_in_seconds,
        "ParallelizationFactor": parallelization_factor,
        "StartingPosition": starting_position,
        "StartingPositionTimestamp": starting_position_timestamp,
        "DestinationConfig": destination_config,
        "MaximumRecordAgeInSeconds": maximum_record_age_in_seconds,
        "BisectBatchOnFunctionError": bisect_batch_on_function_error,
        "MaximumRetryAttempts": maximum_retry_attempts,
        "Tags": tags,
        "TumblingWindowInSeconds": tumbling_window_in_seconds,
        "Topics": topics,
        "Queues": queues,
        "SourceAccessConfigurations": source_access_configurations,
        "SelfManagedEventSource": self_managed_event_source,
        "FunctionResponseTypes": function_response_types,
        "AmazonManagedKafkaEventSourceConfig": amazon_managed_kafka_event_source_config,
        "SelfManagedKafkaEventSourceConfig": self_managed_kafka_event_source_config,
        "ScalingConfig": scaling_config,
        "DocumentDBEventSourceConfig": document_db_event_source_config,
        "KMSKeyArn": kms_key_arn,
        "MetricsConfig": metrics_config,
        "LoggingConfig": logging_config,
        "ProvisionedPollerConfig": provisioned_poller_config,
    }

    store.event_source_mappings(function_name, record)

    return {
        "UUID": record.get("UUID", {}),
        "StartingPosition": record.get("StartingPosition", {}),
        "StartingPositionTimestamp": record.get("StartingPositionTimestamp", {}),
        "BatchSize": record.get("BatchSize", {}),
        "MaximumBatchingWindowInSeconds": record.get("MaximumBatchingWindowInSeconds", {}),
        "ParallelizationFactor": record.get("ParallelizationFactor", {}),
        "EventSourceArn": record.get("EventSourceArn", {}),
        "FilterCriteria": record.get("FilterCriteria", {}),
        "FunctionArn": record.get("FunctionArn", {}),
        "LastModified": record.get("LastModified", {}),
        "LastProcessingResult": record.get("LastProcessingResult", {}),
        "State": record.get("State", {}),
        "StateTransitionReason": record.get("StateTransitionReason", {}),
        "DestinationConfig": record.get("DestinationConfig", {}),
        "Topics": record.get("Topics", {}),
        "Queues": record.get("Queues", {}),
        "SourceAccessConfigurations": record.get("SourceAccessConfigurations", {}),
        "SelfManagedEventSource": record.get("SelfManagedEventSource", {}),
        "MaximumRecordAgeInSeconds": record.get("MaximumRecordAgeInSeconds", {}),
        "BisectBatchOnFunctionError": record.get("BisectBatchOnFunctionError", {}),
        "MaximumRetryAttempts": record.get("MaximumRetryAttempts", {}),
        "TumblingWindowInSeconds": record.get("TumblingWindowInSeconds", {}),
        "FunctionResponseTypes": record.get("FunctionResponseTypes", {}),
        "AmazonManagedKafkaEventSourceConfig": record.get("AmazonManagedKafkaEventSourceConfig", {}),
        "SelfManagedKafkaEventSourceConfig": record.get("SelfManagedKafkaEventSourceConfig", {}),
        "ScalingConfig": record.get("ScalingConfig", {}),
        "DocumentDBEventSourceConfig": record.get("DocumentDBEventSourceConfig", {}),
        "KMSKeyArn": record.get("KMSKeyArn", {}),
        "FilterCriteriaError": record.get("FilterCriteriaError", {}),
        "EventSourceMappingArn": record.get("EventSourceMappingArn", {}),
        "MetricsConfig": record.get("MetricsConfig", {}),
        "LoggingConfig": record.get("LoggingConfig", {}),
        "ProvisionedPollerConfig": record.get("ProvisionedPollerConfig", {}),
    }
```
