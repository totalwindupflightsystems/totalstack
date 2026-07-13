---
id: "@specs/aws/ec2/delete_ipam_prefix_list_resolver"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteIpamPrefixListResolver"
---

# DeleteIpamPrefixListResolver

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_ipam_prefix_list_resolver
> **spec:implements:** @kind:operation DeleteIpamPrefixListResolver
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteIpamPrefixListResolver.spec.md

Deletes an IPAM prefix list resolver. Before deleting a resolver, you must first delete all resolver targets associated with it.

## Input Shape: DeleteIpamPrefixListResolverRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPrefixListResolverId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver to delete. |

## Output Shape: DeleteIpamPrefixListResolverResult

- **IpamPrefixListResolver** (Any  # complex shape): Information about the IPAM prefix list resolver that was deleted.

## Implementation

```speclang
def delete_ipam_prefix_list_resolver(store, request: dict) -> dict:
    """Deletes an IPAM prefix list resolver. Before deleting a resolver, you must first delete all resolver targets associated with it."""
    ipam_prefix_list_resolver_id = request.get("IpamPrefixListResolverId", "").strip() if isinstance(request.get("IpamPrefixListResolverId"), str) else request.get("IpamPrefixListResolverId")

    if not store.ipam_prefix_list_resolvers(ipam_prefix_list_resolver_id):
        raise ResourceNotFoundException(f"Resource ipam_prefix_list_resolver_id not found")
    store.delete_ipam_prefix_list_resolvers(ipam_prefix_list_resolver_id)
    return {}
```
