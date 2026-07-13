---
id: "@specs/aws/ec2/purchase_scheduled_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_PurchaseScheduledInstances"
---

# PurchaseScheduledInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/purchase_scheduled_instances
> **spec:implements:** @kind:operation PurchaseScheduledInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_PurchaseScheduledInstances.spec.md

You can no longer purchase Scheduled Instances. Purchases the Scheduled Instances with the specified schedule. Scheduled Instances enable you to purchase Amazon EC2 compute capacity by the hour for a one-year term. Before you can purchase a Scheduled Instance, you must call DescribeScheduledInstanceAvailability to check for available schedules and obtain a purchase token. After you purchase a Scheduled Instance, you must call RunScheduledInstances during each scheduled time period. After you purchase a Scheduled Instance, you can't cancel, modify, or resell your purchase.

## Input Shape: PurchaseScheduledInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see Ensuring Idempo |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PurchaseRequests | Any  # complex shape | ✓ | The purchase requests. |

## Output Shape: PurchaseScheduledInstancesResult

- **ScheduledInstanceSet** (Any  # complex shape): Information about the Scheduled Instances.

## Implementation

```speclang
def purchase_scheduled_instances(store, request: dict) -> dict:
    """You can no longer purchase Scheduled Instances. Purchases the Scheduled Instances with the specified schedule. Scheduled Instances enable you to purchase Amazon EC2 compute capacity by the hour for a """
    purchase_requests = request.get("PurchaseRequests", "").strip() if isinstance(request.get("PurchaseRequests"), str) else request.get("PurchaseRequests")
    if not purchase_requests:
        raise ValidationException("PurchaseRequests is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("PurchaseScheduledInstances", request)
```
