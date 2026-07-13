---
id: "@specs/aws/ec2/disassociate_client_vpn_target_network"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisassociateClientVpnTargetNetwork"
---

# DisassociateClientVpnTargetNetwork

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disassociate_client_vpn_target_network
> **spec:implements:** @kind:operation DisassociateClientVpnTargetNetwork
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisassociateClientVpnTargetNetwork.spec.md

Disassociates a target network from the specified Client VPN endpoint. When you disassociate the last target network from a Client VPN, the following happens: The route that was automatically added for the VPC is deleted All active client connections are terminated New client connections are disallowed The Client VPN endpoint's status changes to pending-associate

## Input Shape: DisassociateClientVpnTargetNetworkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AssociationId | str | ✓ | The ID of the target network association. |
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint from which to disassociate the target network. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DisassociateClientVpnTargetNetworkResult

- **AssociationId** (str): The ID of the target network association.
- **Status** (Any  # complex shape): The current state of the target network association.

## Implementation

```speclang
def disassociate_client_vpn_target_network(store, request: dict) -> dict:
    """Disassociates a target network from the specified Client VPN endpoint. When you disassociate the last target network from a Client VPN, the following happens: The route that was automatically added fo"""
    association_id = request.get("AssociationId", "").strip() if isinstance(request.get("AssociationId"), str) else request.get("AssociationId")
    if not association_id:
        raise ValidationException("AssociationId is required")
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")

    resource = store.disassociate_client_vpn_target_networks(association_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource association_id not found")
    return {"AssociationId": association_id, **resource}
```
