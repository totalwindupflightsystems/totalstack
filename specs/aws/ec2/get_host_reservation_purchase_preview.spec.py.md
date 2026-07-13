---
id: "@specs/aws/ec2/get_host_reservation_purchase_preview"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetHostReservationPurchasePreview"
---

# GetHostReservationPurchasePreview

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_host_reservation_purchase_preview
> **spec:implements:** @kind:operation GetHostReservationPurchasePreview
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetHostReservationPurchasePreview.spec.md

Preview a reservation purchase with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This is a preview of the PurchaseHostReservation action and does not result in the offering being purchased.

## Input Shape: GetHostReservationPurchasePreviewRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| HostIdSet | Any  # complex shape | ✓ | The IDs of the Dedicated Hosts with which the reservation is associated. |
| OfferingId | Any  # complex shape | ✓ | The offering ID of the reservation. |

## Output Shape: GetHostReservationPurchasePreviewResult

- **CurrencyCode** (Any  # complex shape): The currency in which the totalUpfrontPrice and totalHourlyPrice amounts are specified. At this time, the only supported
- **Purchase** (Any  # complex shape): The purchase information of the Dedicated Host reservation and the Dedicated Hosts associated with it.
- **TotalHourlyPrice** (str): The potential total hourly price of the reservation per hour.
- **TotalUpfrontPrice** (str): The potential total upfront price. This is billed immediately.

## Implementation

```speclang
def get_host_reservation_purchase_preview(store, request: dict) -> dict:
    """Preview a reservation purchase with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This is a preview of"""
    host_id_set = request.get("HostIdSet", "").strip() if isinstance(request.get("HostIdSet"), str) else request.get("HostIdSet")
    if not host_id_set:
        raise ValidationException("HostIdSet is required")
    offering_id = request.get("OfferingId", "").strip() if isinstance(request.get("OfferingId"), str) else request.get("OfferingId")
    if not offering_id:
        raise ValidationException("OfferingId is required")

    resource = store.host_reservation_purchase_previews(host_id_set)
    if not resource:
        raise ResourceNotFoundException(f"Resource host_id_set not found")
    return {"HostIdSet": host_id_set, **resource}
```
