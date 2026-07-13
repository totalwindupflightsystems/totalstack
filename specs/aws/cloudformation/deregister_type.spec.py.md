---
id: "@specs/aws/cloudformation/deregister_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DeregisterType"
---

# DeregisterType

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/deregister_type
> **spec:implements:** @kind:operation DeregisterType
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DeregisterType.spec.md

Marks an extension or extension version as DEPRECATED in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations. To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry. You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated. To view the deprecation status of an extension or extension version, use DescribeType . For more information, see Remove third-party private extensions from your account in the CloudFormation User Guide .

## Input Shape: DeregisterTypeInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the extension. Conditional: You must specify either TypeName and Type , or Arn . |
| Type | Any  # complex shape |  | The kind of extension. Conditional: You must specify either TypeName and Type , or Arn . |
| TypeName | Any  # complex shape |  | The name of the extension. Conditional: You must specify either TypeName and Type , or Arn . |
| VersionId | Any  # complex shape |  | The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN)  |

## Output Shape: DeregisterTypeOutput


## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def deregister_type(store, request: dict) -> dict:
    """Marks an extension or extension version as DEPRECATED in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operatio"""


    record = {
        "Arn": arn,
        "Type": type,
        "TypeName": type_name,
        "VersionId": version_id,
    }

    store.deregister_types(record)

    return {
    }
```
