// spec:trace spec=/home/kara/totalstack/specs/aws/codecommit/get-repository.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

@aws-operation: GetRepository
@required: [repositoryName]
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, EncryptionIntegrityChecksFailedException]

def get_repository(store, request):
    repository_name = request.get('repositoryName')

    if not repository_name:
        raise ValidationException("repositoryName is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    return {
        'repositoryMetadata': store.repositories[repository_name]
    }


class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)