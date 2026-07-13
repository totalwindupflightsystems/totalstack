---
id: "@specs/aws/ec2/describe_image_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeImageAttribute"
---

# DescribeImageAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_image_attribute
> **spec:implements:** @kind:operation DescribeImageAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeImageAttribute.spec.md

Describes the specified attribute of the specified AMI. You can specify only one attribute at a time. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeImageAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The AMI attribute. Note : The blockDeviceMapping attribute is deprecated. Using this attribute returns the Client.AuthFa |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |

## Output Shape: ImageAttribute

- **BlockDeviceMappings** (list[Any  # complex shape]): The block device mapping entries.
- **BootMode** (Any  # complex shape): The boot mode.
- **DeregistrationProtection** (Any  # complex shape): Indicates whether deregistration protection is enabled for the AMI.
- **Description** (Any  # complex shape): A description for the AMI.
- **ImageId** (str): The ID of the AMI.
- **ImdsSupport** (Any  # complex shape): If v2.0 , it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have HttpTokens automa
- **KernelId** (Any  # complex shape): The kernel ID.
- **LastLaunchedTime** (Any  # complex shape): The date and time, in ISO 8601 date-time format , when the AMI was last used to launch an EC2 instance. When the AMI is 
- **LaunchPermissions** (list[Any  # complex shape]): The launch permissions.
- **ProductCodes** (list[Any  # complex shape]): The product codes.
- **RamdiskId** (Any  # complex shape): The RAM disk ID.
- **SriovNetSupport** (Any  # complex shape): Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.
- **TpmSupport** (Any  # complex shape): If the image is configured for NitroTPM support, the value is v2.0 .
- **UefiData** (Any  # complex shape): Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the GetInstanceUefiData co

## Implementation

```speclang
def describe_image_attribute(store, request: dict) -> dict:
    """Describes the specified attribute of the specified AMI. You can specify only one attribute at a time. The order of the elements in the response, including those within nested structures, might vary. A"""
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    resource = store.image_attributes(image_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource image_id not found")
    return {"ImageId": image_id, **resource}
```
