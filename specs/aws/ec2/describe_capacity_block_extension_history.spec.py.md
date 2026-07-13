---
id: "@specs/aws/ec2/describe_capacity_block_extension_history"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityBlockExtensionHistory"
---

# DescribeCapacityBlockExtensionHistory

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_block_extension_history
> **spec:implements:** @kind:operation DescribeCapacityBlockExtensionHistory
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityBlockExtensionHistory.spec.md

Describes the events for the specified Capacity Block extension during the specified time.

## Input Shape: DescribeCapacityBlockExtensionHistoryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationIds | Any  # complex shape |  | The IDs of Capacity Block reservations that you want to display the history for. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters availability-zone - The Availability Zone of the extension. availability-zone-id - The Availability  |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeCapacityBlockExtensionHistoryResult

- **CapacityBlockExtensions** (Any  # complex shape): Describes one or more of your Capacity Block extensions. The results describe only the Capacity Block extensions in the 
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_block_extension_history(store, request: dict) -> dict:
    """Describes the events for the specified Capacity Block extension during the specified time."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
