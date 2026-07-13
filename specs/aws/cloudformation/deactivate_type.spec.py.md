---
id: "@specs/aws/cloudformation/deactivate_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeactivateType"
---

# DeactivateType

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/deactivate_type
> **spec:implements:** @kind:operation DeactivateType
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeactivateType.spec.md

Deactivates a public third-party extension, such as a resource or module, or a CloudFormation Hook when you no longer use it. Deactivating an extension deletes the configuration details that are associated with it. To temporarily disable a CloudFormation Hook instead, you can use SetTypeConfiguration . Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released. To see which extensions are currently activated, use ListTypes .

## Input Shape: DeactivateTypeInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape |  | The Amazon Resource Name (ARN) for the extension in this account and Region. Conditional: You must specify either Arn ,  |
| Type | Any  # complex shape |  | The extension type. Conditional: You must specify either Arn , or TypeName and Type . |
| TypeName | Any  # complex shape |  | The type name of the extension in this account and Region. If you specified a type name alias when enabling the extensio |

## Output Shape: DeactivateTypeOutput


## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def deactivate_type(store, request: dict) -> dict:
    """Deactivates a public third-party extension, such as a resource or module, or a CloudFormation Hook when you no longer use it. Deactivating an extension deletes the configuration details that are assoc"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DeactivateType", request)
```
