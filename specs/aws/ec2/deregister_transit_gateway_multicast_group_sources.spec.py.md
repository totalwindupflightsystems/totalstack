---
id: "@specs/aws/ec2/deregister_transit_gateway_multicast_group_sources"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeregisterTransitGatewayMulticastGroupSources"
---

# DeregisterTransitGatewayMulticastGroupSources

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deregister_transit_gateway_multicast_group_sources
> **spec:implements:** @kind:operation DeregisterTransitGatewayMulticastGroupSources
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeregisterTransitGatewayMulticastGroupSources.spec.md

Deregisters the specified sources (network interfaces) from the transit gateway multicast group.

## Input Shape: DeregisterTransitGatewayMulticastGroupSourcesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupIpAddress | str |  | The IP address assigned to the transit gateway multicast group. |
| NetworkInterfaceIds | list[Any  # complex shape] |  | The IDs of the group sources' network interfaces. |
| TransitGatewayMulticastDomainId | Any  # complex shape |  | The ID of the transit gateway multicast domain. |

## Output Shape: DeregisterTransitGatewayMulticastGroupSourcesResult

- **DeregisteredMulticastGroupSources** (Any  # complex shape): Information about the deregistered group sources.

## Implementation

```speclang
def deregister_transit_gateway_multicast_group_sources(store, request: dict) -> dict:
    """Deregisters the specified sources (network interfaces) from the transit gateway multicast group."""


    record = {
        "TransitGatewayMulticastDomainId": transit_gateway_multicast_domain_id,
        "GroupIpAddress": group_ip_address,
        "NetworkInterfaceIds": network_interface_ids,
        "DryRun": dry_run,
    }

    store.deregister_transit_gateway_multicast_group_sourcess(record)

    return {
        "DeregisteredMulticastGroupSources": record.get("DeregisteredMulticastGroupSources", {}),
    }
```
