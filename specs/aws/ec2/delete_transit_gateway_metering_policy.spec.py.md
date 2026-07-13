---
id: "@specs/aws/ec2/delete_transit_gateway_metering_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayMeteringPolicy"
---

# DeleteTransitGatewayMeteringPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_metering_policy
> **spec:implements:** @kind:operation DeleteTransitGatewayMeteringPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayMeteringPolicy.spec.md

Deletes a transit gateway metering policy.

## Input Shape: DeleteTransitGatewayMeteringPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayMeteringPolicyId | Any  # complex shape | ✓ | The ID of the transit gateway metering policy to delete. |

## Output Shape: DeleteTransitGatewayMeteringPolicyResult

- **TransitGatewayMeteringPolicy** (Any  # complex shape): Information about the deleted transit gateway metering policy.

## Implementation

```speclang
def delete_transit_gateway_metering_policy(store, request: dict) -> dict:
    """Deletes a transit gateway metering policy."""
    transit_gateway_metering_policy_id = request.get("TransitGatewayMeteringPolicyId", "").strip() if isinstance(request.get("TransitGatewayMeteringPolicyId"), str) else request.get("TransitGatewayMeteringPolicyId")

    if not store.transit_gateway_metering_policys(transit_gateway_metering_policy_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_metering_policy_id not found")
    store.delete_transit_gateway_metering_policys(transit_gateway_metering_policy_id)
    return {}
```
