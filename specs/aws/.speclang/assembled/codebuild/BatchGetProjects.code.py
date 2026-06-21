"""BatchGetProjects handler for CodeBuild."""

def batch_get_projects(store, request):
    """Get information about multiple build projects."""
    names = request.get('names', [])
    if not names:
        raise InvalidInputException("names is required")
    projects, projects_not_found = store.projects.batch_get_projects(names)
    result = {'projects': [p.to_dict() for p in projects]}
    if projects_not_found:
        result['projectsNotFound'] = projects_not_found
    return result
