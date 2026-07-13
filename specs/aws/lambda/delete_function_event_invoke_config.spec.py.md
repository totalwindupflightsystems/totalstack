---
id: "@specs/aws/lambda/delete_function_event_invoke_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteFunctionEventInvokeConfig"
---

# DeleteFunctionEventInvokeConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_function_event_invoke_config
> **spec:implements:** @kind:operation DeleteFunctionEventInvokeConfig
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2019-09-25/functions/{FunctionName}/event-invoke-config
> **@ref:** specs/aws/lambda/docs/API_DeleteFunctionEventInvokeConfig.spec.md

Deletes the configuration for asynchronous invocation for a function, version, or alias. To configure options for asynchronous invocation, use PutFunctionEventInvokeConfig .

## Input Shape: DeleteFunctionEventInvokeConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function, version, or alias. Name formats Function name - my-function (name-only), my-func |
| Qualifier | Any  # complex shape |  | A version number or alias name. |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def delete_function_event_invoke_config(store, request: dict) -> dict:
    """Deletes the configuration for asynchronous invocation for a function, version, or alias. To configure options for asynchronous invocation, use PutFunctionEventInvokeConfig ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")

    if not store.function_event_invoke_configs(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_function_event_invoke_configs(function_name)
    return {}
```
