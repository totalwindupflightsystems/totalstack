---
id: "@specs/aws/lambda/list_function_versions_by_capacity_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListFunctionVersionsByCapacityProvider"
---

# ListFunctionVersionsByCapacityProvider

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_function_versions_by_capacity_provider
> **spec:implements:** @kind:operation ListFunctionVersionsByCapacityProvider
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-11-30/capacity-providers/{CapacityProviderName}/function-versions
> **@ref:** specs/aws/lambda/docs/API_ListFunctionVersionsByCapacityProvider.spec.md

Returns a list of function versions that are configured to use a specific capacity provider.

## Input Shape: ListFunctionVersionsByCapacityProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityProviderName | Any  # complex shape | ✓ | The name of the capacity provider to list function versions for. |
| Marker | str |  | Specify the pagination token that's returned by a previous request to retrieve the next page of results. |
| MaxItems | Any  # complex shape |  | The maximum number of function versions to return in the response. |

## Output Shape: ListFunctionVersionsByCapacityProviderResponse

- **CapacityProviderArn** (Any  # complex shape): The Amazon Resource Name (ARN) of the capacity provider.
- **FunctionVersions** (list[Any  # complex shape]): A list of function versions that use the specified capacity provider.
- **NextMarker** (str): The pagination token that's included if more results are available.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_function_versions_by_capacity_provider(store, request: dict) -> dict:
    """Returns a list of function versions that are configured to use a specific capacity provider."""
    capacity_provider_name = request.get("CapacityProviderName", "").strip() if isinstance(request.get("CapacityProviderName"), str) else request.get("CapacityProviderName")
    if not capacity_provider_name:
        raise ValidationException("CapacityProviderName is required")

    items = store.list_function_versions_by_capacity_providers()
    return {"FunctionVersions": list(items.values())}
```
