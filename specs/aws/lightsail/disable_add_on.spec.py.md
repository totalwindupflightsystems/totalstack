---
id: "@specs/aws/lightsail/disable_add_on"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DisableAddOn"
---

# DisableAddOn

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/disable_add_on
> **spec:implements:** @kind:operation DisableAddOn
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DisableAddOn.spec.md

Disables an add-on for an Amazon Lightsail resource. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DisableAddOnRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| addOnType | Any  # complex shape | ✓ | The add-on type to disable. |
| resourceName | Any  # complex shape | ✓ | The name of the source resource for which to disable the add-on. |

## Output Shape: DisableAddOnResult

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
def disable_add_on(store, request: dict) -> dict:
    """Disables an add-on for an Amazon Lightsail resource. For more information, see the Amazon Lightsail Developer Guide ."""
    add_on_type = request.get("addOnType", "").strip() if isinstance(request.get("addOnType"), str) else request.get("addOnType")
    if not add_on_type:
        raise ValidationException("addOnType is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    if store.disable_add_ons(resource_name):
        raise ResourceInUseException(f"Resource resource_name already exists")

    record = {
        "addOnType": add_on_type,
        "resourceName": resource_name,
    }

    store.disable_add_ons(resource_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
