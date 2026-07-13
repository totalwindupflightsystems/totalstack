---
id: "@specs/aws/ec2/get_spot_placement_scores"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetSpotPlacementScores"
---

# GetSpotPlacementScores

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_spot_placement_scores
> **spec:implements:** @kind:operation GetSpotPlacementScores
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetSpotPlacementScores.spec.md

Calculates the Spot placement score for a Region or Availability Zone based on the specified target capacity and compute requirements. You can specify your compute requirements either by using InstanceRequirementsWithMetadata and letting Amazon EC2 choose the optimal instance types to fulfill your Spot request, or you can specify the instance types by using InstanceTypes . For more information, see Spot placement score in the Amazon EC2 User Guide .

## Input Shape: GetSpotPlacementScoresRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceRequirementsWithMetadata | Any  # complex shape |  | The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types wit |
| InstanceTypes | Any  # complex shape |  | The instance types. We recommend that you specify at least three instance types. If you specify one or two instance type |
| MaxResults | Any  # complex shape |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| RegionNames | Any  # complex shape |  | The Regions used to narrow down the list of Regions to be scored. Enter the Region code, for example, us-east-1 . |
| SingleAvailabilityZone | bool |  | Specify true so that the response returns a list of scored Availability Zones. Otherwise, the response returns a list of |
| TargetCapacity | Any  # complex shape | ✓ | The target capacity. |
| TargetCapacityUnitType | Any  # complex shape |  | The unit for the target capacity. |

## Output Shape: GetSpotPlacementScoresResult

- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t
- **SpotPlacementScores** (Any  # complex shape): The Spot placement score for the top 10 Regions or Availability Zones, scored on a scale from 1 to 10. Each score reflec

## Implementation

```speclang
def get_spot_placement_scores(store, request: dict) -> dict:
    """Calculates the Spot placement score for a Region or Availability Zone based on the specified target capacity and compute requirements. You can specify your compute requirements either by using Instanc"""
    target_capacity = request.get("TargetCapacity", "").strip() if isinstance(request.get("TargetCapacity"), str) else request.get("TargetCapacity")
    if not target_capacity:
        raise ValidationException("TargetCapacity is required")

    resource = store.spot_placement_scoress(target_capacity)
    if not resource:
        raise ResourceNotFoundException(f"Resource target_capacity not found")
    return {"TargetCapacity": target_capacity, **resource}
```
