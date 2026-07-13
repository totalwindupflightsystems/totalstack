---
id: "@specs/aws/ec2/request_spot_fleet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RequestSpotFleet"
---

# RequestSpotFleet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/request_spot_fleet
> **spec:implements:** @kind:operation RequestSpotFleet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RequestSpotFleet.spec.md

Creates a Spot Fleet request. The Spot Fleet request specifies the total target capacity and the On-Demand target capacity. Amazon EC2 calculates the difference between the total capacity and On-Demand capacity, and launches the difference as Spot capacity. You can submit a single request that includes multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet. By default, the Spot Fleet requests Spot Instances in the Spot Instance pool where the price per unit is the lowest. Each launch specification can include its own instance weighting that reflects the value of the instance type to your application workload. Alternatively, you can specify that the Spot Fleet distribute the target capacity across the Spot pools included in its launch specifications. By ensuring that the Spot Instances in your Spot Fleet are in different Spot pools, you can improve the availability of your fleet. You can specify tags for the Spot Fleet request and instances launched by the fleet. You cannot tag other resource types in a Spot Fleet request because only the spot-fleet-request and instance resource types are supported. For more information, see Spot Fleet requests in the Amazon EC2 User Guide . We strongly discourage using the RequestSpotFleet API because it is a legacy API with no planned investment. For options for requesting Spot Instances, see Which is the best Spot request method to use? in the Amazon EC2 User Guide .

## Input Shape: RequestSpotFleetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SpotFleetRequestConfig | Any  # complex shape | ✓ | The configuration for the Spot Fleet request. |

## Output Shape: RequestSpotFleetResponse

- **SpotFleetRequestId** (str): The ID of the Spot Fleet request.

## Implementation

```speclang
def request_spot_fleet(store, request: dict) -> dict:
    """Creates a Spot Fleet request. The Spot Fleet request specifies the total target capacity and the On-Demand target capacity. Amazon EC2 calculates the difference between the total capacity and On-Deman"""
    spot_fleet_request_config = request.get("SpotFleetRequestConfig", "").strip() if isinstance(request.get("SpotFleetRequestConfig"), str) else request.get("SpotFleetRequestConfig")
    if not spot_fleet_request_config:
        raise ValidationException("SpotFleetRequestConfig is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RequestSpotFleet", request)
```
