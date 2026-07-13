---
id: "@specs/aws/ec2/delete_client_vpn_endpoint"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteClientVpnEndpoint"
---

# DeleteClientVpnEndpoint

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_client_vpn_endpoint
> **spec:implements:** @kind:operation DeleteClientVpnEndpoint
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteClientVpnEndpoint.spec.md

Deletes the specified Client VPN endpoint. You must disassociate all target networks before you can delete a Client VPN endpoint.

## Input Shape: DeleteClientVpnEndpointRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN to be deleted. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DeleteClientVpnEndpointResult

- **Status** (Any  # complex shape): The current state of the Client VPN endpoint.

## Implementation

```speclang
def delete_client_vpn_endpoint(store, request: dict) -> dict:
    """Deletes the specified Client VPN endpoint. You must disassociate all target networks before you can delete a Client VPN endpoint."""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")

    if not store.client_vpn_endpoints(client_vpn_endpoint_id):
        raise ResourceNotFoundException(f"Resource client_vpn_endpoint_id not found")
    store.delete_client_vpn_endpoints(client_vpn_endpoint_id)
    return {}
```
