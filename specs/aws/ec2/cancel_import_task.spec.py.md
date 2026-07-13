---
id: "@specs/aws/ec2/cancel_import_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelImportTask"
---

# CancelImportTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_import_task
> **spec:implements:** @kind:operation CancelImportTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelImportTask.spec.md

Cancels an in-process import virtual machine or import snapshot task.

## Input Shape: CancelImportTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CancelReason | str |  | The reason for canceling the task. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImportTaskId | Any  # complex shape |  | The ID of the import image or import snapshot task to be canceled. |

## Output Shape: CancelImportTaskResult

- **ImportTaskId** (str): The ID of the task being canceled.
- **PreviousState** (str): The current state of the task being canceled.
- **State** (str): The current state of the task being canceled.

## Implementation

```speclang
def cancel_import_task(store, request: dict) -> dict:
    """Cancels an in-process import virtual machine or import snapshot task."""

    return {}
```
