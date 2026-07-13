---
id: "@specs/aws/ec2/delete_transit_gateway_policy_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteTransitGatewayPolicyTable"
---

# DeleteTransitGatewayPolicyTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_transit_gateway_policy_table
> **spec:implements:** @kind:operation DeleteTransitGatewayPolicyTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteTransitGatewayPolicyTable.spec.md

Deletes the specified transit gateway policy table.

## Input Shape: DeleteTransitGatewayPolicyTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TransitGatewayPolicyTableId | Any  # complex shape | ✓ | The transit gateway policy table to delete. |

## Output Shape: DeleteTransitGatewayPolicyTableResult

- **TransitGatewayPolicyTable** (Any  # complex shape): Provides details about the deleted transit gateway policy table.

## Implementation

```speclang
def delete_transit_gateway_policy_table(store, request: dict) -> dict:
    """Deletes the specified transit gateway policy table."""
    transit_gateway_policy_table_id = request.get("TransitGatewayPolicyTableId", "").strip() if isinstance(request.get("TransitGatewayPolicyTableId"), str) else request.get("TransitGatewayPolicyTableId")

    if not store.transit_gateway_policy_tables(transit_gateway_policy_table_id):
        raise ResourceNotFoundException(f"Resource transit_gateway_policy_table_id not found")
    store.delete_transit_gateway_policy_tables(transit_gateway_policy_table_id)
    return {}
```
