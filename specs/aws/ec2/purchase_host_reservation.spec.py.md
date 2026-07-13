---
id: "@specs/aws/ec2/purchase_host_reservation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_PurchaseHostReservation"
---

# PurchaseHostReservation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/purchase_host_reservation
> **spec:implements:** @kind:operation PurchaseHostReservation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_PurchaseHostReservation.spec.md

Purchase a reservation with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This action results in the specified reservation being purchased and charged to your account.

## Input Shape: PurchaseHostReservationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| CurrencyCode | Any  # complex shape |  | The currency in which the totalUpfrontPrice , LimitPrice , and totalHourlyPrice amounts are specified. At this time, the |
| HostIdSet | Any  # complex shape | ✓ | The IDs of the Dedicated Hosts with which the reservation will be associated. |
| LimitPrice | str |  | The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront c |
| OfferingId | Any  # complex shape | ✓ | The ID of the offering. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the Dedicated Host Reservation during purchase. |

## Output Shape: PurchaseHostReservationResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E
- **CurrencyCode** (Any  # complex shape): The currency in which the totalUpfrontPrice and totalHourlyPrice amounts are specified. At this time, the only supported
- **Purchase** (Any  # complex shape): Describes the details of the purchase.
- **TotalHourlyPrice** (str): The total hourly price of the reservation calculated per hour.
- **TotalUpfrontPrice** (str): The total amount charged to your account when you purchase the reservation.

## Implementation

```speclang
def purchase_host_reservation(store, request: dict) -> dict:
    """Purchase a reservation with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This action results in the s"""
    host_id_set = request.get("HostIdSet", "").strip() if isinstance(request.get("HostIdSet"), str) else request.get("HostIdSet")
    if not host_id_set:
        raise ValidationException("HostIdSet is required")
    offering_id = request.get("OfferingId", "").strip() if isinstance(request.get("OfferingId"), str) else request.get("OfferingId")
    if not offering_id:
        raise ValidationException("OfferingId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PurchaseHostReservation", request)
```
