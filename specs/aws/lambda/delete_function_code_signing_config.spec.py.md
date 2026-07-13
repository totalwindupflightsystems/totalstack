---
id: "@specs/aws/lambda/delete_function_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteFunctionCodeSigningConfig"
---

# DeleteFunctionCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_function_code_signing_config
> **spec:implements:** @kind:operation DeleteFunctionCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2020-06-30/functions/{FunctionName}/code-signing-config
> **@ref:** specs/aws/lambda/docs/API_DeleteFunctionCodeSigningConfig.spec.md

Removes the code signing configuration from the function.

## Input Shape: DeleteFunctionCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **CodeSigningConfigNotFoundException**: The specified code signing configuration does not exist.

## Implementation

```speclang
def delete_function_code_signing_config(store, request: dict) -> dict:
    """Removes the code signing configuration from the function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")

    if not store.function_code_signing_configs(function_name):
        raise ResourceNotFoundException(f"Resource function_name not found")
    store.delete_function_code_signing_configs(function_name)
    return {}
```
