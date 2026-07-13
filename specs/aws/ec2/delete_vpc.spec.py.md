---
id: "@specs/aws/ec2/delete_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpc"
---

# DeleteVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpc
> **spec:implements:** @kind:operation DeleteVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpc.spec.md

Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it. For example, you must terminate all instances running in the VPC, delete all security groups associated with the VPC (except the default one), delete all route tables associated with the VPC (except the default one), and so on. When you delete the VPC, it deletes the default security group, network ACL, and route table for the VPC. If you created a flow log for the VPC that you are deleting, note that flow logs for deleted VPCs are eventually automatically removed.

## Input Shape: DeleteVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Implementation

```speclang
def delete_vpc(store, request: dict) -> dict:
    """Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it. For example, you must terminate all instances running in the """
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")

    if not store.vpcs(vpc_id):
        raise ResourceNotFoundException(f"Resource vpc_id not found")
    store.delete_vpcs(vpc_id)
    return {}
```
