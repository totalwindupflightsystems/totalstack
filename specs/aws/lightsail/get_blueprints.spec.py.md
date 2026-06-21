---
id: "@specs/aws/lightsail/get_blueprints"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetBlueprints"
---

# GetBlueprints

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_blueprints
> **spec:implements:** @kind:operation GetBlueprints
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetBlueprints.spec.md

Returns the list of available instance images, or blueprints . You can use a blueprint to create a new instance already running a specific operating system, as well as a preinstalled app or development stack. The software each instance is running depends on the blueprint image you choose. Use active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.

## Input Shape: GetBlueprintsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| appCategory | Any  # complex shape |  | Returns a list of blueprints that are specific to Lightsail for Research. You must use this parameter to view Lightsail  |
| includeInactive | Any  # complex shape |  | A Boolean value that indicates whether to include inactive (unavailable) blueprints in the response of your request. |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetBlueprint |

## Output Shape: GetBlueprintsResult

- **blueprints** (list[Any  # complex shape]): An array of key-value pairs that contains information about the available blueprints.
- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo

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
def get_blueprints(store, request: dict) -> dict:
    """Returns the list of available instance images, or blueprints . You can use a blueprint to create a new instance already running a specific operating system, as well as a preinstalled app or developmen"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
