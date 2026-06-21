// spec:trace spec=/home/kara/totalstack/specs/aws/codecommit/list-branches.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

@aws-operation: ListBranches
@required: [repositoryName]
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, InvalidContinuationTokenException]

def list_branches(store, request):
    repository_name = request.get('repositoryName')

    if not repository_name:
        raise ValidationException("repositoryName is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    branches = store.branches.get(repository_name, {})
    branch_list = list(branches.values())
    branch_list.sort(key=lambda b: b.get('branchName', ''))

    return {
        'branches': branch_list
    }


class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)