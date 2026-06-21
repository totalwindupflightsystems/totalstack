"""BatchDeleteBuilds handler for CodeBuild."""

def batch_delete_builds(store, request):
    """Delete multiple builds."""
    ids = request.get('ids', [])
    if not ids:
        raise InvalidInputException("ids is required")

    deleted = []
    not_found = []
    for bid in ids:
        try:
            store.builds.delete_build(bid)
            deleted.append(bid)
        except ResourceNotFoundException:
            not_found.append(bid)

    result = {'buildsDeleted': deleted}
    if not_found:
        result['buildsNotDeleted'] = [{'id': x, 'statusCode': '404'} for x in not_found]
    return result
