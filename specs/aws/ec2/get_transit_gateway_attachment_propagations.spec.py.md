---
id: "@specs/aws/ec2/get_transit_gateway_attachment_propagations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetTransitGatewayAttachmentPropagations"
---

# GetTransitGatewayAttachmentPropagations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_transit_gateway_attachment_propagations
> **spec:implements:** @kind:operation GetTransitGatewayAttachmentPropagations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetTransitGatewayAttachmentPropagations.spec.md

Lists the route tables to which the specified resource attachment propagates routes.

## Input Shape: GetTransitGatewayAttachmentPropagationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: transit-gateway-route-table-id - The ID of the transit gateway route table |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the attachment. |

## Output Shape: GetTransitGatewayAttachmentPropagationsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayAttachmentPropagations** (list[Any  # complex shape]): Information about the propagation route tables.

## Implementation

```speclang
def get_transit_gateway_attachment_propagations(store, request: dict) -> dict:
    """Lists the route tables to which the specified resource attachment propagates routes."""
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")

    resource = store.transit_gateway_attachment_propagationss(transit_gateway_attachment_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_attachment_id not found")
    return {"TransitGatewayAttachmentId": transit_gateway_attachment_id, **resource}
```
