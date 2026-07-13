---
id: "@specs/aws/ec2/describe_store_image_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeStoreImageTasks"
---

# DescribeStoreImageTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_store_image_tasks
> **spec:implements:** @kind:operation DescribeStoreImageTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeStoreImageTasks.spec.md

Describes the progress of the AMI store tasks. You can describe the store tasks for specified AMIs. If you don't specify the AMIs, you get a paginated list of store tasks from the last 31 days. For each AMI task, the response indicates if the task is InProgress , Completed , or Failed . For tasks InProgress , the response shows the estimated progress as a percentage. Tasks are listed in reverse chronological order. Currently, only tasks from the past 31 days can be viewed. To use this API, you must have the required permissions. For more information, see Permissions for storing and restoring AMIs using S3 in the Amazon EC2 User Guide . For more information, see Store and restore an AMI using S3 in the Amazon EC2 User Guide .

## Input Shape: DescribeStoreImageTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. task-state - Returns tasks in a certain state ( InProgress | Completed | Failed ) bucket - Returns task inf |
| ImageIds | list[Any  # complex shape] |  | The AMI IDs for which to show progress. Up to 20 AMI IDs can be included in a request. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeStoreImageTasksResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **StoreImageTaskResults** (Any  # complex shape): The information about the AMI store tasks.

## Implementation

```speclang
def describe_store_image_tasks(store, request: dict) -> dict:
    """Describes the progress of the AMI store tasks. You can describe the store tasks for specified AMIs. If you don't specify the AMIs, you get a paginated list of store tasks from the last 31 days. For ea"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
