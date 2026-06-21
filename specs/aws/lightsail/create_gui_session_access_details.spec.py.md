---
id: "@specs/aws/lightsail/create_gui_session_access_details"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateGUISessionAccessDetails"
---

# CreateGUISessionAccessDetails

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_gui_session_access_details
> **spec:implements:** @kind:operation CreateGUISessionAccessDetails
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateGUISessionAccessDetails.spec.md

Creates two URLs that are used to access a virtual computer’s graphical user interface (GUI) session. The primary URL initiates a web-based Amazon DCV session to the virtual computer's application. The secondary URL initiates a web-based Amazon DCV session to the virtual computer's operating session. Use StartGUISession to open the session.

## Input Shape: CreateGUISessionAccessDetailsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| resourceName | Any  # complex shape | ✓ | The resource name. |

## Output Shape: CreateGUISessionAccessDetailsResult

- **failureReason** (Any  # complex shape): The reason the operation failed.
- **percentageComplete** (Any  # complex shape): The percentage of completion for the operation.
- **resourceName** (Any  # complex shape): The resource name.
- **sessions** (Any  # complex shape): Returns information about the specified Amazon DCV GUI session.
- **status** (Any  # complex shape): The status of the operation.

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def create_gui_session_access_details(store, request: dict) -> dict:
    """Creates two URLs that are used to access a virtual computer’s graphical user interface (GUI) session. The primary URL initiates a web-based Amazon DCV session to the virtual computer's application. Th"""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    if store.gui_session_access_detailss(resource_name):
        raise ResourceInUseException(f"Resource resource_name already exists")

    record = {
        "resourceName": resource_name,
    }

    store.gui_session_access_detailss(resource_name, record)

    return {
        "resourceName": resource_name,
        "status": record.get("status", {}),
        "percentageComplete": record.get("percentageComplete", {}),
        "failureReason": record.get("failureReason", {}),
        "sessions": record.get("sessions", {}),
    }
```
