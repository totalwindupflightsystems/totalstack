---
id: "@specs/aws/lambda/list_capacity_providers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListCapacityProviders"
---

# ListCapacityProviders

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_capacity_providers
> **spec:implements:** @kind:operation ListCapacityProviders
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-11-30/capacity-providers
> **@ref:** specs/aws/lambda/docs/API_ListCapacityProviders.spec.md

Returns a list of capacity providers in your account.

## Input Shape: ListCapacityProvidersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | The maximum number of capacity providers to return. |
| State | Any  # complex shape |  | Filter capacity providers by their current state. |

## Output Shape: ListCapacityProvidersResponse

- **CapacityProviders** (list[Any  # complex shape]): A list of capacity providers in your account.
- **NextMarker** (str): The pagination token that's included if more results are available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .

## Implementation

```speclang
def list_capacity_providers(store, request: dict) -> dict:
    """Returns a list of capacity providers in your account."""

    items = store.list_capacity_providerss()
    return {"CapacityProviders": list(items.values())}
```
