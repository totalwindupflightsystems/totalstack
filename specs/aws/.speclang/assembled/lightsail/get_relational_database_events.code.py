# spec:trace: aws/lightsail/get_relational_database_events.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-events
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_events(store, request: dict) -> dict:
    """Returns a list of events for a specific database in Amazon Lightsail."""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_eventss(relational_database_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}

