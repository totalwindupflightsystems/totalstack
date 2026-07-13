---
id: "@specs/aws/ec2/modify_traffic_mirror_session"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyTrafficMirrorSession"
---

# ModifyTrafficMirrorSession

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_traffic_mirror_session
> **spec:implements:** @kind:operation ModifyTrafficMirrorSession
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyTrafficMirrorSession.spec.md

Modifies a Traffic Mirror session.

## Input Shape: ModifyTrafficMirrorSessionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | The description to assign to the Traffic Mirror session. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PacketLength | int |  | The number of bytes in each packet to mirror. These are bytes after the VXLAN header. To mirror a subset, set this to th |
| RemoveFields | list[Any  # complex shape] |  | The properties that you want to remove from the Traffic Mirror session. When you remove a property from a Traffic Mirror |
| SessionNumber | int |  | The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions.  |
| TrafficMirrorFilterId | Any  # complex shape |  | The ID of the Traffic Mirror filter. |
| TrafficMirrorSessionId | Any  # complex shape | ✓ | The ID of the Traffic Mirror session. |
| TrafficMirrorTargetId | Any  # complex shape |  | The Traffic Mirror target. The target must be in the same VPC as the source, or have a VPC peering connection with the s |
| VirtualNetworkId | int |  | The virtual network ID of the Traffic Mirror session. |

## Output Shape: ModifyTrafficMirrorSessionResult

- **TrafficMirrorSession** (Any  # complex shape): Information about the Traffic Mirror session.

## Implementation

```speclang
def modify_traffic_mirror_session(store, request: dict) -> dict:
    """Modifies a Traffic Mirror session."""
    traffic_mirror_session_id = request.get("TrafficMirrorSessionId", "").strip() if isinstance(request.get("TrafficMirrorSessionId"), str) else request.get("TrafficMirrorSessionId")
    if not traffic_mirror_session_id:
        raise ValidationException("TrafficMirrorSessionId is required")

    resource = store.traffic_mirror_sessions(traffic_mirror_session_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource traffic_mirror_session_id not found")

    # Update mutable fields
    if "TrafficMirrorTargetId" in request:
        resource["TrafficMirrorTargetId"] = traffic_mirror_target_id
    if "TrafficMirrorFilterId" in request:
        resource["TrafficMirrorFilterId"] = traffic_mirror_filter_id
    if "PacketLength" in request:
        resource["PacketLength"] = packet_length
    if "SessionNumber" in request:
        resource["SessionNumber"] = session_number
    if "VirtualNetworkId" in request:
        resource["VirtualNetworkId"] = virtual_network_id
    if "Description" in request:
        resource["Description"] = description
    if "RemoveFields" in request:
        resource["RemoveFields"] = remove_fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.traffic_mirror_sessions(traffic_mirror_session_id, resource)
    return resource
```
