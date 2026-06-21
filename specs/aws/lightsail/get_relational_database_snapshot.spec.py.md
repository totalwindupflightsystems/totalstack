---
id: "@specs/aws/lightsail/get_relational_database_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetRelationalDatabaseSnapshot"
---

# GetRelationalDatabaseSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_relational_database_snapshot
> **spec:implements:** @kind:operation GetRelationalDatabaseSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetRelationalDatabaseSnapshot.spec.md

Returns information about a specific database snapshot in Amazon Lightsail.

## Input Shape: GetRelationalDatabaseSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| relationalDatabaseSnapshotName | Any  # complex shape | ✓ | The name of the database snapshot for which to get information. |

## Output Shape: GetRelationalDatabaseSnapshotResult

- **relationalDatabaseSnapshot** (Any  # complex shape): An object describing the specified database snapshot.

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
def get_relational_database_snapshot(store, request: dict) -> dict:
    """Returns information about a specific database snapshot in Amazon Lightsail."""
    relational_database_snapshot_name = request.get("relationalDatabaseSnapshotName", "").strip() if isinstance(request.get("relationalDatabaseSnapshotName"), str) else request.get("relationalDatabaseSnapshotName")
    if not relational_database_snapshot_name:
        raise ValidationException("relationalDatabaseSnapshotName is required")

    resource = store.relational_database_snapshots(relational_database_snapshot_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource relational_database_snapshot_name not found")
    return {"relationalDatabaseSnapshotName": relational_database_snapshot_name, **resource}
```
