---
id: "@specs/aws/ec2/delete_ipam_scope"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteIpamScope"
---

# DeleteIpamScope

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_ipam_scope
> **spec:implements:** @kind:operation DeleteIpamScope
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteIpamScope.spec.md

Delete the scope for an IPAM. You cannot delete the default scopes. For more information, see Delete a scope in the Amazon VPC IPAM User Guide .

## Input Shape: DeleteIpamScopeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamScopeId | Any  # complex shape | ✓ | The ID of the scope to delete. |

## Output Shape: DeleteIpamScopeResult

- **IpamScope** (Any  # complex shape): Information about the results of the deletion.

## Implementation

```speclang
def delete_ipam_scope(store, request: dict) -> dict:
    """Delete the scope for an IPAM. You cannot delete the default scopes. For more information, see Delete a scope in the Amazon VPC IPAM User Guide ."""
    ipam_scope_id = request.get("IpamScopeId", "").strip() if isinstance(request.get("IpamScopeId"), str) else request.get("IpamScopeId")

    if not store.ipam_scopes(ipam_scope_id):
        raise ResourceNotFoundException(f"Resource ipam_scope_id not found")
    store.delete_ipam_scopes(ipam_scope_id)
    return {}
```
