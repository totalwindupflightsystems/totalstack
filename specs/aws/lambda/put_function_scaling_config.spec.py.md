---
id: "@specs/aws/lambda/put_function_scaling_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PutFunctionScalingConfig"
---

# PutFunctionScalingConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/put_function_scaling_config
> **spec:implements:** @kind:operation PutFunctionScalingConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2025-11-30/functions/{FunctionName}/function-scaling-config
> **@ref:** specs/aws/lambda/docs/API_PutFunctionScalingConfig.spec.md

Sets the scaling configuration for a Lambda Managed Instances function. The scaling configuration defines the minimum and maximum number of execution environments that can be provisioned for the function, allowing you to control scaling behavior and resource allocation.

## Input Shape: PutFunctionScalingConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. |
| FunctionScalingConfig | Any  # complex shape |  | The scaling configuration to apply to the function, including minimum and maximum execution environment limits. |
| Qualifier | Any  # complex shape | ✓ | Specify a version or alias to set the scaling configuration for a published version of the function. |

## Output Shape: PutFunctionScalingConfigResponse

- **FunctionState** (Any  # complex shape): The current state of the function after applying the scaling configuration.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def put_function_scaling_config(store, request: dict) -> dict:
    """Sets the scaling configuration for a Lambda Managed Instances function. The scaling configuration defines the minimum and maximum number of execution environments that can be provisioned for the funct"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    qualifier = request.get("Qualifier", "").strip() if isinstance(request.get("Qualifier"), str) else request.get("Qualifier")
    if not qualifier:
        raise ValidationException("Qualifier is required")

    if store.function_scaling_configs(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "Qualifier": qualifier,
        "FunctionScalingConfig": function_scaling_config,
    }

    store.function_scaling_configs(function_name, record)

    return {
        "FunctionState": record.get("FunctionState", {}),
    }
```
