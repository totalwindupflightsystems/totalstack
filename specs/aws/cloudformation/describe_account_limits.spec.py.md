---
id: "@specs/aws/cloudformation/describe_account_limits"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeAccountLimits"
---

# DescribeAccountLimits

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_account_limits
> **spec:implements:** @kind:operation DescribeAccountLimits
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeAccountLimits.spec.md

Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see Understand CloudFormation quotas in the CloudFormation User Guide .

## Input Shape: DescribeAccountLimitsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |

## Output Shape: DescribeAccountLimitsOutput

- **AccountLimits** (list[Any  # complex shape]): An account limit structure that contain a list of CloudFormation account limits and their values.
- **NextToken** (Any  # complex shape): If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this

## Implementation

```speclang
def describe_account_limits(store, request: dict) -> dict:
    """Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see Understand CloudFormation quota"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
