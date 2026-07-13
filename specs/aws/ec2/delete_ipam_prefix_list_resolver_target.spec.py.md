---
id: "@specs/aws/ec2/delete_ipam_prefix_list_resolver_target"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteIpamPrefixListResolverTarget"
---

# DeleteIpamPrefixListResolverTarget

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_ipam_prefix_list_resolver_target
> **spec:implements:** @kind:operation DeleteIpamPrefixListResolverTarget
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteIpamPrefixListResolverTarget.spec.md

Deletes an IPAM prefix list resolver target. This removes the association between the resolver and the managed prefix list, stopping automatic CIDR synchronization. For more information about IPAM prefix list resolver, see Automate prefix list updates with IPAM in the Amazon VPC IPAM User Guide .

## Input Shape: DeleteIpamPrefixListResolverTargetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPrefixListResolverTargetId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver target to delete. |

## Output Shape: DeleteIpamPrefixListResolverTargetResult

- **IpamPrefixListResolverTarget** (Any  # complex shape): Information about the IPAM prefix list resolver target that was deleted.

## Implementation

```speclang
def delete_ipam_prefix_list_resolver_target(store, request: dict) -> dict:
    """Deletes an IPAM prefix list resolver target. This removes the association between the resolver and the managed prefix list, stopping automatic CIDR synchronization. For more information about IPAM pre"""
    ipam_prefix_list_resolver_target_id = request.get("IpamPrefixListResolverTargetId", "").strip() if isinstance(request.get("IpamPrefixListResolverTargetId"), str) else request.get("IpamPrefixListResolverTargetId")

    resource = store.ipam_prefix_list_resolver_targets(ipam_prefix_list_resolver_target_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_prefix_list_resolver_target_id not found")
    return {"IpamPrefixListResolverTargetId": ipam_prefix_list_resolver_target_id, **resource}
```
