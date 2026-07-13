---
id: "@specs/aws/ec2/associate_subnet_cidr_block"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateSubnetCidrBlock"
---

# AssociateSubnetCidrBlock

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_subnet_cidr_block
> **spec:implements:** @kind:operation AssociateSubnetCidrBlock
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateSubnetCidrBlock.spec.md

Associates a CIDR block with your subnet. You can only associate a single IPv6 CIDR block with your subnet.

## Input Shape: AssociateSubnetCidrBlockRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Ipv6CidrBlock | str |  | The IPv6 CIDR block for your subnet. |
| Ipv6IpamPoolId | Any  # complex shape |  | An IPv6 IPAM pool ID. |
| Ipv6NetmaskLength | Any  # complex shape |  | An IPv6 netmask length. |
| SubnetId | Any  # complex shape | ✓ | The ID of your subnet. |

## Output Shape: AssociateSubnetCidrBlockResult

- **Ipv6CidrBlockAssociation** (Any  # complex shape): Information about the IPv6 association.
- **SubnetId** (str): The ID of the subnet.

## Implementation

```speclang
def associate_subnet_cidr_block(store, request: dict) -> dict:
    """Associates a CIDR block with your subnet. You can only associate a single IPv6 CIDR block with your subnet."""
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateSubnetCidrBlock", request)
```
