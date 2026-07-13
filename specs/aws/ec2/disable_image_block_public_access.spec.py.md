---
id: "@specs/aws/ec2/disable_image_block_public_access"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableImageBlockPublicAccess"
---

# DisableImageBlockPublicAccess

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_image_block_public_access
> **spec:implements:** @kind:operation DisableImageBlockPublicAccess
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableImageBlockPublicAccess.spec.md

Disables block public access for AMIs at the account level in the specified Amazon Web Services Region. This removes the block public access restriction from your account. With the restriction removed, you can publicly share your AMIs in the specified Amazon Web Services Region. For more information, see Block public access to your AMIs in the Amazon EC2 User Guide .

## Input Shape: DisableImageBlockPublicAccessRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisableImageBlockPublicAccessResult

- **ImageBlockPublicAccessState** (Any  # complex shape): Returns unblocked if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disable_image_block_public_access(store, request: dict) -> dict:
    """Disables block public access for AMIs at the account level in the specified Amazon Web Services Region. This removes the block public access restriction from your account. With the restriction removed"""

```
