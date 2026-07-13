---
id: "@specs/aws/ec2/describe_ipam_resource_discovery_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamResourceDiscoveryAssociations"
---

# DescribeIpamResourceDiscoveryAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_resource_discovery_associations
> **spec:implements:** @kind:operation DescribeIpamResourceDiscoveryAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamResourceDiscoveryAssociations.spec.md

Describes resource discovery association with an Amazon VPC IPAM. An associated resource discovery is a resource discovery that has been associated with an IPAM..

## Input Shape: DescribeIpamResourceDiscoveryAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | The resource discovery association filters. |
| IpamResourceDiscoveryAssociationIds | list[str] |  | The resource discovery association IDs. |
| MaxResults | Any  # complex shape |  | The maximum number of resource discovery associations to return in one page of results. |
| NextToken | Any  # complex shape |  | Specify the pagination token from a previous request to retrieve the next page of results. |

## Output Shape: DescribeIpamResourceDiscoveryAssociationsResult

- **IpamResourceDiscoveryAssociations** (Any  # complex shape): The resource discovery associations.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_resource_discovery_associations(store, request: dict) -> dict:
    """Describes resource discovery association with an Amazon VPC IPAM. An associated resource discovery is a resource discovery that has been associated with an IPAM.."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
