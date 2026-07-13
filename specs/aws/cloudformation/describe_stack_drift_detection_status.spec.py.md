---
id: "@specs/aws/cloudformation/describe_stack_drift_detection_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DescribeStackDriftDetectionStatus"
---

# DescribeStackDriftDetectionStatus

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/describe_stack_drift_detection_status
> **spec:implements:** @kind:operation DescribeStackDriftDetectionStatus
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DescribeStackDriftDetectionStatus.spec.md

Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see Detect unmanaged configuration changes to stacks and resources with drift detection . Use DetectStackDrift to initiate a stack drift detection operation. DetectStackDrift returns a StackDriftDetectionId you can use to monitor the progress of the operation using DescribeStackDriftDetectionStatus . Once the drift detection operation has completed, use DescribeStackResourceDrifts to return drift information about the stack and its resources.

## Input Shape: DescribeStackDriftDetectionStatusInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| StackDriftDetectionId | Any  # complex shape | ✓ | The ID of the drift detection results of this operation. CloudFormation generates new results, with a new drift detectio |

## Output Shape: DescribeStackDriftDetectionStatusOutput

- **DetectionStatus** (Any  # complex shape): The status of the stack drift detection operation. DETECTION_COMPLETE : The stack drift detection operation has successf
- **DetectionStatusReason** (Any  # complex shape): The reason the stack drift detection operation has its current status.
- **DriftedStackResourceCount** (Any  # complex shape): Total number of stack resources that have drifted. This is NULL until the drift detection operation reaches a status of 
- **StackDriftDetectionId** (Any  # complex shape): The ID of the drift detection results of this operation. CloudFormation generates new results, with a new drift detectio
- **StackDriftStatus** (Any  # complex shape): Status of the stack's actual configuration compared to its expected configuration. DRIFTED : The stack differs from its 
- **StackId** (Any  # complex shape): The ID of the stack.
- **Timestamp** (str  # ISO8601): Time at which the stack drift detection operation was initiated.

## Implementation

```speclang
def describe_stack_drift_detection_status(store, request: dict) -> dict:
    """Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has drifted , from its expected configuration,"""
    stack_drift_detection_id = request.get("StackDriftDetectionId", "").strip() if isinstance(request.get("StackDriftDetectionId"), str) else request.get("StackDriftDetectionId")
    if not stack_drift_detection_id:
        raise ValidationException("StackDriftDetectionId is required")

    resource = store.stack_drift_detection_statuss(stack_drift_detection_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource stack_drift_detection_id not found")
    return {"StackDriftDetectionId": stack_drift_detection_id, **resource}
```
