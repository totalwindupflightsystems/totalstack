"""Handler for DescribeConstraint — AWS Service Catalog."""
def execute_describe_constraint(store, request):
    constraint_id = request.get("Id")
    if not constraint_id:
        raise InvalidParametersException("Id is required")
    result = store.get_constraint(constraint_id)
    return {"ConstraintDetail": result}
