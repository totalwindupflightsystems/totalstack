---
id: "@specs/aws/ec2/describe_vpn_connections"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVpnConnections"
---

# DescribeVpnConnections

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_vpn_connections
> **spec:implements:** @kind:operation DescribeVpnConnections
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVpnConnections.spec.md

Describes one or more of your VPN connections. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: DescribeVpnConnectionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. customer-gateway-configuration - The configuration information for the customer gateway. customer-g |
| VpnConnectionIds | list[Any  # complex shape] |  | One or more VPN connection IDs. Default: Describes your VPN connections. |

## Output Shape: DescribeVpnConnectionsResult

- **VpnConnections** (list[Any  # complex shape]): Information about one or more VPN connections.

## Implementation

```speclang
def describe_vpn_connections(store, request: dict) -> dict:
    """Describes one or more of your VPN connections. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
