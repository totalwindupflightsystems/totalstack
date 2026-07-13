---
id: "@specs/aws/ec2/disassociate_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateAddress"
---

# DisassociateAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_address
> **spec:implements:** @kind:operation DisassociateAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateAddress.spec.md

Disassociates an Elastic IP address from the instance or network interface it's associated with. This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error. An address cannot be disassociated if the all of the following conditions are met: Network interface has a publicDualStackDnsName publicDnsName Public IPv4 address is the primary public IPv4 address Network interface only has one remaining public IPv4 address

## Input Shape: DisassociateAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | Any  # complex shape |  | The association ID. This parameter is required. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PublicIp | Any  # complex shape |  | Deprecated. |

## Implementation

```speclang
def disassociate_address(store, request: dict) -> dict:
    """Disassociates an Elastic IP address from the instance or network interface it's associated with. This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return"""


    record = {
        "AssociationId": association_id,
        "PublicIp": public_ip,
        "DryRun": dry_run,
    }

    store.disassociate_addresss(record)

    return {
    }
```
