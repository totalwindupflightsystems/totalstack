# spec:trace: aws/lightsail/get_relational_database_log_streams.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-log-streams
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_log_streams(store, request: dict) -> dict:
    """Returns a list of available log streams for a specific database in Amazon Lightsail."""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_log_streamss(relational_database_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}

