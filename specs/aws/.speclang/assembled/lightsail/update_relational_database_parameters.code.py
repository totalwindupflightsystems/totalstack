# spec:trace: aws/lightsail/update_relational_database_parameters.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-relational-database-parameters
# spec:generated: DO NOT EDIT — edit the spec instead

def update_relational_database_parameters(store, request: dict) -> dict:
    """Allows the update of one or more parameters of a database in Amazon Lightsail. Parameter updates don't cause outages; therefore, their application is not subject to the preferred maintenance window. H"""
    parameters = request.get("parameters", "").strip() if isinstance(request.get("parameters"), str) else request.get("parameters")
    if not parameters:
        raise ValidationException("parameters is required")
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    resource = store.relational_database_parameterss(relational_database_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_name not found")

    # Update mutable fields

    store.relational_database_parameterss(relational_database_name, resource)
    return resource

