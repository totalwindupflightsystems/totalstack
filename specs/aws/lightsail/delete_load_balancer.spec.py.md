---
id: "@specs/aws/lightsail/delete_load_balancer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteLoadBalancer"
---

# DeleteLoadBalancer

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_load_balancer
> **spec:implements:** @kind:operation DeleteLoadBalancer
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteLoadBalancer.spec.md

Deletes a Lightsail load balancer and all its associated SSL/TLS certificates. Once the load balancer is deleted, you will need to create a new load balancer, create a new certificate, and verify domain ownership again. The delete load balancer operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteLoadBalancerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| loadBalancerName | Any  # complex shape | ✓ | The name of the load balancer you want to delete. |

## Output Shape: DeleteLoadBalancerResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

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
def delete_load_balancer(store, request: dict) -> dict:
    """Deletes a Lightsail load balancer and all its associated SSL/TLS certificates. Once the load balancer is deleted, you will need to create a new load balancer, create a new certificate, and verify doma"""
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")

    if not store.load_balancers(load_balancer_name):
        raise ResourceNotFoundException(f"Resource load_balancer_name not found")
    store.delete_load_balancers(load_balancer_name)
    return {}
```
