---
id: "@specs/aws/ec2/create_egress_only_internet_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateEgressOnlyInternetGateway"
---

# CreateEgressOnlyInternetGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_egress_only_internet_gateway
> **spec:implements:** @kind:operation CreateEgressOnlyInternetGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateEgressOnlyInternetGateway.spec.md

[IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance.

## Input Shape: CreateEgressOnlyInternetGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the egress-only internet gateway. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC for which to create the egress-only internet gateway. |

## Output Shape: CreateEgressOnlyInternetGatewayResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
- **EgressOnlyInternetGateway** (Any  # complex shape): Information about the egress-only internet gateway.

## Implementation

```speclang
def create_egress_only_internet_gateway(store, request: dict) -> dict:
    """[IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and pre"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.egress_only_internet_gateways(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "ClientToken": client_token,
        "DryRun": dry_run,
        "VpcId": vpc_id,
        "TagSpecifications": tag_specifications,
    }

    store.egress_only_internet_gateways(vpc_id, record)

    return {
        "ClientToken": record.get("ClientToken", {}),
        "EgressOnlyInternetGateway": record.get("EgressOnlyInternetGateway", {}),
    }
```
