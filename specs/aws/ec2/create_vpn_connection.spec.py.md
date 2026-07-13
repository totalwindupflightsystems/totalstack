---
id: "@specs/aws/ec2/create_vpn_connection"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpnConnection"
---

# CreateVpnConnection

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpn_connection
> **spec:implements:** @kind:operation CreateVpnConnection
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpnConnection.spec.md

Creates a VPN connection between an existing virtual private gateway or transit gateway and a customer gateway. The supported connection type is ipsec.1 . The response includes information that you need to give to your network administrator to configure your customer gateway. We strongly recommend that you use HTTPS when calling this operation because the response contains sensitive cryptographic information for configuring your customer gateway device. If you decide to shut down your VPN connection for any reason and later create a new VPN connection, you must reconfigure your customer gateway with the new information returned from this call. This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesn't return an error. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: CreateVpnConnectionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CustomerGatewayId | Any  # complex shape | ✓ | The ID of the customer gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape |  | The options for the VPN connection. |
| PreSharedKeyStorage | str |  | Specifies the storage mode for the pre-shared key (PSK). Valid values are Standard " (stored in the Site-to-Site VPN ser |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the VPN connection. |
| TransitGatewayId | Any  # complex shape |  | The ID of the transit gateway. If you specify a transit gateway, you cannot specify a virtual private gateway. |
| Type | str | ✓ | The type of VPN connection ( ipsec.1 ). |
| VpnConcentratorId | Any  # complex shape |  | The ID of the VPN concentrator to associate with the VPN connection. |
| VpnGatewayId | Any  # complex shape |  | The ID of the virtual private gateway. If you specify a virtual private gateway, you cannot specify a transit gateway. |

## Output Shape: CreateVpnConnectionResult

- **VpnConnection** (Any  # complex shape): Information about the VPN connection.

## Implementation

```speclang
def create_vpn_connection(store, request: dict) -> dict:
    """Creates a VPN connection between an existing virtual private gateway or transit gateway and a customer gateway. The supported connection type is ipsec.1 . The response includes information that you ne"""
    customer_gateway_id = request.get("CustomerGatewayId", "").strip() if isinstance(request.get("CustomerGatewayId"), str) else request.get("CustomerGatewayId")
    if not customer_gateway_id:
        raise ValidationException("CustomerGatewayId is required")
    type = request.get("Type", "").strip() if isinstance(request.get("Type"), str) else request.get("Type")
    if not type:
        raise ValidationException("Type is required")

    if store.vpn_connections(customer_gateway_id):
        raise ResourceInUseException(f"Resource customer_gateway_id already exists")

    record = {
        "CustomerGatewayId": customer_gateway_id,
        "Type": type,
        "VpnGatewayId": vpn_gateway_id,
        "TransitGatewayId": transit_gateway_id,
        "VpnConcentratorId": vpn_concentrator_id,
        "TagSpecifications": tag_specifications,
        "PreSharedKeyStorage": pre_shared_key_storage,
        "DryRun": dry_run,
        "Options": options,
    }

    store.vpn_connections(customer_gateway_id, record)

    return {
        "VpnConnection": record.get("VpnConnection", {}),
    }
```
