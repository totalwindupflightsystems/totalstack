---
id: "@specs/aws/ec2/run_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RunInstances"
---

# RunInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/run_instances
> **spec:implements:** @kind:operation RunInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RunInstances.spec.md

Launches the specified number of instances using an AMI for which you have permissions. You can specify a number of options, or leave the default options. The following rules apply: If you don't specify a subnet ID, we choose a default subnet from your default VPC for you. If you don't have a default VPC, you must specify a subnet ID in the request. All instances have a network interface with a primary private IPv4 address. If you don't specify this address, we choose one from the IPv4 range of your subnet. Not all instance types support IPv6 addresses. For more information, see Instance types . If you don't specify a security group ID, we use the default security group for the VPC. For more information, see Security groups . If any of the AMIs have a product code attached for which the user has not subscribed, the request fails. You can create a launch template , which is a resource that contains the parameters to launch an instance. When you launch an instance using RunInstances , you can specify the launch template instead of specifying the launch parameters. To ensure faster instance launches, break up large requests into smaller batches. For example, create five separate launch requests for 100 instances each instead of one launch request for 500 instances. RunInstances is subject to both request rate limiting and resource rate limiting. For more information, see Request throttling . An instance is ready for you to use when it's in the running state. You can check the state of your instance using DescribeInstances . You can tag instances and EBS volumes during launch, after launch, or both. For more information, see CreateTags and Tagging your Amazon EC2 resources . Linux instances have access to the public key of the key pair at boot. You can use this key to provide secure access to the instance. Amazon EC2 public images use this feature to provide secure access without passwords. For more information, see Key pairs . For troubleshooting, see What to do if an instance immediately terminates , and Troubleshooting connecting to your instance .

## Input Shape: RunInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AdditionalInfo | str |  | Reserved. |
| BlockDeviceMappings | list[Any  # complex shape] |  | The block device mapping, which defines the EBS volumes and instance store volumes to attach to the instance at launch.  |
| CapacityReservationSpecification | Any  # complex shape |  | Information about the Capacity Reservation targeting option. If you do not specify this parameter, the instance's Capaci |
| ClientToken | str |  | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client t |
| CpuOptions | Any  # complex shape |  | The CPU options for the instance. For more information, see Optimize CPU options in the Amazon EC2 User Guide . |
| CreditSpecification | Any  # complex shape |  | The credit option for CPU usage of the burstable performance instance. Valid values are standard and unlimited . To chan |
| DisableApiStop | bool |  | Indicates whether an instance is enabled for stop protection. For more information, see Enable stop protection for your  |
| DisableApiTermination | bool |  | Indicates whether termination protection is enabled for the instance. The default is false , which means that you can te |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| EbsOptimized | bool |  | Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazo |
| ElasticGpuSpecification | Any  # complex shape |  | An elastic GPU to associate with the instance. Amazon Elastic Graphics reached end of life on January 8, 2024. |
| ElasticInferenceAccelerators | Any  # complex shape |  | An elastic inference accelerator to associate with the instance. Amazon Elastic Inference is no longer available. |
| EnablePrimaryIpv6 | bool |  | If you’re launching an instance into a dual-stack or IPv6-only subnet, you can enable assigning a primary IPv6 address.  |
| EnclaveOptions | Any  # complex shape |  | Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more information, see Amazon Web S |
| HibernationOptions | Any  # complex shape |  | Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the hiberna |
| IamInstanceProfile | Any  # complex shape |  | The name or Amazon Resource Name (ARN) of an IAM instance profile. |
| ImageId | Any  # complex shape |  | The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in a launch template. |
| InstanceInitiatedShutdownBehavior | Any  # complex shape |  | Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating syst |
| InstanceMarketOptions | Any  # complex shape |  | The market (purchasing) option for the instances. For RunInstances , persistent Spot Instance requests are only supporte |
| InstanceType | Any  # complex shape |  | The instance type. For more information, see Amazon EC2 Instance Types Guide . |
| Ipv6AddressCount | int |  | The number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from |
| Ipv6Addresses | list[Any  # complex shape] |  | The IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this |
| KernelId | Any  # complex shape |  | The ID of the kernel. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see PV-G |
| KeyName | Any  # complex shape |  | The name of the key pair. For more information, see Create a key pair for your EC2 instance . If you do not specify a ke |
| LaunchTemplate | Any  # complex shape |  | The launch template. Any additional parameters that you specify for the new instance overwrite the corresponding paramet |
| LicenseSpecifications | Any  # complex shape |  | The license configurations. |
| MaintenanceOptions | Any  # complex shape |  | The maintenance and recovery options for the instance. |
| MaxCount | int | ✓ | The maximum number of instances to launch. If you specify a value that is more capacity than Amazon EC2 can launch in th |
| MetadataOptions | Any  # complex shape |  | The metadata options for the instance. For more information, see Configure the Instance Metadata Service options . |
| MinCount | int | ✓ | The minimum number of instances to launch. If you specify a value that is more capacity than Amazon EC2 can provide in t |
| Monitoring | Any  # complex shape |  | Specifies whether detailed monitoring is enabled for the instance. |
| NetworkInterfaces | list[Any  # complex shape] |  | The network interfaces to associate with the instance. |
| NetworkPerformanceOptions | Any  # complex shape |  | Contains settings for the network performance options for the instance. |
| Operator | Any  # complex shape |  | Reserved for internal use. |
| Placement | Any  # complex shape |  | The placement for the instance. |
| PrivateDnsNameOptions | Any  # complex shape |  | The options for the instance hostname. The default values are inherited from the subnet. Applies only if creating a netw |
| PrivateIpAddress | str |  | The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet. Only one private IP addres |
| RamdiskId | Any  # complex shape |  | The ID of the RAM disk to select. Some kernels require additional drivers at launch. Check the kernel requirements for i |
| SecondaryInterfaces | Any  # complex shape |  | The secondary interfaces to associate with the instance. |
| SecurityGroupIds | list[Any  # complex shape] |  | The IDs of the security groups. If you specify a network interface, you must specify any security groups as part of the  |
| SecurityGroups | list[Any  # complex shape] |  | [Default VPC] The names of the security groups. If you specify a network interface, you must specify any security groups |
| SubnetId | Any  # complex shape |  | The ID of the subnet to launch the instance into. If you specify a network interface, you must specify any subnets as pa |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the resources that are created during instance launch. You can specify tags for the following resou |
| UserData | Any  # complex shape |  | The user data to make available to the instance. User data must be base64-encoded. Depending on the tool or SDK that you |

## Output Shape: Reservation

- **Groups** (list[Any  # complex shape]): Not supported.
- **Instances** (list[Any  # complex shape]): The instances.
- **OwnerId** (str): The ID of the Amazon Web Services account that owns the reservation.
- **RequesterId** (str): The ID of the requester that launched the instances on your behalf (for example, Amazon Web Services Management Console 
- **ReservationId** (str): The ID of the reservation.

## Implementation

```speclang
def run_instances(store, request: dict) -> dict:
    """Launches the specified number of instances using an AMI for which you have permissions. You can specify a number of options, or leave the default options. The following rules apply: If you don't speci"""
    max_count = request.get("MaxCount", "").strip() if isinstance(request.get("MaxCount"), str) else request.get("MaxCount")
    if not max_count:
        raise ValidationException("MaxCount is required")
    min_count = request.get("MinCount", "").strip() if isinstance(request.get("MinCount"), str) else request.get("MinCount")
    if not min_count:
        raise ValidationException("MinCount is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RunInstances", request)
```
