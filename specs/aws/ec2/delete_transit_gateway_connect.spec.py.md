---
id: "@specs/aws/ec2/delete_transit_gateway_connect"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayConnect"
---

# DeleteTransitGatewayConnect

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_connect
> **spec:implements:** @kind:operation DeleteTransitGatewayConnect
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayConnect.spec.md

Deletes the specified Connect attachment. You must first delete any Connect peers for the attachment.

## Input Shape: DeleteTransitGatewayConnectRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the Connect attachment. |

## Output Shape: DeleteTransitGatewayConnectResult

- **TransitGatewayConnect** (Any  # complex shape): Information about the deleted Connect attachment.

## Implementation

```speclang
def delete_transit_gateway_connect(store, request: dict) -> dict:
    """Deletes the specified Connect attachment. You must first delete any Connect peers for the attachment."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")

    if not store.transit_gateway_connects(transit_gateway_attachment_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_attachment_id not found")
    store.delete_transit_gateway_connects(transit_gateway_attachment_id)
    return {}
```
