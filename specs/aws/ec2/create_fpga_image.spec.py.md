---
id: "@specs/aws/ec2/create_fpga_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateFpgaImage"
---

# CreateFpgaImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_fpga_image
> **spec:implements:** @kind:operation CreateFpgaImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateFpgaImage.spec.md

Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP). The create operation is asynchronous. To verify that the AFI was successfully created and is ready for use, check the output logs. An AFI contains the FPGA bitstream that is ready to download to an FPGA. You can securely deploy an AFI on multiple FPGA-accelerated instances. For more information, see the Amazon Web Services FPGA Hardware Development Kit .

## Input Shape: CreateFpgaImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| Description | str |  | A description for the AFI. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InputStorageLocation | Any  # complex shape | ✓ | The location of the encrypted design checkpoint in Amazon S3. The input must be a tarball. |
| LogsStorageLocation | Any  # complex shape |  | The location in Amazon S3 for the output logs. |
| Name | str |  | A name for the AFI. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the FPGA image during creation. |

## Output Shape: CreateFpgaImageResult

- **FpgaImageGlobalId** (str): The global FPGA image identifier (AGFI ID).
- **FpgaImageId** (str): The FPGA image identifier (AFI ID).

## Implementation

```speclang
def create_fpga_image(store, request: dict) -> dict:
    """Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP). The create operation is asynchronous. To verify that the AFI was successfully created and is ready for use, check the out"""
    input_storage_location = request.get("InputStorageLocation", "").strip() if isinstance(request.get("InputStorageLocation"), str) else request.get("InputStorageLocation")
    if not input_storage_location:
        raise ValidationException("InputStorageLocation is required")

    if store.fpga_images(input_storage_location):
        raise ResourceInUseException(f"Resource input_storage_location already exists")

    record = {
        "DryRun": dry_run,
        "InputStorageLocation": input_storage_location,
        "LogsStorageLocation": logs_storage_location,
        "Description": description,
        "Name": name,
        "ClientToken": client_token,
        "TagSpecifications": tag_specifications,
    }

    store.fpga_images(input_storage_location, record)

    return {
        "FpgaImageId": record.get("FpgaImageId", {}),
        "FpgaImageGlobalId": record.get("FpgaImageGlobalId", {}),
    }
```
