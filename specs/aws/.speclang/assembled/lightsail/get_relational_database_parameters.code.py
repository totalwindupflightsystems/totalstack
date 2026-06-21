# spec:trace: aws/lightsail/get_relational_database_parameters.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-parameters
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_parameters(store, request: dict) -> dict:
    """Returns all of the runtime parameters offered by the underlying database software, or engine, for a specific database in Amazon Lightsail. In addition to the parameter names and values, this operation"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_parameterss(relational_database_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_name not found")
    return {"relationalDatabaseName": relational_database_name, **resource}

