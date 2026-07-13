---
id: "@specs/aws/ec2/register_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RegisterImage"
---

# RegisterImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/register_image
> **spec:implements:** @kind:operation RegisterImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RegisterImage.spec.md

Registers an AMI. When you're creating an instance-store backed AMI, registering the AMI is the final step in the creation process. For more information about creating AMIs, see Create an AMI from a snapshot and Create an instance-store backed AMI in the Amazon EC2 User Guide . If needed, you can deregister an AMI at any time. Any modifications you make to an AMI backed by an instance store volume invalidates its registration. If you make changes to an image, deregister the previous image and register the new image. Register a snapshot of a root device volume You can use RegisterImage to create an Amazon EBS-backed Linux AMI from a snapshot of a root device volume. You specify the snapshot using a block device mapping. You can't set the encryption state of the volume using the block device mapping. If the snapshot is encrypted, or encryption by default is enabled, the root volume of an instance launched from the AMI is encrypted. For more information, see Create an AMI from a snapshot and Use encryption with EBS-backed AMIs in the Amazon EC2 User Guide . Amazon Web Services Marketplace product codes If any snapshots have Amazon Web Services Marketplace product codes, they are copied to the new AMI. In most cases, AMIs for Windows, RedHat, SUSE, and SQL Server require correct licensing information to be present on the AMI. For more information, see Understand AMI billing information in the Amazon EC2 User Guide . When creating an AMI from a snapshot, the RegisterImage operation derives the correct billing information from the snapshot's metadata, but this requires the appropriate metadata to be present. To verify if the correct billing information was applied, check the PlatformDetails field on the new AMI. If the field is empty or doesn't match the expected operating system code (for example, Windows, RedHat, SUSE, or SQL), the AMI creation was unsuccessful, and you should discard the AMI and instead create the AMI from an instance. For more information, see Create an AMI from an instance in the Amazon EC2 User Guide . If you purchase a Reserved Instance to apply to an On-Demand Instance that was launched from an AMI with a billing product code, make sure that the Reserved Instance has the matching billing product code. If you purchase a Reserved Instance without the matching billing product code, the Reserved Instance is not applied to the On-Demand Instance. For information about how to obtain the platform details and billing information of an AMI, see Understand AMI billing information in the Amazon EC2 User Guide .

## Input Shape: RegisterImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Architecture | Any  # complex shape |  | The architecture of the AMI. Default: For Amazon EBS-backed AMIs, i386 . For instance store-backed AMIs, the architectur |
| BillingProducts | list[str] |  | The billing product codes. Your account must be authorized to specify billing product codes. If your account is not auth |
| BlockDeviceMappings | list[Any  # complex shape] |  | The block device mapping entries. If you specify an Amazon EBS volume using the ID of an Amazon EBS snapshot, you can't  |
| BootMode | Any  # complex shape |  | The boot mode of the AMI. A value of uefi-preferred indicates that the AMI supports both UEFI and Legacy BIOS. The opera |
| Description | str |  | A description for your AMI. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EnaSupport | bool |  | Set to true to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI. This opti |
| ImageLocation | str |  | The full path to your AMI manifest in Amazon S3 storage. The specified bucket must have the aws-exec-read canned access  |
| ImdsSupport | Any  # complex shape |  | Set to v2.0 to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have HttpTokens autom |
| KernelId | Any  # complex shape |  | The ID of the kernel. |
| Name | str | ✓ | A name for your AMI. Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), per |
| RamdiskId | Any  # complex shape |  | The ID of the RAM disk. |
| RootDeviceName | str |  | The device name of the root device volume (for example, /dev/sda1 ). |
| SriovNetSupport | str |  | Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instance |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the AMI. To tag the AMI, the value for ResourceType must be image . If you specify another value fo |
| TpmSupport | Any  # complex shape |  | Set to v2.0 to enable Trusted Platform Module (TPM) support. For more information, see NitroTPM in the Amazon EC2 User G |
| UefiData | Any  # complex shape |  | Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the GetInstanceUefiData co |
| VirtualizationType | str |  | The type of virtualization ( hvm | paravirtual ). Default: paravirtual |

## Output Shape: RegisterImageResult

- **ImageId** (str): The ID of the newly registered AMI.

## Implementation

```speclang
def register_image(store, request: dict) -> dict:
    """Registers an AMI. When you're creating an instance-store backed AMI, registering the AMI is the final step in the creation process. For more information about creating AMIs, see Create an AMI from a s"""
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")
    if not name:
        raise ValidationException("Name is required")

    if store.register_images(name):
        raise ResourceInUseException(f"Resource name already exists")

    record = {
        "ImageLocation": image_location,
        "BillingProducts": billing_products,
        "BootMode": boot_mode,
        "TpmSupport": tpm_support,
        "UefiData": uefi_data,
        "ImdsSupport": imds_support,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "Name": name,
        "Description": description,
        "Architecture": architecture,
        "KernelId": kernel_id,
        "RamdiskId": ramdisk_id,
        "RootDeviceName": root_device_name,
        "BlockDeviceMappings": block_device_mappings,
        "VirtualizationType": virtualization_type,
        "SriovNetSupport": sriov_net_support,
        "EnaSupport": ena_support,
    }

    store.register_images(name, record)

    return {
        "ImageId": record.get("ImageId", {}),
    }
```
