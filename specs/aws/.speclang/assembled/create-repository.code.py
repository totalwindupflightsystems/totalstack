
@aws-operation: CreateRepository
@required: [repositoryName]
@errors: [RepositoryNameExistsException, RepositoryNameRequiredException, InvalidRepositoryNameException,
          RepositoryLimitExceededException, EncryptionIntegrityChecksFailedException,
          EncryptionKeyAccessDeniedException, EncryptionKeyDisabledException,
          EncryptionKeyNotFoundException, EncryptionKeyUnavailableException]

import uuid, time

def create_repository(store, request):
    repository_name = request.get('repositoryName')
    repository_description = request.get('repositoryDescription', '')
    tags = request.get('tags', {})

    # Validation
    if not repository_name:
        raise ValidationException("repositoryName is required")
    if not repository_name or len(repository_name) < 1 or len(repository_name) > 100:
        raise InvalidRepositoryNameException(
            "Repository name must be between 1 and 100 characters"
        )
    if repository_name in store.repositories:
        raise RepositoryNameExistsException(
            f"Repository named {repository_name} already exists"
        )

    # Create repository
    now = time.time()
    repo_id = str(uuid.uuid4())
    arn = f"arn:aws:codecommit:us-east-1:000000000000:{repository_name}"
    default_branch = request.get('defaultBranch', 'main')

    repository = {
        'repositoryName': repository_name,
        'repositoryId': repo_id,
        'repositoryDescription': repository_description,
        'defaultBranch': default_branch,
        'arn': arn,
        'cloneUrlHttp': f"https://git-codecommit.us-east-1.amazonaws.com/v1/repos/{repository_name}",
        'cloneUrlSsh': f"ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/{repository_name}",
        'creationDate': now,
        'lastModifiedDate': now,
        'tags': tags,
    }

    store.repositories[repository_name] = repository

    # Initialize default branch
    store.branches.setdefault(repository_name, {})
    store.commits.setdefault(repository_name, {})

    return {
        'repositoryMetadata': repository
    }


class RepositoryNameExistsException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidRepositoryNameException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)