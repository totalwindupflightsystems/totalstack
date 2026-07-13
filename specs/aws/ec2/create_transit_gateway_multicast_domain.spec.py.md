---
id: "@specs/aws/ec2/create_transit_gateway_multicast_domain"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayMulticastDomain"
---

# CreateTransitGatewayMulticastDomain

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_multicast_domain
> **spec:implements:** @kind:operation CreateTransitGatewayMulticastDomain
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayMulticastDomain.spec.md

Creates a multicast domain using the specified transit gateway. The transit gateway must be in the available state before you create a domain. Use DescribeTransitGateways to see the state of transit gateway.

## Input Shape: CreateTransitGatewayMulticastDomainRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape |  | The options for the transit gateway multicast domain. |
| TagSpecifications | list[Any  # complex shape] |  | The tags for the transit gateway multicast domain. |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway. |

## Output Shape: CreateTransitGatewayMulticastDomainResult

- **TransitGatewayMulticastDomain** (Any  # complex shape): Information about the transit gateway multicast domain.

## Implementation

```speclang
def create_transit_gateway_multicast_domain(store, request: dict) -> dict:
    """Creates a multicast domain using the specified transit gateway. The transit gateway must be in the available state before you create a domain. Use DescribeTransitGateways to see the state of transit g"""
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")
    if not transit_gateway_id:
        raise ValidationException("TransitGatewayId is required")

    if store.transit_gateway_multicast_domains(transit_gateway_id):
        raise ResourceInUseException(f"Resource transit_gateway_id already exists")

    record = {
        "TransitGatewayId": transit_gateway_id,
        "Options": options,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_multicast_domains(transit_gateway_id, record)

    return {
        "TransitGatewayMulticastDomain": record.get("TransitGatewayMulticastDomain", {}),
    }
```
