"""Handler for DeleteConstraint — AWS Service Catalog."""
def execute_delete_constraint(store, request):
    constraint_id = request.get("Id")
    if not constraint_id:
        raise InvalidParametersException("Id is required")
    store.delete_constraint(constraint_id)
    return {}
