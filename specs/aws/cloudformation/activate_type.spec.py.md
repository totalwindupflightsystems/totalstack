---
id: "@specs/aws/cloudformation/activate_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ActivateType"
---

# ActivateType

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/activate_type
> **spec:implements:** @kind:operation ActivateType
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ActivateType.spec.md

Activates a public third-party extension, such as a resource or module, to make it available for use in stack templates in your current account and Region. It can also create CloudFormation Hooks, which allow you to evaluate resource configurations before CloudFormation provisions them. Hooks integrate with both CloudFormation and Cloud Control API operations. After you activate an extension, you can use SetTypeConfiguration to set specific properties for the extension. To see which extensions have been activated, use ListTypes . To see configuration details for an extension, use DescribeType . For more information, see Activate a third-party public extension in your account in the CloudFormation User Guide . For information about creating Hooks, see the CloudFormation Hooks User Guide .

## Input Shape: ActivateTypeInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AutoUpdate | Any  # complex shape |  | Whether to automatically update the extension in this account and Region when a new minor version is published by the ex |
| ExecutionRoleArn | Any  # complex shape |  | The name of the IAM execution role to use to activate the extension. |
| LoggingConfig | Any  # complex shape |  | Contains logging configuration information for an extension. |
| MajorVersion | Any  # complex shape |  | The major version of this extension you want to activate, if multiple major versions are available. The default is the l |
| PublicTypeArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the public extension. Conditional: You must specify PublicTypeArn , or TypeName , Type |
| PublisherId | Any  # complex shape |  | The ID of the extension publisher. Conditional: You must specify PublicTypeArn , or TypeName , Type , and PublisherId . |
| Type | Any  # complex shape |  | The extension type. Conditional: You must specify PublicTypeArn , or TypeName , Type , and PublisherId . |
| TypeName | Any  # complex shape |  | The name of the extension. Conditional: You must specify PublicTypeArn , or TypeName , Type , and PublisherId . |
| TypeNameAlias | Any  # complex shape |  | An alias to assign to the public extension in this account and Region. If you specify an alias for the extension, CloudF |
| VersionBump | Any  # complex shape |  | Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parame |

## Output Shape: ActivateTypeOutput

- **Arn** (Any  # complex shape): The Amazon Resource Name (ARN) of the activated extension in this account and Region.

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def activate_type(store, request: dict) -> dict:
    """Activates a public third-party extension, such as a resource or module, to make it available for use in stack templates in your current account and Region. It can also create CloudFormation Hooks, whi"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ActivateType", request)
```
