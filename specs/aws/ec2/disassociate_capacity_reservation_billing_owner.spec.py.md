---
id: "@specs/aws/ec2/disassociate_capacity_reservation_billing_owner"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateCapacityReservationBillingOwner"
---

# DisassociateCapacityReservationBillingOwner

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_capacity_reservation_billing_owner
> **spec:implements:** @kind:operation DisassociateCapacityReservationBillingOwner
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateCapacityReservationBillingOwner.spec.md

Cancels a pending request to assign billing of the unused capacity of a Capacity Reservation to a consumer account, or revokes a request that has already been accepted. For more information, see Billing assignment for shared Amazon EC2 Capacity Reservations .

## Input Shape: DisassociateCapacityReservationBillingOwnerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| UnusedReservationBillingOwnerId | Any  # complex shape | ✓ | The ID of the consumer account to which the request was sent. |

## Output Shape: DisassociateCapacityReservationBillingOwnerResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disassociate_capacity_reservation_billing_owner(store, request: dict) -> dict:
    """Cancels a pending request to assign billing of the unused capacity of a Capacity Reservation to a consumer account, or revokes a request that has already been accepted. For more information, see Billi"""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")
    unused_reservation_billing_owner_id = request.get("UnusedReservationBillingOwnerId", "").strip() if isinstance(request.get("UnusedReservationBillingOwnerId"), str) else request.get("UnusedReservationBillingOwnerId")
    if not unused_reservation_billing_owner_id:
        raise ValidationException("UnusedReservationBillingOwnerId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateCapacityReservationBillingOwner", request)
```
