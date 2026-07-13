---
id: "@specs/aws/cloudformation/detect_stack_drift"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DetectStackDrift"
---

# DetectStackDrift

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/detect_stack_drift
> **spec:implements:** @kind:operation DetectStackDrift
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DetectStackDrift.spec.md

Detects whether a stack's actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see Detect unmanaged configuration changes to stacks and resources with drift detection . Use DetectStackDrift to detect drift on all supported resources for a given stack, or DetectStackResourceDrift to detect drift on individual resources. For a list of stack resources that currently support drift detection, see Resource type support for imports and drift detection . DetectStackDrift can take up to several minutes, depending on the number of resources contained within the stack. Use DescribeStackDriftDetectionStatus to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use DescribeStackResourceDrifts to return drift information about the stack and its resources. When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform DetectStackDrift directly on the nested stack itself.

## Input Shape: DetectStackDriftInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LogicalResourceIds | Any  # complex shape |  | The logical names of any resources you want to use as filters. |
| StackName | Any  # complex shape | ✓ | The name of the stack for which you want to detect drift. |

## Output Shape: DetectStackDriftOutput

- **StackDriftDetectionId** (Any  # complex shape): The ID of the drift detection results of this operation. CloudFormation generates new results, with a new drift detectio

## Implementation

```speclang
def detect_stack_drift(store, request: dict) -> dict:
    """Detects whether a stack's actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template parameters. For each res"""
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetectStackDrift", request)
```
