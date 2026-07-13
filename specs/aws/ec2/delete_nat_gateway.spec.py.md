---
id: "@specs/aws/ec2/delete_nat_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNatGateway"
---

# DeleteNatGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_nat_gateway
> **spec:implements:** @kind:operation DeleteNatGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNatGateway.spec.md

Deletes the specified NAT gateway. Deleting a public NAT gateway disassociates its Elastic IP address, but does not release the address from your account. Deleting a NAT gateway does not delete any NAT gateway routes in your route tables.

## Input Shape: DeleteNatGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NatGatewayId | Any  # complex shape | ✓ | The ID of the NAT gateway. |

## Output Shape: DeleteNatGatewayResult

- **NatGatewayId** (str): The ID of the NAT gateway.

## Implementation

```speclang
def delete_nat_gateway(store, request: dict) -> dict:
    """Deletes the specified NAT gateway. Deleting a public NAT gateway disassociates its Elastic IP address, but does not release the address from your account. Deleting a NAT gateway does not delete any NA"""
    nat_gateway_id = request.get("NatGatewayId", "").strip() if isinstance(request.get("NatGatewayId"), str) else request.get("NatGatewayId")

    if not store.nat_gateways(nat_gateway_id):
        raise ResourceNotFoundException(f"Resource nat_gateway_id not found")
    store.delete_nat_gateways(nat_gateway_id)
    return {}
```
