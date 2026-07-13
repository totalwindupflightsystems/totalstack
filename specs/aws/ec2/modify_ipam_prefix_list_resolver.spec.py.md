---
id: "@specs/aws/ec2/modify_ipam_prefix_list_resolver"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpamPrefixListResolver"
---

# ModifyIpamPrefixListResolver

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam_prefix_list_resolver
> **spec:implements:** @kind:operation ModifyIpamPrefixListResolver
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpamPrefixListResolver.spec.md

Modifies an IPAM prefix list resolver. You can update the description and CIDR selection rules. Changes to rules will trigger re-evaluation and potential updates to associated prefix lists.

## Input Shape: ModifyIpamPrefixListResolverRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | A new description for the IPAM prefix list resolver. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPrefixListResolverId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver to modify. |
| Rules | Any  # complex shape |  | The updated CIDR selection rules for the resolver. These rules replace the existing rules entirely. |

## Output Shape: ModifyIpamPrefixListResolverResult

- **IpamPrefixListResolver** (Any  # complex shape): Information about the modified IPAM prefix list resolver.

## Implementation

```speclang
def modify_ipam_prefix_list_resolver(store, request: dict) -> dict:
    """Modifies an IPAM prefix list resolver. You can update the description and CIDR selection rules. Changes to rules will trigger re-evaluation and potential updates to associated prefix lists."""
    ipam_prefix_list_resolver_id = request.get("IpamPrefixListResolverId", "").strip() if isinstance(request.get("IpamPrefixListResolverId"), str) else request.get("IpamPrefixListResolverId")
    if not ipam_prefix_list_resolver_id:
        raise ValidationException("IpamPrefixListResolverId is required")

    items = store.list_ipam_prefix_list_resolvers()
    return {"IpamPrefixListResolver": list(items.values())}
```
