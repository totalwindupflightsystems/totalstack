---
id: "@specs/aws/ec2/create_transit_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGateway"
---

# CreateTransitGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway
> **spec:implements:** @kind:operation CreateTransitGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGateway.spec.md

Creates a transit gateway. You can use a transit gateway to interconnect your virtual private clouds (VPC) and on-premises networks. After the transit gateway enters the available state, you can attach your VPCs and VPN connections to the transit gateway. To attach your VPCs, use CreateTransitGatewayVpcAttachment . To attach a VPN connection, use CreateCustomerGateway to create a customer gateway and specify the ID of the customer gateway and the ID of the transit gateway in a call to CreateVpnConnection . When you create a transit gateway, we create a default transit gateway route table and use it as the default association route table and the default propagation route table. You can use CreateTransitGatewayRouteTable to create additional transit gateway route tables. If you disable automatic route propagation, we do not create a default transit gateway route table. You can use EnableTransitGatewayRouteTablePropagation to propagate routes from a resource attachment to a transit gateway route table. If you disable automatic associations, you can use AssociateTransitGatewayRouteTable to associate a resource attachment with a transit gateway route table.

## Input Shape: CreateTransitGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | A description of the transit gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Options | Any  # complex shape |  | The transit gateway options. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the transit gateway. |

## Output Shape: CreateTransitGatewayResult

- **TransitGateway** (Any  # complex shape): Information about the transit gateway.

## Implementation

```speclang
def create_transit_gateway(store, request: dict) -> dict:
    """Creates a transit gateway. You can use a transit gateway to interconnect your virtual private clouds (VPC) and on-premises networks. After the transit gateway enters the available state, you can attac"""


    record = {
        "Description": description,
        "Options": options,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateways(record)

    return {
        "TransitGateway": record.get("TransitGateway", {}),
    }
```
