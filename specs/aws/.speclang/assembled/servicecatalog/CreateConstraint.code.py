"""Handler for CreateConstraint — AWS Service Catalog."""
def execute_create_constraint(store, request):
    portfolio_id = request.get("PortfolioId", "")
    product_id = request.get("ProductId", "")
    type = request.get("Type")
    parameters = request.get("Parameters")
    if not type:
        raise InvalidParametersException("Type is required")
    if not parameters:
        raise InvalidParametersException("Parameters is required")
    desc = request.get("Description", "")
    result = store.create_constraint(portfolio_id, product_id, type, parameters, desc)
    return {"ConstraintDetail": result}
