def handler(store, request):
    next_token = request.get("NextToken")
    max_results = request.get("MaxResults")
    inclusion_filters = request.get("InclusionFilters")
    return store.list_protections(next_token=next_token, max_results=max_results, inclusion_filters=inclusion_filters)
