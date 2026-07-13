---
id: "@specs/aws/lambda/delete_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteCodeSigningConfig"
---

# DeleteCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_code_signing_config
> **spec:implements:** @kind:operation DeleteCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2020-04-22/code-signing-configs/{CodeSigningConfigArn}
> **@ref:** specs/aws/lambda/docs/API_DeleteCodeSigningConfig.spec.md

Deletes the code signing configuration. You can delete the code signing configuration only if no function is using it.

## Input Shape: DeleteCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CodeSigningConfigArn | Any  # complex shape | ✓ | The The Amazon Resource Name (ARN) of the code signing configuration. |

## Output Shape: DeleteCodeSigningConfigResponse


## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def delete_code_signing_config(store, request: dict) -> dict:
    """Deletes the code signing configuration. You can delete the code signing configuration only if no function is using it."""
    code_signing_config_arn = request.get("CodeSigningConfigArn", "").strip() if isinstance(request.get("CodeSigningConfigArn"), str) else request.get("CodeSigningConfigArn")

    if not store.code_signing_configs(code_signing_config_arn):
        raise ResourceNotFoundException(f"Resource code_signing_config_arn not found")
    store.delete_code_signing_configs(code_signing_config_arn)
    return {}
```
