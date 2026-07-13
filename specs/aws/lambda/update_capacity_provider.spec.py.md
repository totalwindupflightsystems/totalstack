---
id: "@specs/aws/lambda/update_capacity_provider"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_UpdateCapacityProvider"
---

# UpdateCapacityProvider

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/update_capacity_provider
> **spec:implements:** @kind:operation UpdateCapacityProvider
> **AWS Protocol:** rest-json
> **HTTP:** PUT /2025-11-30/capacity-providers/{CapacityProviderName}
> **@ref:** specs/aws/lambda/docs/API_UpdateCapacityProvider.spec.md

Updates the configuration of an existing capacity provider.

## Input Shape: UpdateCapacityProviderRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CapacityProviderName | Any  # complex shape | ✓ | The name of the capacity provider to update. |
| CapacityProviderScalingConfig | Any  # complex shape |  | The updated scaling configuration for the capacity provider. |

## Output Shape: UpdateCapacityProviderResponse

- **CapacityProvider** (Any  # complex shape): Information about the updated capacity provider.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ResourceConflictException**: The resource already exists, or another operation is in progress.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def update_capacity_provider(store, request: dict) -> dict:
    """Updates the configuration of an existing capacity provider."""
    capacity_provider_name = request.get("CapacityProviderName", "").strip() if isinstance(request.get("CapacityProviderName"), str) else request.get("CapacityProviderName")
    if not capacity_provider_name:
        raise ValidationException("CapacityProviderName is required")

    resource = store.capacity_providers(capacity_provider_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource capacity_provider_name not found")

    # Update mutable fields
    if "CapacityProviderScalingConfig" in request:
        resource["CapacityProviderScalingConfig"] = capacity_provider_scaling_config

    store.capacity_providers(capacity_provider_name, resource)
    return resource
```
