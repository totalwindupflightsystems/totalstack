---
id: "@specs/aws/cloudformation/describe_change_set_hooks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeChangeSetHooks"
---

# DescribeChangeSetHooks

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_change_set_hooks
> **spec:implements:** @kind:operation DescribeChangeSetHooks
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeChangeSetHooks.spec.md

Returns Hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

## Input Shape: DescribeChangeSetHooksInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ChangeSetName | Any  # complex shape | ✓ | The name or Amazon Resource Name (ARN) of the change set that you want to describe. |
| LogicalResourceId | Any  # complex shape |  | If specified, lists only the Hooks related to the specified LogicalResourceId . |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackName | Any  # complex shape |  | If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to descri |

## Output Shape: DescribeChangeSetHooksOutput

- **ChangeSetId** (Any  # complex shape): The change set identifier (stack ID).
- **ChangeSetName** (Any  # complex shape): The change set name.
- **Hooks** (Any  # complex shape): List of Hook objects.
- **NextToken** (Any  # complex shape): Pagination token, null or empty if no more results.
- **StackId** (Any  # complex shape): The stack identifier (stack ID).
- **StackName** (Any  # complex shape): The stack name.
- **Status** (Any  # complex shape): Provides the status of the change set Hook.

## Errors
- **ChangeSetNotFoundException**: The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the ListChangeSets operation.

## Implementation

```speclang
def describe_change_set_hooks(store, request: dict) -> dict:
    """Returns Hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set."""
    change_set_name = request.get("ChangeSetName", "").strip() if isinstance(request.get("ChangeSetName"), str) else request.get("ChangeSetName")
    if not change_set_name:
        raise ValidationException("ChangeSetName is required")

    resource = store.change_set_hookss(change_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource change_set_name not found")
    return {"ChangeSetName": change_set_name, **resource}
```
