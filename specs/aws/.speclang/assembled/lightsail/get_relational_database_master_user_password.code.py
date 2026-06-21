# spec:trace: aws/lightsail/get_relational_database_master_user_password.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-master-user-password
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_master_user_password(store, request: dict) -> dict:
    """Returns the current, previous, or pending versions of the master user password for a Lightsail database. The GetRelationalDatabaseMasterUserPassword operation supports tag-based access control via res"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_master_user_passwords(relational_database_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}

