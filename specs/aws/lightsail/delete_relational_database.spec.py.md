---
id: "@specs/aws/lightsail/delete_relational_database"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteRelationalDatabase"
---

# DeleteRelationalDatabase

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_relational_database
> **spec:implements:** @kind:operation DeleteRelationalDatabase
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteRelationalDatabase.spec.md

Deletes a database in Amazon Lightsail. The delete relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteRelationalDatabaseRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| finalRelationalDatabaseSnapshotName | Any  # complex shape |  | The name of the database snapshot created if skip final snapshot is false , which is the default value for that paramete |
| relationalDatabaseName | Any  # complex shape | ✓ | The name of the database that you are deleting. |
| skipFinalSnapshot | Any  # complex shape |  | Determines whether a final database snapshot is created before your database is deleted. If true is specified, no databa |

## Output Shape: DeleteRelationalDatabaseResult

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
def delete_relational_database(store, request: dict) -> dict:
    """Deletes a database in Amazon Lightsail. The delete relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For m"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")

    if not store.relational_databases(relational_database_name):
        raise ResourceNotFoundException(f"Resource relational_database_name not found")
    store.delete_relational_databases(relational_database_name)
    return {}
```
