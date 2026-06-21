// spec:trace spec=/home/kara/totalstack/specs/aws/codecommit/create-commit.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

@aws-operation: CreateCommit
@required: [repositoryName, branchName]
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, BranchDoesNotExistException, BranchNameRequiredException,
          InvalidBranchNameException, ParentCommitIdRequiredException]

import uuid, time, hashlib

def create_commit(store, request):
    repository_name = request.get('repositoryName')
    branch_name = request.get('branchName')
    parent_commit_id = request.get('parentCommitId')
    commit_message = request.get('commitMessage', '')
    put_files = request.get('putFiles', [])
    delete_files = request.get('deleteFiles', [])
    author_name = request.get('authorName', 'TotalStack User')
    email = request.get('email', 'user@totalstack.local')

    if not repository_name:
        raise ValidationException("repositoryName is required")
    if not branch_name:
        raise ValidationException("branchName is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    branches = store.branches.setdefault(repository_name, {})
    if branch_name not in branches:
        raise BranchDoesNotExistException(
            f"Branch {branch_name} does not exist in repository {repository_name}"
        )

    # Create commit
    now = int(time.time())
    commit_id = hashlib.sha1(f"{repository_name}:{branch_name}:{now}:{uuid.uuid4()}".encode()).hexdigest()
    tree_id = hashlib.sha1(f"{repository_name}:{commit_id}:tree".encode()).hexdigest()

    commit = {
        'commitId': commit_id,
        'treeId': tree_id,
        'message': commit_message,
        'author': {'name': author_name, 'email': email, 'date': now},
        'committer': {'name': author_name, 'email': email, 'date': now},
        'parents': [parent_commit_id] if parent_commit_id else [],
        'additionalData': '',
    }

    store.commits.setdefault(repository_name, {})[commit_id] = commit

    # Update branch pointer
    branches[branch_name]['commitId'] = commit_id

    # Store file changes in commit
    file_changes = {}
    for pf in put_files:
        file_changes[pf.get('filePath')] = pf.get('fileContent', '')
    commit['_files'] = file_changes

    return {
        'commitId': commit_id,
        'treeId': tree_id,
        'filesAdded': [pf.get('filePath') for pf in put_files],
        'filesDeleted': [df.get('filePath') for df in delete_files],
        'filesUpdated': [],
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