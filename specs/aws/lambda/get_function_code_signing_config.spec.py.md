---
id: "@specs/aws/lambda/get_function_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetFunctionCodeSigningConfig"
---

# GetFunctionCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_function_code_signing_config
> **spec:implements:** @kind:operation GetFunctionCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** GET /2020-06-30/functions/{FunctionName}/code-signing-config
> **@ref:** specs/aws/lambda/docs/API_GetFunctionCodeSigningConfig.spec.md

Returns the code signing configuration for the specified function.

## Input Shape: GetFunctionCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |

## Output Shape: GetFunctionCodeSigningConfigResponse

- **CodeSigningConfigArn** (Any  # complex shape): The The Amazon Resource Name (ARN) of the code signing configuration.
- **FunctionName** (Any  # complex shape): The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west-

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_function_code_signing_config(store, request: dict) -> dict:
    """Returns the code signing configuration for the specified function."""
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    resource = store.function_code_signing_configs(function_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource function_name not found")
    return {"FunctionName": function_name, **resource}
```
