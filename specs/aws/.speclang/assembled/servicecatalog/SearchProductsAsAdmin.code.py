"""Handler for SearchProductsAsAdmin — AWS Service Catalog."""
def execute_search_products_as_admin(store, request):
    result = store.search_products()
    return {"ProductViewDetails": [{"ProductViewSummary": r} for r in result]}
