---
id: "@specs/aws/ec2/create_internet_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateInternetGateway"
---

# CreateInternetGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_internet_gateway
> **spec:implements:** @kind:operation CreateInternetGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateInternetGateway.spec.md

Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using AttachInternetGateway . For more information, see Internet gateways in the Amazon VPC User Guide .

## Input Shape: CreateInternetGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the internet gateway. |

## Output Shape: CreateInternetGatewayResult

- **InternetGateway** (Any  # complex shape): Information about the internet gateway.

## Implementation

```speclang
def create_internet_gateway(store, request: dict) -> dict:
    """Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using AttachInternetGateway . For more information, see Internet gateways in the Amazon VPC """


    record = {
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.internet_gateways(record)

    return {
        "InternetGateway": record.get("InternetGateway", {}),
    }
```
