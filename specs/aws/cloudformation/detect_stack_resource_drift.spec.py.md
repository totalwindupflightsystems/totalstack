---
id: "@specs/aws/cloudformation/detect_stack_resource_drift"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_DetectStackResourceDrift"
---

# DetectStackResourceDrift

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/detect_stack_resource_drift
> **spec:implements:** @kind:operation DetectStackResourceDrift
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_DetectStackResourceDrift.spec.md

Returns information about whether a resource's actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see Detect unmanaged configuration changes to stacks and resources with drift detection . Use DetectStackResourceDrift to detect drift on individual resources, or DetectStackDrift to detect drift on all resources in a given stack that support drift detection. Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see Resource type support for imports and drift detection .

## Input Shape: DetectStackResourceDriftInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LogicalResourceId | Any  # complex shape | ✓ | The logical name of the resource for which to return drift information. |
| StackName | Any  # complex shape | ✓ | The name of the stack to which the resource belongs. |

## Output Shape: DetectStackResourceDriftOutput

- **StackResourceDrift** (Any  # complex shape): Information about whether the resource's actual configuration has drifted from its expected template configuration, incl

## Implementation

```speclang
def detect_stack_resource_drift(store, request: dict) -> dict:
    """Returns information about whether a resource's actual configuration differs, or has drifted , from its expected configuration, as defined in the stack template and any values specified as template par"""
    logical_resource_id = request.get("LogicalResourceId", "").strip() if isinstance(request.get("LogicalResourceId"), str) else request.get("LogicalResourceId")
    if not logical_resource_id:
        raise ValidationException("LogicalResourceId is required")
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetectStackResourceDrift", request)
```
