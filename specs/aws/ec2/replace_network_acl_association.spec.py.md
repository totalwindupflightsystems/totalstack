---
id: "@specs/aws/ec2/replace_network_acl_association"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReplaceNetworkAclAssociation"
---

# ReplaceNetworkAclAssociation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/replace_network_acl_association
> **spec:implements:** @kind:operation ReplaceNetworkAclAssociation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReplaceNetworkAclAssociation.spec.md

Changes which network ACL a subnet is associated with. By default when you create a subnet, it's automatically associated with the default network ACL. For more information, see Network ACLs in the Amazon VPC User Guide . This is an idempotent operation.

## Input Shape: ReplaceNetworkAclAssociationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape | ✓ | The ID of the current association between the original network ACL and the subnet. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkAclId | Any  # complex shape | ✓ | The ID of the new network ACL to associate with the subnet. |

## Output Shape: ReplaceNetworkAclAssociationResult

- **NewAssociationId** (str): The ID of the new association.

## Implementation

```speclang
def replace_network_acl_association(store, request: dict) -> dict:
    """Changes which network ACL a subnet is associated with. By default when you create a subnet, it's automatically associated with the default network ACL. For more information, see Network ACLs in the Am"""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")
    network_acl_id = request.get("NetworkAclId", "").strip() if isinstance(request.get("NetworkAclId"), str) else request.get("NetworkAclId")
    if not network_acl_id:
        raise ValidationException("NetworkAclId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReplaceNetworkAclAssociation", request)
```
