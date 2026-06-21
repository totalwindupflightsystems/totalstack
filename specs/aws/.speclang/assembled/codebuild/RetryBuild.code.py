"""RetryBuild handler for CodeBuild."""

def retry_build(store, request):
    """Retry a failed build."""
    build_id = request.get('id', '').strip()
    if not build_id:
        raise InvalidInputException("Build id is required")

    # Get original build to copy project name
    original = store.builds.get_build(build_id)
    
    build = store.builds.start_build(
        project_name=original.projectName,
        idempotencyToken=request.get('idempotencyToken', ''),
    )

    return {'build': build.to_dict()}
