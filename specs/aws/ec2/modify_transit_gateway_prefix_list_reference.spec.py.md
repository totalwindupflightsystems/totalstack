---
id: "@specs/aws/ec2/modify_transit_gateway_prefix_list_reference"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyTransitGatewayPrefixListReference"
---

# ModifyTransitGatewayPrefixListReference

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_transit_gateway_prefix_list_reference
> **spec:implements:** @kind:operation ModifyTransitGatewayPrefixListReference
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyTransitGatewayPrefixListReference.spec.md

Modifies a reference (route) to a prefix list in a specified transit gateway route table.

## Input Shape: ModifyTransitGatewayPrefixListReferenceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Blackhole | bool |  | Indicates whether to drop traffic that matches this route. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PrefixListId | Any  # complex shape | ✓ | The ID of the prefix list. |
| TransitGatewayAttachmentId | Any  # complex shape |  | The ID of the attachment to which traffic is routed. |
| TransitGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the transit gateway route table. |

## Output Shape: ModifyTransitGatewayPrefixListReferenceResult

- **TransitGatewayPrefixListReference** (Any  # complex shape): Information about the prefix list reference.

## Implementation

```speclang
def modify_transit_gateway_prefix_list_reference(store, request: dict) -> dict:
    """Modifies a reference (route) to a prefix list in a specified transit gateway route table."""
    prefix_list_id = request.get("PrefixListId", "").strip() if isinstance(request.get("PrefixListId"), str) else request.get("PrefixListId")
    if not prefix_list_id:
        raise ValidationException("PrefixListId is required")
    transit_gateway_route_table_id = request.get("TransitGatewayRouteTableId", "").strip() if isinstance(request.get("TransitGatewayRouteTableId"), str) else request.get("TransitGatewayRouteTableId")
    if not transit_gateway_route_table_id:
        raise ValidationException("TransitGatewayRouteTableId is required")

    items = store.list_transit_gateway_prefix_list_references()
    return {"TransitGatewayPrefixListReference": list(items.values())}
```
