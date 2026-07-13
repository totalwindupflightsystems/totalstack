---
id: "@specs/aws/ec2/get_ipam_discovered_resource_cidrs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetIpamDiscoveredResourceCidrs"
---

# GetIpamDiscoveredResourceCidrs

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_ipam_discovered_resource_cidrs
> **spec:implements:** @kind:operation GetIpamDiscoveredResourceCidrs
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetIpamDiscoveredResourceCidrs.spec.md

Returns the resource CIDRs that are monitored as part of a resource discovery. A discovered resource is a resource CIDR monitored under a resource discovery. The following resources can be discovered: VPCs, Public IPv4 pools, VPC subnets, and Elastic IP addresses.

## Input Shape: GetIpamDiscoveredResourceCidrsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | Filters. |
| IpamResourceDiscoveryId | Any  # complex shape | ✓ | A resource discovery ID. |
| MaxResults | Any  # complex shape |  | The maximum number of discovered resource CIDRs to return in one page of results. |
| NextToken | Any  # complex shape |  | Specify the pagination token from a previous request to retrieve the next page of results. |
| ResourceRegion | str | ✓ | A resource Region. |

## Output Shape: GetIpamDiscoveredResourceCidrsResult

- **IpamDiscoveredResourceCidrs** (Any  # complex shape): Discovered resource CIDRs.
- **NextToken** (Any  # complex shape): Specify the pagination token from a previous request to retrieve the next page of results.

## Implementation

```speclang
def get_ipam_discovered_resource_cidrs(store, request: dict) -> dict:
    """Returns the resource CIDRs that are monitored as part of a resource discovery. A discovered resource is a resource CIDR monitored under a resource discovery. The following resources can be discovered:"""
    ipam_resource_discovery_id = request.get("IpamResourceDiscoveryId", "").strip() if isinstance(request.get("IpamResourceDiscoveryId"), str) else request.get("IpamResourceDiscoveryId")
    if not ipam_resource_discovery_id:
        raise ValidationException("IpamResourceDiscoveryId is required")
    resource_region = request.get("ResourceRegion", "").strip() if isinstance(request.get("ResourceRegion"), str) else request.get("ResourceRegion")
    if not resource_region:
        raise ValidationException("ResourceRegion is required")

    resource = store.ipam_discovered_resource_cidrss(ipam_resource_discovery_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_resource_discovery_id not found")
    return {"IpamResourceDiscoveryId": ipam_resource_discovery_id, **resource}
```
