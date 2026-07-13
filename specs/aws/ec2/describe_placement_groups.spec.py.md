---
id: "@specs/aws/ec2/describe_placement_groups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribePlacementGroups"
---

# DescribePlacementGroups

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_placement_groups
> **spec:implements:** @kind:operation DescribePlacementGroups
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribePlacementGroups.spec.md

Describes the specified placement groups or all of your placement groups. To describe a specific placement group that is shared with your account, you must specify the ID of the placement group using the GroupId parameter. Specifying the name of a shared placement group using the GroupNames parameter will result in an error. For more information, see Placement groups in the Amazon EC2 User Guide .

## Input Shape: DescribePlacementGroupsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| Filters | list[Any  # complex shape] |  | The filters. group-name - The name of the placement group. group-arn - The Amazon Resource Name (ARN) of the placement g |
| GroupIds | list[Any  # complex shape] |  | The IDs of the placement groups. |
| GroupNames | list[Any  # complex shape] |  | The names of the placement groups. Constraints: You can specify a name only if the placement group is owned by your acco |

## Output Shape: DescribePlacementGroupsResult

- **PlacementGroups** (list[Any  # complex shape]): Information about the placement groups.

## Implementation

```speclang
def describe_placement_groups(store, request: dict) -> dict:
    """Describes the specified placement groups or all of your placement groups. To describe a specific placement group that is shared with your account, you must specify the ID of the placement group using """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
