---
id: "@specs/aws/ec2/reset_fpga_image_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ResetFpgaImageAttribute"
---

# ResetFpgaImageAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reset_fpga_image_attribute
> **spec:implements:** @kind:operation ResetFpgaImageAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ResetFpgaImageAttribute.spec.md

Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its default value. You can only reset the load permission attribute.

## Input Shape: ResetFpgaImageAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape |  | The attribute. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FpgaImageId | Any  # complex shape | ✓ | The ID of the AFI. |

## Output Shape: ResetFpgaImageAttributeResult

- **Return** (bool): Is true if the request succeeds, and an error otherwise.

## Implementation

```speclang
def reset_fpga_image_attribute(store, request: dict) -> dict:
    """Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its default value. You can only reset the load permission attribute."""
    fpga_image_id = request.get("FpgaImageId", "").strip() if isinstance(request.get("FpgaImageId"), str) else request.get("FpgaImageId")
    if not fpga_image_id:
        raise ValidationException("FpgaImageId is required")

    resource = store.reset_fpga_image_attributes(fpga_image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource fpga_image_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Attribute" in request:
        resource["Attribute"] = attribute

    store.reset_fpga_image_attributes(fpga_image_id, resource)
    return resource
```
