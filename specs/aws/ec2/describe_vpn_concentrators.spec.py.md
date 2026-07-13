---
id: "@specs/aws/ec2/describe_vpn_concentrators"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpnConcentrators"
---

# DescribeVpnConcentrators

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpn_concentrators
> **spec:implements:** @kind:operation DescribeVpnConcentrators
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpnConcentrators.spec.md

Describes one or more of your VPN concentrators.

## Input Shape: DescribeVpnConcentratorsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters to limit the results. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | Any  # complex shape |  | The token for the next page of results. |
| VpnConcentratorIds | list[Any  # complex shape] |  | One or more VPN concentrator IDs. |

## Output Shape: DescribeVpnConcentratorsResult

- **NextToken** (Any  # complex shape): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **VpnConcentrators** (list[Any  # complex shape]): Information about the VPN concentrators.

## Implementation

```speclang
def describe_vpn_concentrators(store, request: dict) -> dict:
    """Describes one or more of your VPN concentrators."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
