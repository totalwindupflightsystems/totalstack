"""DeleteProject handler for CodeBuild."""

def delete_project(store, request):
    """Delete a build project."""
    name = request.get('name', '').strip()
    if not name:
        raise InvalidInputException("Project name is required")
    store.projects.delete_project(name)
    return {}
