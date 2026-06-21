---
id: "@specs/aws/lightsail/get_load_balancer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetLoadBalancer"
---

# GetLoadBalancer

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_load_balancer
> **spec:implements:** @kind:operation GetLoadBalancer
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetLoadBalancer.spec.md

Returns information about the specified Lightsail load balancer.

## Input Shape: GetLoadBalancerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| loadBalancerName | Any  # complex shape | ✓ | The name of the load balancer. |

## Output Shape: GetLoadBalancerResult

- **loadBalancer** (Any  # complex shape): An object containing information about your load balancer.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def get_load_balancer(store, request: dict) -> dict:
    """Returns information about the specified Lightsail load balancer."""
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    resource = store.load_balancers(load_balancer_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource load_balancer_name not found")
    return {"loadBalancerName": load_balancer_name, **resource}
```
