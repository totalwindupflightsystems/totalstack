---
id: "@specs/aws/ec2/enable_vgw_route_propagation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableVgwRoutePropagation"
---

# EnableVgwRoutePropagation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_vgw_route_propagation
> **spec:implements:** @kind:operation EnableVgwRoutePropagation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableVgwRoutePropagation.spec.md

Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC.

## Input Shape: EnableVgwRoutePropagationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GatewayId | Any  # complex shape | ✓ | The ID of the virtual private gateway that is attached to a VPC. The virtual private gateway must be attached to the sam |
| RouteTableId | Any  # complex shape | ✓ | The ID of the route table. The routing table must be associated with the same VPC that the virtual private gateway is at |

## Implementation

```speclang
def enable_vgw_route_propagation(store, request: dict) -> dict:
    """Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC."""
    gateway_id = request.get("GatewayId", "").strip() if isinstance(request.get("GatewayId"), str) else request.get("GatewayId")
    if not gateway_id:
        raise ValidationException("GatewayId is required")
    route_table_id = request.get("RouteTableId", "").strip() if isinstance(request.get("RouteTableId"), str) else request.get("RouteTableId")
    if not route_table_id:
        raise ValidationException("RouteTableId is required")

    resource = store.enable_vgw_route_propagations(route_table_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource route_table_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_vgw_route_propagations(route_table_id, resource)
    return resource
```
