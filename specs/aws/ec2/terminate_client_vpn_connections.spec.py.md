---
id: "@specs/aws/ec2/terminate_client_vpn_connections"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_TerminateClientVpnConnections"
---

# TerminateClientVpnConnections

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/terminate_client_vpn_connections
> **spec:implements:** @kind:operation TerminateClientVpnConnections
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_TerminateClientVpnConnections.spec.md

Terminates active Client VPN endpoint connections. This action can be used to terminate a specific client connection, or up to five connections established by a specific user.

## Input Shape: TerminateClientVpnConnectionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint to which the client is connected. |
| ConnectionId | str |  | The ID of the client connection to be terminated. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Username | str |  | The name of the user who initiated the connection. Use this option to terminate all active connections for the specified |

## Output Shape: TerminateClientVpnConnectionsResult

- **ClientVpnEndpointId** (str): The ID of the Client VPN endpoint.
- **ConnectionStatuses** (Any  # complex shape): The current state of the client connections.
- **Username** (str): The user who established the terminated client connections.

## Implementation

```speclang
def terminate_client_vpn_connections(store, request: dict) -> dict:
    """Terminates active Client VPN endpoint connections. This action can be used to terminate a specific client connection, or up to five connections established by a specific user."""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")

    if not store.terminate_client_vpn_connectionss(client_vpn_endpoint_id):
        raise ResourceNotFoundException(f"Resource client_vpn_endpoint_id not found")
    store.delete_terminate_client_vpn_connectionss(client_vpn_endpoint_id)
    return {}
```
