"""Handler for ListPortfolios — AWS Service Catalog."""
def execute_list_portfolios(store, request):
    result = store.list_portfolios()
    return {"PortfolioDetails": result}
