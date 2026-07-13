---
id: "@specs/aws/ec2/delete_traffic_mirror_target"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTrafficMirrorTarget"
---

# DeleteTrafficMirrorTarget

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_traffic_mirror_target
> **spec:implements:** @kind:operation DeleteTrafficMirrorTarget
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTrafficMirrorTarget.spec.md

Deletes the specified Traffic Mirror target. You cannot delete a Traffic Mirror target that is in use by a Traffic Mirror session.

## Input Shape: DeleteTrafficMirrorTargetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TrafficMirrorTargetId | Any  # complex shape | ✓ | The ID of the Traffic Mirror target. |

## Output Shape: DeleteTrafficMirrorTargetResult

- **TrafficMirrorTargetId** (str): The ID of the deleted Traffic Mirror target.

## Implementation

```speclang
def delete_traffic_mirror_target(store, request: dict) -> dict:
    """Deletes the specified Traffic Mirror target. You cannot delete a Traffic Mirror target that is in use by a Traffic Mirror session."""
    traffic_mirror_target_id = request.get("TrafficMirrorTargetId", "").strip() if isinstance(request.get("TrafficMirrorTargetId"), str) else request.get("TrafficMirrorTargetId")

    resource = store.traffic_mirror_targets(traffic_mirror_target_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource traffic_mirror_target_id not found")
    return {"TrafficMirrorTargetId": traffic_mirror_target_id, **resource}
```
