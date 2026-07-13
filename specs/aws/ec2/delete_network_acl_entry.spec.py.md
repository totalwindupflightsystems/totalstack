---
id: "@specs/aws/ec2/delete_network_acl_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkAclEntry"
---

# DeleteNetworkAclEntry

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_acl_entry
> **spec:implements:** @kind:operation DeleteNetworkAclEntry
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkAclEntry.spec.md

Deletes the specified ingress or egress entry (rule) from the specified network ACL.

## Input Shape: DeleteNetworkAclEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Egress | bool | ✓ | Indicates whether the rule is an egress rule. |
| NetworkAclId | Any  # complex shape | ✓ | The ID of the network ACL. |
| RuleNumber | int | ✓ | The rule number of the entry to delete. |

## Implementation

```speclang
def delete_network_acl_entry(store, request: dict) -> dict:
    """Deletes the specified ingress or egress entry (rule) from the specified network ACL."""
    egress = request.get("Egress", "").strip() if isinstance(request.get("Egress"), str) else request.get("Egress")
    network_acl_id = request.get("NetworkAclId", "").strip() if isinstance(request.get("NetworkAclId"), str) else request.get("NetworkAclId")
    rule_number = request.get("RuleNumber", "").strip() if isinstance(request.get("RuleNumber"), str) else request.get("RuleNumber")

    if not store.network_acl_entrys(network_acl_id):
        raise ResourceNotFoundException(f"Resource network_acl_id not found")
    store.delete_network_acl_entrys(network_acl_id)
    return {}
```
