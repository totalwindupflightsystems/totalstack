---
id: "@specs/aws/ec2/describe_transit_gateway_metering_policies"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeTransitGatewayMeteringPolicies"
---

# DescribeTransitGatewayMeteringPolicies

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_transit_gateway_metering_policies
> **spec:implements:** @kind:operation DescribeTransitGatewayMeteringPolicies
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeTransitGatewayMeteringPolicies.spec.md

Describes one or more transit gateway metering policies.

## Input Shape: DescribeTransitGatewayMeteringPoliciesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters to apply when describing transit gateway metering policies. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayMeteringPolicyIds | list[Any  # complex shape] |  | The IDs of the transit gateway metering policies to describe. |

## Output Shape: DescribeTransitGatewayMeteringPoliciesResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayMeteringPolicies** (list[Any  # complex shape]): Information about the transit gateway metering policies.

## Implementation

```speclang
def describe_transit_gateway_metering_policies(store, request: dict) -> dict:
    """Describes one or more transit gateway metering policies."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
