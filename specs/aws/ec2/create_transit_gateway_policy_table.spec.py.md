---
id: "@specs/aws/ec2/create_transit_gateway_policy_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateTransitGatewayPolicyTable"
---

# CreateTransitGatewayPolicyTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_transit_gateway_policy_table
> **spec:implements:** @kind:operation CreateTransitGatewayPolicyTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateTransitGatewayPolicyTable.spec.md

Creates a transit gateway policy table.

## Input Shape: CreateTransitGatewayPolicyTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags specification for the transit gateway policy table created during the request. |
| TransitGatewayId | Any  # complex shape | ✓ | The ID of the transit gateway used for the policy table. |

## Output Shape: CreateTransitGatewayPolicyTableResult

- **TransitGatewayPolicyTable** (Any  # complex shape): Describes the created transit gateway policy table.

## Implementation

```speclang
def create_transit_gateway_policy_table(store, request: dict) -> dict:
    """Creates a transit gateway policy table."""
    transit_gateway_id = request.get("TransitGatewayId", "").strip() if isinstance(request.get("TransitGatewayId"), str) else request.get("TransitGatewayId")
    if not transit_gateway_id:
        raise ValidationException("TransitGatewayId is required")

    if store.transit_gateway_policy_tables(transit_gateway_id):
        raise ResourceInUseException(f"Resource transit_gateway_id already exists")

    record = {
        "TransitGatewayId": transit_gateway_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.transit_gateway_policy_tables(transit_gateway_id, record)

    return {
        "TransitGatewayPolicyTable": record.get("TransitGatewayPolicyTable", {}),
    }
```
