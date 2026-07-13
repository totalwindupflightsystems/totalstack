---
id: "@specs/aws/lambda/get_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetCodeSigningConfig"
---

# GetCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_code_signing_config
> **spec:implements:** @kind:operation GetCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** GET /2020-04-22/code-signing-configs/{CodeSigningConfigArn}
> **@ref:** specs/aws/lambda/docs/API_GetCodeSigningConfig.spec.md

Returns information about the specified code signing configuration.

## Input Shape: GetCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CodeSigningConfigArn | Any  # complex shape | ✓ | The The Amazon Resource Name (ARN) of the code signing configuration. |

## Output Shape: GetCodeSigningConfigResponse

- **CodeSigningConfig** (Any  # complex shape): The code signing configuration

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_code_signing_config(store, request: dict) -> dict:
    """Returns information about the specified code signing configuration."""
    code_signing_config_arn = request.get("CodeSigningConfigArn", "").strip() if isinstance(request.get("CodeSigningConfigArn"), str) else request.get("CodeSigningConfigArn")
    if not code_signing_config_arn:
        raise ValidationException("CodeSigningConfigArn is required")

    resource = store.code_signing_configs(code_signing_config_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource code_signing_config_arn not found")
    return {"CodeSigningConfigArn": code_signing_config_arn, **resource}
```
