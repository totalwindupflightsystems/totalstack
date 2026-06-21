---
id: "@specs/aws/lightsail/stop_gui_session"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_StopGUISession"
---

# StopGUISession

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/stop_gui_session
> **spec:implements:** @kind:operation StopGUISession
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_StopGUISession.spec.md

Terminates a web-based Amazon DCV session that’s used to access a virtual computer’s operating system or application. The session will close and any unsaved data will be lost.

## Input Shape: StopGUISessionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| resourceName | Any  # complex shape | ✓ | The resource name. |

## Output Shape: StopGUISessionResult

- **operations** (list[Any  # complex shape]): The available API operations.

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def stop_gui_session(store, request: dict) -> dict:
    """Terminates a web-based Amazon DCV session that’s used to access a virtual computer’s operating system or application. The session will close and any unsaved data will be lost."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")

    if not store.gui_sessions(resource_name):
        raise ResourceNotFoundException(f"Resource resource_name not found")
    store.delete_gui_sessions(resource_name)
    return {}
```
