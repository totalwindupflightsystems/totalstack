---
id: "@specs/aws/ec2/export_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ExportImage"
---

# ExportImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/export_image
> **spec:implements:** @kind:operation ExportImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ExportImage.spec.md

Exports an Amazon Machine Image (AMI) to a VM file. For more information, see Exporting a VM directly from an Amazon Machine Image (AMI) in the VM Import/Export User Guide .

## Input Shape: ExportImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Token to enable idempotency for export image requests. |
| Description | str |  | A description of the image being exported. The maximum length is 255 characters. |
| DiskImageFormat | Any  # complex shape | ✓ | The disk image format. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the image. |
| RoleName | str |  | The name of the role that grants VM Import/Export permission to export images to your Amazon S3 bucket. If this paramete |
| S3ExportLocation | Any  # complex shape | ✓ | The Amazon S3 bucket for the destination image. The destination bucket must exist. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the export image task during creation. |

## Output Shape: ExportImageResult

- **Description** (str): A description of the image being exported.
- **DiskImageFormat** (Any  # complex shape): The disk image format for the exported image.
- **ExportImageTaskId** (str): The ID of the export image task.
- **ImageId** (str): The ID of the image.
- **Progress** (str): The percent complete of the export image task.
- **RoleName** (str): The name of the role that grants VM Import/Export permission to export images to your Amazon S3 bucket.
- **S3ExportLocation** (Any  # complex shape): Information about the destination Amazon S3 bucket.
- **Status** (str): The status of the export image task. The possible values are active , completed , deleting , and deleted .
- **StatusMessage** (str): The status message for the export image task.
- **Tags** (list[Any  # complex shape]): Any tags assigned to the export image task.

## Implementation

```speclang
def export_image(store, request: dict) -> dict:
    """Exports an Amazon Machine Image (AMI) to a VM file. For more information, see Exporting a VM directly from an Amazon Machine Image (AMI) in the VM Import/Export User Guide ."""
    disk_image_format = request.get("DiskImageFormat", "").strip() if isinstance(request.get("DiskImageFormat"), str) else request.get("DiskImageFormat")
    if not disk_image_format:
        raise ValidationException("DiskImageFormat is required")
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")
    s3_export_location = request.get("S3ExportLocation", "").strip() if isinstance(request.get("S3ExportLocation"), str) else request.get("S3ExportLocation")
    if not s3_export_location:
        raise ValidationException("S3ExportLocation is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ExportImage", request)
```
