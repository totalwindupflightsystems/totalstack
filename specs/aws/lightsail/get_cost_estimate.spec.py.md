---
id: "@specs/aws/lightsail/get_cost_estimate"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetCostEstimate"
---

# GetCostEstimate

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_cost_estimate
> **spec:implements:** @kind:operation GetCostEstimate
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetCostEstimate.spec.md

Retrieves information about the cost estimate for a specified resource. A cost estimate will not generate for a resource that has been deleted.

## Input Shape: GetCostEstimateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| endTime | Any  # complex shape | ✓ | The cost estimate end time. Constraints: Specified in Coordinated Universal Time (UTC). Specified in the Unix time forma |
| resourceName | Any  # complex shape | ✓ | The resource name. |
| startTime | Any  # complex shape | ✓ | The cost estimate start time. Constraints: Specified in Coordinated Universal Time (UTC). Specified in the Unix time for |

## Output Shape: GetCostEstimateResult

- **resourcesBudgetEstimate** (Any  # complex shape): Returns the estimate's forecasted cost or usage.

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_cost_estimate(store, request: dict) -> dict:
    """Retrieves information about the cost estimate for a specified resource. A cost estimate will not generate for a resource that has been deleted."""
    end_time = request.get("endTime", "").strip() if isinstance(request.get("endTime"), str) else request.get("endTime")
    if not end_time:
        raise ValidationException("endTime is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    start_time = request.get("startTime", "").strip() if isinstance(request.get("startTime"), str) else request.get("startTime")
    if not start_time:
        raise ValidationException("startTime is required")

    resource = store.cost_estimates(resource_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource resource_name not found")
    return {"resourceName": resource_name, **resource}
```
