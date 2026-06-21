"""Handler for CreatePortfolio — AWS Service Catalog."""
def execute_create_portfolio(store, request):
    display_name = request.get("DisplayName")
    provider_name = request.get("ProviderName")
    if not display_name:
        raise InvalidParametersException("DisplayName is required")
    if not provider_name:
        raise InvalidParametersException("ProviderName is required")
    desc = request.get("Description", "")
    result = store.create_portfolio(display_name, provider_name, desc)
    return {"PortfolioDetail": result}
