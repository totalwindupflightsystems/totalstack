---
id: "@specs/aws/ec2/disable_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableImage"
---

# DisableImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_image
> **spec:implements:** @kind:operation DisableImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableImage.spec.md

Sets the AMI state to disabled and removes all launch permissions from the AMI. A disabled AMI can't be used for instance launches. A disabled AMI can't be shared. If an AMI was public or previously shared, it is made private. If an AMI was shared with an Amazon Web Services account, organization, or Organizational Unit, they lose access to the disabled AMI. A disabled AMI does not appear in DescribeImages API calls by default. Only the AMI owner can disable an AMI. You can re-enable a disabled AMI using EnableImage . For more information, see Disable an AMI in the Amazon EC2 User Guide .

## Input Shape: DisableImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |

## Output Shape: DisableImageResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disable_image(store, request: dict) -> dict:
    """Sets the AMI state to disabled and removes all launch permissions from the AMI. A disabled AMI can't be used for instance launches. A disabled AMI can't be shared. If an AMI was public or previously s"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.disable_images(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.disable_images(image_id, resource)
    return resource
```
