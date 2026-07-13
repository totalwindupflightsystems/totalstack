---
id: "@specs/aws/ec2/modify_fleet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyFleet"
---

# ModifyFleet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_fleet
> **spec:implements:** @kind:operation ModifyFleet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyFleet.spec.md

Modifies the specified EC2 Fleet. You can only modify an EC2 Fleet request of type maintain . While the EC2 Fleet is being modified, it is in the modifying state. To scale up your EC2 Fleet, increase its target capacity. The EC2 Fleet launches the additional Spot Instances according to the allocation strategy for the EC2 Fleet request. If the allocation strategy is lowest-price , the EC2 Fleet launches instances using the Spot Instance pool with the lowest price. If the allocation strategy is diversified , the EC2 Fleet distributes the instances across the Spot Instance pools. If the allocation strategy is capacity-optimized , EC2 Fleet launches instances from Spot Instance pools with optimal capacity for the number of instances that are launching. To scale down your EC2 Fleet, decrease its target capacity. First, the EC2 Fleet cancels any open requests that exceed the new target capacity. You can request that the EC2 Fleet terminate Spot Instances until the size of the fleet no longer exceeds the new target capacity. If the allocation strategy is lowest-price , the EC2 Fleet terminates the instances with the highest price per unit. If the allocation strategy is capacity-optimized , the EC2 Fleet terminates the instances in the Spot Instance pools that have the least available Spot Instance capacity. If the allocation strategy is diversified , the EC2 Fleet terminates instances across the Spot Instance pools. Alternatively, you can request that the EC2 Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually. If you are finished with your EC2 Fleet for now, but will use it again later, you can set the target capacity to 0.

## Input Shape: ModifyFleetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Context | str |  | Reserved. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExcessCapacityTerminationPolicy | Any  # complex shape |  | Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased belo |
| FleetId | Any  # complex shape | ✓ | The ID of the EC2 Fleet. |
| LaunchTemplateConfigs | Any  # complex shape |  | The launch template and overrides. |
| TargetCapacitySpecification | Any  # complex shape |  | The size of the EC2 Fleet. |

## Output Shape: ModifyFleetResult

- **Return** (bool): If the request succeeds, the response returns true . If the request fails, no response is returned, and instead an error

## Implementation

```speclang
def modify_fleet(store, request: dict) -> dict:
    """Modifies the specified EC2 Fleet. You can only modify an EC2 Fleet request of type maintain . While the EC2 Fleet is being modified, it is in the modifying state. To scale up your EC2 Fleet, increase """
    fleet_id = request.get("FleetId", "").strip() if isinstance(request.get("FleetId"), str) else request.get("FleetId")
    if not fleet_id:
        raise ValidationException("FleetId is required")

    resource = store.fleets(fleet_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource fleet_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "ExcessCapacityTerminationPolicy" in request:
        resource["ExcessCapacityTerminationPolicy"] = excess_capacity_termination_policy
    if "LaunchTemplateConfigs" in request:
        resource["LaunchTemplateConfigs"] = launch_template_configs
    if "TargetCapacitySpecification" in request:
        resource["TargetCapacitySpecification"] = target_capacity_specification
    if "Context" in request:
        resource["Context"] = context

    store.fleets(fleet_id, resource)
    return resource
```
