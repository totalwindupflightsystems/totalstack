---
id: "@specs/aws/ec2/describe_spot_fleet_requests"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSpotFleetRequests"
---

# DescribeSpotFleetRequests

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_spot_fleet_requests
> **spec:implements:** @kind:operation DescribeSpotFleetRequests
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSpotFleetRequests.spec.md

Describes your Spot Fleet requests. Spot Fleet requests are deleted 48 hours after they are canceled and their instances are terminated.

## Input Shape: DescribeSpotFleetRequestsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to include in another request to get the next page of items. This value is null when there are no more items t |
| SpotFleetRequestIds | list[Any  # complex shape] |  | The IDs of the Spot Fleet requests. |

## Output Shape: DescribeSpotFleetRequestsResponse

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SpotFleetRequestConfigs** (Any  # complex shape): Information about the configuration of your Spot Fleet.

## Implementation

```speclang
def describe_spot_fleet_requests(store, request: dict) -> dict:
    """Describes your Spot Fleet requests. Spot Fleet requests are deleted 48 hours after they are canceled and their instances are terminated."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
