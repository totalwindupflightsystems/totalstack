"""Handler for DescribePortfolio — AWS Service Catalog."""
def execute_describe_portfolio(store, request):
    portfolio_id = request.get("Id")
    if not portfolio_id:
        raise InvalidParametersException("Id is required")
    result = store.get_portfolio(portfolio_id)
    return {"PortfolioDetail": result}
