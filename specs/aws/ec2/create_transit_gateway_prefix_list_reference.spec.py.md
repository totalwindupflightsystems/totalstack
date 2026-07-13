---
id: "@specs/aws/ec2/create_transit_gateway_prefix_list_reference"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayPrefixListReference"
---

# CreateTransitGatewayPrefixListReference

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_prefix_list_reference
> **spec:implements:** @kind:operation CreateTransitGatewayPrefixListReference
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayPrefixListReference.spec.md

Creates a reference (route) to a prefix list in a specified transit gateway route table.

## Input Shape: CreateTransitGatewayPrefixListReferenceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Blackhole | bool |  | Indicates whether to drop traffic that matches this route. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PrefixListId | Any  # complex shape | ✓ | The ID of the prefix list that is used for destination matches. |
| TransitGatewayAttachmentId | Any  # complex shape |  | The ID of the attachment to which traffic is routed. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: CreateTransitGatewayPrefixListReferenceResult

- **TransitGatewayPrefixListReference** (Any  # complex shape): Information about the prefix list reference.

## Implementation

```speclang
def create_transit_gateway_prefix_list_reference(store, request: dict) -> dict:
    """Creates a reference (route) to a prefix list in a specified transit gateway route table."""
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")
    if not prefix_list_id:
        raise ValidationException("PrefixListId is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    if store.transit_gateway_prefix_list_references(transit_gateway_route_table_id):
        raise ResourceInUseException(f"Resource transit_gateway_route_table_id already exists")

    record = {
        "TransitGatewayRouteTableId": transit_gateway_route_table_id,
        "PrefixListId": prefix_list_id,
        "TransitGatewayAttachmentId": transit_gateway_attachment_id,
        "Blackhole": blackhole,
        "DryRun": dry_run,
    }

    store.transit_gateway_prefix_list_references(transit_gateway_route_table_id, record)

    return {
        "TransitGatewayPrefixListReference": record.get("TransitGatewayPrefixListReference", {}),
    }
```
