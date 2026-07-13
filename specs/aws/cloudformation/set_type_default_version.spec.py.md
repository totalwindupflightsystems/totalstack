---
id: "@specs/aws/cloudformation/set_type_default_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_SetTypeDefaultVersion"
---

# SetTypeDefaultVersion

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/set_type_default_version
> **spec:implements:** @kind:operation SetTypeDefaultVersion
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_SetTypeDefaultVersion.spec.md

Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.

## Input Shape: SetTypeDefaultVersionInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the extension for which you want version summary information. Conditional: You must sp |
| Type | Any  # complex shape |  | The kind of extension. Conditional: You must specify either TypeName and Type , or Arn . |
| TypeName | Any  # complex shape |  | The name of the extension. Conditional: You must specify either TypeName and Type , or Arn . |
| VersionId | Any  # complex shape |  | The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN)  |

## Output Shape: SetTypeDefaultVersionOutput


## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def set_type_default_version(store, request: dict) -> dict:
    """Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations."""

```
