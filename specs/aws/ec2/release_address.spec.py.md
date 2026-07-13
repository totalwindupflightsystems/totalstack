---
id: "@specs/aws/ec2/release_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ReleaseAddress"
---

# ReleaseAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/release_address
> **spec:implements:** @kind:operation ReleaseAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ReleaseAddress.spec.md

Releases the specified Elastic IP address. [Default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it's associated with. Alternatively, you can disassociate an Elastic IP address without releasing it. [Nondefault VPC] You must disassociate the Elastic IP address before you can release it. Otherwise, Amazon EC2 returns an error ( InvalidIPAddress.InUse ). After releasing an Elastic IP address, it is released to the IP address pool. Be sure to update your DNS records and any servers or devices that communicate with the address. If you attempt to release an Elastic IP address that you already released, you'll get an AuthFailure error if the address is already allocated to another Amazon Web Services account. After you release an Elastic IP address, you might be able to recover it. For more information, see Release an Elastic IP address .

## Input Shape: ReleaseAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationId | Any  # complex shape |  | The allocation ID. This parameter is required. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkBorderGroup | str |  | The set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.  |
| PublicIp | str |  | Deprecated. |

## Implementation

```speclang
def release_address(store, request: dict) -> dict:
    """Releases the specified Elastic IP address. [Default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it's associated with. Alternatively, you can disassociate"""


    record = {
        "AllocationId": allocation_id,
        "PublicIp": public_ip,
        "NetworkBorderGroup": network_border_group,
        "DryRun": dry_run,
    }

    store.release_addresss(record)

    return {
    }
```
