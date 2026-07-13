---
id: "@specs/aws/ec2/get_transit_gateway_policy_table_entries"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetTransitGatewayPolicyTableEntries"
---

# GetTransitGatewayPolicyTableEntries

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_transit_gateway_policy_table_entries
> **spec:implements:** @kind:operation GetTransitGatewayPolicyTableEntries
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetTransitGatewayPolicyTableEntries.spec.md

Returns a list of transit gateway policy table entries.

## Input Shape: GetTransitGatewayPolicyTableEntriesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters associated with the transit gateway policy table. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayPolicyTableId | Any  # complex shape | ✓ | The ID of the transit gateway policy table. |

## Output Shape: GetTransitGatewayPolicyTableEntriesResult

- **TransitGatewayPolicyTableEntries** (list[Any  # complex shape]): The entries for the transit gateway policy table.

## Implementation

```speclang
def get_transit_gateway_policy_table_entries(store, request: dict) -> dict:
    """Returns a list of transit gateway policy table entries."""
    transit_gateway_policy_table_id = request.get("TransitGatewayPolicyTableId", "").strip() if isinstance(request.get("TransitGatewayPolicyTableId"), str) else request.get("TransitGatewayPolicyTableId")
    if not transit_gateway_policy_table_id:
        raise ValidationException("TransitGatewayPolicyTableId is required")

    resource = store.transit_gateway_policy_table_entriess(transit_gateway_policy_table_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_policy_table_id not found")
    return {"TransitGatewayPolicyTableId": transit_gateway_policy_table_id, **resource}
```
