"""Handler for SearchProducts — AWS Service Catalog."""
def execute_search_products(store, request):
    result = store.search_products()
    return {"ProductViewSummaries": result}
