---
id: "@specs/aws/ec2/modify_spot_fleet_request"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifySpotFleetRequest"
---

# ModifySpotFleetRequest

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_spot_fleet_request
> **spec:implements:** @kind:operation ModifySpotFleetRequest
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifySpotFleetRequest.spec.md

Modifies the specified Spot Fleet request. You can only modify a Spot Fleet request of type maintain . While the Spot Fleet request is being modified, it is in the modifying state. To scale up your Spot Fleet, increase its target capacity. The Spot Fleet launches the additional Spot Instances according to the allocation strategy for the Spot Fleet request. If the allocation strategy is lowestPrice , the Spot Fleet launches instances using the Spot Instance pool with the lowest price. If the allocation strategy is diversified , the Spot Fleet distributes the instances across the Spot Instance pools. If the allocation strategy is capacityOptimized , Spot Fleet launches instances from Spot Instance pools with optimal capacity for the number of instances that are launching. To scale down your Spot Fleet, decrease its target capacity. First, the Spot Fleet cancels any open requests that exceed the new target capacity. You can request that the Spot Fleet terminate Spot Instances until the size of the fleet no longer exceeds the new target capacity. If the allocation strategy is lowestPrice , the Spot Fleet terminates the instances with the highest price per unit. If the allocation strategy is capacityOptimized , the Spot Fleet terminates the instances in the Spot Instance pools that have the least available Spot Instance capacity. If the allocation strategy is diversified , the Spot Fleet terminates instances across the Spot Instance pools. Alternatively, you can request that the Spot Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually. If you are finished with your Spot Fleet for now, but will use it again later, you can set the target capacity to 0.

## Input Shape: ModifySpotFleetRequestRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Context | str |  | Reserved. |
| ExcessCapacityTerminationPolicy | Any  # complex shape |  | Indicates whether running instances should be terminated if the target capacity of the Spot Fleet request is decreased b |
| LaunchTemplateConfigs | list[Any  # complex shape] |  | The launch template and overrides. You can only use this parameter if you specified a launch template ( LaunchTemplateCo |
| OnDemandTargetCapacity | int |  | The number of On-Demand Instances in the fleet. |
| SpotFleetRequestId | Any  # complex shape | ✓ | The ID of the Spot Fleet request. |
| TargetCapacity | int |  | The size of the fleet. |

## Output Shape: ModifySpotFleetRequestResponse

- **Return** (bool): If the request succeeds, the response returns true . If the request fails, no response is returned, and instead an error

## Implementation

```speclang
def modify_spot_fleet_request(store, request: dict) -> dict:
    """Modifies the specified Spot Fleet request. You can only modify a Spot Fleet request of type maintain . While the Spot Fleet request is being modified, it is in the modifying state. To scale up your Sp"""
    spot_fleet_request_id = request.get("SpotFleetRequestId", "").strip() if isinstance(request.get("SpotFleetRequestId"), str) else request.get("SpotFleetRequestId")
    if not spot_fleet_request_id:
        raise ValidationException("SpotFleetRequestId is required")

    resource = store.spot_fleet_requests(spot_fleet_request_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource spot_fleet_request_id not found")

    # Update mutable fields
    if "LaunchTemplateConfigs" in request:
        resource["LaunchTemplateConfigs"] = launch_template_configs
    if "OnDemandTargetCapacity" in request:
        resource["OnDemandTargetCapacity"] = on_demand_target_capacity
    if "Context" in request:
        resource["Context"] = context
    if "TargetCapacity" in request:
        resource["TargetCapacity"] = target_capacity
    if "ExcessCapacityTerminationPolicy" in request:
        resource["ExcessCapacityTerminationPolicy"] = excess_capacity_termination_policy

    store.spot_fleet_requests(spot_fleet_request_id, resource)
    return resource
```
