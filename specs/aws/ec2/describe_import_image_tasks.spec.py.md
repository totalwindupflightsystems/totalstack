---
id: "@specs/aws/ec2/describe_import_image_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeImportImageTasks"
---

# DescribeImportImageTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_import_image_tasks
> **spec:implements:** @kind:operation DescribeImportImageTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeImportImageTasks.spec.md

Displays details about an import virtual machine or import snapshot tasks that are already created.

## Input Shape: DescribeImportImageTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | Filter tasks using the task-state filter and one of the following values: active , completed , deleting , or deleted . |
| ImportTaskIds | list[Any  # complex shape] |  | The IDs of the import image tasks. |
| MaxResults | int |  | The maximum number of results to return in a single call. |
| NextToken | str |  | A token that indicates the next page of results. |

## Output Shape: DescribeImportImageTasksResult

- **ImportImageTasks** (list[Any  # complex shape]): A list of zero or more import image tasks that are currently active or were completed or canceled in the previous 7 days
- **NextToken** (str): The token to use to get the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_import_image_tasks(store, request: dict) -> dict:
    """Displays details about an import virtual machine or import snapshot tasks that are already created."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
