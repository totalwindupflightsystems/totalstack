---
id: "@specs/aws/lambda/put_function_event_invoke_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PutFunctionEventInvokeConfig"
---

# PutFunctionEventInvokeConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/put_function_event_invoke_config
> **spec:implements:** @kind:operation PutFunctionEventInvokeConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2019-09-25/functions/{FunctionName}/event-invoke-config
> **@ref:** specs/aws/lambda/docs/API_PutFunctionEventInvokeConfig.spec.md

Configures options for asynchronous invocation on a function, version, or alias. If a configuration already exists for a function, version, or alias, this operation overwrites it. If you exclude any settings, they are removed. To set one option without affecting existing settings for other options, use UpdateFunctionEventInvokeConfig . By default, Lambda retries an asynchronous invocation twice if the function returns an error. It retains events in a queue for up to six hours. When an event fails all processing attempts or stays in the asynchronous invocation queue for too long, Lambda discards it. To retain discarded events, configure a dead-letter queue with UpdateFunctionConfiguration . To send an invocation record to a queue, topic, S3 bucket, function, or event bus, specify a destination . You can configure separate destinations for successful invocations (on-success) and events that fail all processing attempts (on-failure). You can configure destinations in addition to or instead of a dead-letter queue. S3 buckets are supported only for on-failure destinations. To retain records of successful invocations, use another destination type.

## Input Shape: PutFunctionEventInvokeConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DestinationConfig | Any  # complex shape |  | A destination for events after they have been sent to a function for processing. Destinations Function - The Amazon Reso |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name - my-function (name-only), my-func |
| MaximumEventAgeInSeconds | Any  # complex shape |  | The maximum age of a request that Lambda sends to a function for processing. |
| MaximumRetryAttempts | Any  # complex shape |  | The maximum number of times to retry when the function returns an error. |
| Qualifier | Any  # complex shape |  | A version number or alias name. |

## Output Shape: FunctionEventInvokeConfig

- **DestinationConfig** (Any  # complex shape): A destination for events after they have been sent to a function for processing. Destinations Function - The Amazon Reso
- **FunctionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the function.
- **LastModified** (str  # ISO8601): The date and time that the configuration was last updated.
- **MaximumEventAgeInSeconds** (Any  # complex shape): The maximum age of a request that Lambda sends to a function for processing.
- **MaximumRetryAttempts** (Any  # complex shape): The maximum number of times to retry when the function returns an error.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def put_function_event_invoke_config(store, request: dict) -> dict:
    """Configures options for asynchronous invocation on a function, version, or alias. If a configuration already exists for a function, version, or alias, this operation overwrites it. If you exclude any s"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    if store.function_event_invoke_configs(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "Qualifier": qualifier,
        "MaximumRetryAttempts": maximum_retry_attempts,
        "MaximumEventAgeInSeconds": maximum_event_age_in_seconds,
        "DestinationConfig": destination_config,
    }

    store.function_event_invoke_configs(function_name, record)

    return {
        "LastModified": record.get("LastModified", {}),
        "FunctionArn": record.get("FunctionArn", {}),
        "MaximumRetryAttempts": record.get("MaximumRetryAttempts", {}),
        "MaximumEventAgeInSeconds": record.get("MaximumEventAgeInSeconds", {}),
        "DestinationConfig": record.get("DestinationConfig", {}),
    }
```
