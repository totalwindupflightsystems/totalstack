---
id: "@specs/aws/ec2/describe_instance_sql_ha_history_states"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceSqlHaHistoryStates"
---

# DescribeInstanceSqlHaHistoryStates

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_sql_ha_history_states
> **spec:implements:** @kind:operation DescribeInstanceSqlHaHistoryStates
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceSqlHaHistoryStates.spec.md

Describes the historical SQL Server High Availability states for Amazon EC2 instances that are enabled for Amazon EC2 High Availability for SQL Server monitoring.

## Input Shape: DescribeInstanceSqlHaHistoryStatesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndTime | Any  # complex shape |  | The end data and time of the period for which to get historical SQL Server High Availability states. If omitted, the API |
| Filters | list[Any  # complex shape] |  | One or more filters to apply to the results. Supported filters include: tag:<key> - The tag key and value pair assigned  |
| InstanceIds | list[Any  # complex shape] |  | The IDs of the SQL Server High Availability instances to describe. If omitted, the API returns historical states for all |
| MaxResults | Any  # complex shape |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| NextToken | Any  # complex shape |  | The token to use to retrieve the next page of results. |
| StartTime | Any  # complex shape |  | The start data and time of the period for which to get the historical SQL Server High Availability states. If omitted, t |

## Output Shape: DescribeInstanceSqlHaHistoryStatesResult

- **Instances** (list[Any  # complex shape]): Information about the historical SQL Server High Availability states of the SQL Server High Availability instances.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_instance_sql_ha_history_states(store, request: dict) -> dict:
    """Describes the historical SQL Server High Availability states for Amazon EC2 instances that are enabled for Amazon EC2 High Availability for SQL Server monitoring."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
