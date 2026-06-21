"""Handler for UpdatePortfolio — AWS Service Catalog."""
def execute_update_portfolio(store, request):
    portfolio_id = request.get("Id")
    if not portfolio_id:
        raise InvalidParametersException("Id is required")
    display_name = request.get("DisplayName", "")
    provider_name = request.get("ProviderName", "")
    description = request.get("Description", "")
    result = store.update_portfolio(portfolio_id, display_name, provider_name, description)
    return {"PortfolioDetail": result}
