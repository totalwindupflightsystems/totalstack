---
id: "@specs/aws/ec2/copy_fpga_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CopyFpgaImage"
---

# CopyFpgaImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/copy_fpga_image
> **spec:implements:** @kind:operation CopyFpgaImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CopyFpgaImage.spec.md

Copies the specified Amazon FPGA Image (AFI) to the current Region.

## Input Shape: CopyFpgaImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| Description | str |  | The description for the new AFI. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Name | str |  | The name for the new AFI. The default is the name of the source AFI. |
| SourceFpgaImageId | str | ✓ | The ID of the source AFI. |
| SourceRegion | str | ✓ | The Region that contains the source AFI. |

## Output Shape: CopyFpgaImageResult

- **FpgaImageId** (str): The ID of the new AFI.

## Implementation

```speclang
def copy_fpga_image(store, request: dict) -> dict:
    """Copies the specified Amazon FPGA Image (AFI) to the current Region."""
    source_fpga_image_id = request.get("SourceFpgaImageId", "").strip() if isinstance(request.get("SourceFpgaImageId"), str) else request.get("SourceFpgaImageId")
    if not source_fpga_image_id:
        raise ValidationException("SourceFpgaImageId is required")
    source_region = request.get("SourceRegion", "").strip() if isinstance(request.get("SourceRegion"), str) else request.get("SourceRegion")
    if not source_region:
        raise ValidationException("SourceRegion is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CopyFpgaImage", request)
```
