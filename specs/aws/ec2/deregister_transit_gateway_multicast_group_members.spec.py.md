---
id: "@specs/aws/ec2/deregister_transit_gateway_multicast_group_members"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeregisterTransitGatewayMulticastGroupMembers"
---

# DeregisterTransitGatewayMulticastGroupMembers

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deregister_transit_gateway_multicast_group_members
> **spec:implements:** @kind:operation DeregisterTransitGatewayMulticastGroupMembers
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeregisterTransitGatewayMulticastGroupMembers.spec.md

Deregisters the specified members (network interfaces) from the transit gateway multicast group.

## Input Shape: DeregisterTransitGatewayMulticastGroupMembersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupIpAddress | str |  | The IP address assigned to the transit gateway multicast group. |
| NetworkInterfaceIds | list[Any  # complex shape] |  | The IDs of the group members' network interfaces. |
| TransitGatewayMulticastDomainId | Any  # complex shape |  | The ID of the transit gateway multicast domain. |

## Output Shape: DeregisterTransitGatewayMulticastGroupMembersResult

- **DeregisteredMulticastGroupMembers** (Any  # complex shape): Information about the deregistered members.

## Implementation

```speclang
def deregister_transit_gateway_multicast_group_members(store, request: dict) -> dict:
    """Deregisters the specified members (network interfaces) from the transit gateway multicast group."""


    record = {
        "TransitGatewayMulticastDomainId": transit_gateway_multicast_domain_id,
        "GroupIpAddress": group_ip_address,
        "NetworkInterfaceIds": network_interface_ids,
        "DryRun": dry_run,
    }

    store.deregister_transit_gateway_multicast_group_memberss(record)

    return {
        "DeregisteredMulticastGroupMembers": record.get("DeregisteredMulticastGroupMembers", {}),
    }
```
