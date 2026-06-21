"""ListBuilds handler for CodeBuild."""

def list_builds(store, request):
    """List all builds."""
    sort_order = request.get('sortOrder', 'ASCENDING')
    next_token = request.get('nextToken')

    if sort_order not in ('ASCENDING', 'DESCENDING'):
        raise InvalidInputException(f"Invalid sortOrder: {sort_order}")

    ids = store.builds.list_builds(sort_order=sort_order, next_token=next_token)
    result = {'ids': ids}
    return result
