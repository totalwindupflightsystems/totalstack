---
id: "@specs/aws/ec2/modify_ipam_pool"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpamPool"
---

# ModifyIpamPool

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam_pool
> **spec:implements:** @kind:operation ModifyIpamPool
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpamPool.spec.md

Modify the configurations of an IPAM pool. For more information, see Modify a pool in the Amazon VPC IPAM User Guide .

## Input Shape: ModifyIpamPoolRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddAllocationResourceTags | list[Any  # complex shape] |  | Add tag allocation rules to a pool. For more information about allocation rules, see Create a top-level pool in the Amaz |
| AllocationDefaultNetmaskLength | Any  # complex shape |  | The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0 |
| AllocationMaxNetmaskLength | Any  # complex shape |  | The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for |
| AllocationMinNetmaskLength | Any  # complex shape |  | The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for |
| AutoImport | bool |  | If true, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as a |
| ClearAllocationDefaultNetmaskLength | bool |  | Clear the default netmask length allocation rule for this pool. |
| Description | str |  | The description of the IPAM pool you want to modify. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamPoolId | Any  # complex shape | ✓ | The ID of the IPAM pool you want to modify. |
| RemoveAllocationResourceTags | list[Any  # complex shape] |  | Remove tag allocation rules from a pool. |

## Output Shape: ModifyIpamPoolResult

- **IpamPool** (Any  # complex shape): The results of the modification.

## Implementation

```speclang
def modify_ipam_pool(store, request: dict) -> dict:
    """Modify the configurations of an IPAM pool. For more information, see Modify a pool in the Amazon VPC IPAM User Guide ."""
    ipam_pool_id = request.get("IpamPoolId", "").strip() if isinstance(request.get("IpamPoolId"), str) else request.get("IpamPoolId")
    if not ipam_pool_id:
        raise ValidationException("IpamPoolId is required")

    resource = store.ipam_pools(ipam_pool_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_pool_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Description" in request:
        resource["Description"] = description
    if "AutoImport" in request:
        resource["AutoImport"] = auto_import
    if "AllocationMinNetmaskLength" in request:
        resource["AllocationMinNetmaskLength"] = allocation_min_netmask_length
    if "AllocationMaxNetmaskLength" in request:
        resource["AllocationMaxNetmaskLength"] = allocation_max_netmask_length
    if "AllocationDefaultNetmaskLength" in request:
        resource["AllocationDefaultNetmaskLength"] = allocation_default_netmask_length
    if "ClearAllocationDefaultNetmaskLength" in request:
        resource["ClearAllocationDefaultNetmaskLength"] = clear_allocation_default_netmask_length
    if "AddAllocationResourceTags" in request:
        resource["AddAllocationResourceTags"] = add_allocation_resource_tags
    if "RemoveAllocationResourceTags" in request:
        resource["RemoveAllocationResourceTags"] = remove_allocation_resource_tags

    store.ipam_pools(ipam_pool_id, resource)
    return resource
```
