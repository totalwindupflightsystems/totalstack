---
id: "@specs/aws/ec2/cancel_export_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelExportTask"
---

# CancelExportTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_export_task
> **spec:implements:** @kind:operation CancelExportTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelExportTask.spec.md

Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring the final disk image, the command fails and returns an error.

## Input Shape: CancelExportTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ExportTaskId | Any  # complex shape | ✓ | The ID of the export task. This is the ID returned by the CreateInstanceExportTask and ExportImage operations. |

## Implementation

```speclang
def cancel_export_task(store, request: dict) -> dict:
    """Cancels an active export task. The request removes all artifacts of the export, including any partially-created Amazon S3 objects. If the export task is complete or is in the process of transferring t"""
    export_task_id = request.get("ExportTaskId", "").strip() if isinstance(request.get("ExportTaskId"), str) else request.get("ExportTaskId")

    if not store.export_tasks(export_task_id):
        raise ResourceNotFoundException(f"Resource export_task_id not found")
    store.delete_export_tasks(export_task_id)
    return {}
```
