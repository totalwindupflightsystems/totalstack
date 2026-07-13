---
id: "@specs/aws/cloudformation/list_stack_resources"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackResources"
---

# ListStackResources

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_resources
> **spec:implements:** @kind:operation ListStackResources
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackResources.spec.md

Returns descriptions of all resources of the specified stack. For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.

## Input Shape: ListStackResourcesInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackName | Any  # complex shape | ✓ | The name or the unique stack ID that is associated with the stack, which aren't always interchangeable: Running stacks:  |

## Output Shape: ListStackResourcesOutput

- **NextToken** (Any  # complex shape): If the output exceeds 1 MB, a string that identifies the next page of stack resources. If no additional page exists, thi
- **StackResourceSummaries** (Any  # complex shape): A list of StackResourceSummary structures.

## Implementation

```speclang
def list_stack_resources(store, request: dict) -> dict:
    """Returns descriptions of all resources of the specified stack. For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted."""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    items = store.list_stack_resourcess()
    return {"StackResourceSummaries": list(items.values())}
```
