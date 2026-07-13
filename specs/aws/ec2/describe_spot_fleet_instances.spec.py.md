---
id: "@specs/aws/ec2/describe_spot_fleet_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSpotFleetInstances"
---

# DescribeSpotFleetInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_spot_fleet_instances
> **spec:implements:** @kind:operation DescribeSpotFleetInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSpotFleetInstances.spec.md

Describes the running instances for the specified Spot Fleet.

## Input Shape: DescribeSpotFleetInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to include in another request to get the next page of items. This value is null when there are no more items t |
| SpotFleetRequestId | Any  # complex shape | ✓ | The ID of the Spot Fleet request. |

## Output Shape: DescribeSpotFleetInstancesResponse

- **ActiveInstances** (Any  # complex shape): The running instances. This list is refreshed periodically and might be out of date.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SpotFleetRequestId** (str): The ID of the Spot Fleet request.

## Implementation

```speclang
def describe_spot_fleet_instances(store, request: dict) -> dict:
    """Describes the running instances for the specified Spot Fleet."""
    spot_fleet_request_id = request.get("SpotFleetRequestId", "").strip() if isinstance(request.get("SpotFleetRequestId"), str) else request.get("SpotFleetRequestId")
    if not spot_fleet_request_id:
        raise ValidationException("SpotFleetRequestId is required")

    resource = store.spot_fleet_instancess(spot_fleet_request_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource spot_fleet_request_id not found")
    return {"SpotFleetRequestId": spot_fleet_request_id, **resource}
```
