# spec:trace: aws/lightsail/start_relational_database.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/start-relational-database
# spec:generated: DO NOT EDIT — edit the spec instead

def start_relational_database(store, request: dict) -> dict:
    """Starts a specific database from a stopped state in Amazon Lightsail. To restart a database, use the reboot relational database operation. The start relational database operation supports tag-based acc"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    if store.relational_databases(relational_database_name):
        raise ResourceInUseException("Resource relational_database_name already exists")

    record = {
        "relationalDatabaseName": relational_database_name,
    }

    store.relational_databases(relational_database_name, record)

    return {
        "operations": record.get("operations", {}),
    }

