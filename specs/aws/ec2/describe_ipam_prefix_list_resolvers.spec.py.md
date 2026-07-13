---
id: "@specs/aws/ec2/describe_ipam_prefix_list_resolvers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamPrefixListResolvers"
---

# DescribeIpamPrefixListResolvers

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_prefix_list_resolvers
> **spec:implements:** @kind:operation DescribeIpamPrefixListResolvers
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamPrefixListResolvers.spec.md

Describes one or more IPAM prefix list resolvers. Use this operation to view the configuration, status, and properties of your resolvers.

## Input Shape: DescribeIpamPrefixListResolversRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters to limit the results. |
| IpamPrefixListResolverIds | list[str] |  | The IDs of the IPAM prefix list resolvers to describe. If not specified, all resolvers in your account are described. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamPrefixListResolversResult

- **IpamPrefixListResolvers** (Any  # complex shape): Information about the IPAM prefix list resolvers.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_prefix_list_resolvers(store, request: dict) -> dict:
    """Describes one or more IPAM prefix list resolvers. Use this operation to view the configuration, status, and properties of your resolvers."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
