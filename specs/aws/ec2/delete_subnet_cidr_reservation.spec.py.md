---
id: "@specs/aws/ec2/delete_subnet_cidr_reservation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteSubnetCidrReservation"
---

# DeleteSubnetCidrReservation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_subnet_cidr_reservation
> **spec:implements:** @kind:operation DeleteSubnetCidrReservation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteSubnetCidrReservation.spec.md

Deletes a subnet CIDR reservation.

## Input Shape: DeleteSubnetCidrReservationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SubnetCidrReservationId | Any  # complex shape | ✓ | The ID of the subnet CIDR reservation. |

## Output Shape: DeleteSubnetCidrReservationResult

- **DeletedSubnetCidrReservation** (Any  # complex shape): Information about the deleted subnet CIDR reservation.

## Implementation

```speclang
def delete_subnet_cidr_reservation(store, request: dict) -> dict:
    """Deletes a subnet CIDR reservation."""
    subnet_cidr_reservation_id = request.get("SubnetCidrReservationId", "").strip() if isinstance(request.get("SubnetCidrReservationId"), str) else request.get("SubnetCidrReservationId")

    if not store.subnet_cidr_reservations(subnet_cidr_reservation_id):
        raise ResourceNotFoundException(f"Resource subnet_cidr_reservation_id not found")
    store.delete_subnet_cidr_reservations(subnet_cidr_reservation_id)
    return {}
```
