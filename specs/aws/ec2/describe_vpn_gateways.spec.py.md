---
id: "@specs/aws/ec2/describe_vpn_gateways"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpnGateways"
---

# DescribeVpnGateways

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpn_gateways
> **spec:implements:** @kind:operation DescribeVpnGateways
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpnGateways.spec.md

Describes one or more of your virtual private gateways. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: DescribeVpnGatewaysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. amazon-side-asn - The Autonomous System Number (ASN) for the Amazon side of the gateway. attachment |
| VpnGatewayIds | list[Any  # complex shape] |  | One or more virtual private gateway IDs. Default: Describes all your virtual private gateways. |

## Output Shape: DescribeVpnGatewaysResult

- **VpnGateways** (list[Any  # complex shape]): Information about one or more virtual private gateways.

## Implementation

```speclang
def describe_vpn_gateways(store, request: dict) -> dict:
    """Describes one or more of your virtual private gateways. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
