"""StartBuild handler for CodeBuild."""

def start_build(store, request):
    """Start a new build."""
    project_name = request.get('projectName', '').strip()
    if not project_name:
        raise InvalidInputException("projectName is required")

    # Verify project exists
    store.projects.get_project(project_name)

    build = store.builds.start_build(
        project_name=project_name,
        sourceVersion=request.get('sourceVersion', ''),
        timeoutInMinutes=request.get('timeoutInMinutesOverride', 60),
        queuedTimeoutInMinutes=request.get('queuedTimeoutInMinutesOverride', 480),
        environmentVariablesOverride=request.get('environmentVariablesOverride'),
        sourceTypeOverride=request.get('sourceTypeOverride'),
        sourceLocationOverride=request.get('sourceLocationOverride'),
        artifactsOverride=request.get('artifactsOverride'),
        cacheOverride=request.get('cacheOverride'),
        initiator=request.get('idempotencyToken', ''),
    )

    return {'build': build.to_dict()}
