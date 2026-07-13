---
id: "@specs/aws/ec2/modify_vpc_tenancy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcTenancy"
---

# ModifyVpcTenancy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_tenancy
> **spec:implements:** @kind:operation ModifyVpcTenancy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcTenancy.spec.md

Modifies the instance tenancy attribute of the specified VPC. You can change the instance tenancy attribute of a VPC to default only. You cannot change the instance tenancy attribute to dedicated . After you modify the tenancy of the VPC, any new instances that you launch into the VPC have a tenancy of default , unless you specify otherwise during launch. The tenancy of any existing instances in the VPC is not affected. For more information, see Dedicated Instances in the Amazon EC2 User Guide .

## Input Shape: ModifyVpcTenancyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceTenancy | Any  # complex shape | ✓ | The instance tenancy attribute for the VPC. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: ModifyVpcTenancyResult

- **ReturnValue** (bool): Returns true if the request succeeds; otherwise, returns an error.

## Implementation

```speclang
def modify_vpc_tenancy(store, request: dict) -> dict:
    """Modifies the instance tenancy attribute of the specified VPC. You can change the instance tenancy attribute of a VPC to default only. You cannot change the instance tenancy attribute to dedicated . Af"""
    instance_tenancy = request.get("InstanceTenancy", "").strip() if isinstance(request.get("InstanceTenancy"), str) else request.get("InstanceTenancy")
    if not instance_tenancy:
        raise ValidationException("InstanceTenancy is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.vpc_tenancys(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.vpc_tenancys(vpc_id, resource)
    return resource
```
