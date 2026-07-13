---
id: "@specs/aws/cloudformation/publish_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_PublishType"
---

# PublishType

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/publish_type
> **spec:implements:** @kind:operation PublishType
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_PublishType.spec.md

Publishes the specified extension to the CloudFormation registry as a public extension in this Region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see Publishing extensions to make them available for public use in the CloudFormation Command Line Interface (CLI) User Guide . To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see RegisterPublisher .

## Input Shape: PublishTypeInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the extension. Conditional: You must specify Arn , or TypeName and Type . |
| PublicVersionNumber | Any  # complex shape |  | The version number to assign to this version of the extension. Use the following format, and adhere to semantic versioni |
| Type | Any  # complex shape |  | The type of the extension. Conditional: You must specify Arn , or TypeName and Type . |
| TypeName | Any  # complex shape |  | The name of the extension. Conditional: You must specify Arn , or TypeName and Type . |

## Output Shape: PublishTypeOutput

- **PublicTypeArn** (Any  # complex shape): The Amazon Resource Name (ARN) assigned to the public extension upon publication.

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def publish_type(store, request: dict) -> dict:
    """Publishes the specified extension to the CloudFormation registry as a public extension in this Region. Public extensions are available for use by all CloudFormation users. For more information about p"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PublishType", request)
```
