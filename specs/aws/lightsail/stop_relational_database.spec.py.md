---
id: "@specs/aws/lightsail/stop_relational_database"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_StopRelationalDatabase"
---

# StopRelationalDatabase

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/stop_relational_database
> **spec:implements:** @kind:operation StopRelationalDatabase
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_StopRelationalDatabase.spec.md

Stops a specific database that is currently running in Amazon Lightsail. If you don't manually start your database instance after it has been stopped for seven consecutive days, Amazon Lightsail automatically starts it for you. This action helps ensure that your database instance doesn't fall behind on any required maintenance updates. The stop relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: StopRelationalDatabaseRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| relationalDatabaseName | Any  # complex shape | ✓ | The name of your database to stop. |
| relationalDatabaseSnapshotName | Any  # complex shape |  | The name of your new database snapshot to be created before stopping your database. |

## Output Shape: StopRelationalDatabaseResult

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
def stop_relational_database(store, request: dict) -> dict:
    """Stops a specific database that is currently running in Amazon Lightsail. If you don't manually start your database instance after it has been stopped for seven consecutive days, Amazon Lightsail autom"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")

    if not store.relational_databases(relational_database_name):
        raise ResourceNotFoundException(f"Resource relational_database_name not found")
    store.delete_relational_databases(relational_database_name)
    return {}
```
