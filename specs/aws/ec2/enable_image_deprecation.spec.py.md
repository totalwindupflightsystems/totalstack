---
id: "@specs/aws/ec2/enable_image_deprecation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableImageDeprecation"
---

# EnableImageDeprecation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_image_deprecation
> **spec:implements:** @kind:operation EnableImageDeprecation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableImageDeprecation.spec.md

Enables deprecation of the specified AMI at the specified date and time. For more information, see Deprecate an AMI in the Amazon EC2 User Guide .

## Input Shape: EnableImageDeprecationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DeprecateAt | Any  # complex shape | ✓ | The date and time to deprecate the AMI, in UTC, in the following format: YYYY - MM - DD T HH : MM : SS Z. If you specify |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |

## Output Shape: EnableImageDeprecationResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def enable_image_deprecation(store, request: dict) -> dict:
    """Enables deprecation of the specified AMI at the specified date and time. For more information, see Deprecate an AMI in the Amazon EC2 User Guide ."""
    deprecate_at = request.get("DeprecateAt", "").strip() if isinstance(request.get("DeprecateAt"), str) else request.get("DeprecateAt")
    if not deprecate_at:
        raise ValidationException("DeprecateAt is required")
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.enable_image_deprecations(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_image_deprecations(image_id, resource)
    return resource
```
