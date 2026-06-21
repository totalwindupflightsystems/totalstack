# spec:trace: aws/lightsail/update_relational_database.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-relational-database
# spec:generated: DO NOT EDIT — edit the spec instead

def update_relational_database(store, request: dict) -> dict:
    """Allows the update of one or more attributes of a database in Amazon Lightsail. Updates are applied immediately, or in cases where the updates could result in an outage, are applied during the database"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_databases(relational_database_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_name not found")

    # Update mutable fields
    if "masterUserPassword" in request:
        resource["masterUserPassword"] = master_user_password
    if "rotateMasterUserPassword" in request:
        resource["rotateMasterUserPassword"] = rotate_master_user_password
    if "preferredBackupWindow" in request:
        resource["preferredBackupWindow"] = preferred_backup_window
    if "preferredMaintenanceWindow" in request:
        resource["preferredMaintenanceWindow"] = preferred_maintenance_window
    if "enableBackupRetention" in request:
        resource["enableBackupRetention"] = enable_backup_retention
    if "disableBackupRetention" in request:
        resource["disableBackupRetention"] = disable_backup_retention
    if "publiclyAccessible" in request:
        resource["publiclyAccessible"] = publicly_accessible
    if "applyImmediately" in request:
        resource["applyImmediately"] = apply_immediately
    if "caCertificateIdentifier" in request:
        resource["caCertificateIdentifier"] = ca_certificate_identifier
    if "relationalDatabaseBlueprintId" in request:
        resource["relationalDatabaseBlueprintId"] = relational_database_blueprint_id

    store.relational_databases(relational_database_name, resource)
    return resource

