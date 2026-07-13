---
id: "@specs/aws/ec2/accept_capacity_reservation_billing_ownership"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptCapacityReservationBillingOwnership"
---

# AcceptCapacityReservationBillingOwnership

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_capacity_reservation_billing_ownership
> **spec:implements:** @kind:operation AcceptCapacityReservationBillingOwnership
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptCapacityReservationBillingOwnership.spec.md

Accepts a request to assign billing of the available capacity of a shared Capacity Reservation to your account. For more information, see Billing assignment for shared Amazon EC2 Capacity Reservations .

## Input Shape: AcceptCapacityReservationBillingOwnershipRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityReservationId | Any  # complex shape | ✓ | The ID of the Capacity Reservation for which to accept the request. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: AcceptCapacityReservationBillingOwnershipResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def accept_capacity_reservation_billing_ownership(store, request: dict) -> dict:
    """Accepts a request to assign billing of the available capacity of a shared Capacity Reservation to your account. For more information, see Billing assignment for shared Amazon EC2 Capacity Reservations"""
    capacity_reservation_id = request.get("CapacityReservationId", "").strip() if isinstance(request.get("CapacityReservationId"), str) else request.get("CapacityReservationId")
    if not capacity_reservation_id:
        raise ValidationException("CapacityReservationId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AcceptCapacityReservationBillingOwnership", request)
```
