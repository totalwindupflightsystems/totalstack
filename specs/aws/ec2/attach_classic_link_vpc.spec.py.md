---
id: "@specs/aws/ec2/attach_classic_link_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AttachClassicLinkVpc"
---

# AttachClassicLinkVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/attach_classic_link_vpc
> **spec:implements:** @kind:operation AttachClassicLinkVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AttachClassicLinkVpc.spec.md

This action is deprecated. Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC security groups. You cannot link an EC2-Classic instance to more than one VPC at a time. You can only link an instance that's in the running state. An instance is automatically unlinked from a VPC when it's stopped - you can link it to the VPC again when you restart it. After you've linked an instance, you cannot change the VPC security groups that are associated with it. To change the security groups, you must first unlink the instance, and then link it again. Linking your instance to a VPC is sometimes referred to as attaching your instance.

## Input Shape: AttachClassicLinkVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Groups | list[Any  # complex shape] | ✓ | The IDs of the security groups. You cannot specify security groups from a different VPC. |
| InstanceId | Any  # complex shape | ✓ | The ID of the EC2-Classic instance. |
| VpcId | Any  # complex shape | ✓ | The ID of the ClassicLink-enabled VPC. |

## Output Shape: AttachClassicLinkVpcResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def attach_classic_link_vpc(store, request: dict) -> dict:
    """This action is deprecated. Links an EC2-Classic instance to a ClassicLink-enabled VPC through one or more of the VPC security groups. You cannot link an EC2-Classic instance to more than one VPC at a """
    groups = request.get("Groups", "").strip() if isinstance(request.get("Groups"), str) else request.get("Groups")
    if not groups:
        raise ValidationException("Groups is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachClassicLinkVpc", request)
```
