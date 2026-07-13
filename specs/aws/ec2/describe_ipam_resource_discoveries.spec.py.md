---
id: "@specs/aws/ec2/describe_ipam_resource_discoveries"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamResourceDiscoveries"
---

# DescribeIpamResourceDiscoveries

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_resource_discoveries
> **spec:implements:** @kind:operation DescribeIpamResourceDiscoveries
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamResourceDiscoveries.spec.md

Describes IPAM resource discoveries. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Input Shape: DescribeIpamResourceDiscoveriesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | The resource discovery filters. |
| IpamResourceDiscoveryIds | list[str] |  | The IPAM resource discovery IDs. |
| MaxResults | Any  # complex shape |  | The maximum number of resource discoveries to return in one page of results. |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamResourceDiscoveriesResult

- **IpamResourceDiscoveries** (Any  # complex shape): The resource discoveries.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_resource_discoveries(store, request: dict) -> dict:
    """Describes IPAM resource discoveries. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
