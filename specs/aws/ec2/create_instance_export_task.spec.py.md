---
id: "@specs/aws/ec2/create_instance_export_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateInstanceExportTask"
---

# CreateInstanceExportTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_instance_export_task
> **spec:implements:** @kind:operation CreateInstanceExportTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateInstanceExportTask.spec.md

Exports a running or stopped instance to an Amazon S3 bucket. For information about the prerequisites for your Amazon S3 bucket, supported operating systems, image formats, and known limitations for the types of instances you can export, see Exporting an instance as a VM Using VM Import/Export in the VM Import/Export User Guide .

## Input Shape: CreateInstanceExportTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | A description for the conversion task or the resource being exported. The maximum length is 255 characters. |
| ExportToS3Task | Any  # complex shape | ✓ | The format and location for an export instance task. |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the export instance task during creation. |
| TargetEnvironment | Any  # complex shape | ✓ | The target virtualization environment. |

## Output Shape: CreateInstanceExportTaskResult

- **ExportTask** (Any  # complex shape): Information about the export instance task.

## Implementation

```speclang
def create_instance_export_task(store, request: dict) -> dict:
    """Exports a running or stopped instance to an Amazon S3 bucket. For information about the prerequisites for your Amazon S3 bucket, supported operating systems, image formats, and known limitations for t"""
    export_to_s3_task = request.get("ExportToS3Task", "").strip() if isinstance(request.get("ExportToS3Task"), str) else request.get("ExportToS3Task")
    if not export_to_s3_task:
        raise ValidationException("ExportToS3Task is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    target_environment = request.get("TargetEnvironment", "").strip() if isinstance(request.get("TargetEnvironment"), str) else request.get("TargetEnvironment")
    if not target_environment:
        raise ValidationException("TargetEnvironment is required")

    if store.instance_export_tasks(instance_id):
        raise ResourceInUseException(f"Resource instance_id already exists")

    record = {
        "TagSpecifications": tag_specifications,
        "Description": description,
        "InstanceId": instance_id,
        "TargetEnvironment": target_environment,
        "ExportToS3Task": export_to_s3_task,
    }

    store.instance_export_tasks(instance_id, record)

    return {
        "ExportTask": record.get("ExportTask", {}),
    }
```
