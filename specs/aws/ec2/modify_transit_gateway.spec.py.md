---
id: "@specs/aws/ec2/modify_transit_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyTransitGateway"
---

# ModifyTransitGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_transit_gateway
> **spec:implements:** @kind:operation ModifyTransitGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyTransitGateway.spec.md

Modifies the specified transit gateway. When you modify a transit gateway, the modified options are applied to new transit gateway attachments only. Your existing transit gateway attachments are not modified.

## Input Shape: ModifyTransitGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | The description for the transit gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape |  | The options to modify. |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway. |

## Output Shape: ModifyTransitGatewayResult

- **TransitGateway** (Any  # complex shape): Information about the transit gateway.

## Implementation

```speclang
def modify_transit_gateway(store, request: dict) -> dict:
    """Modifies the specified transit gateway. When you modify a transit gateway, the modified options are applied to new transit gateway attachments only. Your existing transit gateway attachments are not m"""
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")
    if not transit_gateway_id:
        raise ValidationException("TransitGatewayId is required")

    resource = store.transit_gateways(transit_gateway_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_id not found")

    # Update mutable fields
    if "Description" in request:
        resource["Description"] = description
    if "Options" in request:
        resource["Options"] = options
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.transit_gateways(transit_gateway_id, resource)
    return resource
```
