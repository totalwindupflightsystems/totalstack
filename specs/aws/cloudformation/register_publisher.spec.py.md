---
id: "@specs/aws/cloudformation/register_publisher"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_RegisterPublisher"
---

# RegisterPublisher

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/register_publisher
> **spec:implements:** @kind:operation RegisterPublisher
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_RegisterPublisher.spec.md

Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions. For information about requirements for registering as a public extension publisher, see Prerequisite: Registering your account to publish CloudFormation extensions in the CloudFormation Command Line Interface (CLI) User Guide .

## Input Shape: RegisterPublisherInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AcceptTermsAndConditions | Any  # complex shape |  | Whether you accept the Terms and Conditions for publishing extensions in the CloudFormation registry. You must accept th |
| ConnectionArn | Any  # complex shape |  | If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connec |

## Output Shape: RegisterPublisherOutput

- **PublisherId** (Any  # complex shape): The ID assigned this account by CloudFormation for publishing extensions.

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.

## Implementation

```speclang
def register_publisher(store, request: dict) -> dict:
    """Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your accoun"""


    record = {
        "AcceptTermsAndConditions": accept_terms_and_conditions,
        "ConnectionArn": connection_arn,
    }

    store.register_publishers(record)

    return {
        "PublisherId": record.get("PublisherId", {}),
    }
```
