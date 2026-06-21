// spec:trace spec=/home/kara/totalstack/specs/aws/codecommit/get-branch.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

@aws-operation: GetBranch
@required: []
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, BranchDoesNotExistException,
          BranchNameRequiredException, InvalidBranchNameException]

def get_branch(store, request):
    repository_name = request.get('repositoryName')
    branch_name = request.get('branchName')

    if not repository_name:
        raise ValidationException("repositoryName is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    # Default to repo's default branch if branch_name not specified
    if not branch_name:
        branch_name = store.repositories[repository_name].get('defaultBranch', 'main')

    branches = store.branches.get(repository_name, {})
    if branch_name not in branches:
        raise BranchDoesNotExistException(
            f"Branch {branch_name} does not exist in repository {repository_name}"
        )

    return {
        'branch': branches[branch_name]
    }


class BranchDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)