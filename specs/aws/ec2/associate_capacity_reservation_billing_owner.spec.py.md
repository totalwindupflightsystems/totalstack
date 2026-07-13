---
id: "@specs/aws/ec2/associate_capacity_reservation_billing_owner"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateCapacityReservationBillingOwner"
---

# AssociateCapacityReservationBillingOwner

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_capacity_reservation_billing_owner
> **spec:implements:** @kind:operation AssociateCapacityReservationBillingOwner
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateCapacityReservationBillingOwner.spec.md

Initiates a request to assign billing of the unused capacity of a shared Capacity Reservation to a consumer account that is consolidated under the same Amazon Web Services organizations payer account. For more information, see Billing assignment for shared Amazon EC2 Capacity Reservations .

## Input Shape: AssociateCapacityReservationBillingOwnerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| UnusedReservationBillingOwnerId | Any  # complex shape | ✓ | The ID of the consumer account to which to assign billing. |

## Output Shape: AssociateCapacityReservationBillingOwnerResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def associate_capacity_reservation_billing_owner(store, request: dict) -> dict:
    """Initiates a request to assign billing of the unused capacity of a shared Capacity Reservation to a consumer account that is consolidated under the same Amazon Web Services organizations payer account."""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")
    unused_reservation_billing_owner_id = request.get("UnusedReservationBillingOwnerId", "").strip() if isinstance(request.get("UnusedReservationBillingOwnerId"), str) else request.get("UnusedReservationBillingOwnerId")
    if not unused_reservation_billing_owner_id:
        raise ValidationException("UnusedReservationBillingOwnerId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateCapacityReservationBillingOwner", request)
```
