---
id: "@specs/aws/ec2/delete_transit_gateway_multicast_domain"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayMulticastDomain"
---

# DeleteTransitGatewayMulticastDomain

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_multicast_domain
> **spec:implements:** @kind:operation DeleteTransitGatewayMulticastDomain
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayMulticastDomain.spec.md

Deletes the specified transit gateway multicast domain.

## Input Shape: DeleteTransitGatewayMulticastDomainRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayMulticastDomainId | Any  # complex shape | ✓ | The ID of the transit gateway multicast domain. |

## Output Shape: DeleteTransitGatewayMulticastDomainResult

- **TransitGatewayMulticastDomain** (Any  # complex shape): Information about the deleted transit gateway multicast domain.

## Implementation

```speclang
def delete_transit_gateway_multicast_domain(store, request: dict) -> dict:
    """Deletes the specified transit gateway multicast domain."""
    transit_gateway_multicast_domain_id = request.get("TransitGatewayMulticastDomainId", "").strip() if isinstance(request.get("TransitGatewayMulticastDomainId"), str) else request.get("TransitGatewayMulticastDomainId")

    if not store.transit_gateway_multicast_domains(transit_gateway_multicast_domain_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_multicast_domain_id not found")
    store.delete_transit_gateway_multicast_domains(transit_gateway_multicast_domain_id)
    return {}
```
