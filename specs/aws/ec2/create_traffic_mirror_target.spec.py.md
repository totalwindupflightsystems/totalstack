---
id: "@specs/aws/ec2/create_traffic_mirror_target"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTrafficMirrorTarget"
---

# CreateTrafficMirrorTarget

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_traffic_mirror_target
> **spec:implements:** @kind:operation CreateTrafficMirrorTarget
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTrafficMirrorTarget.spec.md

Creates a target for your Traffic Mirror session. A Traffic Mirror target is the destination for mirrored traffic. The Traffic Mirror source and the Traffic Mirror target (monitoring appliances) can be in the same VPC, or in different VPCs connected via VPC peering or a transit gateway. A Traffic Mirror target can be a network interface, a Network Load Balancer, or a Gateway Load Balancer endpoint. To use the target in a Traffic Mirror session, use CreateTrafficMirrorSession .

## Input Shape: CreateTrafficMirrorTargetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H |
| Description | str |  | The description of the Traffic Mirror target. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GatewayLoadBalancerEndpointId | Any  # complex shape |  | The ID of the Gateway Load Balancer endpoint. |
| NetworkInterfaceId | Any  # complex shape |  | The network interface ID that is associated with the target. |
| NetworkLoadBalancerArn | str |  | The Amazon Resource Name (ARN) of the Network Load Balancer that is associated with the target. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the Traffic Mirror target. |

## Output Shape: CreateTrafficMirrorTargetResult

- **ClientToken** (str): Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see H
- **TrafficMirrorTarget** (Any  # complex shape): Information about the Traffic Mirror target.

## Implementation

```speclang
def create_traffic_mirror_target(store, request: dict) -> dict:
    """Creates a target for your Traffic Mirror session. A Traffic Mirror target is the destination for mirrored traffic. The Traffic Mirror source and the Traffic Mirror target (monitoring appliances) can b"""


    record = {
        "NetworkInterfaceId": network_interface_id,
        "NetworkLoadBalancerArn": network_load_balancer_arn,
        "Description": description,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "ClientToken": client_token,
        "GatewayLoadBalancerEndpointId": gateway_load_balancer_endpoint_id,
    }

    store.traffic_mirror_targets(record)

    return {
        "TrafficMirrorTarget": record.get("TrafficMirrorTarget", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
