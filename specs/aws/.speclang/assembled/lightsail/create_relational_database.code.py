# spec:trace: aws/lightsail/create_relational_database.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-relational-database
# spec:generated: DO NOT EDIT — edit the spec instead

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
        raise ResourceInUseException("Resource master_database_name already exists")

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

