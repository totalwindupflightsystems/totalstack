---
id: "@specs/aws/cloudformation/detect_stack_set_drift"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DetectStackSetDrift"
---

# DetectStackSetDrift

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/detect_stack_set_drift
> **spec:implements:** @kind:operation DetectStackSetDrift
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DetectStackSetDrift.spec.md

Detect drift on a StackSet. When CloudFormation performs drift detection on a StackSet, it performs drift detection on the stack associated with each stack instance in the StackSet. For more information, see Performing drift detection on CloudFormation StackSets . DetectStackSetDrift returns the OperationId of the StackSet drift detection operation. Use this operation id with DescribeStackSetOperation to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the StackSet, in addition to the number of resources included in each stack. Once the operation has completed, use the following actions to return drift information: Use DescribeStackSet to return detailed information about the stack set, including detailed information about the last completed drift operation performed on the StackSet. (Information about drift operations that are in progress isn't included.) Use ListStackInstances to return a list of stack instances belonging to the StackSet, including the drift status and last drift time checked of each instance. Use DescribeStackInstance to return detailed information about a specific stack instance, including its drift status and last drift time checked. You can only run a single drift detection operation on a given StackSet at one time. To stop a drift detection StackSet operation, use StopStackSetOperation .

## Input Shape: DetectStackSetDriftInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CallAs | Any  # complex shape |  | [Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's managem |
| OperationId | Any  # complex shape |  | The ID of the StackSet operation. |
| OperationPreferences | Any  # complex shape |  | The user-specified preferences for how CloudFormation performs a StackSet operation. For more information about maximum  |
| StackSetName | Any  # complex shape | ✓ | The name of the StackSet on which to perform the drift detection operation. |

## Output Shape: DetectStackSetDriftOutput

- **OperationId** (Any  # complex shape): The ID of the drift detection StackSet operation. You can use this operation ID with DescribeStackSetOperation to monito

## Errors
- **InvalidOperationException**: The specified operation isn't valid.
- **OperationInProgressException**: Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.
- **StackSetNotFoundException**: The specified StackSet doesn't exist.

## Implementation

```speclang
def detect_stack_set_drift(store, request: dict) -> dict:
    """Detect drift on a StackSet. When CloudFormation performs drift detection on a StackSet, it performs drift detection on the stack associated with each stack instance in the StackSet. For more informati"""
    stack_set_name = request.get("StackSetName", "").strip() if isinstance(request.get("StackSetName"), str) else request.get("StackSetName")
    if not stack_set_name:
        raise ValidationException("StackSetName is required")

    resource = store.detect_stack_set_drifts(stack_set_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_set_name not found")

    # Update mutable fields
    if "OperationPreferences" in request:
        resource["OperationPreferences"] = operation_preferences
    if "OperationId" in request:
        resource["OperationId"] = operation_id
    if "CallAs" in request:
        resource["CallAs"] = call_as

    store.detect_stack_set_drifts(stack_set_name, resource)
    return resource
```
