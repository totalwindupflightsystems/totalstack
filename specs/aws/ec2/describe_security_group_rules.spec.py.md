---
id: "@specs/aws/ec2/describe_security_group_rules"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSecurityGroupRules"
---

# DescribeSecurityGroupRules

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_security_group_rules
> **spec:implements:** @kind:operation DescribeSecurityGroupRules
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSecurityGroupRules.spec.md

Describes one or more of your security group rules.

## Input Shape: DescribeSecurityGroupRulesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. group-id - The ID of the security group. security-group-rule-id - The ID of the security group rule |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| SecurityGroupRuleIds | list[str] |  | The IDs of the security group rules. |

## Output Shape: DescribeSecurityGroupRulesResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SecurityGroupRules** (list[Any  # complex shape]): Information about security group rules.

## Implementation

```speclang
def describe_security_group_rules(store, request: dict) -> dict:
    """Describes one or more of your security group rules."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
