# spec:trace: aws/lightsail/get_relational_database.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database(store, request: dict) -> dict:
    """Returns information about a specific database in Amazon Lightsail."""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_databases(relational_database_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}

