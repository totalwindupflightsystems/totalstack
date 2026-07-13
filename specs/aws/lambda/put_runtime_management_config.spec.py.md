---
id: "@specs/aws/lambda/put_runtime_management_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PutRuntimeManagementConfig"
---

# PutRuntimeManagementConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/put_runtime_management_config
> **spec:implements:** @kind:operation PutRuntimeManagementConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2021-07-20/functions/{FunctionName}/runtime-management-config
> **@ref:** specs/aws/lambda/docs/API_PutRuntimeManagementConfig.spec.md

Sets the runtime management configuration for a function's version. For more information, see Runtime updates .

## Input Shape: PutRuntimeManagementConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name – my-function . Function ARN – arn:aws:lambda:us-west |
| Qualifier | Any  # complex shape |  | Specify a version of the function. This can be $LATEST or a published version number. If no value is specified, the conf |
| RuntimeVersionArn | Any  # complex shape |  | The ARN of the runtime version you want the function to use. This is only required if you're using the Manual runtime up |
| UpdateRuntimeOn | Any  # complex shape | ✓ | Specify the runtime update mode. Auto (default) - Automatically update to the most recent and secure runtime version usi |

## Output Shape: PutRuntimeManagementConfigResponse

- **FunctionArn** (Any  # complex shape): The ARN of the function
- **RuntimeVersionArn** (Any  # complex shape): The ARN of the runtime the function is configured to use. If the runtime update mode is manual , the ARN is returned, ot
- **UpdateRuntimeOn** (Any  # complex shape): The runtime update mode.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def put_runtime_management_config(store, request: dict) -> dict:
    """Sets the runtime management configuration for a function's version. For more information, see Runtime updates ."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")
    update_runtime_on = request.get("UpdateRuntimeOn", "").strip() if isinstance(request.get("UpdateRuntimeOn"), str) else request.get("UpdateRuntimeOn")
    if not update_runtime_on:
        raise ValidationException("UpdateRuntimeOn is required")

    if store.runtime_management_configs(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "FunctionName": function_name,
        "Qualifier": qualifier,
        "UpdateRuntimeOn": update_runtime_on,
        "RuntimeVersionArn": runtime_version_arn,
    }

    store.runtime_management_configs(function_name, record)

    return {
        "UpdateRuntimeOn": record.get("UpdateRuntimeOn", {}),
        "FunctionArn": record.get("FunctionArn", {}),
        "RuntimeVersionArn": record.get("RuntimeVersionArn", {}),
    }
```
