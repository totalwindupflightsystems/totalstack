---
id: "@specs/aws/ec2/describe_spot_fleet_request_history"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSpotFleetRequestHistory"
---

# DescribeSpotFleetRequestHistory

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_spot_fleet_request_history
> **spec:implements:** @kind:operation DescribeSpotFleetRequestHistory
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSpotFleetRequestHistory.spec.md

Describes the events for the specified Spot Fleet request during the specified time. Spot Fleet events are delayed by up to 30 seconds before they can be described. This ensures that you can query by the last evaluated time and not miss a recorded event. Spot Fleet events are available for 48 hours. For more information, see Monitor fleet events using Amazon EventBridge in the Amazon EC2 User Guide .

## Input Shape: DescribeSpotFleetRequestHistoryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EventType | Any  # complex shape |  | The type of events to describe. By default, all events are described. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to include in another request to get the next page of items. This value is null when there are no more items t |
| SpotFleetRequestId | Any  # complex shape | ✓ | The ID of the Spot Fleet request. |
| StartTime | Any  # complex shape | ✓ | The starting date and time for the events, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z). |

## Output Shape: DescribeSpotFleetRequestHistoryResponse

- **HistoryRecords** (Any  # complex shape): Information about the events in the history of the Spot Fleet request.
- **LastEvaluatedTime** (Any  # complex shape): The last date and time for the events, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z). All records up to t
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SpotFleetRequestId** (str): The ID of the Spot Fleet request.
- **StartTime** (Any  # complex shape): The starting date and time for the events, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z).

## Implementation

```speclang
def describe_spot_fleet_request_history(store, request: dict) -> dict:
    """Describes the events for the specified Spot Fleet request during the specified time. Spot Fleet events are delayed by up to 30 seconds before they can be described. This ensures that you can query by """
    spot_fleet_request_id = request.get("SpotFleetRequestId", "").strip() if isinstance(request.get("SpotFleetRequestId"), str) else request.get("SpotFleetRequestId")
    if not spot_fleet_request_id:
        raise ValidationException("SpotFleetRequestId is required")
    start_time = request.get("StartTime", "").strip() if isinstance(request.get("StartTime"), str) else request.get("StartTime")
    if not start_time:
        raise ValidationException("StartTime is required")

    resource = store.spot_fleet_request_historys(spot_fleet_request_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource spot_fleet_request_id not found")
    return {"SpotFleetRequestId": spot_fleet_request_id, **resource}
```
