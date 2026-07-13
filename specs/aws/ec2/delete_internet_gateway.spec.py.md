---
id: "@specs/aws/ec2/delete_internet_gateway"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteInternetGateway"
---

# DeleteInternetGateway

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_internet_gateway
> **spec:implements:** @kind:operation DeleteInternetGateway
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteInternetGateway.spec.md

Deletes the specified internet gateway. You must detach the internet gateway from the VPC before you can delete it.

## Input Shape: DeleteInternetGatewayRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InternetGatewayId | Any  # complex shape | ✓ | The ID of the internet gateway. |

## Implementation

```speclang
def delete_internet_gateway(store, request: dict) -> dict:
    """Deletes the specified internet gateway. You must detach the internet gateway from the VPC before you can delete it."""
    internet_gateway_id = request.get("InternetGatewayId", "").strip() if isinstance(request.get("InternetGatewayId"), str) else request.get("InternetGatewayId")

    if not store.internet_gateways(internet_gateway_id):
        raise ResourceNotFoundException(f"Resource internet_gateway_id not found")
    store.delete_internet_gateways(internet_gateway_id)
    return {}
```
