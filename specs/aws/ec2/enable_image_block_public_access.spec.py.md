---
id: "@specs/aws/ec2/enable_image_block_public_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableImageBlockPublicAccess"
---

# EnableImageBlockPublicAccess

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_image_block_public_access
> **spec:implements:** @kind:operation EnableImageBlockPublicAccess
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableImageBlockPublicAccess.spec.md

Enables block public access for AMIs at the account level in the specified Amazon Web Services Region. This prevents the public sharing of your AMIs. However, if you already have public AMIs, they will remain publicly available. The API can take up to 10 minutes to configure this setting. During this time, if you run GetImageBlockPublicAccessState , the response will be unblocked . When the API has completed the configuration, the response will be block-new-sharing . For more information, see Block public access to your AMIs in the Amazon EC2 User Guide .

## Input Shape: EnableImageBlockPublicAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageBlockPublicAccessState | Any  # complex shape | ✓ | Specify block-new-sharing to enable block public access for AMIs at the account level in the specified Region. This will |

## Output Shape: EnableImageBlockPublicAccessResult

- **ImageBlockPublicAccessState** (Any  # complex shape): Returns block-new-sharing if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def enable_image_block_public_access(store, request: dict) -> dict:
    """Enables block public access for AMIs at the account level in the specified Amazon Web Services Region. This prevents the public sharing of your AMIs. However, if you already have public AMIs, they wil"""
    image_block_public_access_state = request.get("ImageBlockPublicAccessState", "").strip() if isinstance(request.get("ImageBlockPublicAccessState"), str) else request.get("ImageBlockPublicAccessState")
    if not image_block_public_access_state:
        raise ValidationException("ImageBlockPublicAccessState is required")

    resource = store.enable_image_block_public_accesss(image_block_public_access_state)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_block_public_access_state not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_image_block_public_accesss(image_block_public_access_state, resource)
    return resource
```
