---
id: "@specs/aws/lambda/update_function_event_invoke_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateFunctionEventInvokeConfig"
---

# UpdateFunctionEventInvokeConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_function_event_invoke_config
> **spec:implements:** @kind:operation UpdateFunctionEventInvokeConfig
> **AWS Protocol:** rest-json
> **HTTP:** POST /2019-09-25/functions/{FunctionName}/event-invoke-config
> **@ref:** specs/aws/lambda/docs/API_UpdateFunctionEventInvokeConfig.spec.md

Updates the configuration for asynchronous invocation for a function, version, or alias. To configure options for asynchronous invocation, use PutFunctionEventInvokeConfig .

## Input Shape: UpdateFunctionEventInvokeConfigRequest

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
def update_function_event_invoke_config(store, request: dict) -> dict:
    """Updates the configuration for asynchronous invocation for a function, version, or alias. To configure options for asynchronous invocation, use PutFunctionEventInvokeConfig ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_event_invoke_configs(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")

    # Update mutable fields
    if "Qualifier" in request:
        resource["Qualifier"] = qualifier
    if "MaximumRetryAttempts" in request:
        resource["MaximumRetryAttempts"] = maximum_retry_attempts
    if "MaximumEventAgeInSeconds" in request:
        resource["MaximumEventAgeInSeconds"] = maximum_event_age_in_seconds
    if "DestinationConfig" in request:
        resource["DestinationConfig"] = destination_config

    store.function_event_invoke_configs(function_name, resource)
    return resource
```
