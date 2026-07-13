---
id: "@specs/aws/ec2/get_ipam_prefix_list_resolver_rules"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamPrefixListResolverRules"
---

# GetIpamPrefixListResolverRules

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_prefix_list_resolver_rules
> **spec:implements:** @kind:operation GetIpamPrefixListResolverRules
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamPrefixListResolverRules.spec.md

Retrieves the CIDR selection rules for an IPAM prefix list resolver. Use this operation to view the business logic that determines which CIDRs are selected for synchronization with prefix lists.

## Input Shape: GetIpamPrefixListResolverRulesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters to limit the results. |
| IpamPrefixListResolverId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver whose rules you want to retrieve. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetIpamPrefixListResolverRulesResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **Rules** (Any  # complex shape): The CIDR selection rules for the IPAM prefix list resolver.

## Implementation

```speclang
def get_ipam_prefix_list_resolver_rules(store, request: dict) -> dict:
    """Retrieves the CIDR selection rules for an IPAM prefix list resolver. Use this operation to view the business logic that determines which CIDRs are selected for synchronization with prefix lists."""
    ipam_prefix_list_resolver_id = request.get("IpamPrefixListResolverId", "").strip() if isinstance(request.get("IpamPrefixListResolverId"), str) else request.get("IpamPrefixListResolverId")
    if not ipam_prefix_list_resolver_id:
        raise ValidationException("IpamPrefixListResolverId is required")

    resource = store.ipam_prefix_list_resolver_ruless(ipam_prefix_list_resolver_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_prefix_list_resolver_id not found")
    return {"IpamPrefixListResolverId": ipam_prefix_list_resolver_id, **resource}
```
