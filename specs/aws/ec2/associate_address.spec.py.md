---
id: "@specs/aws/ec2/associate_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateAddress"
---

# AssociateAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_address
> **spec:implements:** @kind:operation AssociateAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateAddress.spec.md

Associates an Elastic IP address, or carrier IP address (for instances that are in subnets in Wavelength Zones) with an instance or a network interface. Before you can use an Elastic IP address, you must allocate it to your account. If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance. If you associate an Elastic IP address with an instance that has an existing Elastic IP address, the existing address is disassociated from the instance, but remains allocated to your account. [Subnets in Wavelength Zones] You can associate an IP address from the telecommunication carrier to the instance or network interface. You cannot associate an Elastic IP address with an interface in a different network border group. This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error, and you may be charged for each time the Elastic IP address is remapped to the same instance. For more information, see the Elastic IP Addresses section of Amazon EC2 Pricing .

## Input Shape: AssociateAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationId | Any  # complex shape |  | The allocation ID. This is required. |
| AllowReassociation | bool |  | Reassociation is automatic, but you can specify false to ensure the operation fails if the Elastic IP address is already |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape |  | The ID of the instance. The instance must have exactly one attached network interface. You can specify either the instan |
| NetworkInterfaceId | Any  # complex shape |  | The ID of the network interface. If the instance has more than one network interface, you must specify a network interfa |
| PrivateIpAddress | str |  | The primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specif |
| PublicIp | Any  # complex shape |  | Deprecated. |

## Output Shape: AssociateAddressResult

- **AssociationId** (str): The ID that represents the association of the Elastic IP address with an instance.

## Implementation

```speclang
def associate_address(store, request: dict) -> dict:
    """Associates an Elastic IP address, or carrier IP address (for instances that are in subnets in Wavelength Zones) with an instance or a network interface. Before you can use an Elastic IP address, you m"""


    record = {
        "AllocationId": allocation_id,
        "InstanceId": instance_id,
        "PublicIp": public_ip,
        "DryRun": dry_run,
        "NetworkInterfaceId": network_interface_id,
        "PrivateIpAddress": private_ip_address,
        "AllowReassociation": allow_reassociation,
    }

    store.associate_addresss(record)

    return {
        "AssociationId": record.get("AssociationId", {}),
    }
```
