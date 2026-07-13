---
id: "@specs/aws/ec2/modify_availability_zone_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyAvailabilityZoneGroup"
---

# ModifyAvailabilityZoneGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_availability_zone_group
> **spec:implements:** @kind:operation ModifyAvailabilityZoneGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyAvailabilityZoneGroup.spec.md

Changes the opt-in status of the specified zone group for your account.

## Input Shape: ModifyAvailabilityZoneGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupName | str | ✓ | The name of the Availability Zone group, Local Zone group, or Wavelength Zone group. |
| OptInStatus | Any  # complex shape | ✓ | Indicates whether to opt in to the zone group. The only valid value is opted-in . You must contact Amazon Web Services S |

## Output Shape: ModifyAvailabilityZoneGroupResult

- **Return** (bool): Is true if the request succeeds, and an error otherwise.

## Implementation

```speclang
def modify_availability_zone_group(store, request: dict) -> dict:
    """Changes the opt-in status of the specified zone group for your account."""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")
    opt_in_status = request.get("OptInStatus", "").strip() if isinstance(request.get("OptInStatus"), str) else request.get("OptInStatus")
    if not opt_in_status:
        raise ValidationException("OptInStatus is required")

    resource = store.availability_zone_groups(group_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource group_name not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.availability_zone_groups(group_name, resource)
    return resource
```
