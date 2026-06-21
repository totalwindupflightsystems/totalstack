"""Handler for DeletePortfolio — AWS Service Catalog."""
def execute_delete_portfolio(store, request):
    portfolio_id = request.get("Id")
    if not portfolio_id:
        raise InvalidParametersException("Id is required")
    store.delete_portfolio(portfolio_id)
    return {}
