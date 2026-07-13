---
id: "@specs/aws/ec2/describe_capacity_block_offerings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityBlockOfferings"
---

# DescribeCapacityBlockOfferings

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_block_offerings
> **spec:implements:** @kind:operation DescribeCapacityBlockOfferings
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityBlockOfferings.spec.md

Describes Capacity Block offerings available for purchase in the Amazon Web Services Region that you're currently using. With Capacity Blocks, you can purchase a specific GPU instance type or EC2 UltraServer for a period of time. To search for an available Capacity Block offering, you specify a reservation duration and instance count.

## Input Shape: DescribeCapacityBlockOfferingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityDurationHours | int | ✓ | The reservation duration for the Capacity Block, in hours. You must specify the duration in 1-day increments up 14 days, |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EndDateRange | Any  # complex shape |  | The latest end date for the Capacity Block offering. |
| InstanceCount | int |  | The number of instances for which to reserve capacity. Each Capacity Block can have up to 64 instances, and you can have |
| InstanceType | str |  | The type of instance for which the Capacity Block offering reserves capacity. |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |
| StartDateRange | Any  # complex shape |  | The earliest start date for the Capacity Block offering. |
| UltraserverCount | int |  | The number of EC2 UltraServers in the offerings. |
| UltraserverType | str |  | The EC2 UltraServer type of the Capacity Block offerings. |

## Output Shape: DescribeCapacityBlockOfferingsResult

- **CapacityBlockOfferings** (Any  # complex shape): The recommended Capacity Block offering for the dates specified.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_block_offerings(store, request: dict) -> dict:
    """Describes Capacity Block offerings available for purchase in the Amazon Web Services Region that you're currently using. With Capacity Blocks, you can purchase a specific GPU instance type or EC2 Ultr"""
    capacity_duration_hours = request.get("CapacityDurationHours", "").strip() if isinstance(request.get("CapacityDurationHours"), str) else request.get("CapacityDurationHours")
    if not capacity_duration_hours:
        raise ValidationException("CapacityDurationHours is required")

    resource = store.capacity_block_offeringss(capacity_duration_hours)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_duration_hours not found")
    return {"CapacityDurationHours": capacity_duration_hours, **resource}
```
