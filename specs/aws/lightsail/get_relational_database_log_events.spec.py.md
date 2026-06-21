---
id: "@specs/aws/lightsail/get_relational_database_log_events"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetRelationalDatabaseLogEvents"
---

# GetRelationalDatabaseLogEvents

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_relational_database_log_events
> **spec:implements:** @kind:operation GetRelationalDatabaseLogEvents
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetRelationalDatabaseLogEvents.spec.md

Returns a list of log events for a database in Amazon Lightsail.

## Input Shape: GetRelationalDatabaseLogEventsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| endTime | Any  # complex shape |  | The end of the time interval from which to get log events. Constraints: Specified in Coordinated Universal Time (UTC). S |
| logStreamName | Any  # complex shape | ✓ | The name of the log stream. Use the get relational database log streams operation to get a list of available log streams |
| pageToken | Any  # complex shape |  | The token to advance to the next or previous page of results from your request. To get a page token, perform an initial  |
| relationalDatabaseName | Any  # complex shape | ✓ | The name of your database for which to get log events. |
| startFromHead | Any  # complex shape |  | Parameter to specify if the log should start from head or tail. If true is specified, the log event starts from the head |
| startTime | Any  # complex shape |  | The start of the time interval from which to get log events. Constraints: Specified in Coordinated Universal Time (UTC). |

## Output Shape: GetRelationalDatabaseLogEventsResult

- **nextBackwardToken** (Any  # complex shape): A token used for advancing to the previous page of results from your get relational database log events request.
- **nextForwardToken** (Any  # complex shape): A token used for advancing to the next page of results from your get relational database log events request.
- **resourceLogEvents** (list[Any  # complex shape]): An object describing the result of your get relational database log events request.

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
def get_relational_database_log_events(store, request: dict) -> dict:
    """Returns a list of log events for a database in Amazon Lightsail."""
    log_stream_name = request.get("logStreamName", "").strip() if isinstance(request.get("logStreamName"), str) else request.get("logStreamName")
    if not log_stream_name:
        raise ValidationException("logStreamName is required")
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_log_eventss(log_stream_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource log_stream_name not found")
    return {"logStreamName": log_stream_name, **resource}
```
