---
id: "@specs/aws/ec2/create_placement_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreatePlacementGroup"
---

# CreatePlacementGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_placement_group
> **spec:implements:** @kind:operation CreatePlacementGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreatePlacementGroup.spec.md

Creates a placement group in which to launch instances. The strategy of the placement group determines how the instances are organized within the group. A cluster placement group is a logical grouping of instances within a single Availability Zone that benefit from low network latency, high network throughput. A spread placement group places instances on distinct hardware. A partition placement group places groups of instances in different partitions, where instances in one partition do not share the same hardware with instances in another partition. For more information, see Placement groups in the Amazon EC2 User Guide .

## Input Shape: CreatePlacementGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| GroupName | str |  | A name for the placement group. Must be unique within the scope of your account for the Region. Constraints: Up to 255 A |
| LinkedGroupId | Any  # complex shape |  | Reserved for future use. |
| Operator | Any  # complex shape |  | Reserved for internal use. |
| PartitionCount | int |  | The number of partitions. Valid only when Strategy is set to partition . |
| SpreadLevel | Any  # complex shape |  | Determines how placement groups spread instances. Host – You can use host only with Outpost placement groups. Rack – No  |
| Strategy | Any  # complex shape |  | The placement strategy. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the new placement group. |

## Output Shape: CreatePlacementGroupResult

- **PlacementGroup** (Any  # complex shape): Information about the placement group.

## Implementation

```speclang
def create_placement_group(store, request: dict) -> dict:
    """Creates a placement group in which to launch instances. The strategy of the placement group determines how the instances are organized within the group. A cluster placement group is a logical grouping"""


    record = {
        "PartitionCount": partition_count,
        "TagSpecifications": tag_specifications,
        "SpreadLevel": spread_level,
        "LinkedGroupId": linked_group_id,
        "Operator": operator,
        "DryRun": dry_run,
        "GroupName": group_name,
        "Strategy": strategy,
    }

    store.placement_groups(record)

    return {
        "PlacementGroup": record.get("PlacementGroup", {}),
    }
```
