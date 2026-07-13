---
id: "@specs/aws/ec2/describe_import_snapshot_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeImportSnapshotTasks"
---

# DescribeImportSnapshotTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_import_snapshot_tasks
> **spec:implements:** @kind:operation DescribeImportSnapshotTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeImportSnapshotTasks.spec.md

Describes your import snapshot tasks.

## Input Shape: DescribeImportSnapshotTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. |
| ImportTaskIds | list[Any  # complex shape] |  | A list of import snapshot task IDs. |
| MaxResults | int |  | The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the  |
| NextToken | str |  | A token that indicates the next page of results. |

## Output Shape: DescribeImportSnapshotTasksResult

- **ImportSnapshotTasks** (list[Any  # complex shape]): A list of zero or more import snapshot tasks that are currently active or were completed or canceled in the previous 7 d
- **NextToken** (str): The token to use to get the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_import_snapshot_tasks(store, request: dict) -> dict:
    """Describes your import snapshot tasks."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
