---
id: "@specs/aws/lightsail/get_relational_database_events"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetRelationalDatabaseEvents"
---

# GetRelationalDatabaseEvents

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_relational_database_events
> **spec:implements:** @kind:operation GetRelationalDatabaseEvents
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetRelationalDatabaseEvents.spec.md

Returns a list of events for a specific database in Amazon Lightsail.

## Input Shape: GetRelationalDatabaseEventsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| durationInMinutes | Any  # complex shape |  | The number of minutes in the past from which to retrieve events. For example, to get all events from the past 2 hours, e |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetRelationa |
| relationalDatabaseName | Any  # complex shape | ✓ | The name of the database from which to get events. |

## Output Shape: GetRelationalDatabaseEventsResult

- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo
- **relationalDatabaseEvents** (list[Any  # complex shape]): An object describing the result of your get relational database events request.

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
def get_relational_database_events(store, request: dict) -> dict:
    """Returns a list of events for a specific database in Amazon Lightsail."""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_eventss(relational_database_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}
```
