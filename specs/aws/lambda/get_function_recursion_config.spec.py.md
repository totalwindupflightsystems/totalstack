---
id: "@specs/aws/lambda/get_function_recursion_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetFunctionRecursionConfig"
---

# GetFunctionRecursionConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_function_recursion_config
> **spec:implements:** @kind:operation GetFunctionRecursionConfig
> **AWS Protocol:** rest-json
> **HTTP:** GET /2024-08-31/functions/{FunctionName}/recursion-config
> **@ref:** specs/aws/lambda/docs/API_GetFunctionRecursionConfig.spec.md

Returns your function's recursive loop detection configuration.

## Input Shape: GetFunctionRecursionConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name of the function. |

## Output Shape: GetFunctionRecursionConfigResponse

- **RecursiveLoop** (Any  # complex shape): If your function's recursive loop detection configuration is Allow , Lambda doesn't take any action when it detects your

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_function_recursion_config(store, request: dict) -> dict:
    """Returns your function's recursive loop detection configuration."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_recursion_configs(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
