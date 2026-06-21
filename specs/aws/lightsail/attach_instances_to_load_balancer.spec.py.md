---
id: "@specs/aws/lightsail/attach_instances_to_load_balancer"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_AttachInstancesToLoadBalancer"
---

# AttachInstancesToLoadBalancer

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/attach_instances_to_load_balancer
> **spec:implements:** @kind:operation AttachInstancesToLoadBalancer
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_AttachInstancesToLoadBalancer.spec.md

Attaches one or more Lightsail instances to a load balancer. After some time, the instances are attached to the load balancer and the health check status is available. The attach instances to load balancer operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Lightsail Developer Guide .

## Input Shape: AttachInstancesToLoadBalancerRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceNames | list[Any  # complex shape] | ✓ | An array of strings representing the instance name(s) you want to attach to your load balancer. An instance must be runn |
| loadBalancerName | Any  # complex shape | ✓ | The name of the load balancer. |

## Output Shape: AttachInstancesToLoadBalancerResult

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
def attach_instances_to_load_balancer(store, request: dict) -> dict:
    """Attaches one or more Lightsail instances to a load balancer. After some time, the instances are attached to the load balancer and the health check status is available. The attach instances to load bal"""
    instance_names = request.get("instanceNames", "").strip() if isinstance(request.get("instanceNames"), str) else request.get("instanceNames")
    if not instance_names:
        raise ValidationException("instanceNames is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachInstancesToLoadBalancer", request)
```
