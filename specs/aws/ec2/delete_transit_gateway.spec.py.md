---
id: "@specs/aws/ec2/delete_transit_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGateway"
---

# DeleteTransitGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway
> **spec:implements:** @kind:operation DeleteTransitGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGateway.spec.md

Deletes the specified transit gateway.

## Input Shape: DeleteTransitGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway. |

## Output Shape: DeleteTransitGatewayResult

- **TransitGateway** (Any  # complex shape): Information about the deleted transit gateway.

## Implementation

```speclang
def delete_transit_gateway(store, request: dict) -> dict:
    """Deletes the specified transit gateway."""
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")

    if not store.transit_gateways(transit_gateway_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_id not found")
    store.delete_transit_gateways(transit_gateway_id)
    return {}
```
