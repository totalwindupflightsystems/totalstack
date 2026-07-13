---
id: "@specs/aws/cloudformation/list_stack_set_auto_deployment_targets"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackSetAutoDeploymentTargets"
---

# ListStackSetAutoDeploymentTargets

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_set_auto_deployment_targets
> **spec:implements:** @kind:operation ListStackSetAutoDeploymentTargets
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackSetAutoDeploymentTargets.spec.md

Returns summary information about deployment targets for a StackSet.

## Input Shape: ListStackSetAutoDeploymentTargetsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | Specifies whether you are acting as an account administrator in the organization's management account or as a delegated  |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to get automatic deployment targets for. |

## Output Shape: ListStackSetAutoDeploymentTargetsOutput

- **NextToken** (Any  # complex shape): If the request doesn't return all the remaining results, NextToken is set to a token. To retrieve the next set of result
- **Summaries** (Any  # complex shape): An array of summaries of the deployment targets for the StackSet.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.

## Implementation

```speclang
def list_stack_set_auto_deployment_targets(store, request: dict) -> dict:
    """Returns summary information about deployment targets for a StackSet."""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.stack_set_auto_deployment_targetss(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")
    return {"StackSetName": stack_set_name, **resource}
```
