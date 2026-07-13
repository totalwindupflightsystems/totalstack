---
id: "@specs/aws/ec2/describe_bundle_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeBundleTasks"
---

# DescribeBundleTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_bundle_tasks
> **spec:implements:** @kind:operation DescribeBundleTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeBundleTasks.spec.md

Describes the specified bundle tasks or all of your bundle tasks. Completed bundle tasks are listed for only a limited time. If your bundle task is no longer in the list, you can still register an AMI from it. Just use RegisterImage with the Amazon S3 bucket name and image manifest name you provided to the bundle task. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeBundleTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BundleIds | list[Any  # complex shape] |  | The bundle task IDs. Default: Describes all your bundle tasks. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. bundle-id - The ID of the bundle task. error-code - If the task failed, the error code returned. error-mess |

## Output Shape: DescribeBundleTasksResult

- **BundleTasks** (list[Any  # complex shape]): Information about the bundle tasks.

## Implementation

```speclang
def describe_bundle_tasks(store, request: dict) -> dict:
    """Describes the specified bundle tasks or all of your bundle tasks. Completed bundle tasks are listed for only a limited time. If your bundle task is no longer in the list, you can still register an AMI"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
