---
id: "@specs/aws/ec2/describe_instance_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceStatus"
---

# DescribeInstanceStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_status
> **spec:implements:** @kind:operation DescribeInstanceStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceStatus.spec.md

Describes the status of the specified instances or all of your instances. By default, only running instances are described, unless you specifically indicate to return the status of all instances. Instance status includes the following components: Status checks - Amazon EC2 performs status checks on running EC2 instances to identify hardware and software issues. For more information, see Status checks for your instances and Troubleshoot instances with failed status checks in the Amazon EC2 User Guide . Scheduled events - Amazon EC2 can schedule events (such as reboot, stop, or terminate) for your instances related to hardware issues, software updates, or system maintenance. For more information, see Scheduled events for your instances in the Amazon EC2 User Guide . Instance state - You can manage your instances from the moment you launch them through their termination. For more information, see Instance lifecycle in the Amazon EC2 User Guide . The Amazon EC2 API follows an eventual consistency model. This means that the result of an API command you run that creates or modifies resources might not be immediately available to all subsequent commands you run. For guidance on how to manage eventual consistency, see Eventual consistency in the Amazon EC2 API in the Amazon EC2 Developer Guide . The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeInstanceStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The Availability Zone of the instance. availability-zone-id - The ID of the Availabilit |
| IncludeAllInstances | bool |  | When true , includes the health status for all instances. When false , includes the health status for running instances  |
| InstanceIds | list[Any  # complex shape] |  | The instance IDs. Default: Describes all your instances. Constraints: Maximum 100 explicitly specified instance IDs. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |

## Output Shape: DescribeInstanceStatusResult

- **InstanceStatuses** (list[Any  # complex shape]): Information about the status of the instances.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_instance_status(store, request: dict) -> dict:
    """Describes the status of the specified instances or all of your instances. By default, only running instances are described, unless you specifically indicate to return the status of all instances. Inst"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
