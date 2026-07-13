---
id: "@specs/aws/ec2/modify_image_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyImageAttribute"
---

# ModifyImageAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_image_attribute
> **spec:implements:** @kind:operation ModifyImageAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyImageAttribute.spec.md

Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time. To specify the attribute, you can use the Attribute parameter, or one of the following parameters: Description , ImdsSupport , or LaunchPermission . Images with an Amazon Web Services Marketplace product code cannot be made public. To enable the SriovNetSupport enhanced networking attribute of an image, enable SriovNetSupport on an instance and create an AMI from the instance.

## Input Shape: ModifyImageAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | str |  | The name of the attribute to modify. Valid values: description | imdsSupport | launchPermission |
| Description | Any  # complex shape |  | A new description for the AMI. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |
| ImdsSupport | Any  # complex shape |  | Set to v2.0 to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have HttpTokens autom |
| LaunchPermission | Any  # complex shape |  | A new launch permission for the AMI. |
| OperationType | Any  # complex shape |  | The operation type. This parameter can be used only when the Attribute parameter is launchPermission . |
| OrganizationArns | list[str] |  | The Amazon Resource Name (ARN) of an organization. This parameter can be used only when the Attribute parameter is launc |
| OrganizationalUnitArns | list[str] |  | The Amazon Resource Name (ARN) of an organizational unit (OU). This parameter can be used only when the Attribute parame |
| ProductCodes | list[str] |  | Not supported. |
| UserGroups | list[str] |  | The user groups. This parameter can be used only when the Attribute parameter is launchPermission . |
| UserIds | list[str] |  | The Amazon Web Services account IDs. This parameter can be used only when the Attribute parameter is launchPermission . |
| Value | str |  | The value of the attribute being modified. This parameter can be used only when the Attribute parameter is description o |

## Implementation

```speclang
def modify_image_attribute(store, request: dict) -> dict:
    """Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time. To specify the attribute, you can use the Attribute parameter, or one of the following parameters: """
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.image_attributes(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")

    # Update mutable fields
    if "Attribute" in request:
        resource["Attribute"] = attribute
    if "Description" in request:
        resource["Description"] = description
    if "LaunchPermission" in request:
        resource["LaunchPermission"] = launch_permission
    if "OperationType" in request:
        resource["OperationType"] = operation_type
    if "ProductCodes" in request:
        resource["ProductCodes"] = product_codes
    if "UserGroups" in request:
        resource["UserGroups"] = user_groups
    if "UserIds" in request:
        resource["UserIds"] = user_ids
    if "Value" in request:
        resource["Value"] = value
    if "OrganizationArns" in request:
        resource["OrganizationArns"] = organization_arns
    if "OrganizationalUnitArns" in request:
        resource["OrganizationalUnitArns"] = organizational_unit_arns
    if "ImdsSupport" in request:
        resource["ImdsSupport"] = imds_support
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.image_attributes(image_id, resource)
    return resource
```
