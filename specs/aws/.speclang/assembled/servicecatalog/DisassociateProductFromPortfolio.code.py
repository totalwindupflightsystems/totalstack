"""Handler for DisassociateProductFromPortfolio — AWS Service Catalog."""
def execute_disassociate_product_from_portfolio(store, request):
    portfolio_id = request.get("PortfolioId")
    product_id = request.get("ProductId")
    if not portfolio_id:
        raise InvalidParametersException("PortfolioId is required")
    if not product_id:
        raise InvalidParametersException("ProductId is required")
    store.disassociate_product_from_portfolio(portfolio_id, product_id)
    return {}
