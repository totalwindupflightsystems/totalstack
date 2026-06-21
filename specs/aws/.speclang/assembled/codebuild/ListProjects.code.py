"""ListProjects handler for CodeBuild."""

def list_projects(store, request):
    """List all build projects."""
    sort_by = request.get('sortBy', 'NAME')
    sort_order = request.get('sortOrder', 'ASCENDING')
    next_token = request.get('nextToken')
    
    if sort_by not in ('NAME', 'CREATED_TIME', 'LAST_MODIFIED_TIME'):
        raise InvalidInputException(f"Invalid sortBy: {sort_by}")
    if sort_order not in ('ASCENDING', 'DESCENDING'):
        raise InvalidInputException(f"Invalid sortOrder: {sort_order}")

    names = store.projects.list_projects(sort_by=sort_by, sort_order=sort_order, next_token=next_token)
    result = {'projects': names}
    return result
