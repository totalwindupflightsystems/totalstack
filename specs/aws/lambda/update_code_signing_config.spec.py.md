---
id: "@specs/aws/lambda/update_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateCodeSigningConfig"
---

# UpdateCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_code_signing_config
> **spec:implements:** @kind:operation UpdateCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2020-04-22/code-signing-configs/{CodeSigningConfigArn}
> **@ref:** specs/aws/lambda/docs/API_UpdateCodeSigningConfig.spec.md

Update the code signing configuration. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function.

## Input Shape: UpdateCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllowedPublishers | Any  # complex shape |  | Signing profiles for this code signing configuration. |
| CodeSigningConfigArn | Any  # complex shape | ✓ | The The Amazon Resource Name (ARN) of the code signing configuration. |
| CodeSigningPolicies | Any  # complex shape |  | The code signing policy. |
| Description | Any  # complex shape |  | Descriptive name for this code signing configuration. |

## Output Shape: UpdateCodeSigningConfigResponse

- **CodeSigningConfig** (Any  # complex shape): The code signing configuration

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def update_code_signing_config(store, request: dict) -> dict:
    """Update the code signing configuration. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function."""
    code_signing_config_arn = request.get("CodeSigningConfigArn", "").strip() if isinstance(request.get("CodeSigningConfigArn"), str) else request.get("CodeSigningConfigArn")
    if not code_signing_config_arn:
        raise ValidationException("CodeSigningConfigArn is required")

    resource = store.code_signing_configs(code_signing_config_arn)
    if not resource:
        raise ResourceNotFoundException(f"Resource code_signing_config_arn not found")

    # Update mutable fields
    if "Description" in request:
        resource["Description"] = description
    if "AllowedPublishers" in request:
        resource["AllowedPublishers"] = allowed_publishers
    if "CodeSigningPolicies" in request:
        resource["CodeSigningPolicies"] = code_signing_policies

    store.code_signing_configs(code_signing_config_arn, resource)
    return resource
```
