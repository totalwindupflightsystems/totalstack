---
id: "@specs/aws/ec2/detach_classic_link_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DetachClassicLinkVpc"
---

# DetachClassicLinkVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/detach_classic_link_vpc
> **spec:implements:** @kind:operation DetachClassicLinkVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DetachClassicLinkVpc.spec.md

This action is deprecated. Unlinks (detaches) a linked EC2-Classic instance from a VPC. After the instance has been unlinked, the VPC security groups are no longer associated with it. An instance is automatically unlinked from a VPC when it's stopped.

## Input Shape: DetachClassicLinkVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance to unlink from the VPC. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC to which the instance is linked. |

## Output Shape: DetachClassicLinkVpcResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def detach_classic_link_vpc(store, request: dict) -> dict:
    """This action is deprecated. Unlinks (detaches) a linked EC2-Classic instance from a VPC. After the instance has been unlinked, the VPC security groups are no longer associated with it. An instance is a"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachClassicLinkVpc", request)
```
