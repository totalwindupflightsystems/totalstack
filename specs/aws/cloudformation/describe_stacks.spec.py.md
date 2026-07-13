---
id: "@specs/aws/cloudformation/describe_stacks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStacks"
---

# DescribeStacks

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stacks
> **spec:implements:** @kind:operation DescribeStacks
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStacks.spec.md

Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created. For more information about a stack's event history, see Understand CloudFormation stack creation events in the CloudFormation User Guide . If the stack doesn't exist, a ValidationError is returned.

## Input Shape: DescribeStacksInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackName | Any  # complex shape |  | If you don't pass a parameter to StackName , the API returns a response that describes all resources in the account, whi |

## Output Shape: DescribeStacksOutput

- **NextToken** (Any  # complex shape): If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this
- **Stacks** (Any  # complex shape): A list of stack structures.

## Implementation

```speclang
def describe_stacks(store, request: dict) -> dict:
    """Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created. For more information about a stack's event history, see Und"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
