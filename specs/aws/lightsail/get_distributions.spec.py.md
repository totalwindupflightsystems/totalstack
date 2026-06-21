---
id: "@specs/aws/lightsail/get_distributions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetDistributions"
---

# GetDistributions

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_distributions
> **spec:implements:** @kind:operation GetDistributions
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetDistributions.spec.md

Returns information about one or more of your Amazon Lightsail content delivery network (CDN) distributions.

## Input Shape: GetDistributionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| distributionName | Any  # complex shape |  | The name of the distribution for which to return information. When omitted, the response includes all of your distributi |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetDistribut |

## Output Shape: GetDistributionsResult

- **distributions** (list[Any  # complex shape]): An array of objects that describe your distributions.
- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def get_distributions(store, request: dict) -> dict:
    """Returns information about one or more of your Amazon Lightsail content delivery network (CDN) distributions."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
