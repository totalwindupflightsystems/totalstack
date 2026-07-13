---
id: "@specs/aws/ec2/describe_export_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeExportTasks"
---

# DescribeExportTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_export_tasks
> **spec:implements:** @kind:operation DescribeExportTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeExportTasks.spec.md

Describes the specified export instance tasks or all of your export instance tasks.

## Input Shape: DescribeExportTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ExportTaskIds | list[Any  # complex shape] |  | The export task IDs. |
| Filters | list[Any  # complex shape] |  | the filters for the export tasks. |

## Output Shape: DescribeExportTasksResult

- **ExportTasks** (list[Any  # complex shape]): Information about the export tasks.

## Implementation

```speclang
def describe_export_tasks(store, request: dict) -> dict:
    """Describes the specified export instance tasks or all of your export instance tasks."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
