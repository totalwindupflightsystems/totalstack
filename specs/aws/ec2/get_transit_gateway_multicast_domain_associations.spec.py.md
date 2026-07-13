---
id: "@specs/aws/ec2/get_transit_gateway_multicast_domain_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetTransitGatewayMulticastDomainAssociations"
---

# GetTransitGatewayMulticastDomainAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_transit_gateway_multicast_domain_associations
> **spec:implements:** @kind:operation GetTransitGatewayMulticastDomainAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetTransitGatewayMulticastDomainAssociations.spec.md

Gets information about the associations for the transit gateway multicast domain.

## Input Shape: GetTransitGatewayMulticastDomainAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: resource-id - The ID of the resource. resource-type - The type of resource |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayMulticastDomainId | Any  # complex shape | ✓ | The ID of the transit gateway multicast domain. |

## Output Shape: GetTransitGatewayMulticastDomainAssociationsResult

- **MulticastDomainAssociations** (list[Any  # complex shape]): Information about the multicast domain associations.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_transit_gateway_multicast_domain_associations(store, request: dict) -> dict:
    """Gets information about the associations for the transit gateway multicast domain."""
    transit_gateway_multicast_domain_id = request.get("TransitGatewayMulticastDomainId", "").strip() if isinstance(request.get("TransitGatewayMulticastDomainId"), str) else request.get("TransitGatewayMulticastDomainId")
    if not transit_gateway_multicast_domain_id:
        raise ValidationException("TransitGatewayMulticastDomainId is required")

    resource = store.transit_gateway_multicast_domain_associationss(transit_gateway_multicast_domain_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_multicast_domain_id not found")
    return {"TransitGatewayMulticastDomainId": transit_gateway_multicast_domain_id, **resource}
```
