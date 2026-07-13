---
id: "@specs/aws/ec2/accept_transit_gateway_multicast_domain_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AcceptTransitGatewayMulticastDomainAssociations"
---

# AcceptTransitGatewayMulticastDomainAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/accept_transit_gateway_multicast_domain_associations
> **spec:implements:** @kind:operation AcceptTransitGatewayMulticastDomainAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AcceptTransitGatewayMulticastDomainAssociations.spec.md

Accepts a request to associate subnets with a transit gateway multicast domain.

## Input Shape: AcceptTransitGatewayMulticastDomainAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SubnetIds | list[str] |  | The IDs of the subnets to associate with the transit gateway multicast domain. |
| TransitGatewayAttachmentId | Any  # complex shape |  | The ID of the transit gateway attachment. |
| TransitGatewayMulticastDomainId | Any  # complex shape |  | The ID of the transit gateway multicast domain. |

## Output Shape: AcceptTransitGatewayMulticastDomainAssociationsResult

- **Associations** (Any  # complex shape): Information about the multicast domain associations.

## Implementation

```speclang
def accept_transit_gateway_multicast_domain_associations(store, request: dict) -> dict:
    """Accepts a request to associate subnets with a transit gateway multicast domain."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AcceptTransitGatewayMulticastDomainAssociations", request)
```
