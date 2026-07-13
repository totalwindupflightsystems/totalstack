---
id: "@specs/aws/ec2/register_transit_gateway_multicast_group_members"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RegisterTransitGatewayMulticastGroupMembers"
---

# RegisterTransitGatewayMulticastGroupMembers

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/register_transit_gateway_multicast_group_members
> **spec:implements:** @kind:operation RegisterTransitGatewayMulticastGroupMembers
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RegisterTransitGatewayMulticastGroupMembers.spec.md

Registers members (network interfaces) with the transit gateway multicast group. A member is a network interface associated with a supported EC2 instance that receives multicast traffic. For more information, see Multicast on transit gateways in the Amazon Web Services Transit Gateways Guide . After you add the members, use SearchTransitGatewayMulticastGroups to verify that the members were added to the transit gateway multicast group.

## Input Shape: RegisterTransitGatewayMulticastGroupMembersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupIpAddress | str |  | The IP address assigned to the transit gateway multicast group. |
| NetworkInterfaceIds | list[Any  # complex shape] | ✓ | The group members' network interface IDs to register with the transit gateway multicast group. |
| TransitGatewayMulticastDomainId | Any  # complex shape | ✓ | The ID of the transit gateway multicast domain. |

## Output Shape: RegisterTransitGatewayMulticastGroupMembersResult

- **RegisteredMulticastGroupMembers** (Any  # complex shape): Information about the registered transit gateway multicast group members.

## Implementation

```speclang
def register_transit_gateway_multicast_group_members(store, request: dict) -> dict:
    """Registers members (network interfaces) with the transit gateway multicast group. A member is a network interface associated with a supported EC2 instance that receives multicast traffic. For more info"""
    network_interface_ids = request.get("NetworkInterfaceIds", "").strip() if isinstance(request.get("NetworkInterfaceIds"), str) else request.get("NetworkInterfaceIds")
    if not network_interface_ids:
        raise ValidationException("NetworkInterfaceIds is required")
    transit_gateway_multicast_domain_id = request.get("TransitGatewayMulticastDomainId", "").strip() if isinstance(request.get("TransitGatewayMulticastDomainId"), str) else request.get("TransitGatewayMulticastDomainId")
    if not transit_gateway_multicast_domain_id:
        raise ValidationException("TransitGatewayMulticastDomainId is required")

    if store.register_transit_gateway_multicast_group_memberss(network_interface_ids):
        raise ResourceInUseException(f"Resource network_interface_ids already exists")

    record = {
        "TransitGatewayMulticastDomainId": transit_gateway_multicast_domain_id,
        "GroupIpAddress": group_ip_address,
        "NetworkInterfaceIds": network_interface_ids,
        "DryRun": dry_run,
    }

    store.register_transit_gateway_multicast_group_memberss(network_interface_ids, record)

    return {
        "RegisteredMulticastGroupMembers": record.get("RegisteredMulticastGroupMembers", {}),
    }
```
