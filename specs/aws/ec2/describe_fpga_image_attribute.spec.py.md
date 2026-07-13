---
id: "@specs/aws/ec2/describe_fpga_image_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeFpgaImageAttribute"
---

# DescribeFpgaImageAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_fpga_image_attribute
> **spec:implements:** @kind:operation DescribeFpgaImageAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeFpgaImageAttribute.spec.md

Describes the specified attribute of the specified Amazon FPGA Image (AFI).

## Input Shape: DescribeFpgaImageAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The AFI attribute. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FpgaImageId | Any  # complex shape | ✓ | The ID of the AFI. |

## Output Shape: DescribeFpgaImageAttributeResult

- **FpgaImageAttribute** (Any  # complex shape): Information about the attribute.

## Implementation

```speclang
def describe_fpga_image_attribute(store, request: dict) -> dict:
    """Describes the specified attribute of the specified Amazon FPGA Image (AFI)."""
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    fpga_image_id = request.get("FpgaImageId", "").strip() if isinstance(request.get("FpgaImageId"), str) else request.get("FpgaImageId")
    if not fpga_image_id:
        raise ValidationException("FpgaImageId is required")

    resource = store.fpga_image_attributes(fpga_image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource fpga_image_id not found")
    return {"FpgaImageId": fpga_image_id, **resource}
```
