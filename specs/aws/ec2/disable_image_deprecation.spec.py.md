---
id: "@specs/aws/ec2/disable_image_deprecation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableImageDeprecation"
---

# DisableImageDeprecation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_image_deprecation
> **spec:implements:** @kind:operation DisableImageDeprecation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableImageDeprecation.spec.md

Cancels the deprecation of the specified AMI. For more information, see Deprecate an Amazon EC2 AMI in the Amazon EC2 User Guide .

## Input Shape: DisableImageDeprecationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |

## Output Shape: DisableImageDeprecationResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disable_image_deprecation(store, request: dict) -> dict:
    """Cancels the deprecation of the specified AMI. For more information, see Deprecate an Amazon EC2 AMI in the Amazon EC2 User Guide ."""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.disable_image_deprecations(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.disable_image_deprecations(image_id, resource)
    return resource
```
