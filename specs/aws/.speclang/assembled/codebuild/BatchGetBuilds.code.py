"""BatchGetBuilds handler for CodeBuild."""

def batch_get_builds(store, request):
    """Get information about multiple builds."""
    ids = request.get('ids', [])
    if not ids:
        raise InvalidInputException("ids is required")

    builds, builds_not_found = store.builds.batch_get_builds(ids)
    result = {'builds': [b.to_dict() for b in builds]}
    if builds_not_found:
        result['buildsNotFound'] = builds_not_found
    return result
