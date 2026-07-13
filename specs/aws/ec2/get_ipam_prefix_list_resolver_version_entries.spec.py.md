---
id: "@specs/aws/ec2/get_ipam_prefix_list_resolver_version_entries"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamPrefixListResolverVersionEntries"
---

# GetIpamPrefixListResolverVersionEntries

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_prefix_list_resolver_version_entries
> **spec:implements:** @kind:operation GetIpamPrefixListResolverVersionEntries
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamPrefixListResolverVersionEntries.spec.md

Retrieves the CIDR entries for a specific version of an IPAM prefix list resolver. This shows the actual CIDRs that were selected and synchronized at a particular point in time.

## Input Shape: GetIpamPrefixListResolverVersionEntriesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPrefixListResolverId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver whose version entries you want to retrieve. |
| IpamPrefixListResolverVersion | int | ✓ | The version number of the resolver for which to retrieve CIDR entries. If not specified, the latest version is used. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetIpamPrefixListResolverVersionEntriesResult

- **Entries** (Any  # complex shape): The CIDR entries for the specified resolver version.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_ipam_prefix_list_resolver_version_entries(store, request: dict) -> dict:
    """Retrieves the CIDR entries for a specific version of an IPAM prefix list resolver. This shows the actual CIDRs that were selected and synchronized at a particular point in time."""
    ipam_prefix_list_resolver_id = request.get("IpamPrefixListResolverId", "").strip() if isinstance(request.get("IpamPrefixListResolverId"), str) else request.get("IpamPrefixListResolverId")
    if not ipam_prefix_list_resolver_id:
        raise ValidationException("IpamPrefixListResolverId is required")
    ipam_prefix_list_resolver_version = request.get("IpamPrefixListResolverVersion", "").strip() if isinstance(request.get("IpamPrefixListResolverVersion"), str) else request.get("IpamPrefixListResolverVersion")
    if not ipam_prefix_list_resolver_version:
        raise ValidationException("IpamPrefixListResolverVersion is required")

    resource = store.ipam_prefix_list_resolver_version_entriess(ipam_prefix_list_resolver_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_prefix_list_resolver_id not found")
    return {"IpamPrefixListResolverId": ipam_prefix_list_resolver_id, **resource}
```
