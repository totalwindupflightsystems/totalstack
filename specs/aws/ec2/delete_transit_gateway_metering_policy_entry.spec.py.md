---
id: "@specs/aws/ec2/delete_transit_gateway_metering_policy_entry"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayMeteringPolicyEntry"
---

# DeleteTransitGatewayMeteringPolicyEntry

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_metering_policy_entry
> **spec:implements:** @kind:operation DeleteTransitGatewayMeteringPolicyEntry
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayMeteringPolicyEntry.spec.md

Deletes an entry from a transit gateway metering policy.

## Input Shape: DeleteTransitGatewayMeteringPolicyEntryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PolicyRuleNumber | int | ✓ | The rule number of the metering policy entry to delete. |
| TransitGatewayMeteringPolicyId | Any  # complex shape | ✓ | The ID of the transit gateway metering policy containing the entry to delete. |

## Output Shape: DeleteTransitGatewayMeteringPolicyEntryResult

- **TransitGatewayMeteringPolicyEntry** (Any  # complex shape): Information about the deleted transit gateway metering policy entry.

## Implementation

```speclang
def delete_transit_gateway_metering_policy_entry(store, request: dict) -> dict:
    """Deletes an entry from a transit gateway metering policy."""
    policy_rule_number = request.get("PolicyRuleNumber", "").strip() if isinstance(request.get("PolicyRuleNumber"), str) else request.get("PolicyRuleNumber")
    transit_gateway_metering_policy_id = request.get("TransitGatewayMeteringPolicyId", "").strip() if isinstance(request.get("TransitGatewayMeteringPolicyId"), str) else request.get("TransitGatewayMeteringPolicyId")

    if not store.transit_gateway_metering_policy_entrys(transit_gateway_metering_policy_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_metering_policy_id not found")
    store.delete_transit_gateway_metering_policy_entrys(transit_gateway_metering_policy_id)
    return {}
```
