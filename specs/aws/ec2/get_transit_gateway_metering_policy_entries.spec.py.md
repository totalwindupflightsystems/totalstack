---
id: "@specs/aws/ec2/get_transit_gateway_metering_policy_entries"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetTransitGatewayMeteringPolicyEntries"
---

# GetTransitGatewayMeteringPolicyEntries

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_transit_gateway_metering_policy_entries
> **spec:implements:** @kind:operation GetTransitGatewayMeteringPolicyEntries
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetTransitGatewayMeteringPolicyEntries.spec.md

Retrieves the entries for a transit gateway metering policy.

## Input Shape: GetTransitGatewayMeteringPolicyEntriesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters to apply when retrieving metering policy entries. |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| TransitGatewayMeteringPolicyId | Any  # complex shape | ✓ | The ID of the transit gateway metering policy to retrieve entries for. |

## Output Shape: GetTransitGatewayMeteringPolicyEntriesResult

- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **TransitGatewayMeteringPolicyEntries** (list[Any  # complex shape]): Information about the transit gateway metering policy entries.

## Implementation

```speclang
def get_transit_gateway_metering_policy_entries(store, request: dict) -> dict:
    """Retrieves the entries for a transit gateway metering policy."""
    transit_gateway_metering_policy_id = request.get("TransitGatewayMeteringPolicyId", "").strip() if isinstance(request.get("TransitGatewayMeteringPolicyId"), str) else request.get("TransitGatewayMeteringPolicyId")
    if not transit_gateway_metering_policy_id:
        raise ValidationException("TransitGatewayMeteringPolicyId is required")

    resource = store.transit_gateway_metering_policy_entriess(transit_gateway_metering_policy_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource transit_gateway_metering_policy_id not found")
    return {"TransitGatewayMeteringPolicyId": transit_gateway_metering_policy_id, **resource}
```
