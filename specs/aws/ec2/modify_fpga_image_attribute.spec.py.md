---
id: "@specs/aws/ec2/modify_fpga_image_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyFpgaImageAttribute"
---

# ModifyFpgaImageAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_fpga_image_attribute
> **spec:implements:** @kind:operation ModifyFpgaImageAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyFpgaImageAttribute.spec.md

Modifies the specified attribute of the specified Amazon FPGA Image (AFI).

## Input Shape: ModifyFpgaImageAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape |  | The name of the attribute. |
| Description | str |  | A description for the AFI. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| FpgaImageId | Any  # complex shape | ✓ | The ID of the AFI. |
| LoadPermission | Any  # complex shape |  | The load permission for the AFI. |
| Name | str |  | A name for the AFI. |
| OperationType | Any  # complex shape |  | The operation type. |
| ProductCodes | list[str] |  | The product codes. After you add a product code to an AFI, it can't be removed. This parameter is valid only when modify |
| UserGroups | list[str] |  | The user groups. This parameter is valid only when modifying the loadPermission attribute. |
| UserIds | list[str] |  | The Amazon Web Services account IDs. This parameter is valid only when modifying the loadPermission attribute. |

## Output Shape: ModifyFpgaImageAttributeResult

- **FpgaImageAttribute** (Any  # complex shape): Information about the attribute.

## Implementation

```speclang
def modify_fpga_image_attribute(store, request: dict) -> dict:
    """Modifies the specified attribute of the specified Amazon FPGA Image (AFI)."""
    fpga_image_id = request.get("FpgaImageId", "").strip() if isinstance(request.get("FpgaImageId"), str) else request.get("FpgaImageId")
    if not fpga_image_id:
        raise ValidationException("FpgaImageId is required")

    resource = store.fpga_image_attributes(fpga_image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource fpga_image_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Attribute" in request:
        resource["Attribute"] = attribute
    if "OperationType" in request:
        resource["OperationType"] = operation_type
    if "UserIds" in request:
        resource["UserIds"] = user_ids
    if "UserGroups" in request:
        resource["UserGroups"] = user_groups
    if "ProductCodes" in request:
        resource["ProductCodes"] = product_codes
    if "LoadPermission" in request:
        resource["LoadPermission"] = load_permission
    if "Description" in request:
        resource["Description"] = description
    if "Name" in request:
        resource["Name"] = name

    store.fpga_image_attributes(fpga_image_id, resource)
    return resource
```
