---
id: "@specs/aws/lightsail/delete_relational_database_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteRelationalDatabaseSnapshot"
---

# DeleteRelationalDatabaseSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_relational_database_snapshot
> **spec:implements:** @kind:operation DeleteRelationalDatabaseSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteRelationalDatabaseSnapshot.spec.md

Deletes a database snapshot in Amazon Lightsail. The delete relational database snapshot operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteRelationalDatabaseSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| relationalDatabaseSnapshotName | Any  # complex shape | ✓ | The name of the database snapshot that you are deleting. |

## Output Shape: DeleteRelationalDatabaseSnapshotResult

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
def delete_relational_database_snapshot(store, request: dict) -> dict:
    """Deletes a database snapshot in Amazon Lightsail. The delete relational database snapshot operation supports tag-based access control via resource tags applied to the resource identified by relationalD"""
    relational_database_snapshot_name = request.get("relationalDatabaseSnapshotName", "").strip() if isinstance(request.get("relationalDatabaseSnapshotName"), str) else request.get("relationalDatabaseSnapshotName")

    if not store.relational_database_snapshots(relational_database_snapshot_name):
        raise ResourceNotFoundException(f"Resource relational_database_snapshot_name not found")
    store.delete_relational_database_snapshots(relational_database_snapshot_name)
    return {}
```
