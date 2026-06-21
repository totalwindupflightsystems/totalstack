---
id: "@specs/aws/lightsail/create_relational_database"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateRelationalDatabase"
---

# CreateRelationalDatabase

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_relational_database
> **spec:implements:** @kind:operation CreateRelationalDatabase
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateRelationalDatabase.spec.md

Creates a new database in Amazon Lightsail. The create relational database operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateRelationalDatabaseRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| availabilityZone | Any  # complex shape |  | The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format. You can get a list |
| masterDatabaseName | Any  # complex shape | ✓ | The meaning of this parameter differs according to the database engine you use. MySQL The name of the database to create |
| masterUserPassword | Any  # complex shape |  | The password for the master user. The password can include any printable ASCII character except "/", """, or "@". It can |
| masterUsername | Any  # complex shape | ✓ | The name for the master user. MySQL Constraints: Required for MySQL. Must be 1 to 16 letters or numbers. Can contain und |
| preferredBackupWindow | Any  # complex shape |  | The daily time range during which automated backups are created for your new database if automated backups are enabled.  |
| preferredMaintenanceWindow | Any  # complex shape |  | The weekly time range during which system maintenance can occur on your new database. The default is a 30-minute window  |
| publiclyAccessible | Any  # complex shape |  | Specifies the accessibility options for your new database. A value of true specifies a database that is available to res |
| relationalDatabaseBlueprintId | Any  # complex shape | ✓ | The blueprint ID for your new database. A blueprint describes the major engine version of a database. You can get a list |
| relationalDatabaseBundleId | Any  # complex shape | ✓ | The bundle ID for your new database. A bundle describes the performance specifications for your database. You can get a  |
| relationalDatabaseName | Any  # complex shape | ✓ | The name to use for your new Lightsail database resource. Constraints: Must contain from 2 to 255 alphanumeric character |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateRelationalDatabaseResult

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
def create_relational_database(store, request: dict) -> dict:
    """Creates a new database in Amazon Lightsail. The create relational database operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide """
    master_database_name = request.get("masterDatabaseName", "").strip() if isinstance(request.get("masterDatabaseName"), str) else request.get("masterDatabaseName")
    if not master_database_name:
        raise ValidationException("masterDatabaseName is required")
    master_username = request.get("masterUsername", "").strip() if isinstance(request.get("masterUsername"), str) else request.get("masterUsername")
    if not master_username:
        raise ValidationException("masterUsername is required")
    relational_database_blueprint_id = request.get("relationalDatabaseBlueprintId", "").strip() if isinstance(request.get("relationalDatabaseBlueprintId"), str) else request.get("relationalDatabaseBlueprintId")
    if not relational_database_blueprint_id:
        raise ValidationException("relationalDatabaseBlueprintId is required")
    relational_database_bundle_id = request.get("relationalDatabaseBundleId", "").strip() if isinstance(request.get("relationalDatabaseBundleId"), str) else request.get("relationalDatabaseBundleId")
    if not relational_database_bundle_id:
        raise ValidationException("relationalDatabaseBundleId is required")
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    if store.relational_databases(master_database_name):
        raise ResourceInUseException(f"Resource master_database_name already exists")

    record = {
        "relationalDatabaseName": relational_database_name,
        "availabilityZone": availability_zone,
        "relationalDatabaseBlueprintId": relational_database_blueprint_id,
        "relationalDatabaseBundleId": relational_database_bundle_id,
        "masterDatabaseName": master_database_name,
        "masterUsername": master_username,
        "masterUserPassword": master_user_password,
        "preferredBackupWindow": preferred_backup_window,
        "preferredMaintenanceWindow": preferred_maintenance_window,
        "publiclyAccessible": publicly_accessible,
        "tags": tags,
    }

    store.relational_databases(master_database_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
