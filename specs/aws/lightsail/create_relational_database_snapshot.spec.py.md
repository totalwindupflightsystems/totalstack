---
id: "@specs/aws/lightsail/create_relational_database_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateRelationalDatabaseSnapshot"
---

# CreateRelationalDatabaseSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_relational_database_snapshot
> **spec:implements:** @kind:operation CreateRelationalDatabaseSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateRelationalDatabaseSnapshot.spec.md

Creates a snapshot of your database in Amazon Lightsail. You can use snapshots for backups, to make copies of a database, and to save data before deleting a database. The create relational database snapshot operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateRelationalDatabaseSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| relationalDatabaseName | Any  # complex shape | ✓ | The name of the database on which to base your new snapshot. |
| relationalDatabaseSnapshotName | Any  # complex shape | ✓ | The name for your new database snapshot. Constraints: Must contain from 2 to 255 alphanumeric characters, or hyphens. Th |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateRelationalDatabaseSnapshotResult

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
def create_relational_database_snapshot(store, request: dict) -> dict:
    """Creates a snapshot of your database in Amazon Lightsail. You can use snapshots for backups, to make copies of a database, and to save data before deleting a database. The create relational database sn"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")
    relational_database_snapshot_name = request.get("relationalDatabaseSnapshotName", "").strip() if isinstance(request.get("relationalDatabaseSnapshotName"), str) else request.get("relationalDatabaseSnapshotName")
    if not relational_database_snapshot_name:
        raise ValidationException("relationalDatabaseSnapshotName is required")

    if store.relational_database_snapshots(relational_database_name):
        raise ResourceInUseException(f"Resource relational_database_name already exists")

    record = {
        "relationalDatabaseName": relational_database_name,
        "relationalDatabaseSnapshotName": relational_database_snapshot_name,
        "tags": tags,
    }

    store.relational_database_snapshots(relational_database_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
