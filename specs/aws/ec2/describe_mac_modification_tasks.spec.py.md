---
id: "@specs/aws/ec2/describe_mac_modification_tasks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeMacModificationTasks"
---

# DescribeMacModificationTasks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_mac_modification_tasks
> **spec:implements:** @kind:operation DescribeMacModificationTasks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeMacModificationTasks.spec.md

Describes a System Integrity Protection (SIP) modification task or volume ownership delegation task for an Amazon EC2 Mac instance. For more information, see Configure SIP for Amazon EC2 instances in the Amazon EC2 User Guide .

## Input Shape: DescribeMacModificationTasksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | Specifies one or more filters for the request: instance-id - The ID of the instance for which the task was created. task |
| MacModificationTaskIds | list[Any  # complex shape] |  | The ID of task. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeMacModificationTasksResult

- **MacModificationTasks** (list[Any  # complex shape]): Information about the tasks.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_mac_modification_tasks(store, request: dict) -> dict:
    """Describes a System Integrity Protection (SIP) modification task or volume ownership delegation task for an Amazon EC2 Mac instance. For more information, see Configure SIP for Amazon EC2 instances in """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
