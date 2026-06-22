
@aws-operation: DeleteRepository
@required: [repositoryName]
@errors: [RepositoryNameRequiredException, InvalidRepositoryNameException,
          EncryptionIntegrityChecksFailedException, EncryptionKeyAccessDeniedException,
          EncryptionKeyDisabledException, EncryptionKeyNotFoundException, EncryptionKeyUnavailableException]

def delete_repository(store, request):
    repository_name = request.get('repositoryName')

    if not repository_name:
        raise ValidationException("repositoryName is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    repository_id = store.repositories[repository_name]['repositoryId']
    del store.repositories[repository_name]
    store.branches.pop(repository_name, None)
    store.commits.pop(repository_name, None)
    store.pull_requests.pop(repository_name, None)

    return {
        'repositoryId': repository_id
    }


class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)