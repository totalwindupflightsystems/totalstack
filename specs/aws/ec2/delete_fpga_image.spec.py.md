---
id: "@specs/aws/ec2/delete_fpga_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteFpgaImage"
---

# DeleteFpgaImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_fpga_image
> **spec:implements:** @kind:operation DeleteFpgaImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteFpgaImage.spec.md

Deletes the specified Amazon FPGA Image (AFI).

## Input Shape: DeleteFpgaImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FpgaImageId | Any  # complex shape | ✓ | The ID of the AFI. |

## Output Shape: DeleteFpgaImageResult

- **Return** (bool): Is true if the request succeeds, and an error otherwise.

## Implementation

```speclang
def delete_fpga_image(store, request: dict) -> dict:
    """Deletes the specified Amazon FPGA Image (AFI)."""
    fpga_image_id = request.get("FpgaImageId", "").strip() if isinstance(request.get("FpgaImageId"), str) else request.get("FpgaImageId")

    if not store.fpga_images(fpga_image_id):
        raise ResourceNotFoundException(f"Resource fpga_image_id not found")
    store.delete_fpga_images(fpga_image_id)
    return {}
```
