---
id: "@specs/aws/ec2/enable_image_deregistration_protection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableImageDeregistrationProtection"
---

# EnableImageDeregistrationProtection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_image_deregistration_protection
> **spec:implements:** @kind:operation EnableImageDeregistrationProtection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableImageDeregistrationProtection.spec.md

Enables deregistration protection for an AMI. When deregistration protection is enabled, the AMI can't be deregistered. To allow the AMI to be deregistered, you must first disable deregistration protection. For more information, see Protect an Amazon EC2 AMI from deregistration in the Amazon EC2 User Guide .

## Input Shape: EnableImageDeregistrationProtectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |
| WithCooldown | bool |  | If true , enforces deregistration protection for 24 hours after deregistration protection is disabled. |

## Output Shape: EnableImageDeregistrationProtectionResult

- **Return** (str): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def enable_image_deregistration_protection(store, request: dict) -> dict:
    """Enables deregistration protection for an AMI. When deregistration protection is enabled, the AMI can't be deregistered. To allow the AMI to be deregistered, you must first disable deregistration prote"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.enable_image_deregistration_protections(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "WithCooldown" in request:
        resource["WithCooldown"] = with_cooldown
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_image_deregistration_protections(image_id, resource)
    return resource
```
