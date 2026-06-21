---
id: "@specs/aws/lightsail/enable_add_on"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_EnableAddOn"
---

# EnableAddOn

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/enable_add_on
> **spec:implements:** @kind:operation EnableAddOn
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_EnableAddOn.spec.md

Enables or modifies an add-on for an Amazon Lightsail resource. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: EnableAddOnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| addOnRequest | Any  # complex shape | ✓ | An array of strings representing the add-on to enable or modify. |
| resourceName | Any  # complex shape | ✓ | The name of the source resource for which to enable or modify the add-on. |

## Output Shape: EnableAddOnResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def enable_add_on(store, request: dict) -> dict:
    """Enables or modifies an add-on for an Amazon Lightsail resource. For more information, see the Amazon Lightsail Developer Guide ."""
    add_on_request = request.get("addOnRequest", "").strip() if isinstance(request.get("addOnRequest"), str) else request.get("addOnRequest")
    if not add_on_request:
        raise ValidationException("addOnRequest is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    if store.enable_add_ons(resource_name):
        raise ResourceInUseException(f"Resource resource_name already exists")

    record = {
        "resourceName": resource_name,
        "addOnRequest": add_on_request,
    }

    store.enable_add_ons(resource_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
