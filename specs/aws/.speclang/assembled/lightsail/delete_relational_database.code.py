# spec:trace: aws/lightsail/delete_relational_database.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-relational-database
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_relational_database(store, request: dict) -> dict:
    """Deletes a database in Amazon Lightsail. The delete relational database operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For m"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")

    if not store.relational_databases(relational_database_name):
        raise ResourceNotFoundException("Resource relational_database_name not found")
    store.delete_relational_databases(relational_database_name)
    return {}

