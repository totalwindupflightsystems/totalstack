---
id: "@specs/aws/ec2/get_coip_pool_usage"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetCoipPoolUsage"
---

# GetCoipPoolUsage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_coip_pool_usage
> **spec:implements:** @kind:operation GetCoipPoolUsage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetCoipPoolUsage.spec.md

Describes the allocations from the specified customer-owned address pool.

## Input Shape: GetCoipPoolUsageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Filters | list[Any  # complex shape] |  | One or more filters. coip-address-usage.allocation-id - The allocation ID of the address. coip-address-usage.aws-account |
| MaxResults | Any  # complex shape |  | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with th |
| NextToken | str |  | The token for the next page of results. |
| PoolId | Any  # complex shape | ✓ | The ID of the address pool. |

## Output Shape: GetCoipPoolUsageResult

- **CoipAddressUsages** (Any  # complex shape): Information about the address usage.
- **CoipPoolId** (str): The ID of the customer-owned address pool.
- **LocalGatewayRouteTableId** (str): The ID of the local gateway route table.
- **NextToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.

## Implementation

```speclang
def get_coip_pool_usage(store, request: dict) -> dict:
    """Describes the allocations from the specified customer-owned address pool."""
    pool_id = request.get("PoolId", "").strip() if isinstance(request.get("PoolId"), str) else request.get("PoolId")
    if not pool_id:
        raise ValidationException("PoolId is required")

    resource = store.coip_pool_usages(pool_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource pool_id not found")
    return {"PoolId": pool_id, **resource}
```
