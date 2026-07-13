---
id: "@specs/aws/ec2/delete_placement_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeletePlacementGroup"
---

# DeletePlacementGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_placement_group
> **spec:implements:** @kind:operation DeletePlacementGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeletePlacementGroup.spec.md

Deletes the specified placement group. You must terminate all instances in the placement group before you can delete the placement group. For more information, see Placement groups in the Amazon EC2 User Guide .

## Input Shape: DeletePlacementGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| GroupName | Any  # complex shape | ✓ | The name of the placement group. |

## Implementation

```speclang
def delete_placement_group(store, request: dict) -> dict:
    """Deletes the specified placement group. You must terminate all instances in the placement group before you can delete the placement group. For more information, see Placement groups in the Amazon EC2 U"""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")

    if not store.placement_groups(group_name):
        raise ResourceNotFoundException(f"Resource group_name not found")
    store.delete_placement_groups(group_name)
    return {}
```
