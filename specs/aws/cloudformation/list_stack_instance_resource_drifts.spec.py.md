---
id: "@specs/aws/cloudformation/list_stack_instance_resource_drifts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_ListStackInstanceResourceDrifts"
---

# ListStackInstanceResourceDrifts

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/list_stack_instance_resource_drifts
> **spec:implements:** @kind:operation ListStackInstanceResourceDrifts
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_ListStackInstanceResourceDrifts.spec.md

Returns drift information for resources in a stack instance. ListStackInstanceResourceDrifts returns drift information for the most recent drift detection operation. If an operation is in progress, it may only return partial results.

## Input Shape: ListStackInstanceResourceDriftsInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| MaxResults | Any  # complex shape |  | The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum |
| NextToken | Any  # complex shape |  | The token for the next set of items to return. (You received this token from a previous call.) |
| OperationId | Any  # complex shape | ✓ | The unique ID of the drift operation. |
| StackInstanceAccount | Any  # complex shape | ✓ | The name of the Amazon Web Services account that you want to list resource drifts for. |
| StackInstanceRegion | Any  # complex shape | ✓ | The name of the Region where you want to list resource drifts. |
| StackInstanceResourceDriftStatuses | Any  # complex shape |  | The resource drift status of the stack instance. DELETED : The resource differs from its expected template configuration |
| StackSetName | Any  # complex shape | ✓ | The name or unique ID of the StackSet that you want to list drifted resources for. |

## Output Shape: ListStackInstanceResourceDriftsOutput

- **NextToken** (Any  # complex shape): If the previous paginated request didn't return all of the remaining results, the response object's NextToken parameter 
- **Summaries** (Any  # complex shape): A list of StackInstanceResourceDriftsSummary structures that contain information about the specified stack instances.

## Errors
- **StackSetNotFoundException**: The specified StackSet doesn't exist.
- **StackInstanceNotFoundException**: The specified stack instance doesn't exist.
- **OperationNotFoundException**: The specified ID refers to an operation that doesn't exist.

## Implementation

```speclang
def list_stack_instance_resource_drifts(store, request: dict) -> dict:
    """Returns drift information for resources in a stack instance. ListStackInstanceResourceDrifts returns drift information for the most recent drift detection operation. If an operation is in progress, it"""
    operation_id = request.get("OperationId", "").strip() if isinstance(request.get("OperationId"), str) else request.get("OperationId")
    if not operation_id:
        raise ValidationException("OperationId is required")
    stack_instance_account = request.get("StackInstanceAccount", "").strip() if isinstance(request.get("StackInstanceAccount"), str) else request.get("StackInstanceAccount")
    if not stack_instance_account:
        raise ValidationException("StackInstanceAccount is required")
    stack_instance_region = request.get("StackInstanceRegion", "").strip() if isinstance(request.get("StackInstanceRegion"), str) else request.get("StackInstanceRegion")
    if not stack_instance_region:
        raise ValidationException("StackInstanceRegion is required")
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    items = store.list_stack_instance_resource_driftss()
    return {"Summaries": list(items.values())}
```
