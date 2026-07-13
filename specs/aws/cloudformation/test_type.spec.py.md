---
id: "@specs/aws/cloudformation/test_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_TestType"
---

# TestType

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/test_type
> **spec:implements:** @kind:operation TestType
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_TestType.spec.md

Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry. For resource types, this includes passing all contracts tests defined for the type. For modules, this includes determining if the module's model meets all necessary requirements. For more information, see Testing your public extension before publishing in the CloudFormation Command Line Interface (CLI) User Guide . If you don't specify a version, CloudFormation uses the default version of the extension in your account and Region for testing. To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see RegisterType . Once you've initiated testing on an extension using TestType , you can pass the returned TypeVersionArn into DescribeType to monitor the current test status and test status description for the extension. An extension must have a test status of PASSED before it can be published. For more information, see Publishing extensions to make them available for public use in the CloudFormation Command Line Interface (CLI) User Guide .

## Input Shape: TestTypeInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the extension. Conditional: You must specify Arn , or TypeName and Type . |
| LogDeliveryBucket | Any  # complex shape |  | The S3 bucket to which CloudFormation delivers the contract test execution logs. CloudFormation delivers the logs by the |
| Type | Any  # complex shape |  | The type of the extension to test. Conditional: You must specify Arn , or TypeName and Type . |
| TypeName | Any  # complex shape |  | The name of the extension to test. Conditional: You must specify Arn , or TypeName and Type . |
| VersionId | Any  # complex shape |  | The version of the extension to test. You can specify the version id with either Arn , or with TypeName and Type . If yo |

## Output Shape: TestTypeOutput

- **TypeVersionArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the extension.

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.
- **TypeNotFoundException**: The specified extension doesn't exist in the CloudFormation registry.

## Implementation

```speclang
def test_type(store, request: dict) -> dict:
    """Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry. For resource types, this includes passing all contracts tests defined """

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("TestType", request)
```
