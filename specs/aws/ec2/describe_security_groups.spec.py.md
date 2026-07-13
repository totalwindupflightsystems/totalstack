---
id: "@specs/aws/ec2/describe_security_groups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSecurityGroups"
---

# DescribeSecurityGroups

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_security_groups
> **spec:implements:** @kind:operation DescribeSecurityGroups
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSecurityGroups.spec.md

Describes the specified security groups or all of your security groups.

## Input Shape: DescribeSecurityGroupsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. If using multiple filters for rules, the results include security groups for which any combination of rules |
| GroupIds | list[Any  # complex shape] |  | The IDs of the security groups. Required for security groups in a nondefault VPC. Default: Describes all of your securit |
| GroupNames | list[Any  # complex shape] |  | [Default VPC] The names of the security groups. You can specify either the security group name or the security group ID. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeSecurityGroupsResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SecurityGroups** (list[Any  # complex shape]): Information about the security groups.

## Implementation

```speclang
def describe_security_groups(store, request: dict) -> dict:
    """Describes the specified security groups or all of your security groups."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
