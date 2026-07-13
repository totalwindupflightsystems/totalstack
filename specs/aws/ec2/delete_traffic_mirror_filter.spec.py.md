---
id: "@specs/aws/ec2/delete_traffic_mirror_filter"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTrafficMirrorFilter"
---

# DeleteTrafficMirrorFilter

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_traffic_mirror_filter
> **spec:implements:** @kind:operation DeleteTrafficMirrorFilter
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTrafficMirrorFilter.spec.md

Deletes the specified Traffic Mirror filter. You cannot delete a Traffic Mirror filter that is in use by a Traffic Mirror session.

## Input Shape: DeleteTrafficMirrorFilterRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TrafficMirrorFilterId | Any  # complex shape | ✓ | The ID of the Traffic Mirror filter. |

## Output Shape: DeleteTrafficMirrorFilterResult

- **TrafficMirrorFilterId** (str): The ID of the Traffic Mirror filter.

## Implementation

```speclang
def delete_traffic_mirror_filter(store, request: dict) -> dict:
    """Deletes the specified Traffic Mirror filter. You cannot delete a Traffic Mirror filter that is in use by a Traffic Mirror session."""
    traffic_mirror_filter_id = request.get("TrafficMirrorFilterId", "").strip() if isinstance(request.get("TrafficMirrorFilterId"), str) else request.get("TrafficMirrorFilterId")

    if not store.traffic_mirror_filters(traffic_mirror_filter_id):
        raise ResourceNotFoundException(f"Resource traffic_mirror_filter_id not found")
    store.delete_traffic_mirror_filters(traffic_mirror_filter_id)
    return {}
```
