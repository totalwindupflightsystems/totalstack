"""Handler for AssociateProductWithPortfolio — AWS Service Catalog."""
def execute_associate_product_with_portfolio(store, request):
    portfolio_id = request.get("PortfolioId")
    product_id = request.get("ProductId")
    if not portfolio_id:
        raise InvalidParametersException("PortfolioId is required")
    if not product_id:
        raise InvalidParametersException("ProductId is required")
    store.associate_product_with_portfolio(portfolio_id, product_id)
    return {}
