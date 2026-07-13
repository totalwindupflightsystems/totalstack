---
id: "@specs/aws/ec2/get_transit_gateway_policy_table_associations"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetTransitGatewayPolicyTableAssociations"
---

# GetTransitGatewayPolicyTableAssociations

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_transit_gateway_policy_table_associations
> **spec:implements:** @kind:operation GetTransitGatewayPolicyTableAssociations
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetTransitGatewayPolicyTableAssociations.spec.md

Gets a list of the transit gateway policy table associations.

## Input Shape: GetTransitGatewayPolicyTableAssociationsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | The filters associated with the transit gateway policy table. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayPolicyTableId | Any  # complex shape | ✓ | The ID of the transit gateway policy table. |

## Output Shape: GetTransitGatewayPolicyTableAssociationsResult

- **Associations** (list[Any  # complex shape]): Returns details about the transit gateway policy table association.
- **NextToken** (str): The token for the next page of results.

## Implementation

```speclang
def get_transit_gateway_policy_table_associations(store, request: dict) -> dict:
    """Gets a list of the transit gateway policy table associations."""
    transit_gateway_policy_table_id = request.get("TransitGatewayPolicyTableId", "").strip() if isinstance(request.get("TransitGatewayPolicyTableId"), str) else request.get("TransitGatewayPolicyTableId")
    if not transit_gateway_policy_table_id:
        raise ValidationException("TransitGatewayPolicyTableId is required")

    resource = store.transit_gateway_policy_table_associationss(transit_gateway_policy_table_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_policy_table_id not found")
    return {"TransitGatewayPolicyTableId": transit_gateway_policy_table_id, **resource}
```
