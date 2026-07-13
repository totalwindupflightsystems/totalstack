---
id: "@specs/aws/ec2/delete_traffic_mirror_session"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTrafficMirrorSession"
---

# DeleteTrafficMirrorSession

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_traffic_mirror_session
> **spec:implements:** @kind:operation DeleteTrafficMirrorSession
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTrafficMirrorSession.spec.md

Deletes the specified Traffic Mirror session.

## Input Shape: DeleteTrafficMirrorSessionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TrafficMirrorSessionId | Any  # complex shape | ✓ | The ID of the Traffic Mirror session. |

## Output Shape: DeleteTrafficMirrorSessionResult

- **TrafficMirrorSessionId** (str): The ID of the deleted Traffic Mirror session.

## Implementation

```speclang
def delete_traffic_mirror_session(store, request: dict) -> dict:
    """Deletes the specified Traffic Mirror session."""
    traffic_mirror_session_id = request.get("TrafficMirrorSessionId", "").strip() if isinstance(request.get("TrafficMirrorSessionId"), str) else request.get("TrafficMirrorSessionId")

    if not store.traffic_mirror_sessions(traffic_mirror_session_id):
        raise ResourceNotFoundException(f"Resource traffic_mirror_session_id not found")
    store.delete_traffic_mirror_sessions(traffic_mirror_session_id)
    return {}
```
