
def execute_list_presets(store, request):
    """List presets."""
    max_results = min(request.get('MaxResults', 20), 100)
    next_token = request.get('NextToken', '')
    category = request.get('Category', '')
    list_order = request.get('ListOrder', 'ASCENDING')

    all_presets = list(store.presets.values())

    if category:
        all_presets = [p for p in all_presets if p.category == category]

    all_presets.sort(key=lambda p: p.name, reverse=(list_order == 'DESCENDING'))

    start_idx = 0
    if next_token:
        try:
            start_idx = int(next_token)
        except ValueError:
            start_idx = 0

    page = all_presets[start_idx:start_idx + max_results]

    result = {"Presets": [p.to_dict() for p in page]}
    if start_idx + max_results < len(all_presets):
        result["NextToken"] = str(start_idx + max_results)

    return result
