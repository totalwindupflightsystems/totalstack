---
id: "@specs/aws/ec2/modify_instance_placement"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstancePlacement"
---

# ModifyInstancePlacement

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_placement
> **spec:implements:** @kind:operation ModifyInstancePlacement
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstancePlacement.spec.md

Modifies the placement attributes for a specified instance. You can do the following: Modify the affinity between an instance and a Dedicated Host . When affinity is set to host and the instance is not associated with a specific Dedicated Host, the next time the instance is started, it is automatically associated with the host on which it lands. If the instance is restarted or rebooted, this relationship persists. Change the Dedicated Host with which an instance is associated. Change the instance tenancy of an instance. Move an instance to or from a placement group . At least one attribute for affinity, host ID, tenancy, or placement group name must be specified in the request. Affinity and tenancy can be modified in the same request. To modify the host ID, tenancy, placement group, or partition for an instance, the instance must be in the stopped state.

## Input Shape: ModifyInstancePlacementRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Affinity | Any  # complex shape |  | The affinity setting for the instance. For more information, see Host affinity in the Amazon EC2 User Guide . |
| GroupId | Any  # complex shape |  | The Group Id of a placement group. You must specify the Placement Group Group Id to launch an instance in a shared place |
| GroupName | Any  # complex shape |  | The name of the placement group in which to place the instance. For spread placement groups, the instance must have a te |
| HostId | Any  # complex shape |  | The ID of the Dedicated Host with which to associate the instance. |
| HostResourceGroupArn | str |  | The ARN of the host resource group in which to place the instance. The instance must have a tenancy of host to specify t |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance that you are modifying. |
| PartitionNumber | int |  | The number of the partition in which to place the instance. Valid only if the placement group strategy is set to partiti |
| Tenancy | Any  # complex shape |  | The tenancy for the instance. For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of hos |

## Output Shape: ModifyInstancePlacementResult

- **Return** (bool): Is true if the request succeeds, and an error otherwise.

## Implementation

```speclang
def modify_instance_placement(store, request: dict) -> dict:
    """Modifies the placement attributes for a specified instance. You can do the following: Modify the affinity between an instance and a Dedicated Host . When affinity is set to host and the instance is no"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_placements(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "GroupName" in request:
        resource["GroupName"] = group_name
    if "PartitionNumber" in request:
        resource["PartitionNumber"] = partition_number
    if "HostResourceGroupArn" in request:
        resource["HostResourceGroupArn"] = host_resource_group_arn
    if "GroupId" in request:
        resource["GroupId"] = group_id
    if "Tenancy" in request:
        resource["Tenancy"] = tenancy
    if "Affinity" in request:
        resource["Affinity"] = affinity
    if "HostId" in request:
        resource["HostId"] = host_id

    store.instance_placements(instance_id, resource)
    return resource
```
