---
id: "@specs/aws/ec2/describe_transit_gateway_multicast_domains"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTransitGatewayMulticastDomains"
---

# DescribeTransitGatewayMulticastDomains

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_transit_gateway_multicast_domains
> **spec:implements:** @kind:operation DescribeTransitGatewayMulticastDomains
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTransitGatewayMulticastDomains.spec.md

Describes one or more transit gateway multicast domains.

## Input Shape: DescribeTransitGatewayMulticastDomainsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: state - The state of the transit gateway multicast domain. Valid values ar |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayMulticastDomainIds | list[Any  # complex shape] |  | The ID of the transit gateway multicast domain. |

## Output Shape: DescribeTransitGatewayMulticastDomainsResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayMulticastDomains** (list[Any  # complex shape]): Information about the transit gateway multicast domains.

## Implementation

```speclang
def describe_transit_gateway_multicast_domains(store, request: dict) -> dict:
    """Describes one or more transit gateway multicast domains."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
