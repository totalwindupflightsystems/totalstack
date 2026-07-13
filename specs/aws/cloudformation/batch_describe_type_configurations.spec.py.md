---
id: "@specs/aws/cloudformation/batch_describe_type_configurations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_BatchDescribeTypeConfigurations"
---

# BatchDescribeTypeConfigurations

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/batch_describe_type_configurations
> **spec:implements:** @kind:operation BatchDescribeTypeConfigurations
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_BatchDescribeTypeConfigurations.spec.md

Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry in your current account and Region. For more information, see Edit configuration data for extensions in your account in the CloudFormation User Guide .

## Input Shape: BatchDescribeTypeConfigurationsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| TypeConfigurationIdentifiers | Any  # complex shape | ✓ | The list of identifiers for the desired extension configurations. |

## Output Shape: BatchDescribeTypeConfigurationsOutput

- **Errors** (Any  # complex shape): A list of information concerning any errors generated during the setting of the specified configurations.
- **TypeConfigurations** (list[Any  # complex shape]): A list of any of the specified extension configurations from the CloudFormation registry.
- **UnprocessedTypeConfigurations** (Any  # complex shape): A list of any of the specified extension configurations that CloudFormation could not process for any reason.

## Errors
- **TypeConfigurationNotFoundException**: The specified extension configuration can't be found.
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.

## Implementation

```speclang
def batch_describe_type_configurations(store, request: dict) -> dict:
    """Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry in your current account and Region. For more information, see Edit configuration data for exten"""
    type_configuration_identifiers = request.get("TypeConfigurationIdentifiers", "").strip() if isinstance(request.get("TypeConfigurationIdentifiers"), str) else request.get("TypeConfigurationIdentifiers")
    if not type_configuration_identifiers:
        raise ValidationException("TypeConfigurationIdentifiers is required")

    resource = store.batch_describe_type_configurationss(type_configuration_identifiers)
    if not resource:
        raise ResourceNotFoundException(f"Resource type_configuration_identifiers not found")
    return {"TypeConfigurationIdentifiers": type_configuration_identifiers, **resource}
```
