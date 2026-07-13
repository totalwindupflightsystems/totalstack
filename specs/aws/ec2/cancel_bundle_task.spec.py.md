---
id: "@specs/aws/ec2/cancel_bundle_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CancelBundleTask"
---

# CancelBundleTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/cancel_bundle_task
> **spec:implements:** @kind:operation CancelBundleTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CancelBundleTask.spec.md

Cancels a bundling operation for an instance store-backed Windows instance.

## Input Shape: CancelBundleTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BundleId | Any  # complex shape | ✓ | The ID of the bundle task. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: CancelBundleTaskResult

- **BundleTask** (Any  # complex shape): Information about the bundle task.

## Implementation

```speclang
def cancel_bundle_task(store, request: dict) -> dict:
    """Cancels a bundling operation for an instance store-backed Windows instance."""
    bundle_id = request.get("BundleId", "").strip() if isinstance(request.get("BundleId"), str) else request.get("BundleId")

    if not store.bundle_tasks(bundle_id):
        raise ResourceNotFoundException(f"Resource bundle_id not found")
    store.delete_bundle_tasks(bundle_id)
    return {}
```
