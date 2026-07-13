---
id: "@specs/aws/ec2/describe_replace_root_volume_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeReplaceRootVolumeTasks"
---

# DescribeReplaceRootVolumeTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_replace_root_volume_tasks
> **spec:implements:** @kind:operation DescribeReplaceRootVolumeTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeReplaceRootVolumeTasks.spec.md

Describes a root volume replacement task. For more information, see Replace a root volume in the Amazon EC2 User Guide .

## Input Shape: DescribeReplaceRootVolumeTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | Filter to use: instance-id - The ID of the instance for which the root volume replacement task was created. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | Any  # complex shape |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| ReplaceRootVolumeTaskIds | Any  # complex shape |  | The ID of the root volume replacement task to view. |

## Output Shape: DescribeReplaceRootVolumeTasksResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **ReplaceRootVolumeTasks** (Any  # complex shape): Information about the root volume replacement task.

## Implementation

```speclang
def describe_replace_root_volume_tasks(store, request: dict) -> dict:
    """Describes a root volume replacement task. For more information, see Replace a root volume in the Amazon EC2 User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
