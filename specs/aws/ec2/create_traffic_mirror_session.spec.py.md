---
id: "@specs/aws/ec2/create_traffic_mirror_session"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTrafficMirrorSession"
---

# CreateTrafficMirrorSession

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_traffic_mirror_session
> **spec:implements:** @kind:operation CreateTrafficMirrorSession
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTrafficMirrorSession.spec.md

Creates a Traffic Mirror session. A Traffic Mirror session actively copies packets from a Traffic Mirror source to a Traffic Mirror target. Create a filter, and then assign it to the session to define a subset of the traffic to mirror, for example all TCP traffic. The Traffic Mirror source and the Traffic Mirror target (monitoring appliances) can be in the same VPC, or in a different VPC connected via VPC peering or a transit gateway. By default, no traffic is mirrored. Use CreateTrafficMirrorFilter to create filter rules that specify the traffic to mirror.

## Input Shape: CreateTrafficMirrorSessionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| Description | str |  | The description of the Traffic Mirror session. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the source network interface. |
| PacketLength | int |  | The number of bytes in each packet to mirror. These are bytes after the VXLAN header. Do not specify this parameter when |
| SessionNumber | int | ✓ | The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions.  |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to a Traffic Mirror session. |
| TrafficMirrorFilterId | Any  # complex shape | ✓ | The ID of the Traffic Mirror filter. |
| TrafficMirrorTargetId | Any  # complex shape | ✓ | The ID of the Traffic Mirror target. |
| VirtualNetworkId | int |  | The VXLAN ID for the Traffic Mirror session. For more information about the VXLAN protocol, see RFC 7348 . If you do not |

## Output Shape: CreateTrafficMirrorSessionResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H
- **TrafficMirrorSession** (Any  # complex shape): Information about the Traffic Mirror session.

## Implementation

```speclang
def create_traffic_mirror_session(store, request: dict) -> dict:
    """Creates a Traffic Mirror session. A Traffic Mirror session actively copies packets from a Traffic Mirror source to a Traffic Mirror target. Create a filter, and then assign it to the session to define"""
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")
    session_number = request.get("SessionNumber", "").strip() if isinstance(request.get("SessionNumber"), str) else request.get("SessionNumber")
    if not session_number:
        raise ValidationException("SessionNumber is required")
    traffic_mirror_filter_id = request.get("TrafficMirrorFilterId", "").strip() if isinstance(request.get("TrafficMirrorFilterId"), str) else request.get("TrafficMirrorFilterId")
    if not traffic_mirror_filter_id:
        raise ValidationException("TrafficMirrorFilterId is required")
    traffic_mirror_target_id = request.get("TrafficMirrorTargetId", "").strip() if isinstance(request.get("TrafficMirrorTargetId"), str) else request.get("TrafficMirrorTargetId")
    if not traffic_mirror_target_id:
        raise ValidationException("TrafficMirrorTargetId is required")

    if store.traffic_mirror_sessions(traffic_mirror_target_id):
        raise ResourceInUseException(f"Resource traffic_mirror_target_id already exists")

    record = {
        "NetworkInterfaceId": network_interface_id,
        "TrafficMirrorTargetId": traffic_mirror_target_id,
        "TrafficMirrorFilterId": traffic_mirror_filter_id,
        "PacketLength": packet_length,
        "SessionNumber": session_number,
        "VirtualNetworkId": virtual_network_id,
        "Description": description,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "ClientToken": client_token,
    }

    store.traffic_mirror_sessions(traffic_mirror_target_id, record)

    return {
        "TrafficMirrorSession": record.get("TrafficMirrorSession", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
