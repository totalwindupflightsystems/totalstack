---
id: "@specs/aws/ec2/modify_ipam_prefix_list_resolver_target"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpamPrefixListResolverTarget"
---

# ModifyIpamPrefixListResolverTarget

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam_prefix_list_resolver_target
> **spec:implements:** @kind:operation ModifyIpamPrefixListResolverTarget
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpamPrefixListResolverTarget.spec.md

Modifies an IPAM prefix list resolver target. You can update version tracking settings and the desired version of the target prefix list.

## Input Shape: ModifyIpamPrefixListResolverTargetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see |
| DesiredVersion | Any  # complex shape |  | The desired version of the prefix list to target. This allows you to pin the target to a specific version. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPrefixListResolverTargetId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver target to modify. |
| TrackLatestVersion | bool |  | Indicates whether the resolver target should automatically track the latest version of the prefix list. When enabled, th |

## Output Shape: ModifyIpamPrefixListResolverTargetResult

- **IpamPrefixListResolverTarget** (Any  # complex shape): Information about the modified IPAM prefix list resolver target.

## Implementation

```speclang
def modify_ipam_prefix_list_resolver_target(store, request: dict) -> dict:
    """Modifies an IPAM prefix list resolver target. You can update version tracking settings and the desired version of the target prefix list."""
    ipam_prefix_list_resolver_target_id = request.get("IpamPrefixListResolverTargetId", "").strip() if isinstance(request.get("IpamPrefixListResolverTargetId"), str) else request.get("IpamPrefixListResolverTargetId")
    if not ipam_prefix_list_resolver_target_id:
        raise ValidationException("IpamPrefixListResolverTargetId is required")

    resource = store.ipam_prefix_list_resolver_targets(ipam_prefix_list_resolver_target_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_prefix_list_resolver_target_id not found")
    return {"IpamPrefixListResolverTargetId": ipam_prefix_list_resolver_target_id, **resource}
```
