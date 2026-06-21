---
id: "@specs/aws/lightsail/update_load_balancer_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateLoadBalancerAttribute"
---

# UpdateLoadBalancerAttribute

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_load_balancer_attribute
> **spec:implements:** @kind:operation UpdateLoadBalancerAttribute
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateLoadBalancerAttribute.spec.md

Updates the specified attribute for a load balancer. You can only update one attribute at a time. The update load balancer attribute operation supports tag-based access control via resource tags applied to the resource identified by load balancer name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: UpdateLoadBalancerAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| attributeName | Any  # complex shape | ✓ | The name of the attribute you want to update. |
| attributeValue | Any  # complex shape | ✓ | The value that you want to specify for the attribute name. The following values are supported depending on what you spec |
| loadBalancerName | Any  # complex shape | ✓ | The name of the load balancer that you want to modify ( my-load-balancer . |

## Output Shape: UpdateLoadBalancerAttributeResult

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
def update_load_balancer_attribute(store, request: dict) -> dict:
    """Updates the specified attribute for a load balancer. You can only update one attribute at a time. The update load balancer attribute operation supports tag-based access control via resource tags appli"""
    attribute_name = request.get("attributeName", "").strip() if isinstance(request.get("attributeName"), str) else request.get("attributeName")
    if not attribute_name:
        raise ValidationException("attributeName is required")
    attribute_value = request.get("attributeValue", "").strip() if isinstance(request.get("attributeValue"), str) else request.get("attributeValue")
    if not attribute_value:
        raise ValidationException("attributeValue is required")
    load_balancer_name = request.get("loadBalancerName", "").strip() if isinstance(request.get("loadBalancerName"), str) else request.get("loadBalancerName")
    if not load_balancer_name:
        raise ValidationException("loadBalancerName is required")

    resource = store.load_balancer_attributes(attribute_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource attribute_name not found")

    # Update mutable fields

    store.load_balancer_attributes(attribute_name, resource)
    return resource
```
