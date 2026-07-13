---
id: "@specs/aws/ec2/enable_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableImage"
---

# EnableImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_image
> **spec:implements:** @kind:operation EnableImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableImage.spec.md

Re-enables a disabled AMI. The re-enabled AMI is marked as available and can be used for instance launches, appears in describe operations, and can be shared. Amazon Web Services accounts, organizations, and Organizational Units that lost access to the AMI when it was disabled do not regain access automatically. Once the AMI is available, it can be shared with them again. Only the AMI owner can re-enable a disabled AMI. For more information, see Disable an Amazon EC2 AMI in the Amazon EC2 User Guide .

## Input Shape: EnableImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |

## Output Shape: EnableImageResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def enable_image(store, request: dict) -> dict:
    """Re-enables a disabled AMI. The re-enabled AMI is marked as available and can be used for instance launches, appears in describe operations, and can be shared. Amazon Web Services accounts, organizatio"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.enable_images(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_images(image_id, resource)
    return resource
```
