---
id: "@specs/aws/ec2/modify_ipam"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyIpam"
---

# ModifyIpam

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_ipam
> **spec:implements:** @kind:operation ModifyIpam
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyIpam.spec.md

Modify the configurations of an IPAM.

## Input Shape: ModifyIpamRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddOperatingRegions | Any  # complex shape |  | Choose the operating Regions for the IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed t |
| Description | str |  | The description of the IPAM you want to modify. |
| DryRun | bool |  | A check for whether you have the required permissions for the action without actually making the request and provides an |
| EnablePrivateGua | bool |  | Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default. |
| IpamId | Any  # complex shape | ✓ | The ID of the IPAM you want to modify. |
| MeteredAccount | Any  # complex shape |  | A metered account is an Amazon Web Services account that is charged for active IP addresses managed in IPAM. For more in |
| RemoveOperatingRegions | Any  # complex shape |  | The operating Regions to remove. |
| Tier | Any  # complex shape |  | IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and  |

## Output Shape: ModifyIpamResult

- **Ipam** (Any  # complex shape): The results of the modification.

## Implementation

```speclang
def modify_ipam(store, request: dict) -> dict:
    """Modify the configurations of an IPAM."""
    ipam_id = request.get("IpamId", "").strip() if isinstance(request.get("IpamId"), str) else request.get("IpamId")
    if not ipam_id:
        raise ValidationException("IpamId is required")

    resource = store.ipams(ipam_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource ipam_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Description" in request:
        resource["Description"] = description
    if "AddOperatingRegions" in request:
        resource["AddOperatingRegions"] = add_operating_regions
    if "RemoveOperatingRegions" in request:
        resource["RemoveOperatingRegions"] = remove_operating_regions
    if "Tier" in request:
        resource["Tier"] = tier
    if "EnablePrivateGua" in request:
        resource["EnablePrivateGua"] = enable_private_gua
    if "MeteredAccount" in request:
        resource["MeteredAccount"] = metered_account

    store.ipams(ipam_id, resource)
    return resource
```
