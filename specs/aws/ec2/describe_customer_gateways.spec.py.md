---
id: "@specs/aws/ec2/describe_customer_gateways"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeCustomerGateways"
---

# DescribeCustomerGateways

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_customer_gateways
> **spec:implements:** @kind:operation DescribeCustomerGateways
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeCustomerGateways.spec.md

Describes one or more of your VPN customer gateways. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide .

## Input Shape: DescribeCustomerGatewaysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CustomerGatewayIds | list[Any  # complex shape] |  | One or more customer gateway IDs. Default: Describes all your customer gateways. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. bgp-asn - The customer gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN). cust |

## Output Shape: DescribeCustomerGatewaysResult

- **CustomerGateways** (list[Any  # complex shape]): Information about one or more customer gateways.

## Implementation

```speclang
def describe_customer_gateways(store, request: dict) -> dict:
    """Describes one or more of your VPN customer gateways. For more information, see Amazon Web Services Site-to-Site VPN in the Amazon Web Services Site-to-Site VPN User Guide ."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
