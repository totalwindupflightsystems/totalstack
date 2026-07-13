---
id: "@specs/aws/ec2/create_subnet_cidr_reservation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSubnetCidrReservation"
---

# CreateSubnetCidrReservation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_subnet_cidr_reservation
> **spec:implements:** @kind:operation CreateSubnetCidrReservation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSubnetCidrReservation.spec.md

Creates a subnet CIDR reservation. For more information, see Subnet CIDR reservations in the Amazon VPC User Guide and Manage prefixes for your network interfaces in the Amazon EC2 User Guide .

## Input Shape: CreateSubnetCidrReservationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | The IPv4 or IPV6 CIDR range to reserve. |
| Description | str |  | The description to assign to the subnet CIDR reservation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReservationType | Any  # complex shape | ✓ | The type of reservation. The reservation type determines how the reserved IP addresses are assigned to resources. prefix |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the subnet CIDR reservation. |

## Output Shape: CreateSubnetCidrReservationResult

- **SubnetCidrReservation** (Any  # complex shape): Information about the created subnet CIDR reservation.

## Implementation

```speclang
def create_subnet_cidr_reservation(store, request: dict) -> dict:
    """Creates a subnet CIDR reservation. For more information, see Subnet CIDR reservations in the Amazon VPC User Guide and Manage prefixes for your network interfaces in the Amazon EC2 User Guide ."""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    if not cidr:
        raise ValidationException("Cidr is required")
    reservation_type = request.get("ReservationType", "").strip() if isinstance(request.get("ReservationType"), str) else request.get("ReservationType")
    if not reservation_type:
        raise ValidationException("ReservationType is required")
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    if store.subnet_cidr_reservations(cidr):
        raise ResourceInUseException(f"Resource cidr already exists")

    record = {
        "SubnetId": subnet_id,
        "Cidr": cidr,
        "ReservationType": reservation_type,
        "Description": description,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
    }

    store.subnet_cidr_reservations(cidr, record)

    return {
        "SubnetCidrReservation": record.get("SubnetCidrReservation", {}),
    }
```
