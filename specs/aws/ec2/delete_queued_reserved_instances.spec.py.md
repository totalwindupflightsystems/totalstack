---
id: "@specs/aws/ec2/delete_queued_reserved_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteQueuedReservedInstances"
---

# DeleteQueuedReservedInstances

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_queued_reserved_instances
> **spec:implements:** @kind:operation DeleteQueuedReservedInstances
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteQueuedReservedInstances.spec.md

Deletes the queued purchases for the specified Reserved Instances.

## Input Shape: DeleteQueuedReservedInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ReservedInstancesIds | list[Any  # complex shape] | ✓ | The IDs of the Reserved Instances. |

## Output Shape: DeleteQueuedReservedInstancesResult

- **FailedQueuedPurchaseDeletions** (Any  # complex shape): Information about the queued purchases that could not be deleted.
- **SuccessfulQueuedPurchaseDeletions** (Any  # complex shape): Information about the queued purchases that were successfully deleted.

## Implementation

```speclang
def delete_queued_reserved_instances(store, request: dict) -> dict:
    """Deletes the queued purchases for the specified Reserved Instances."""
    reserved_instances_ids = request.get("ReservedInstancesIds", "").strip() if isinstance(request.get("ReservedInstancesIds"), str) else request.get("ReservedInstancesIds")

    if not store.queued_reserved_instancess(reserved_instances_ids):
        raise ResourceNotFoundException(f"Resource reserved_instances_ids not found")
    store.delete_queued_reserved_instancess(reserved_instances_ids)
    return {}
```
