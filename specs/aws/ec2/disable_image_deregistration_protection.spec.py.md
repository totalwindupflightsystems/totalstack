---
id: "@specs/aws/ec2/disable_image_deregistration_protection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableImageDeregistrationProtection"
---

# DisableImageDeregistrationProtection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_image_deregistration_protection
> **spec:implements:** @kind:operation DisableImageDeregistrationProtection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableImageDeregistrationProtection.spec.md

Disables deregistration protection for an AMI. When deregistration protection is disabled, the AMI can be deregistered. If you chose to include a 24-hour cooldown period when you enabled deregistration protection for the AMI, then, when you disable deregistration protection, you won’t immediately be able to deregister the AMI. For more information, see Protect an Amazon EC2 AMI from deregistration in the Amazon EC2 User Guide .

## Input Shape: DisableImageDeregistrationProtectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |

## Output Shape: DisableImageDeregistrationProtectionResult

- **Return** (str): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disable_image_deregistration_protection(store, request: dict) -> dict:
    """Disables deregistration protection for an AMI. When deregistration protection is disabled, the AMI can be deregistered. If you chose to include a 24-hour cooldown period when you enabled deregistratio"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.disable_image_deregistration_protections(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.disable_image_deregistration_protections(image_id, resource)
    return resource
```
