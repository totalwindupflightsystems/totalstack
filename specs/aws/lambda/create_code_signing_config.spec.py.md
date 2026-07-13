---
id: "@specs/aws/lambda/create_code_signing_config"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_CreateCodeSigningConfig"
---

# CreateCodeSigningConfig

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/create_code_signing_config
> **spec:implements:** @kind:operation CreateCodeSigningConfig
> **AWS Protocol:** rest-json
> **HTTP:** POST /2020-04-22/code-signing-configs
> **@ref:** specs/aws/lambda/docs/API_CreateCodeSigningConfig.spec.md

Creates a code signing configuration. A code signing configuration defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail).

## Input Shape: CreateCodeSigningConfigRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllowedPublishers | Any  # complex shape | ✓ | Signing profiles for this code signing configuration. |
| CodeSigningPolicies | Any  # complex shape |  | The code signing policies define the actions to take if the validation checks fail. |
| Description | Any  # complex shape |  | Descriptive name for this code signing configuration. |
| Tags | Any  # complex shape |  | A list of tags to add to the code signing configuration. |

## Output Shape: CreateCodeSigningConfigResponse

- **CodeSigningConfig** (Any  # complex shape): The code signing configuration.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.

## Implementation

```speclang
def create_code_signing_config(store, request: dict) -> dict:
    """Creates a code signing configuration. A code signing configuration defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validatio"""
    allowed_publishers = request.get("AllowedPublishers", "").strip() if isinstance(request.get("AllowedPublishers"), str) else request.get("AllowedPublishers")
    if not allowed_publishers:
        raise ValidationException("AllowedPublishers is required")

    if store.code_signing_configs(allowed_publishers):
        raise ResourceInUseException(f"Resource allowed_publishers already exists")

    record = {
        "Description": description,
        "AllowedPublishers": allowed_publishers,
        "CodeSigningPolicies": code_signing_policies,
        "Tags": tags,
    }

    store.code_signing_configs(allowed_publishers, record)

    return {
        "CodeSigningConfig": record.get("CodeSigningConfig", {}),
    }
```
