---
id: "@specs/aws/lambda/get_function_scaling_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetFunctionScalingConfig"
---

# GetFunctionScalingConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_function_scaling_config
> **spec:implements:** @kind:operation GetFunctionScalingConfig
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-11-30/functions/{FunctionName}/function-scaling-config
> **@ref:** specs/aws/lambda/docs/API_GetFunctionScalingConfig.spec.md

Retrieves the scaling configuration for a Lambda Managed Instances function.

## Input Shape: GetFunctionScalingConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. |
| Qualifier | Any  # complex shape | ✓ | Specify a version or alias to get the scaling configuration for a published version of the function. |

## Output Shape: GetFunctionScalingConfigResponse

- **AppliedFunctionScalingConfig** (Any  # complex shape): The scaling configuration that is currently applied to the function. This represents the actual scaling settings in effe
- **FunctionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the function.
- **RequestedFunctionScalingConfig** (Any  # complex shape): The scaling configuration that was requested for the function.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_function_scaling_config(store, request: dict) -> dict:
    """Retrieves the scaling configuration for a Lambda Managed Instances function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    qualifier = request.get("Qualifier", "").strip() if isinstance(request.get("Qualifier"), str) else request.get("Qualifier")
    if not qualifier:
        raise ValidationException("Qualifier is required")

    resource = store.function_scaling_configs(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
