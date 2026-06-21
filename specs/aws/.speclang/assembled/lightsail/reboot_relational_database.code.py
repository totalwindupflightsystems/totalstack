# spec:trace: aws/lightsail/reboot_relational_database.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/reboot-relational-database
# spec:generated: DO NOT EDIT — edit the spec instead

def reboot_relational_database(store, request: dict) -> dict:
    """Restarts a specific database in Amazon Lightsail. The reboot relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseN"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RebootRelationalDatabase", request)

