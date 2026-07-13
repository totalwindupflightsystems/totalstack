---
id: "@specs/aws/ec2/describe_fleet_history"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFleetHistory"
---

# DescribeFleetHistory

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_fleet_history
> **spec:implements:** @kind:operation DescribeFleetHistory
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFleetHistory.spec.md

Describes the events for the specified EC2 Fleet during the specified time. EC2 Fleet events are delayed by up to 30 seconds before they can be described. This ensures that you can query by the last evaluated time and not miss a recorded event. EC2 Fleet events are available for 48 hours. For more information, see Monitor fleet events using Amazon EventBridge in the Amazon EC2 User Guide .

## Input Shape: DescribeFleetHistoryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EventType | Any  # complex shape |  | The type of events to describe. By default, all events are described. |
| FleetId | Any  # complex shape | ✓ | The ID of the EC2 Fleet. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| StartTime | Any  # complex shape | ✓ | The start date and time for the events, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z). |

## Output Shape: DescribeFleetHistoryResult

- **FleetId** (Any  # complex shape): The ID of the EC Fleet.
- **HistoryRecords** (Any  # complex shape): Information about the events in the history of the EC2 Fleet.
- **LastEvaluatedTime** (Any  # complex shape): The last date and time for the events, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z). All records up to t
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **StartTime** (Any  # complex shape): The start date and time for the events, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z).

## Implementation

```speclang
def describe_fleet_history(store, request: dict) -> dict:
    """Describes the events for the specified EC2 Fleet during the specified time. EC2 Fleet events are delayed by up to 30 seconds before they can be described. This ensures that you can query by the last e"""
    fleet_id = request.get("FleetId", "").strip() if isinstance(request.get("FleetId"), str) else request.get("FleetId")
    if not fleet_id:
        raise ValidationException("FleetId is required")
    start_time = request.get("StartTime", "").strip() if isinstance(request.get("StartTime"), str) else request.get("StartTime")
    if not start_time:
        raise ValidationException("StartTime is required")

    resource = store.fleet_historys(fleet_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource fleet_id not found")
    return {"FleetId": fleet_id, **resource}
```
