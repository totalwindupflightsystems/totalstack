---
id: "@specs/aws/ec2/delete_client_vpn_route"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteClientVpnRoute"
---

# DeleteClientVpnRoute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_client_vpn_route
> **spec:implements:** @kind:operation DeleteClientVpnRoute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteClientVpnRoute.spec.md

Deletes a route from a Client VPN endpoint. You can only delete routes that you manually added using the CreateClientVpnRoute action. You cannot delete routes that were automatically added when associating a subnet. To remove routes that have been automatically added, disassociate the target subnet from the Client VPN endpoint.

## Input Shape: DeleteClientVpnRouteRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint from which the route is to be deleted. |
| DestinationCidrBlock | str | ✓ | The IPv4 address range, in CIDR notation, of the route to be deleted. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TargetVpcSubnetId | Any  # complex shape |  | The ID of the target subnet used by the route. |

## Output Shape: DeleteClientVpnRouteResult

- **Status** (Any  # complex shape): The current state of the route.

## Implementation

```speclang
def delete_client_vpn_route(store, request: dict) -> dict:
    """Deletes a route from a Client VPN endpoint. You can only delete routes that you manually added using the CreateClientVpnRoute action. You cannot delete routes that were automatically added when associ"""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    destination_cidr_block = request.get("DestinationCidrBlock", "").strip() if isinstance(request.get("DestinationCidrBlock"), str) else request.get("DestinationCidrBlock")

    if not store.client_vpn_routes(destination_cidr_block):
        raise ResourceNotFoundException(f"Resource destination_cidr_block not found")
    store.delete_client_vpn_routes(destination_cidr_block)
    return {}
```
