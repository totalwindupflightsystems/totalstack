---
id: "@specs/aws/cloudformation/describe_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeType"
---

# DescribeType

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_type
> **spec:implements:** @kind:operation DescribeType
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeType.spec.md

Returns detailed information about an extension from the CloudFormation registry in your current account and Region. If you specify a VersionId , DescribeType returns information about that specific extension version. Otherwise, it returns information about the default extension version. For more information, see Edit configuration data for extensions in your account in the CloudFormation User Guide .

## Input Shape: DescribeTypeInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the extension. Conditional: You must specify either TypeName and Type , or Arn . |
| PublicVersionNumber | Any  # complex shape |  | The version number of a public third-party extension. |
| PublisherId | Any  # complex shape |  | The publisher ID of the extension publisher. Extensions provided by Amazon Web Services are not assigned a publisher ID. |
| Type | Any  # complex shape |  | The kind of extension. Conditional: You must specify either TypeName and Type , or Arn . |
| TypeName | Any  # complex shape |  | The name of the extension. Conditional: You must specify either TypeName and Type , or Arn . |
| VersionId | Any  # complex shape |  | The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN)  |

## Output Shape: DescribeTypeOutput

- **Arn** (Any  # complex shape): The Amazon Resource Name (ARN) of the extension.
- **AutoUpdate** (Any  # complex shape): Whether CloudFormation automatically updates the extension in this account and Region when a new minor version is publis
- **ConfigurationSchema** (Any  # complex shape): A JSON string that represent the current configuration data for the extension in this account and Region. To set the con
- **DefaultVersionId** (Any  # complex shape): The ID of the default version of the extension. The default version is used when the extension version isn't specified. 
- **DeprecatedStatus** (Any  # complex shape): The deprecation status of the extension version. Valid values include: LIVE : The extension is activated or registered a
- **Description** (Any  # complex shape): The description of the extension.
- **DocumentationUrl** (Any  # complex shape): The URL of a page providing detailed documentation for this extension.
- **ExecutionRoleArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the IAM execution role used to register the extension. This applies only to private ex
- **IsActivated** (Any  # complex shape): Whether the extension is activated in the account and Region. This only applies to public third-party extensions. For al
- **IsDefaultVersion** (Any  # complex shape): Whether the specified extension version is set as the default version. This applies only to private extensions you have 
- **LastUpdated** (str  # ISO8601): When the specified extension version was registered. This applies only to: Private extensions you have registered in you
- **LatestPublicVersion** (Any  # complex shape): The latest version of a public extension that is available for use. This only applies if you specify a public extension,
- **LoggingConfig** (Any  # complex shape): Contains logging configuration information for private extensions. This applies only to private extensions you have regi
- **OriginalTypeArn** (Any  # complex shape): For public extensions that have been activated for this account and Region, the Amazon Resource Name (ARN) of the public
- **OriginalTypeName** (Any  # complex shape): For public extensions that have been activated for this account and Region, the type name of the public extension. If yo
- **ProvisioningType** (Any  # complex shape): For resource type extensions, the provisioning behavior of the resource type. CloudFormation determines the provisioning
- **PublicVersionNumber** (Any  # complex shape): The version number of a public third-party extension. This applies only if you specify a public extension you have activ
- **PublisherId** (Any  # complex shape): The publisher ID of the extension publisher. This applies only to public third-party extensions. For private registered 
- **RequiredActivatedTypes** (Any  # complex shape): For extensions that are modules, the public third-party extensions that must be activated in your account in order for t
- **Schema** (Any  # complex shape): The schema that defines the extension. For more information, see Resource type schema in the CloudFormation Command Line
- **SourceUrl** (Any  # complex shape): The URL of the source code for the extension.
- **TimeCreated** (str  # ISO8601): When the specified private extension version was registered or activated in your account.
- **Type** (Any  # complex shape): The kind of extension.
- **TypeName** (Any  # complex shape): The name of the extension. If the extension is a public third-party type you have activated with a type name alias, Clou
- **TypeTestsStatus** (Any  # complex shape): The contract test status of the registered extension version. To return the extension test status of a specific extensio
- **TypeTestsStatusDescription** (Any  # complex shape): The description of the test status. To return the extension test status of a specific extension version, you must specif
- **Visibility** (Any  # complex shape): The scope at which the extension is visible and usable in CloudFormation operations. Valid values include: PRIVATE : The

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def describe_type(store, request: dict) -> dict:
    """Returns detailed information about an extension from the CloudFormation registry in your current account and Region. If you specify a VersionId , DescribeType returns information about that specific e"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
