---
id: "@specs/aws/ec2/get_ipam_prefix_list_resolver_versions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamPrefixListResolverVersions"
---

# GetIpamPrefixListResolverVersions

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_prefix_list_resolver_versions
> **spec:implements:** @kind:operation GetIpamPrefixListResolverVersions
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamPrefixListResolverVersions.spec.md

Retrieves version information for an IPAM prefix list resolver. Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes. Version example: Initial State (Version 1) Production environment: vpc-prod-web (10.1.0.0/16) - tagged env=prod vpc-prod-db (10.2.0.0/16) - tagged env=prod Resolver rule: Include all VPCs tagged env=prod Version 1 CIDRs: 10.1.0.0/16, 10.2.0.0/16 Infrastructure Change (Version 2) New VPC added: vpc-prod-api (10.3.0.0/16) - tagged env=prod IPAM automatically detects the change and creates a new version. Version 2 CIDRs: 10.1.0.0/16, 10.2.0.0/16, 10.3.0.0/16

## Input Shape: GetIpamPrefixListResolverVersionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters to limit the results. |
| IpamPrefixListResolverId | Any  # complex shape | ✓ | The ID of the IPAM prefix list resolver whose versions you want to retrieve. |
| IpamPrefixListResolverVersions | Any  # complex shape |  | Specific version numbers to retrieve. If not specified, all versions are returned. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: GetIpamPrefixListResolverVersionsResult

- **IpamPrefixListResolverVersions** (Any  # complex shape): Information about the IPAM prefix list resolver versions.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_ipam_prefix_list_resolver_versions(store, request: dict) -> dict:
    """Retrieves version information for an IPAM prefix list resolver. Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR li"""
    ipam_prefix_list_resolver_id = request.get("IpamPrefixListResolverId", "").strip() if isinstance(request.get("IpamPrefixListResolverId"), str) else request.get("IpamPrefixListResolverId")
    if not ipam_prefix_list_resolver_id:
        raise ValidationException("IpamPrefixListResolverId is required")

    resource = store.ipam_prefix_list_resolver_versionss(ipam_prefix_list_resolver_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_prefix_list_resolver_id not found")
    return {"IpamPrefixListResolverId": ipam_prefix_list_resolver_id, **resource}
```
