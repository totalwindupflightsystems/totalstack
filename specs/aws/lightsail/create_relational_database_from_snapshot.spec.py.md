---
id: "@specs/aws/lightsail/create_relational_database_from_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateRelationalDatabaseFromSnapshot"
---

# CreateRelationalDatabaseFromSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_relational_database_from_snapshot
> **spec:implements:** @kind:operation CreateRelationalDatabaseFromSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateRelationalDatabaseFromSnapshot.spec.md

Creates a new database from an existing database snapshot in Amazon Lightsail. You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to a different plan, such as a high availability or standard plan. The create relational database from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by relationalDatabaseSnapshotName. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateRelationalDatabaseFromSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| availabilityZone | Any  # complex shape |  | The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format. You can get a list |
| publiclyAccessible | Any  # complex shape |  | Specifies the accessibility options for your new database. A value of true specifies a database that is available to res |
| relationalDatabaseBundleId | Any  # complex shape |  | The bundle ID for your new database. A bundle describes the performance specifications for your database. You can get a  |
| relationalDatabaseName | Any  # complex shape | ✓ | The name to use for your new Lightsail database resource. Constraints: Must contain from 2 to 255 alphanumeric character |
| relationalDatabaseSnapshotName | Any  # complex shape |  | The name of the database snapshot from which to create your new database. |
| restoreTime | Any  # complex shape |  | The date and time to restore your database from. Constraints: Must be before the latest restorable time for the database |
| sourceRelationalDatabaseName | Any  # complex shape |  | The name of the source database. |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |
| useLatestRestorableTime | Any  # complex shape |  | Specifies whether your database is restored from the latest backup time. A value of true restores from the latest backup |

## Output Shape: CreateRelationalDatabaseFromSnapshotResult

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
def create_relational_database_from_snapshot(store, request: dict) -> dict:
    """Creates a new database from an existing database snapshot in Amazon Lightsail. You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to """
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    if store.relational_database_from_snapshots(relational_database_name):
        raise ResourceInUseException(f"Resource relational_database_name already exists")

    record = {
        "relationalDatabaseName": relational_database_name,
        "availabilityZone": availability_zone,
        "publiclyAccessible": publicly_accessible,
        "relationalDatabaseSnapshotName": relational_database_snapshot_name,
        "relationalDatabaseBundleId": relational_database_bundle_id,
        "sourceRelationalDatabaseName": source_relational_database_name,
        "restoreTime": restore_time,
        "useLatestRestorableTime": use_latest_restorable_time,
        "tags": tags,
    }

    store.relational_database_from_snapshots(relational_database_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
