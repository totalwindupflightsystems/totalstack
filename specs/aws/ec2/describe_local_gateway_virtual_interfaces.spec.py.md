---
id: "@specs/aws/ec2/describe_local_gateway_virtual_interfaces"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeLocalGatewayVirtualInterfaces"
---

# DescribeLocalGatewayVirtualInterfaces

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_local_gateway_virtual_interfaces
> **spec:implements:** @kind:operation DescribeLocalGatewayVirtualInterfaces
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeLocalGatewayVirtualInterfaces.spec.md

Describes the specified local gateway virtual interfaces.

## Input Shape: DescribeLocalGatewayVirtualInterfacesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. local-address - The local address. local-bgp-asn - The Border Gateway Protocol (BGP) Autonomous Sys |
| LocalGatewayVirtualInterfaceIds | Any  # complex shape |  | The IDs of the virtual interfaces. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: DescribeLocalGatewayVirtualInterfacesResult

- **LocalGatewayVirtualInterfaces** (Any  # complex shape): Information about the virtual interfaces.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_local_gateway_virtual_interfaces(store, request: dict) -> dict:
    """Describes the specified local gateway virtual interfaces."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
