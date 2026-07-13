---
id: "@specs/aws/lambda/put_function_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_PutFunctionCodeSigningConfig"
---

# PutFunctionCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/put_function_code_signing_config
> **spec:implements:** @kind:operation PutFunctionCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2020-06-30/functions/{FunctionName}/code-signing-config
> **@ref:** specs/aws/lambda/docs/API_PutFunctionCodeSigningConfig.spec.md

Update the code signing configuration for the function. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function.

## Input Shape: PutFunctionCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CodeSigningConfigArn | Any  # complex shape | ✓ | The The Amazon Resource Name (ARN) of the code signing configuration. |
| FunctionName | Any  # complex shape | ✓ | The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west- |

## Output Shape: PutFunctionCodeSigningConfigResponse

- **CodeSigningConfigArn** (Any  # complex shape): The The Amazon Resource Name (ARN) of the code signing configuration.
- **FunctionName** (Any  # complex shape): The name or ARN of the Lambda function. Name formats Function name - MyFunction . Function ARN - arn:aws:lambda:us-west-

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.
- **CodeSigningConfigNotFoundException**: The specified code signing configuration does not exist.

## Implementation

```speclang
def put_function_code_signing_config(store, request: dict) -> dict:
    """Update the code signing configuration for the function. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function."""
    code_signing_config_arn = request.get("CodeSigningConfigArn", "").strip() if isinstance(request.get("CodeSigningConfigArn"), str) else request.get("CodeSigningConfigArn")
    if not code_signing_config_arn:
        raise ValidationException("CodeSigningConfigArn is required")
    function_name = request.get("FunctionName", "").strip() if isinstance(request.get("FunctionName"), str) else request.get("FunctionName")
    if not function_name:
        raise ValidationException("FunctionName is required")

    if store.function_code_signing_configs(function_name):
        raise ResourceInUseException(f"Resource function_name already exists")

    record = {
        "CodeSigningConfigArn": code_signing_config_arn,
        "FunctionName": function_name,
    }

    store.function_code_signing_configs(function_name, record)

    return {
        "CodeSigningConfigArn": record.get("CodeSigningConfigArn", {}),
        "FunctionName": function_name,
    }
```
