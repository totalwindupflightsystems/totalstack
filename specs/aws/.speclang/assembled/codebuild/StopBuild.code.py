"""StopBuild handler for CodeBuild."""

def stop_build(store, request):
    """Stop a running build."""
    build_id = request.get('id', '').strip()
    if not build_id:
        raise InvalidInputException("Build id is required")

    build = store.builds.stop_build(build_id)
    return {'build': build.to_dict()}
