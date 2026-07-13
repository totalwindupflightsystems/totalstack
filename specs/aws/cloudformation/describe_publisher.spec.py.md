---
id: "@specs/aws/cloudformation/describe_publisher"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribePublisher"
---

# DescribePublisher

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_publisher
> **spec:implements:** @kind:operation DescribePublisher
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribePublisher.spec.md

Returns information about a CloudFormation extension publisher. If you don't supply a PublisherId , and you have registered as an extension publisher, DescribePublisher returns information about your own publisher account. For more information about registering as a publisher, see: RegisterPublisher Publishing extensions to make them available for public use in the CloudFormation Command Line Interface (CLI) User Guide

## Input Shape: DescribePublisherInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PublisherId | Any  # complex shape |  | The ID of the extension publisher. If you don't supply a PublisherId , and you have registered as an extension publisher |

## Output Shape: DescribePublisherOutput

- **IdentityProvider** (Any  # complex shape): The type of account used as the identity provider when registering this publisher with CloudFormation.
- **PublisherId** (Any  # complex shape): The ID of the extension publisher.
- **PublisherProfile** (Any  # complex shape): The URL to the publisher's profile with the identity provider.
- **PublisherStatus** (Any  # complex shape): Whether the publisher is verified. Currently, all registered publishers are verified.

## Errors
- **CFNRegistryException**: An error occurred during a CloudFormation registry operation.

## Implementation

```speclang
def describe_publisher(store, request: dict) -> dict:
    """Returns information about a CloudFormation extension publisher. If you don't supply a PublisherId , and you have registered as an extension publisher, DescribePublisher returns information about your """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
