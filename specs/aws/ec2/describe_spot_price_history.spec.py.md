---
id: "@specs/aws/ec2/describe_spot_price_history"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSpotPriceHistory"
---

# DescribeSpotPriceHistory

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_spot_price_history
> **spec:implements:** @kind:operation DescribeSpotPriceHistory
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSpotPriceHistory.spec.md

Describes the Spot price history. For more information, see Spot Instance pricing history in the Amazon EC2 User Guide . When you specify a start and end time, the operation returns the prices of the instance types within that time range. It also returns the last price change before the start time, which is the effective price as of the start time.

## Input Shape: DescribeSpotPriceHistoryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | str |  | Filters the results by the specified Availability Zone. Either AvailabilityZone or AvailabilityZoneId can be specified,  |
| AvailabilityZoneId | Any  # complex shape |  | Filters the results by the specified ID of the Availability Zone. Either AvailabilityZone or AvailabilityZoneId can be s |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndTime | Any  # complex shape |  | The date and time, up to the current date, from which to stop retrieving the price history data, in UTC format (for exam |
| Filters | list[Any  # complex shape] |  | The filters. availability-zone - The Availability Zone for which prices should be returned. availability-zone-id - The I |
| InstanceTypes | list[Any  # complex shape] |  | Filters the results by the specified instance types. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| ProductDescriptions | list[str] |  | Filters the results by the specified basic product descriptions. |
| StartTime | Any  # complex shape |  | The date and time, up to the past 90 days, from which to start retrieving the price history data, in UTC format (for exa |

## Output Shape: DescribeSpotPriceHistoryResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is an empty string ( "" ) or null when
- **SpotPriceHistory** (list[Any  # complex shape]): The historical Spot prices.

## Implementation

```speclang
def describe_spot_price_history(store, request: dict) -> dict:
    """Describes the Spot price history. For more information, see Spot Instance pricing history in the Amazon EC2 User Guide . When you specify a start and end time, the operation returns the prices of the """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
