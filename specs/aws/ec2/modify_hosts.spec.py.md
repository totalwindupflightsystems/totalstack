---
id: "@specs/aws/ec2/modify_hosts"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyHosts"
---

# ModifyHosts

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_hosts
> **spec:implements:** @kind:operation ModifyHosts
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyHosts.spec.md

Modify the auto-placement setting of a Dedicated Host. When auto-placement is enabled, any instances that you launch with a tenancy of host but without a specific host ID are placed onto any available Dedicated Host in your account that has auto-placement enabled. When auto-placement is disabled, you need to provide a host ID to have the instance launch onto a specific host. If no host ID is provided, the instance is launched onto a suitable host with auto-placement enabled. You can also use this API action to modify a Dedicated Host to support either multiple instance types in an instance family, or to support a specific instance type only.

## Input Shape: ModifyHostsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AutoPlacement | Any  # complex shape |  | Specify whether to enable or disable auto-placement. |
| HostIds | list[Any  # complex shape] | ✓ | The IDs of the Dedicated Hosts to modify. |
| HostMaintenance | Any  # complex shape |  | Indicates whether to enable or disable host maintenance for the Dedicated Host. For more information, see Host maintenan |
| HostRecovery | Any  # complex shape |  | Indicates whether to enable or disable host recovery for the Dedicated Host. For more information, see Host recovery in  |
| InstanceFamily | str |  | Specifies the instance family to be supported by the Dedicated Host. Specify this parameter to modify a Dedicated Host t |
| InstanceType | str |  | Specifies the instance type to be supported by the Dedicated Host. Specify this parameter to modify a Dedicated Host to  |

## Output Shape: ModifyHostsResult

- **Successful** (list[str]): The IDs of the Dedicated Hosts that were successfully modified.
- **Unsuccessful** (list[Any  # complex shape]): The IDs of the Dedicated Hosts that could not be modified. Check whether the setting you requested can be used.

## Implementation

```speclang
def modify_hosts(store, request: dict) -> dict:
    """Modify the auto-placement setting of a Dedicated Host. When auto-placement is enabled, any instances that you launch with a tenancy of host but without a specific host ID are placed onto any available"""
    host_ids = request.get("HostIds", "").strip() if isinstance(request.get("HostIds"), str) else request.get("HostIds")
    if not host_ids:
        raise ValidationException("HostIds is required")

    resource = store.hostss(host_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource host_ids not found")

    # Update mutable fields
    if "HostRecovery" in request:
        resource["HostRecovery"] = host_recovery
    if "InstanceType" in request:
        resource["InstanceType"] = instance_type
    if "InstanceFamily" in request:
        resource["InstanceFamily"] = instance_family
    if "HostMaintenance" in request:
        resource["HostMaintenance"] = host_maintenance
    if "AutoPlacement" in request:
        resource["AutoPlacement"] = auto_placement

    store.hostss(host_ids, resource)
    return resource
```
