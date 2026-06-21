---
id: "@specs/aws/lightsail/get_distribution_latest_cache_reset"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetDistributionLatestCacheReset"
---

# GetDistributionLatestCacheReset

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_distribution_latest_cache_reset
> **spec:implements:** @kind:operation GetDistributionLatestCacheReset
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetDistributionLatestCacheReset.spec.md

Returns the timestamp and status of the last cache reset of a specific Amazon Lightsail content delivery network (CDN) distribution.

## Input Shape: GetDistributionLatestCacheResetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| distributionName | Any  # complex shape |  | The name of the distribution for which to return the timestamp of the last cache reset. Use the GetDistributions action  |

## Output Shape: GetDistributionLatestCacheResetResult

- **createTime** (Any  # complex shape): The timestamp of the last cache reset ( 1479734909.17 ) in Unix time format.
- **status** (Any  # complex shape): The status of the last cache reset.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def get_distribution_latest_cache_reset(store, request: dict) -> dict:
    """Returns the timestamp and status of the last cache reset of a specific Amazon Lightsail content delivery network (CDN) distribution."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
