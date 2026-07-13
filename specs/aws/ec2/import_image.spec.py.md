---
id: "@specs/aws/ec2/import_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ImportImage"
---

# ImportImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/import_image
> **spec:implements:** @kind:operation ImportImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ImportImage.spec.md

To import your virtual machines (VMs) with a console-based experience, you can use the Import virtual machine images to Amazon Web Services template in the Migration Hub Orchestrator console . For more information, see the Migration Hub Orchestrator User Guide . Import single or multi-volume disk images or EBS snapshots into an Amazon Machine Image (AMI). Amazon Web Services VM Import/Export strongly recommends specifying a value for either the --license-type or --usage-operation parameter when you create a new VM Import task. This ensures your operating system is licensed appropriately and your billing is optimized. For more information, see Importing a VM as an image using VM Import/Export in the VM Import/Export User Guide .

## Input Shape: ImportImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Architecture | str |  | The architecture of the virtual machine. Valid values: i386 | x86_64 |
| BootMode | Any  # complex shape |  | The boot mode of the virtual machine. The uefi-preferred boot mode isn't supported for importing images. For more inform |
| ClientData | Any  # complex shape |  | The client-specific data. |
| ClientToken | str |  | The token to enable idempotency for VM import requests. |
| Description | str |  | A description string for the import image task. |
| DiskContainers | list[Any  # complex shape] |  | Information about the disk containers. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Encrypted | bool |  | Specifies whether the destination AMI of the imported image should be encrypted. The default KMS key for EBS is used unl |
| Hypervisor | str |  | The target hypervisor platform. Valid values: xen |
| KmsKeyId | str |  | An identifier for the symmetric KMS key to use when creating the encrypted AMI. This parameter is only required if you w |
| LicenseSpecifications | Any  # complex shape |  | The ARNs of the license configurations. |
| LicenseType | str |  | The license type to be used for the Amazon Machine Image (AMI) after importing. Specify AWS to replace the source-system |
| Platform | str |  | The operating system of the virtual machine. If you import a VM that is compatible with Unified Extensible Firmware Inte |
| RoleName | str |  | The name of the role to use when not using the default role, 'vmimport'. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the import image task during creation. |
| UsageOperation | str |  | The usage operation value. For more information, see Licensing options in the VM Import/Export User Guide . |

## Output Shape: ImportImageResult

- **Architecture** (str): The architecture of the virtual machine.
- **Description** (str): A description of the import task.
- **Encrypted** (bool): Indicates whether the AMI is encrypted.
- **Hypervisor** (str): The target hypervisor of the import task.
- **ImageId** (str): The ID of the Amazon Machine Image (AMI) created by the import task.
- **ImportTaskId** (Any  # complex shape): The task ID of the import image task.
- **KmsKeyId** (str): The identifier for the symmetric KMS key that was used to create the encrypted AMI.
- **LicenseSpecifications** (Any  # complex shape): The ARNs of the license configurations.
- **LicenseType** (str): The license type of the virtual machine.
- **Platform** (str): The operating system of the virtual machine.
- **Progress** (str): The progress of the task.
- **SnapshotDetails** (list[Any  # complex shape]): Information about the snapshots.
- **Status** (str): A brief status of the task.
- **StatusMessage** (str): A detailed status message of the import task.
- **Tags** (list[Any  # complex shape]): Any tags assigned to the import image task.
- **UsageOperation** (str): The usage operation value.

## Implementation

```speclang
def import_image(store, request: dict) -> dict:
    """To import your virtual machines (VMs) with a console-based experience, you can use the Import virtual machine images to Amazon Web Services template in the Migration Hub Orchestrator console . For mor"""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ImportImage", request)
```
