---
id: "@specs/aws/ec2/describe_export_image_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeExportImageTasks"
---

# DescribeExportImageTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_export_image_tasks
> **spec:implements:** @kind:operation DescribeExportImageTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeExportImageTasks.spec.md

Describes the specified export image tasks or all of your export image tasks.

## Input Shape: DescribeExportImageTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExportImageTaskIds | list[Any  # complex shape] |  | The IDs of the export image tasks. |
| Filters | list[Any  # complex shape] |  | Filter tasks using the task-state filter and one of the following values: active , completed , deleting , or deleted . |
| MaxResults | Any  # complex shape |  | The maximum number of results to return in a single call. |
| NextToken | Any  # complex shape |  | A token that indicates the next page of results. |

## Output Shape: DescribeExportImageTasksResult

- **ExportImageTasks** (list[Any  # complex shape]): Information about the export image tasks.
- **NextToken** (Any  # complex shape): The token to use to get the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_export_image_tasks(store, request: dict) -> dict:
    """Describes the specified export image tasks or all of your export image tasks."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
