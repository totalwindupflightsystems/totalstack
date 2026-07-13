---
id: "@specs/aws/ec2/describe_scheduled_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeScheduledInstances"
---

# DescribeScheduledInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_scheduled_instances
> **spec:implements:** @kind:operation DescribeScheduledInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeScheduledInstances.spec.md

Describes the specified Scheduled Instances or all your Scheduled Instances.

## Input Shape: DescribeScheduledInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The Availability Zone (for example, us-west-2a ). instance-type - The instance type (fo |
| MaxResults | int |  | The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 100. |
| NextToken | str |  | The token for the next set of results. |
| ScheduledInstanceIds | Any  # complex shape |  | The Scheduled Instance IDs. |
| SlotStartTimeRange | Any  # complex shape |  | The time period for the first schedule to start. |

## Output Shape: DescribeScheduledInstancesResult

- **NextToken** (str): The token required to retrieve the next set of results. This value is null when there are no more results to return.
- **ScheduledInstanceSet** (Any  # complex shape): Information about the Scheduled Instances.

## Implementation

```speclang
def describe_scheduled_instances(store, request: dict) -> dict:
    """Describes the specified Scheduled Instances or all your Scheduled Instances."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
