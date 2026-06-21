# spec:trace: aws/lightsail/get_relational_database_log_events.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-log-events
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_log_events(store, request: dict) -> dict:
    """Returns a list of log events for a database in Amazon Lightsail."""
    log_stream_name = request.get("logStreamName", "").strip() if isinstance(request.get("logStreamName"), str) else request.get("logStreamName")
    if not log_stream_name:
        raise ValidationException("logStreamName is required")
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_log_eventss(log_stream_name)
    if not resource:
        raise ResourceNotFoundException("Resource log_stream_name not found")
    return {"logStreamName": log_stream_name, **resource}

