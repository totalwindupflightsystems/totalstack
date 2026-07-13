---
id: "@specs/aws/ec2/delete_customer_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteCustomerGateway"
---

# DeleteCustomerGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_customer_gateway
> **spec:implements:** @kind:operation DeleteCustomerGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteCustomerGateway.spec.md

Deletes the specified customer gateway. You must delete the VPN connection before you can delete the customer gateway.

## Input Shape: DeleteCustomerGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CustomerGatewayId | Any  # complex shape | ✓ | The ID of the customer gateway. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Implementation

```speclang
def delete_customer_gateway(store, request: dict) -> dict:
    """Deletes the specified customer gateway. You must delete the VPN connection before you can delete the customer gateway."""
    customer_gateway_id = request.get("CustomerGatewayId", "").strip() if isinstance(request.get("CustomerGatewayId"), str) else request.get("CustomerGatewayId")

    if not store.customer_gateways(customer_gateway_id):
        raise ResourceNotFoundException(f"Resource customer_gateway_id not found")
    store.delete_customer_gateways(customer_gateway_id)
    return {}
```
