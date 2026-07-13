---
id: "@specs/aws/ec2/modify_verified_access_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVerifiedAccessGroup"
---

# ModifyVerifiedAccessGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_verified_access_group
> **spec:implements:** @kind:operation ModifyVerifiedAccessGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVerifiedAccessGroup.spec.md

Modifies the specified Amazon Web Services Verified Access group configuration.

## Input Shape: ModifyVerifiedAccessGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| Description | str |  | A description for the Verified Access group. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessGroupId | Any  # complex shape | ✓ | The ID of the Verified Access group. |
| VerifiedAccessInstanceId | Any  # complex shape |  | The ID of the Verified Access instance. |

## Output Shape: ModifyVerifiedAccessGroupResult

- **VerifiedAccessGroup** (Any  # complex shape): Details about the Verified Access group.

## Implementation

```speclang
def modify_verified_access_group(store, request: dict) -> dict:
    """Modifies the specified Amazon Web Services Verified Access group configuration."""
    verified_access_group_id = request.get("VerifiedAccessGroupId", "").strip() if isinstance(request.get("VerifiedAccessGroupId"), str) else request.get("VerifiedAccessGroupId")
    if not verified_access_group_id:
        raise ValidationException("VerifiedAccessGroupId is required")

    resource = store.verified_access_groups(verified_access_group_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_group_id not found")

    # Update mutable fields
    if "VerifiedAccessInstanceId" in request:
        resource["VerifiedAccessInstanceId"] = verified_access_instance_id
    if "Description" in request:
        resource["Description"] = description
    if "ClientToken" in request:
        resource["ClientToken"] = client_token
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.verified_access_groups(verified_access_group_id, resource)
    return resource
```
