---
id: "@specs/aws/lightsail/reset_distribution_cache"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_ResetDistributionCache"
---

# ResetDistributionCache

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/reset_distribution_cache
> **spec:implements:** @kind:operation ResetDistributionCache
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_ResetDistributionCache.spec.md

Deletes currently cached content from your Amazon Lightsail content delivery network (CDN) distribution. After resetting the cache, the next time a content request is made, your distribution pulls, serves, and caches it from the origin.

## Input Shape: ResetDistributionCacheRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| distributionName | Any  # complex shape |  | The name of the distribution for which to reset cache. Use the GetDistributions action to get a list of distribution nam |

## Output Shape: ResetDistributionCacheResult

- **createTime** (Any  # complex shape): The timestamp of the reset cache request ( 1479734909.17 ) in Unix time format.
- **operation** (Any  # complex shape): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ
- **status** (Any  # complex shape): The status of the reset cache request.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def reset_distribution_cache(store, request: dict) -> dict:
    """Deletes currently cached content from your Amazon Lightsail content delivery network (CDN) distribution. After resetting the cache, the next time a content request is made, your distribution pulls, se"""

```
