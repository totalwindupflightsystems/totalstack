"""ListBuildsForProject handler for CodeBuild."""

def list_builds_for_project(store, request):
    """List builds for a specific project."""
    project_name = request.get('projectName', '').strip()
    if not project_name:
        raise InvalidInputException("projectName is required")

    sort_order = request.get('sortOrder', 'ASCENDING')
    next_token = request.get('nextToken')

    if sort_order not in ('ASCENDING', 'DESCENDING'):
        raise InvalidInputException(f"Invalid sortOrder: {sort_order}")

    ids = store.builds.list_builds_for_project(
        project_name, sort_order=sort_order, next_token=next_token
    )
    result = {'ids': ids}
    return result
