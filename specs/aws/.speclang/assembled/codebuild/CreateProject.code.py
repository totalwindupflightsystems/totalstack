"""CreateProject handler for CodeBuild — validates input, stores project, returns response."""
import uuid


def create_project(store, request):
    """Create a new build project."""
    name = request.get('name', '').strip()
    if not name:
        raise InvalidInputException("Project name is required")
    if len(name) < 2 or len(name) > 255:
        raise InvalidInputException("Project name must be between 2 and 255 characters")

    source = request.get('source')
    if not source or source.get('type', '') not in ('CODECOMMIT', 'CODEPIPELINE', 'GITHUB', 'GITHUB_ENTERPRISE',
                                                      'BITBUCKET', 'S3', 'NO_SOURCE'):
        raise InvalidInputException("Valid source with type is required")

    environment = request.get('environment')
    if not environment:
        raise InvalidInputException("Environment is required")
    if environment.get('computeType', '') not in ('BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_MEDIUM',
                                                     'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_XLARGE',
                                                     'BUILD_GENERAL1_2XLARGE', 'BUILD_LAMBDA_1GB',
                                                     'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB',
                                                     'BUILD_LAMBDA_8GB', 'BUILD_LAMBDA_10GB',
                                                     'ATTRIBUTE_BASED_COMPUTE'):
        raise InvalidInputException("Invalid compute type")

    artifacts = request.get('artifacts', {})
    if artifacts.get('type', '') not in ('CODEPIPELINE', 'S3', 'NO_ARTIFACTS'):
        raise InvalidInputException("Valid artifacts with type is required")

    service_role = request.get('serviceRole', '').strip()
    if not service_role:
        raise InvalidInputException("serviceRole is required")

    # Use dict-based project since we don't have the full ProjectRecord class
    project = store.projects.create_project(
        name=name,
        source=source,
        environment=environment,
        artifacts=artifacts,
        service_role=service_role,
        description=request.get('description', ''),
        timeoutInMinutes=request.get('timeoutInMinutes', 60),
        queuedTimeoutInMinutes=request.get('queuedTimeoutInMinutes', 480),
        encryptionKey=request.get('encryptionKey', ''),
        tags=request.get('tags', []),
        badgeEnabled=request.get('badgeEnabled', False),
        cache=request.get('cache'),
        concurrentBuildLimit=request.get('concurrentBuildLimit', 1),
        buildBatchConfig=request.get('buildBatchConfig'),
        fileSystemLocations=request.get('fileSystemLocations', []),
        logsConfig=request.get('logsConfig'),
        secondaryArtifacts=request.get('secondaryArtifacts', []),
        secondarySources=request.get('secondarySources', []),
        secondarySourceVersions=request.get('secondarySourceVersions', []),
        sourceVersion=request.get('sourceVersion', ''),
        vpcConfig=request.get('vpcConfig'),
        visibility=request.get('projectVisibility', 'PRIVATE'),
    )

    return {'project': project.to_dict()}
