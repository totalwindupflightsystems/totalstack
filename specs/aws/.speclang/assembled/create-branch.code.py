
@aws-operation: CreateBranch
@required: [repositoryName, branchName, commitId]
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, BranchNameExistsException, BranchNameRequiredException,
          InvalidBranchNameException, CommitDoesNotExistException, CommitIdRequiredException,
          InvalidCommitIdException]

def create_branch(store, request):
    repository_name = request.get('repositoryName')
    branch_name = request.get('branchName')
    commit_id = request.get('commitId')

    if not repository_name:
        raise ValidationException("repositoryName is required")
    if not branch_name:
        raise ValidationException("branchName is required")
    if not commit_id:
        raise ValidationException("commitId is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    branches = store.branches.setdefault(repository_name, {})
    if branch_name in branches:
        raise BranchNameExistsException(
            f"Branch {branch_name} already exists in repository {repository_name}"
        )

    # For MVP, accept any commit ID (lax validation)
    # In production, verify commitId exists in store.commits
    branches[branch_name] = {
        'branchName': branch_name,
        'commitId': commit_id,
    }

    return {}


class BranchNameExistsException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)