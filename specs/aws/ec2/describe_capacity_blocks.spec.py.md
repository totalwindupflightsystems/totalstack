---
id: "@specs/aws/ec2/describe_capacity_blocks"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCapacityBlocks"
---

# DescribeCapacityBlocks

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_capacity_blocks
> **spec:implements:** @kind:operation DescribeCapacityBlocks
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCapacityBlocks.spec.md

Describes details about Capacity Blocks in the Amazon Web Services Region that you're currently using.

## Input Shape: DescribeCapacityBlocksRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityBlockIds | Any  # complex shape |  | The IDs of the Capacity Blocks. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. capacity-block-id - The ID of the Capacity Block. ultraserver-type - The Capacity Block type. The t |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token to use to retrieve the next page of results. |

## Output Shape: DescribeCapacityBlocksResult

- **CapacityBlocks** (Any  # complex shape): The Capacity Blocks.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_capacity_blocks(store, request: dict) -> dict:
    """Describes details about Capacity Blocks in the Amazon Web Services Region that you're currently using."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
