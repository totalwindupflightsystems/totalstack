---
id: "@specs/aws/ec2/describe_ipam_prefix_list_resolver_targets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeIpamPrefixListResolverTargets"
---

# DescribeIpamPrefixListResolverTargets

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_ipam_prefix_list_resolver_targets
> **spec:implements:** @kind:operation DescribeIpamPrefixListResolverTargets
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeIpamPrefixListResolverTargets.spec.md

Describes one or more IPAM prefix list resolver Targets. Use this operation to view the configuration and status of resolver targets.

## Input Shape: DescribeIpamPrefixListResolverTargetsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Filters | list[Any  # complex shape] |  | One or more filters to limit the results. |
| IpamPrefixListResolverId | Any  # complex shape |  | The ID of the IPAM prefix list resolver to filter targets by. Only targets associated with this resolver will be returne |
| IpamPrefixListResolverTargetIds | list[str] |  | The IDs of the IPAM prefix list resolver Targets to describe. If not specified, all targets in your account are describe |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token for the next page of results. |

## Output Shape: DescribeIpamPrefixListResolverTargetsResult

- **IpamPrefixListResolverTargets** (Any  # complex shape): Information about the IPAM prefix list resolver Targets.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_ipam_prefix_list_resolver_targets(store, request: dict) -> dict:
    """Describes one or more IPAM prefix list resolver Targets. Use this operation to view the configuration and status of resolver targets."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
