---
id: "@specs/aws/lightsail/get_operations_for_resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetOperationsForResource"
---

# GetOperationsForResource

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_operations_for_resource
> **spec:implements:** @kind:operation GetOperationsForResource
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetOperationsForResource.spec.md

Gets operations for a specific resource (an instance or a static IP).

## Input Shape: GetOperationsForResourceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetOperation |
| resourceName | Any  # complex shape | ✓ | The name of the resource for which you are requesting information. |

## Output Shape: GetOperationsForResourceResult

- **nextPageCount** (Any  # complex shape): (Discontinued) Returns the number of pages of results that remain. In releases prior to June 12, 2017, this parameter re
- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo
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
def get_operations_for_resource(store, request: dict) -> dict:
    """Gets operations for a specific resource (an instance or a static IP)."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.operations_for_resources(resource_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource resource_name not found")
    return {"resourceName": resource_name, **resource}
```
