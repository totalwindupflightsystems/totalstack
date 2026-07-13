---
id: "@specs/aws/ec2/delete_egress_only_internet_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteEgressOnlyInternetGateway"
---

# DeleteEgressOnlyInternetGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_egress_only_internet_gateway
> **spec:implements:** @kind:operation DeleteEgressOnlyInternetGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteEgressOnlyInternetGateway.spec.md

Deletes an egress-only internet gateway.

## Input Shape: DeleteEgressOnlyInternetGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EgressOnlyInternetGatewayId | Any  # complex shape | ✓ | The ID of the egress-only internet gateway. |

## Output Shape: DeleteEgressOnlyInternetGatewayResult

- **ReturnCode** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def delete_egress_only_internet_gateway(store, request: dict) -> dict:
    """Deletes an egress-only internet gateway."""
    egress_only_internet_gateway_id = request.get("EgressOnlyInternetGatewayId", "").strip() if isinstance(request.get("EgressOnlyInternetGatewayId"), str) else request.get("EgressOnlyInternetGatewayId")

    if not store.egress_only_internet_gateways(egress_only_internet_gateway_id):
        raise ResourceNotFoundException(f"Resource egress_only_internet_gateway_id not found")
    store.delete_egress_only_internet_gateways(egress_only_internet_gateway_id)
    return {}
```
