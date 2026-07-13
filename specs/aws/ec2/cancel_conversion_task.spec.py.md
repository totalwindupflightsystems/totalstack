---
id: "@specs/aws/ec2/cancel_conversion_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelConversionTask"
---

# CancelConversionTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_conversion_task
> **spec:implements:** @kind:operation CancelConversionTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelConversionTask.spec.md

Cancels an active conversion task. The task can be the import of an instance or volume. The action removes all artifacts of the conversion, including a partially uploaded volume or instance. If the conversion is complete or is in the process of transferring the final disk image, the command fails and returns an exception.

## Input Shape: CancelConversionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ConversionTaskId | Any  # complex shape | ✓ | The ID of the conversion task. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReasonMessage | str |  | The reason for canceling the conversion task. |

## Implementation

```speclang
def cancel_conversion_task(store, request: dict) -> dict:
    """Cancels an active conversion task. The task can be the import of an instance or volume. The action removes all artifacts of the conversion, including a partially uploaded volume or instance. If the co"""
    conversion_task_id = request.get("ConversionTaskId", "").strip() if isinstance(request.get("ConversionTaskId"), str) else request.get("ConversionTaskId")

    if not store.conversion_tasks(conversion_task_id):
        raise ResourceNotFoundException(f"Resource conversion_task_id not found")
    store.delete_conversion_tasks(conversion_task_id)
    return {}
```
