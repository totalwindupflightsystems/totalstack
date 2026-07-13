---
id: "@specs/aws/ec2/create_default_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateDefaultVpc"
---

# CreateDefaultVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_default_vpc
> **spec:implements:** @kind:operation CreateDefaultVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateDefaultVpc.spec.md

Creates a default VPC with a size /16 IPv4 CIDR block and a default subnet in each Availability Zone. For more information about the components of a default VPC, see Default VPCs in the Amazon VPC User Guide . You cannot specify the components of the default VPC yourself. If you deleted your previous default VPC, you can create a default VPC. You cannot have more than one default VPC per Region.

## Input Shape: CreateDefaultVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: CreateDefaultVpcResult

- **Vpc** (Any  # complex shape): Information about the VPC.

## Implementation

```speclang
def create_default_vpc(store, request: dict) -> dict:
    """Creates a default VPC with a size /16 IPv4 CIDR block and a default subnet in each Availability Zone. For more information about the components of a default VPC, see Default VPCs in the Amazon VPC Use"""


    record = {
        "DryRun": dry_run,
    }

    store.default_vpcs(record)

    return {
        "Vpc": record.get("Vpc", {}),
    }
```
