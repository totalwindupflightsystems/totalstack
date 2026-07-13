---
id: "@specs/aws/ec2/delete_network_acl"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkAcl"
---

# DeleteNetworkAcl

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_acl
> **spec:implements:** @kind:operation DeleteNetworkAcl
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkAcl.spec.md

Deletes the specified network ACL. You can't delete the ACL if it's associated with any subnets. You can't delete the default network ACL.

## Input Shape: DeleteNetworkAclRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkAclId | Any  # complex shape | ✓ | The ID of the network ACL. |

## Implementation

```speclang
def delete_network_acl(store, request: dict) -> dict:
    """Deletes the specified network ACL. You can't delete the ACL if it's associated with any subnets. You can't delete the default network ACL."""
    network_acl_id = request.get("NetworkAclId", "").strip() if isinstance(request.get("NetworkAclId"), str) else request.get("NetworkAclId")

    if not store.network_acls(network_acl_id):
        raise ResourceNotFoundException(f"Resource network_acl_id not found")
    store.delete_network_acls(network_acl_id)
    return {}
```
