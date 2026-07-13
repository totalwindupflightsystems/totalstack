---
id: "@specs/aws/ec2/modify_traffic_mirror_filter_network_services"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyTrafficMirrorFilterNetworkServices"
---

# ModifyTrafficMirrorFilterNetworkServices

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_traffic_mirror_filter_network_services
> **spec:implements:** @kind:operation ModifyTrafficMirrorFilterNetworkServices
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyTrafficMirrorFilterNetworkServices.spec.md

Allows or restricts mirroring network services. By default, Amazon DNS network services are not eligible for Traffic Mirror. Use AddNetworkServices to add network services to a Traffic Mirror filter. When a network service is added to the Traffic Mirror filter, all traffic related to that network service will be mirrored. When you no longer want to mirror network services, use RemoveNetworkServices to remove the network services from the Traffic Mirror filter.

## Input Shape: ModifyTrafficMirrorFilterNetworkServicesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AddNetworkServices | list[Any  # complex shape] |  | The network service, for example Amazon DNS, that you want to mirror. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| RemoveNetworkServices | list[Any  # complex shape] |  | The network service, for example Amazon DNS, that you no longer want to mirror. |
| TrafficMirrorFilterId | Any  # complex shape | ✓ | The ID of the Traffic Mirror filter. |

## Output Shape: ModifyTrafficMirrorFilterNetworkServicesResult

- **TrafficMirrorFilter** (Any  # complex shape): The Traffic Mirror filter that the network service is associated with.

## Implementation

```speclang
def modify_traffic_mirror_filter_network_services(store, request: dict) -> dict:
    """Allows or restricts mirroring network services. By default, Amazon DNS network services are not eligible for Traffic Mirror. Use AddNetworkServices to add network services to a Traffic Mirror filter. """
    traffic_mirror_filter_id = request.get("TrafficMirrorFilterId", "").strip() if isinstance(request.get("TrafficMirrorFilterId"), str) else request.get("TrafficMirrorFilterId")
    if not traffic_mirror_filter_id:
        raise ValidationException("TrafficMirrorFilterId is required")

    resource = store.traffic_mirror_filter_network_servicess(traffic_mirror_filter_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource traffic_mirror_filter_id not found")

    # Update mutable fields
    if "AddNetworkServices" in request:
        resource["AddNetworkServices"] = add_network_services
    if "RemoveNetworkServices" in request:
        resource["RemoveNetworkServices"] = remove_network_services
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.traffic_mirror_filter_network_servicess(traffic_mirror_filter_id, resource)
    return resource
```
