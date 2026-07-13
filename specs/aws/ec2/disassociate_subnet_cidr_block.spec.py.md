---
id: "@specs/aws/ec2/disassociate_subnet_cidr_block"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateSubnetCidrBlock"
---

# DisassociateSubnetCidrBlock

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_subnet_cidr_block
> **spec:implements:** @kind:operation DisassociateSubnetCidrBlock
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateSubnetCidrBlock.spec.md

Disassociates a CIDR block from a subnet. Currently, you can disassociate an IPv6 CIDR block only. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.

## Input Shape: DisassociateSubnetCidrBlockRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape | ✓ | The association ID for the CIDR block. |

## Output Shape: DisassociateSubnetCidrBlockResult

- **Ipv6CidrBlockAssociation** (Any  # complex shape): Information about the IPv6 CIDR block association.
- **SubnetId** (str): The ID of the subnet.

## Implementation

```speclang
def disassociate_subnet_cidr_block(store, request: dict) -> dict:
    """Disassociates a CIDR block from a subnet. Currently, you can disassociate an IPv6 CIDR block only. You must detach or delete all gateways and resources that are associated with the CIDR block before y"""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateSubnetCidrBlock", request)
```
