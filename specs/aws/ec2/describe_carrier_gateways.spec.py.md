---
id: "@specs/aws/ec2/describe_carrier_gateways"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCarrierGateways"
---

# DescribeCarrierGateways

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_carrier_gateways
> **spec:implements:** @kind:operation DescribeCarrierGateways
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCarrierGateways.spec.md

Describes one or more of your carrier gateways.

## Input Shape: DescribeCarrierGatewaysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CarrierGatewayIds | Any  # complex shape |  | One or more carrier gateway IDs. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. carrier-gateway-id - The ID of the carrier gateway. state - The state of the carrier gateway ( pend |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: DescribeCarrierGatewaysResult

- **CarrierGateways** (Any  # complex shape): Information about the carrier gateway.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_carrier_gateways(store, request: dict) -> dict:
    """Describes one or more of your carrier gateways."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
