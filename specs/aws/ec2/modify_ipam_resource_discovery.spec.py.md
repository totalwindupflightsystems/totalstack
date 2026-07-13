---
id: "@specs/aws/ec2/modify_ipam_resource_discovery"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpamResourceDiscovery"
---

# ModifyIpamResourceDiscovery

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam_resource_discovery
> **spec:implements:** @kind:operation ModifyIpamResourceDiscovery
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpamResourceDiscovery.spec.md

Modifies a resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Input Shape: ModifyIpamResourceDiscoveryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddOperatingRegions | Any  # complex shape |  | Add operating Regions to the resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is all |
| AddOrganizationalUnitExclusions | Any  # complex shape |  | Add an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organization |
| Description | str |  | A resource discovery description. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| IpamResourceDiscoveryId | Any  # complex shape | ✓ | A resource discovery ID. |
| RemoveOperatingRegions | Any  # complex shape |  | Remove operating Regions. |
| RemoveOrganizationalUnitExclusions | Any  # complex shape |  | Remove an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizat |

## Output Shape: ModifyIpamResourceDiscoveryResult

- **IpamResourceDiscovery** (Any  # complex shape): A resource discovery.

## Implementation

```speclang
def modify_ipam_resource_discovery(store, request: dict) -> dict:
    """Modifies a resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account."""
    ipam_resource_discovery_id = request.get("IpamResourceDiscoveryId", "").strip() if isinstance(request.get("IpamResourceDiscoveryId"), str) else request.get("IpamResourceDiscoveryId")
    if not ipam_resource_discovery_id:
        raise ValidationException("IpamResourceDiscoveryId is required")

    resource = store.ipam_resource_discoverys(ipam_resource_discovery_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_resource_discovery_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Description" in request:
        resource["Description"] = description
    if "AddOperatingRegions" in request:
        resource["AddOperatingRegions"] = add_operating_regions
    if "RemoveOperatingRegions" in request:
        resource["RemoveOperatingRegions"] = remove_operating_regions
    if "AddOrganizationalUnitExclusions" in request:
        resource["AddOrganizationalUnitExclusions"] = add_organizational_unit_exclusions
    if "RemoveOrganizationalUnitExclusions" in request:
        resource["RemoveOrganizationalUnitExclusions"] = remove_organizational_unit_exclusions

    store.ipam_resource_discoverys(ipam_resource_discovery_id, resource)
    return resource
```
