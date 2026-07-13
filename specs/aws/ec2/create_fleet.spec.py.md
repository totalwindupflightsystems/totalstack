---
id: "@specs/aws/ec2/create_fleet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateFleet"
---

# CreateFleet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_fleet
> **spec:implements:** @kind:operation CreateFleet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateFleet.spec.md

Creates an EC2 Fleet that contains the configuration information for On-Demand Instances and Spot Instances. Instances are launched immediately if there is available capacity. A single EC2 Fleet can include multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet. For more information, see EC2 Fleet in the Amazon EC2 User Guide .

## Input Shape: CreateFleetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a cli |
| Context | str |  | Reserved. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExcessCapacityTerminationPolicy | Any  # complex shape |  | Indicates whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased belo |
| LaunchTemplateConfigs | Any  # complex shape | ✓ | The configuration for the EC2 Fleet. |
| OnDemandOptions | Any  # complex shape |  | Describes the configuration of On-Demand Instances in an EC2 Fleet. |
| ReplaceUnhealthyInstances | bool |  | Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type maintain . For mo |
| SpotOptions | Any  # complex shape |  | Describes the configuration of Spot Instances in an EC2 Fleet. |
| TagSpecifications | list[Any  # complex shape] |  | The key-value pair for tagging the EC2 Fleet request on creation. For more information, see Tag your resources . If the  |
| TargetCapacitySpecification | Any  # complex shape | ✓ | The number of units to request. |
| TerminateInstancesWithExpiration | bool |  | Indicates whether running instances should be terminated when the EC2 Fleet expires. |
| Type | Any  # complex shape |  | The fleet type. The default value is maintain . maintain - The EC2 Fleet places an asynchronous request for your desired |
| ValidFrom | Any  # complex shape |  | The start date and time of the request, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z). The default is to  |
| ValidUntil | Any  # complex shape |  | The end date and time of the request, in UTC format (for example, YYYY - MM - DD T HH : MM : SS Z). At this point, no ne |

## Output Shape: CreateFleetResult

- **Errors** (Any  # complex shape): Information about the instances that could not be launched by the fleet. Supported only for fleets of type instant .
- **FleetId** (Any  # complex shape): The ID of the EC2 Fleet.
- **Instances** (Any  # complex shape): Information about the instances that were launched by the fleet. Supported only for fleets of type instant .

## Implementation

```speclang
def create_fleet(store, request: dict) -> dict:
    """Creates an EC2 Fleet that contains the configuration information for On-Demand Instances and Spot Instances. Instances are launched immediately if there is available capacity. A single EC2 Fleet can i"""
    launch_template_configs = request.get("LaunchTemplateConfigs", "").strip() if isinstance(request.get("LaunchTemplateConfigs"), str) else request.get("LaunchTemplateConfigs")
    if not launch_template_configs:
        raise ValidationException("LaunchTemplateConfigs is required")
    target_capacity_specification = request.get("TargetCapacitySpecification", "").strip() if isinstance(request.get("TargetCapacitySpecification"), str) else request.get("TargetCapacitySpecification")
    if not target_capacity_specification:
        raise ValidationException("TargetCapacitySpecification is required")

    if store.fleets(launch_template_configs):
        raise ResourceInUseException(f"Resource launch_template_configs already exists")

    record = {
        "DryRun": dry_run,
        "ClientToken": client_token,
        "SpotOptions": spot_options,
        "OnDemandOptions": on_demand_options,
        "ExcessCapacityTerminationPolicy": excess_capacity_termination_policy,
        "LaunchTemplateConfigs": launch_template_configs,
        "TargetCapacitySpecification": target_capacity_specification,
        "TerminateInstancesWithExpiration": terminate_instances_with_expiration,
        "Type": type,
        "ValidFrom": valid_from,
        "ValidUntil": valid_until,
        "ReplaceUnhealthyInstances": replace_unhealthy_instances,
        "TagSpecifications": tag_specifications,
        "Context": context,
    }

    store.fleets(launch_template_configs, record)

    return {
        "FleetId": record.get("FleetId", {}),
        "Errors": record.get("Errors", {}),
        "Instances": record.get("Instances", {}),
    }
```
