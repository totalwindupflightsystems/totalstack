---
id: "@specs/aws/lightsail/get_setup_history"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetSetupHistory"
---

# GetSetupHistory

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_setup_history
> **spec:implements:** @kind:operation GetSetupHistory
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetSetupHistory.spec.md

Returns detailed information for five of the most recent SetupInstanceHttps requests that were ran on the target instance.

## Input Shape: GetSetupHistoryRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetSetupHist |
| resourceName | Any  # complex shape | ✓ | The name of the resource for which you are requesting information. |

## Output Shape: GetSetupHistoryResult

- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo
- **setupHistory** (list[Any  # complex shape]): The historical information that's returned.

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_setup_history(store, request: dict) -> dict:
    """Returns detailed information for five of the most recent SetupInstanceHttps requests that were ran on the target instance."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.setup_historys(resource_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource resource_name not found")
    return {"resourceName": resource_name, **resource}
```
