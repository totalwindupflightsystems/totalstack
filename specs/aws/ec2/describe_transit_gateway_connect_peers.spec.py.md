---
id: "@specs/aws/ec2/describe_transit_gateway_connect_peers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTransitGatewayConnectPeers"
---

# DescribeTransitGatewayConnectPeers

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_transit_gateway_connect_peers
> **spec:implements:** @kind:operation DescribeTransitGatewayConnectPeers
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTransitGatewayConnectPeers.spec.md

Describes one or more Connect peers.

## Input Shape: DescribeTransitGatewayConnectPeersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. The possible values are: state - The state of the Connect peer ( pending | available | deleting | d |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayConnectPeerIds | list[Any  # complex shape] |  | The IDs of the Connect peers. |

## Output Shape: DescribeTransitGatewayConnectPeersResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayConnectPeers** (list[Any  # complex shape]): Information about the Connect peers.

## Implementation

```speclang
def describe_transit_gateway_connect_peers(store, request: dict) -> dict:
    """Describes one or more Connect peers."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
