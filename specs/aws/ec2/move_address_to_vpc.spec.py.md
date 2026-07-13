---
id: "@specs/aws/ec2/move_address_to_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_MoveAddressToVpc"
---

# MoveAddressToVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/move_address_to_vpc
> **spec:implements:** @kind:operation MoveAddressToVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_MoveAddressToVpc.spec.md

This action is deprecated. Moves an Elastic IP address from the EC2-Classic platform to the EC2-VPC platform. The Elastic IP address must be allocated to your account for more than 24 hours, and it must not be associated with an instance. After the Elastic IP address is moved, it is no longer available for use in the EC2-Classic platform. You cannot move an Elastic IP address that was originally allocated for use in the EC2-VPC platform to the EC2-Classic platform.

## Input Shape: MoveAddressToVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PublicIp | str | ✓ | The Elastic IP address. |

## Output Shape: MoveAddressToVpcResult

- **AllocationId** (str): The allocation ID for the Elastic IP address.
- **Status** (Any  # complex shape): The status of the move of the IP address.

## Implementation

```speclang
def move_address_to_vpc(store, request: dict) -> dict:
    """This action is deprecated. Moves an Elastic IP address from the EC2-Classic platform to the EC2-VPC platform. The Elastic IP address must be allocated to your account for more than 24 hours, and it mu"""
    public_ip = request.get("PublicIp", "").strip() if isinstance(request.get("PublicIp"), str) else request.get("PublicIp")
    if not public_ip:
        raise ValidationException("PublicIp is required")

    if store.move_address_to_vpcs(public_ip):
        raise ResourceInUseException(f"Resource public_ip already exists")

    record = {
        "DryRun": dry_run,
        "PublicIp": public_ip,
    }

    store.move_address_to_vpcs(public_ip, record)

    return {
        "AllocationId": record.get("AllocationId", {}),
        "Status": record.get("Status", {}),
    }
```
