---
id: "@specs/aws/cloudformation/signal_resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/cloudformation/plan"
  - "@specs/aws/cloudformation/docs/API_SignalResource"
---

# SignalResource

> **spec:trace:** specs/aws/cloudformation/cloudformation.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/cloudformation/signal_resource
> **spec:implements:** @kind:operation SignalResource
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/cloudformation/docs/API_SignalResource.spec.md

Sends a signal to the specified resource with a success or failure status. You can use the SignalResource operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The SignalResource operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.

## Input Shape: SignalResourceInput

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| LogicalResourceId | Any  # complex shape | ✓ | The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the tem |
| StackName | Any  # complex shape | ✓ | The stack name or unique stack ID that includes the resource that you want to signal. |
| Status | Any  # complex shape | ✓ | The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail |
| UniqueId | Any  # complex shape | ✓ | A unique ID of the signal. When you signal Amazon EC2 instances or Amazon EC2 Auto Scaling groups, specify the instance  |

## Implementation

```speclang
def signal_resource(store, request: dict) -> dict:
    """Sends a signal to the specified resource with a success or failure status. You can use the SignalResource operation in conjunction with a creation policy or update policy. CloudFormation doesn't proce"""
    logical_resource_id = request.get("LogicalResourceId", "").strip() if isinstance(request.get("LogicalResourceId"), str) else request.get("LogicalResourceId")
    if not logical_resource_id:
        raise ValidationException("LogicalResourceId is required")
    stack_name = request.get("StackName", "").strip() if isinstance(request.get("StackName"), str) else request.get("StackName")
    if not stack_name:
        raise ValidationException("StackName is required")
    status = request.get("Status", "").strip() if isinstance(request.get("Status"), str) else request.get("Status")
    if not status:
        raise ValidationException("Status is required")
    unique_id = request.get("UniqueId", "").strip() if isinstance(request.get("UniqueId"), str) else request.get("UniqueId")
    if not unique_id:
        raise ValidationException("UniqueId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SignalResource", request)
```
