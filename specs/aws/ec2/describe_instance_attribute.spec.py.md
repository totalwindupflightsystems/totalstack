---
id: "@specs/aws/ec2/describe_instance_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeInstanceAttribute"
---

# DescribeInstanceAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_instance_attribute
> **spec:implements:** @kind:operation DescribeInstanceAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeInstanceAttribute.spec.md

Describes the specified attribute of the specified instance. You can specify only one attribute at a time. Available attributes include SQL license exemption configuration for instances registered with the SQL LE service.

## Input Shape: DescribeInstanceAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The instance attribute. Note that the enaSupport attribute is not supported. |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |

## Output Shape: InstanceAttribute

- **BlockDeviceMappings** (list[Any  # complex shape]): The block device mapping of the instance.
- **DisableApiStop** (Any  # complex shape): Indicates whether stop protection is enabled for the instance.
- **DisableApiTermination** (Any  # complex shape): Indicates whether termination protection is enabled. If the value is true , you can't terminate the instance using the A
- **EbsOptimized** (Any  # complex shape): Indicates whether the instance is optimized for Amazon EBS I/O.
- **EnaSupport** (Any  # complex shape): Indicates whether enhanced networking with ENA is enabled.
- **EnclaveOptions** (Any  # complex shape): Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.
- **Groups** (list[Any  # complex shape]): The security groups associated with the instance.
- **InstanceId** (str): The ID of the instance.
- **InstanceInitiatedShutdownBehavior** (Any  # complex shape): Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating syst
- **InstanceType** (Any  # complex shape): The instance type.
- **KernelId** (Any  # complex shape): The kernel ID.
- **ProductCodes** (list[Any  # complex shape]): The product codes.
- **RamdiskId** (Any  # complex shape): The RAM disk ID.
- **RootDeviceName** (Any  # complex shape): The device name of the root device volume (for example, /dev/sda1 ).
- **SourceDestCheck** (Any  # complex shape): Indicates whether source/destination checks are enabled.
- **SriovNetSupport** (Any  # complex shape): Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.
- **UserData** (Any  # complex shape): The user data.

## Implementation

```speclang
def describe_instance_attribute(store, request: dict) -> dict:
    """Describes the specified attribute of the specified instance. You can specify only one attribute at a time. Available attributes include SQL license exemption configuration for instances registered wit"""
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.instance_attributes(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")
    return {"InstanceId": instance_id, **resource}
```
