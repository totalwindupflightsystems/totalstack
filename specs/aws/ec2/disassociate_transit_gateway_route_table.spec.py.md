---
id: "@specs/aws/ec2/disassociate_transit_gateway_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateTransitGatewayRouteTable"
---

# DisassociateTransitGatewayRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_transit_gateway_route_table
> **spec:implements:** @kind:operation DisassociateTransitGatewayRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateTransitGatewayRouteTable.spec.md

Disassociates a resource attachment from a transit gateway route table.

## Input Shape: DisassociateTransitGatewayRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the attachment. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: DisassociateTransitGatewayRouteTableResult

- **Association** (Any  # complex shape): Information about the association.

## Implementation

```speclang
def disassociate_transit_gateway_route_table(store, request: dict) -> dict:
    """Disassociates a resource attachment from a transit gateway route table."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateTransitGatewayRouteTable", request)
```
