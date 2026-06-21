// spec:trace spec=/home/kara/totalstack/specs/aws/codecommit/get-commit.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

@aws-operation: GetCommit
@required: [repositoryName, commitId]
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, CommitDoesNotExistException, CommitIdRequiredException,
          InvalidCommitIdException, CommitIdDoesNotExistException]

def get_commit(store, request):
    repository_name = request.get('repositoryName')
    commit_id = request.get('commitId')

    if not repository_name:
        raise ValidationException("repositoryName is required")
    if not commit_id:
        raise ValidationException("commitId is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    commits = store.commits.get(repository_name, {})
    if commit_id not in commits:
        raise CommitDoesNotExistException(
            f"Commit {commit_id} does not exist in repository {repository_name}"
        )

    return {
        'commit': commits[commit_id]
    }


class CommitDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)