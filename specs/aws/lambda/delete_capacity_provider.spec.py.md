---
id: "@specs/aws/lambda/delete_capacity_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_DeleteCapacityProvider"
---

# DeleteCapacityProvider

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/delete_capacity_provider
> **spec:implements:** @kind:operation DeleteCapacityProvider
> **AWS Protocol:** rest-json
> **HTTP:** DELETE /2025-11-30/capacity-providers/{CapacityProviderName}
> **@ref:** specs/aws/lambda/docs/API_DeleteCapacityProvider.spec.md

Deletes a capacity provider. You cannot delete a capacity provider that is currently being used by Lambda functions.

## Input Shape: DeleteCapacityProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityProviderName | Any  # complex shape | ✓ | The name of the capacity provider to delete. |

## Output Shape: DeleteCapacityProviderResponse

- **CapacityProvider** (Any  # complex shape): Information about the deleted capacity provider.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def delete_capacity_provider(store, request: dict) -> dict:
    """Deletes a capacity provider. You cannot delete a capacity provider that is currently being used by Lambda functions."""
    capacity_provider_name = request.get("CapacityProviderName", "").strip() if isinstance(request.get("CapacityProviderName"), str) else request.get("CapacityProviderName")

    if not store.capacity_providers(capacity_provider_name):
        raise ResourceNotFoundException(f"Resource capacity_provider_name not found")
    store.delete_capacity_providers(capacity_provider_name)
    return {}
```
