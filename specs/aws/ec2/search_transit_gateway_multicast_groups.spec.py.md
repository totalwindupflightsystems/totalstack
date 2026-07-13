---
id: "@specs/aws/ec2/search_transit_gateway_multicast_groups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_SearchTransitGatewayMulticastGroups"
---

# SearchTransitGatewayMulticastGroups

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/search_transit_gateway_multicast_groups
> **spec:implements:** @kind:operation SearchTransitGatewayMulticastGroups
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_SearchTransitGatewayMulticastGroups.spec.md

Searches one or more transit gateway multicast groups and returns the group membership information.

## Input Shape: SearchTransitGatewayMulticastGroupsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: group-ip-address - The IP address of the transit gateway multicast group.  |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayMulticastDomainId | Any  # complex shape | ✓ | The ID of the transit gateway multicast domain. |

## Output Shape: SearchTransitGatewayMulticastGroupsResult

- **MulticastGroups** (list[Any  # complex shape]): Information about the transit gateway multicast group.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def search_transit_gateway_multicast_groups(store, request: dict) -> dict:
    """Searches one or more transit gateway multicast groups and returns the group membership information."""
    transit_gateway_multicast_domain_id = request.get("TransitGatewayMulticastDomainId", "").strip() if isinstance(request.get("TransitGatewayMulticastDomainId"), str) else request.get("TransitGatewayMulticastDomainId")
    if not transit_gateway_multicast_domain_id:
        raise ValidationException("TransitGatewayMulticastDomainId is required")

    items = store.list_search_transit_gateway_multicast_groupss()
    return {"MulticastGroups": list(items.values())}
```
