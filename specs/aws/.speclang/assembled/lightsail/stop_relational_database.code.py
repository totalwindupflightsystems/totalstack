# spec:trace: aws/lightsail/stop_relational_database.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/stop-relational-database
# spec:generated: DO NOT EDIT — edit the spec instead

def stop_relational_database(store, request: dict) -> dict:
    """Stops a specific database that is currently running in Amazon Lightsail. If you don't manually start your database instance after it has been stopped for seven consecutive days, Amazon Lightsail autom"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")

    if not store.relational_databases(relational_database_name):
        raise ResourceNotFoundException("Resource relational_database_name not found")
    store.delete_relational_databases(relational_database_name)
    return {}

