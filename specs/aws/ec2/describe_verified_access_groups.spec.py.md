---
id: "@specs/aws/ec2/describe_verified_access_groups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVerifiedAccessGroups"
---

# DescribeVerifiedAccessGroups

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_verified_access_groups
> **spec:implements:** @kind:operation DescribeVerifiedAccessGroups
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVerifiedAccessGroups.spec.md

Describes the specified Verified Access groups.

## Input Shape: DescribeVerifiedAccessGroupsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| VerifiedAccessGroupIds | list[Any  # complex shape] |  | The ID of the Verified Access groups. |
| VerifiedAccessInstanceId | Any  # complex shape |  | The ID of the Verified Access instance. |

## Output Shape: DescribeVerifiedAccessGroupsResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **VerifiedAccessGroups** (list[Any  # complex shape]): Details about the Verified Access groups.

## Implementation

```speclang
def describe_verified_access_groups(store, request: dict) -> dict:
    """Describes the specified Verified Access groups."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
