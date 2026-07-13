---
id: "@specs/aws/ec2/describe_capacity_block_status"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityBlockStatus"
---

# DescribeCapacityBlockStatus

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_block_status
> **spec:implements:** @kind:operation DescribeCapacityBlockStatus
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityBlockStatus.spec.md

Describes the availability of capacity for the specified Capacity blocks, or all of your Capacity Blocks.

## Input Shape: DescribeCapacityBlockStatusRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityBlockIds | Any  # complex shape |  | The ID of the Capacity Block. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. interconnect-status - The status of the interconnect for the Capacity Block ( ok | impaired | insuf |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeCapacityBlockStatusResult

- **CapacityBlockStatuses** (Any  # complex shape): The availability of capacity for a Capacity Block.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_block_status(store, request: dict) -> dict:
    """Describes the availability of capacity for the specified Capacity blocks, or all of your Capacity Blocks."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
