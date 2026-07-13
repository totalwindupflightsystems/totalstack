---
id: "@specs/aws/lambda/get_capacity_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_GetCapacityProvider"
---

# GetCapacityProvider

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/get_capacity_provider
> **spec:implements:** @kind:operation GetCapacityProvider
> **AWS Protocol:** rest-json
> **HTTP:** GET /2025-11-30/capacity-providers/{CapacityProviderName}
> **@ref:** specs/aws/lambda/docs/API_GetCapacityProvider.spec.md

Retrieves information about a specific capacity provider, including its configuration, state, and associated resources.

## Input Shape: GetCapacityProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityProviderName | Any  # complex shape | ✓ | The name of the capacity provider to retrieve. |

## Output Shape: GetCapacityProviderResponse

- **CapacityProvider** (Any  # complex shape): Information about the capacity provider, including its configuration and current state.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def get_capacity_provider(store, request: dict) -> dict:
    """Retrieves information about a specific capacity provider, including its configuration, state, and associated resources."""
    capacity_provider_name = request.get("CapacityProviderName", "").strip() if isinstance(request.get("CapacityProviderName"), str) else request.get("CapacityProviderName")
    if not capacity_provider_name:
        raise ValidationException("CapacityProviderName is required")

    resource = store.capacity_providers(capacity_provider_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_provider_name not found")
    return {"CapacityProviderName": capacity_provider_name, **resource}
```
