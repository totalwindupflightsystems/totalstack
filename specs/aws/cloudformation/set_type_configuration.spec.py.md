---
id: "@specs/aws/cloudformation/set_type_configuration"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_SetTypeConfiguration"
---

# SetTypeConfiguration

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/set_type_configuration
> **spec:implements:** @kind:operation SetTypeConfiguration
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_SetTypeConfiguration.spec.md

Specifies the configuration data for a CloudFormation extension, such as a resource or Hook, in the given account and Region. For more information, see Edit configuration data for extensions in your account in the CloudFormation User Guide . To view the current configuration data for an extension, refer to the ConfigurationSchema element of DescribeType . It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more information, see Specify values stored in other services using dynamic references in the CloudFormation User Guide . For more information about setting the configuration data for resource types, see Defining the account-level configuration of an extension in the CloudFormation Command Line Interface (CLI) User Guide . For more information about setting the configuration data for Hooks, see the CloudFormation Hooks User Guide .

## Input Shape: SetTypeConfigurationInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Configuration | Any  # complex shape | ✓ | The configuration data for the extension in this account and Region. The configuration data must be formatted as JSON an |
| ConfigurationAlias | Any  # complex shape |  | An alias by which to refer to this extension configuration data. Conditional: Specifying a configuration alias is requir |
| Type | Any  # complex shape |  | The type of extension. Conditional: You must specify ConfigurationArn , or Type and TypeName . |
| TypeArn | Any  # complex shape |  | The Amazon Resource Name (ARN) for the extension in this account and Region. For public extensions, this will be the ARN |
| TypeName | Any  # complex shape |  | The name of the extension. Conditional: You must specify ConfigurationArn , or Type and TypeName . |

## Output Shape: SetTypeConfigurationOutput

- **ConfigurationArn** (Any  # complex shape): The Amazon Resource Name (ARN) for the configuration data in this account and Region. Conditional: You must specify Conf

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def set_type_configuration(store, request: dict) -> dict:
    """Specifies the configuration data for a CloudFormation extension, such as a resource or Hook, in the given account and Region. For more information, see Edit configuration data for extensions in your a"""
    configuration = request.get("Configuration", "").strip() if isinstance(request.get("Configuration"), str) else request.get("Configuration")
    if not configuration:
        raise ValidationException("Configuration is required")

    resource = store.set_type_configurations(configuration)
    if not resource:
        raise ResourceNotFoundException(f"Resource configuration not found")

    # Update mutable fields
    if "TypeArn" in request:
        resource["TypeArn"] = type_arn
    if "ConfigurationAlias" in request:
        resource["ConfigurationAlias"] = configuration_alias
    if "TypeName" in request:
        resource["TypeName"] = type_name
    if "Type" in request:
        resource["Type"] = type

    store.set_type_configurations(configuration, resource)
    return resource
```
