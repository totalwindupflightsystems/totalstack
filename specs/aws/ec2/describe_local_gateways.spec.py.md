---
id: "@specs/aws/ec2/describe_local_gateways"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeLocalGateways"
---

# DescribeLocalGateways

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_local_gateways
> **spec:implements:** @kind:operation DescribeLocalGateways
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeLocalGateways.spec.md

Describes one or more local gateways. By default, all local gateways are described. Alternatively, you can filter the results.

## Input Shape: DescribeLocalGatewaysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. local-gateway-id - The ID of a local gateway. outpost-arn - The Amazon Resource Name (ARN) of the O |
| LocalGatewayIds | Any  # complex shape |  | The IDs of the local gateways. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |

## Output Shape: DescribeLocalGatewaysResult

- **LocalGateways** (Any  # complex shape): Information about the local gateways.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def describe_local_gateways(store, request: dict) -> dict:
    """Describes one or more local gateways. By default, all local gateways are described. Alternatively, you can filter the results."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
