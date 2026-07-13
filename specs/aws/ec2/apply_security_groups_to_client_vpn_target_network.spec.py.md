---
id: "@specs/aws/ec2/apply_security_groups_to_client_vpn_target_network"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ApplySecurityGroupsToClientVpnTargetNetwork"
---

# ApplySecurityGroupsToClientVpnTargetNetwork

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/apply_security_groups_to_client_vpn_target_network
> **spec:implements:** @kind:operation ApplySecurityGroupsToClientVpnTargetNetwork
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ApplySecurityGroupsToClientVpnTargetNetwork.spec.md

Applies a security group to the association between the target network and the Client VPN endpoint. This action replaces the existing security groups with the specified security groups.

## Input Shape: ApplySecurityGroupsToClientVpnTargetNetworkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientVpnEndpointId | Any  # complex shape | ✓ | The ID of the Client VPN endpoint. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SecurityGroupIds | Any  # complex shape | ✓ | The IDs of the security groups to apply to the associated target network. Up to 5 security groups can be applied to an a |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC in which the associated target network is located. |

## Output Shape: ApplySecurityGroupsToClientVpnTargetNetworkResult

- **SecurityGroupIds** (Any  # complex shape): The IDs of the applied security groups.

## Implementation

```speclang
def apply_security_groups_to_client_vpn_target_network(store, request: dict) -> dict:
    """Applies a security group to the association between the target network and the Client VPN endpoint. This action replaces the existing security groups with the specified security groups."""
    client_vpn_endpoint_id = request.get("ClientVpnEndpointId", "").strip() if isinstance(request.get("ClientVpnEndpointId"), str) else request.get("ClientVpnEndpointId")
    if not client_vpn_endpoint_id:
        raise ValidationException("ClientVpnEndpointId is required")
    security_group_ids = request.get("SecurityGroupIds", "").strip() if isinstance(request.get("SecurityGroupIds"), str) else request.get("SecurityGroupIds")
    if not security_group_ids:
        raise ValidationException("SecurityGroupIds is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.apply_security_groups_to_client_vpn_target_networks(security_group_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource security_group_ids not found")
    return {"SecurityGroupIds": security_group_ids, **resource}
```
