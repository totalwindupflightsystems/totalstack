---
id: "@specs/aws/lightsail/get_relational_database"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetRelationalDatabase"
---

# GetRelationalDatabase

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_relational_database
> **spec:implements:** @kind:operation GetRelationalDatabase
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetRelationalDatabase.spec.md

Returns information about a specific database in Amazon Lightsail.

## Input Shape: GetRelationalDatabaseRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| relationalDatabaseName | Any  # complex shape | ✓ | The name of the database that you are looking up. |

## Output Shape: GetRelationalDatabaseResult

- **relationalDatabase** (Any  # complex shape): An object describing the specified database.

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
def get_relational_database(store, request: dict) -> dict:
    """Returns information about a specific database in Amazon Lightsail."""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_databases(relational_database_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}
```
