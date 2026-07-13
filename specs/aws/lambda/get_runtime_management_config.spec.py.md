---
id: "@specs/aws/lambda/get_runtime_management_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetRuntimeManagementConfig"
---

# GetRuntimeManagementConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_runtime_management_config
> **spec:implements:** @kind:operation GetRuntimeManagementConfig
> **AWS Protocol:** rest-json
> **HTTP:** GET /2021-07-20/functions/{FunctionName}/runtime-management-config
> **@ref:** specs/aws/lambda/docs/API_GetRuntimeManagementConfig.spec.md

Retrieves the runtime management configuration for a function's version. If the runtime update mode is Manual , this includes the ARN of the runtime version and the runtime update mode. If the runtime update mode is Auto or Function update , this includes the runtime update mode and null is returned for the ARN. For more information, see Runtime updates .

## Input Shape: GetRuntimeManagementConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Qualifier | Any  # complex shape |  | Specify a version of the function. This can be $LATEST or a published version number. If no value is specified, the conf |

## Output Shape: GetRuntimeManagementConfigResponse

- **FunctionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of your function.
- **RuntimeVersionArn** (Any  # complex shape): The ARN of the runtime the function is configured to use. If the runtime update mode is Manual , the ARN is returned, ot
- **UpdateRuntimeOn** (Any  # complex shape): The current runtime update mode of the function.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_runtime_management_config(store, request: dict) -> dict:
    """Retrieves the runtime management configuration for a function's version. If the runtime update mode is Manual , this includes the ARN of the runtime version and the runtime update mode. If the runtime"""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.runtime_management_configs(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
