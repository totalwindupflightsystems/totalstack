---
id: "@specs/aws/ec2/disassociate_transit_gateway_multicast_domain"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateTransitGatewayMulticastDomain"
---

# DisassociateTransitGatewayMulticastDomain

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_transit_gateway_multicast_domain
> **spec:implements:** @kind:operation DisassociateTransitGatewayMulticastDomain
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateTransitGatewayMulticastDomain.spec.md

Disassociates the specified subnets from the transit gateway multicast domain.

## Input Shape: DisassociateTransitGatewayMulticastDomainRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SubnetIds | list[Any  # complex shape] | ✓ | The IDs of the subnets; |
| TransitGatewayAttachmentId | Any  # complex shape | ✓ | The ID of the attachment. |
| TransitGatewayMulticastDomainId | Any  # complex shape | ✓ | The ID of the transit gateway multicast domain. |

## Output Shape: DisassociateTransitGatewayMulticastDomainResult

- **Associations** (Any  # complex shape): Information about the association.

## Implementation

```speclang
def disassociate_transit_gateway_multicast_domain(store, request: dict) -> dict:
    """Disassociates the specified subnets from the transit gateway multicast domain."""
    subnet_ids = request.get("SubnetIds", "").strip() if isinstance(request.get("SubnetIds"), str) else request.get("SubnetIds")
    if not subnet_ids:
        raise ValidationException("SubnetIds is required")
    transit_gateway_attachment_id = request.get("TransitGatewayAttachmentId", "").strip() if isinstance(request.get("TransitGatewayAttachmentId"), str) else request.get("TransitGatewayAttachmentId")
    if not transit_gateway_attachment_id:
        raise ValidationException("TransitGatewayAttachmentId is required")
    transit_gateway_multicast_domain_id = request.get("TransitGatewayMulticastDomainId", "").strip() if isinstance(request.get("TransitGatewayMulticastDomainId"), str) else request.get("TransitGatewayMulticastDomainId")
    if not transit_gateway_multicast_domain_id:
        raise ValidationException("TransitGatewayMulticastDomainId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DisassociateTransitGatewayMulticastDomain", request)
```
