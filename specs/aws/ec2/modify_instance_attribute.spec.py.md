---
id: "@specs/aws/ec2/modify_instance_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyInstanceAttribute"
---

# ModifyInstanceAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_instance_attribute
> **spec:implements:** @kind:operation ModifyInstanceAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyInstanceAttribute.spec.md

Modifies the specified attribute of the specified instance. You can specify only one attribute at a time. Note: Using this action to change the security groups associated with an elastic network interface (ENI) attached to an instance can result in an error if the instance has more than one ENI. To change the security groups associated with an ENI attached to an instance that has multiple ENIs, we recommend that you use the ModifyNetworkInterfaceAttribute action. To modify some attributes, the instance must be stopped. For more information, see Modify a stopped instance in the Amazon EC2 User Guide .

## Input Shape: ModifyInstanceAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape |  | The name of the attribute to modify. When changing the instance type: If the original instance type is configured for co |
| BlockDeviceMappings | list[Any  # complex shape] |  | Modifies the DeleteOnTermination attribute for volumes that are currently attached. The volume must be owned by the call |
| DisableApiStop | Any  # complex shape |  | Indicates whether an instance is enabled for stop protection. For more information, see Enable stop protection for your  |
| DisableApiTermination | Any  # complex shape |  | Enable or disable termination protection for the instance. If the value is true , you can't terminate the instance using |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| EbsOptimized | Any  # complex shape |  | Specifies whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazo |
| EnaSupport | Any  # complex shape |  | Set to true to enable enhanced networking with ENA for the instance. This option is supported only for HVM instances. Sp |
| Groups | list[Any  # complex shape] |  | Replaces the security groups of the instance with the specified security groups. You must specify the ID of at least one |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| InstanceInitiatedShutdownBehavior | Any  # complex shape |  | Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating syst |
| InstanceType | Any  # complex shape |  | Changes the instance type to the specified value. For more information, see Instance types in the Amazon EC2 User Guide  |
| Kernel | Any  # complex shape |  | Changes the instance's kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks |
| Ramdisk | Any  # complex shape |  | Changes the instance's RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM dis |
| SourceDestCheck | Any  # complex shape |  | Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of a |
| SriovNetSupport | Any  # complex shape |  | Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance. There is n |
| UserData | Any  # complex shape |  | Changes the instance's user data to the specified value. User data must be base64-encoded. Depending on the tool or SDK  |
| Value | str |  | A new value for the attribute. Use only with the kernel , ramdisk , userData , disableApiTermination , or instanceInitia |

## Implementation

```speclang
def modify_instance_attribute(store, request: dict) -> dict:
    """Modifies the specified attribute of the specified instance. You can specify only one attribute at a time. Note: Using this action to change the security groups associated with an elastic network inter"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_attributes(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "SourceDestCheck" in request:
        resource["SourceDestCheck"] = source_dest_check
    if "DisableApiStop" in request:
        resource["DisableApiStop"] = disable_api_stop
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Attribute" in request:
        resource["Attribute"] = attribute
    if "Value" in request:
        resource["Value"] = value
    if "BlockDeviceMappings" in request:
        resource["BlockDeviceMappings"] = block_device_mappings
    if "DisableApiTermination" in request:
        resource["DisableApiTermination"] = disable_api_termination
    if "InstanceType" in request:
        resource["InstanceType"] = instance_type
    if "Kernel" in request:
        resource["Kernel"] = kernel
    if "Ramdisk" in request:
        resource["Ramdisk"] = ramdisk
    if "UserData" in request:
        resource["UserData"] = user_data
    if "InstanceInitiatedShutdownBehavior" in request:
        resource["InstanceInitiatedShutdownBehavior"] = instance_initiated_shutdown_behavior
    if "Groups" in request:
        resource["Groups"] = groups
    if "EbsOptimized" in request:
        resource["EbsOptimized"] = ebs_optimized
    if "SriovNetSupport" in request:
        resource["SriovNetSupport"] = sriov_net_support
    if "EnaSupport" in request:
        resource["EnaSupport"] = ena_support

    store.instance_attributes(instance_id, resource)
    return resource
```
