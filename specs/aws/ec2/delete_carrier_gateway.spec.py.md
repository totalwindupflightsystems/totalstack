---
id: "@specs/aws/ec2/delete_carrier_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteCarrierGateway"
---

# DeleteCarrierGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_carrier_gateway
> **spec:implements:** @kind:operation DeleteCarrierGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteCarrierGateway.spec.md

Deletes a carrier gateway. If you do not delete the route that contains the carrier gateway as the Target, the route is a blackhole route. For information about how to delete a route, see DeleteRoute .

## Input Shape: DeleteCarrierGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CarrierGatewayId | Any  # complex shape | ✓ | The ID of the carrier gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DeleteCarrierGatewayResult

- **CarrierGateway** (Any  # complex shape): Information about the carrier gateway.

## Implementation

```speclang
def delete_carrier_gateway(store, request: dict) -> dict:
    """Deletes a carrier gateway. If you do not delete the route that contains the carrier gateway as the Target, the route is a blackhole route. For information about how to delete a route, see DeleteRoute """
    carrier_gateway_id = request.get("CarrierGatewayId", "").strip() if isinstance(request.get("CarrierGatewayId"), str) else request.get("CarrierGatewayId")

    if not store.carrier_gateways(carrier_gateway_id):
        raise ResourceNotFoundException(f"Resource carrier_gateway_id not found")
    store.delete_carrier_gateways(carrier_gateway_id)
    return {}
```
