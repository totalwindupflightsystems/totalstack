---
id: "@specs/aws/cloudformation/register_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_RegisterType"
---

# RegisterType

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/register_type
> **spec:implements:** @kind:operation RegisterType
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_RegisterType.spec.md

Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes: Validating the extension schema. Determining which handlers, if any, have been specified for the extension. Making the extension available for use in your account. For more information about how to develop extensions and ready them for registration, see Creating resource types using the CloudFormation CLI in the CloudFormation Command Line Interface (CLI) User Guide . You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per Region. Use DeregisterType to deregister specific extension versions if necessary. Once you have initiated a registration request using RegisterType , you can use DescribeTypeRegistration to monitor the progress of the registration request. Once you have registered a private extension in your account and Region, use SetTypeConfiguration to specify configuration properties for the extension. For more information, see Edit configuration data for extensions in your account in the CloudFormation User Guide .

## Input Shape: RegisterTypeInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientRequestToken | Any  # complex shape |  | A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token pre |
| ExecutionRoleArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension. For CloudFormat |
| LoggingConfig | Any  # complex shape |  | Specifies logging configuration information for an extension. |
| SchemaHandlerPackage | Any  # complex shape | ✓ | A URL to the S3 bucket that contains the extension project package that contains the necessary files for the extension y |
| Type | Any  # complex shape |  | The kind of extension. |
| TypeName | Any  # complex shape | ✓ | The name of the extension being registered. We suggest that extension names adhere to the following patterns: For resour |

## Output Shape: RegisterTypeOutput

- **RegistrationToken** (Any  # complex shape): The identifier for this registration request. Use this registration token when calling DescribeTypeRegistration , which 

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.

## Implementation

```speclang
def register_type(store, request: dict) -> dict:
    """Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes: Validating th"""
    schema_handler_package = request.get("SchemaHandlerPackage", "").strip() if isinstance(request.get("SchemaHandlerPackage"), str) else request.get("SchemaHandlerPackage")
    if not schema_handler_package:
        raise ValidationException("SchemaHandlerPackage is required")
    type_name = request.get("TypeName", "").strip() if isinstance(request.get("TypeName"), str) else request.get("TypeName")
    if not type_name:
        raise ValidationException("TypeName is required")

    if store.register_types(type_name):
        raise ResourceInUseException(f"Resource type_name already exists")

    record = {
        "Type": type,
        "TypeName": type_name,
        "SchemaHandlerPackage": schema_handler_package,
        "LoggingConfig": logging_config,
        "ExecutionRoleArn": execution_role_arn,
        "ClientRequestToken": client_request_token,
    }

    store.register_types(type_name, record)

    return {
        "RegistrationToken": record.get("RegistrationToken", {}),
    }
```
