---
id: "@specs/aws/ec2/modify_ipam_resource_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpamResourceCidr"
---

# ModifyIpamResourceCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam_resource_cidr
> **spec:implements:** @kind:operation ModifyIpamResourceCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpamResourceCidr.spec.md

Modify a resource CIDR. You can use this action to transfer resource CIDRs between scopes and ignore resource CIDRs that you do not want to manage. If set to false, the resource will not be tracked for overlap, it cannot be auto-imported into a pool, and it will be removed from any pool it has an allocation in. For more information, see Move resource CIDRs between scopes and Change the monitoring state of resource CIDRs in the Amazon VPC IPAM User Guide .

## Input Shape: ModifyIpamResourceCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CurrentIpamScopeId | Any  # complex shape | ✓ | The ID of the current scope that the resource CIDR is in. |
| DestinationIpamScopeId | Any  # complex shape |  | The ID of the scope you want to transfer the resource CIDR to. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| Monitored | bool | ✓ | Determines if the resource is monitored by IPAM. If a resource is monitored, the resource is discovered by IPAM and you  |
| ResourceCidr | str | ✓ | The CIDR of the resource you want to modify. |
| ResourceId | str | ✓ | The ID of the resource you want to modify. |
| ResourceRegion | str | ✓ | The Amazon Web Services Region of the resource you want to modify. |

## Output Shape: ModifyIpamResourceCidrResult

- **IpamResourceCidr** (Any  # complex shape): The CIDR of the resource.

## Implementation

```speclang
def modify_ipam_resource_cidr(store, request: dict) -> dict:
    """Modify a resource CIDR. You can use this action to transfer resource CIDRs between scopes and ignore resource CIDRs that you do not want to manage. If set to false, the resource will not be tracked fo"""
    current_ipam_scope_id = request.get("CurrentIpamScopeId", "").strip() if isinstance(request.get("CurrentIpamScopeId"), str) else request.get("CurrentIpamScopeId")
    if not current_ipam_scope_id:
        raise ValidationException("CurrentIpamScopeId is required")
    monitored = request.get("Monitored", "").strip() if isinstance(request.get("Monitored"), str) else request.get("Monitored")
    if not monitored:
        raise ValidationException("Monitored is required")
    resource_cidr = request.get("ResourceCidr", "").strip() if isinstance(request.get("ResourceCidr"), str) else request.get("ResourceCidr")
    if not resource_cidr:
        raise ValidationException("ResourceCidr is required")
    resource_id = request.get("ResourceId", "").strip() if isinstance(request.get("ResourceId"), str) else request.get("ResourceId")
    if not resource_id:
        raise ValidationException("ResourceId is required")
    resource_region = request.get("ResourceRegion", "").strip() if isinstance(request.get("ResourceRegion"), str) else request.get("ResourceRegion")
    if not resource_region:
        raise ValidationException("ResourceRegion is required")

    resource = store.ipam_resource_cidrs(resource_cidr)
    if not resource:
        raise ResourceNotFoundException(f"Resource resource_cidr not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "DestinationIpamScopeId" in request:
        resource["DestinationIpamScopeId"] = destination_ipam_scope_id

    store.ipam_resource_cidrs(resource_cidr, resource)
    return resource
```
