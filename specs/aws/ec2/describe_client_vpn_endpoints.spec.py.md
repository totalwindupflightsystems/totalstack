---
id: "@specs/aws/ec2/describe_client_vpn_endpoints"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeClientVpnEndpoints"
---

# DescribeClientVpnEndpoints

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_client_vpn_endpoints
> **spec:implements:** @kind:operation DescribeClientVpnEndpoints
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeClientVpnEndpoints.spec.md

Describes one or more Client VPN endpoints in the account.

## Input Shape: DescribeClientVpnEndpointsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointIds | list[Any  # complex shape] |  | The ID of the Client VPN endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. Filter names and values are case-sensitive. endpoint-id - The ID of the Client VPN endpoint. transp |
| MaxResults | Any  # complex shape |  | The maximum number of results to return for the request in a single page. The remaining results can be seen by sending a |
| NextToken | Any  # complex shape |  | The token to retrieve the next page of results. |

## Output Shape: DescribeClientVpnEndpointsResult

- **ClientVpnEndpoints** (Any  # complex shape): Information about the Client VPN endpoints.
- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_client_vpn_endpoints(store, request: dict) -> dict:
    """Describes one or more Client VPN endpoints in the account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
