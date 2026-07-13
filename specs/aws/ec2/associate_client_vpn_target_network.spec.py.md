---
id: "@specs/aws/ec2/associate_client_vpn_target_network"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateClientVpnTargetNetwork"
---

# AssociateClientVpnTargetNetwork

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_client_vpn_target_network
> **spec:implements:** @kind:operation AssociateClientVpnTargetNetwork
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateClientVpnTargetNetwork.spec.md

Associates a target network with a Client VPN endpoint. A target network is a subnet in a VPC. You can associate multiple subnets from the same VPC with a Client VPN endpoint. You can associate only one subnet in each Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy. If you specified a VPC when you created the Client VPN endpoint or if you have previous subnet associations, the specified subnet must be in the same VPC. To specify a subnet that's in a different VPC, you must first modify the Client VPN endpoint ( ModifyClientVpnEndpoint ) and change the VPC that's associated with it.

## Input Shape: AssociateClientVpnTargetNetworkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet to associate with the Client VPN endpoint. |

## Output Shape: AssociateClientVpnTargetNetworkResult

- **AssociationId** (str): The unique ID of the target network association.
- **Status** (Any  # complex shape): The current state of the target network association.

## Implementation

```speclang
def associate_client_vpn_target_network(store, request: dict) -> dict:
    """Associates a target network with a Client VPN endpoint. A target network is a subnet in a VPC. You can associate multiple subnets from the same VPC with a Client VPN endpoint. You can associate only o"""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    resource = store.associate_client_vpn_target_networks(subnet_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource subnet_id not found")
    return {"SubnetId": subnet_id, **resource}
```
