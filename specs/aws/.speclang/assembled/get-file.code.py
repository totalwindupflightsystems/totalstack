// spec:trace spec=/home/kara/totalstack/specs/aws/codecommit/get-file.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

@aws-operation: GetFile
@required: [repositoryName, filePath]
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, CommitDoesNotExistException, FileDoesNotExistException,
          PathRequiredException, InvalidPathException, FileTooLargeException]

import base64

def get_file(store, request):
    repository_name = request.get('repositoryName')
    file_path = request.get('filePath')
    commit_specifier = request.get('commitSpecifier')

    if not repository_name:
        raise ValidationException("repositoryName is required")
    if not file_path:
        raise ValidationException("filePath is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    # Determine which commit to read from
    if commit_specifier:
        commit_id = commit_specifier
    else:
        # Default to tip of default branch
        default_branch = store.repositories[repository_name].get('defaultBranch', 'main')
        branches = store.branches.get(repository_name, {})
        if default_branch in branches:
            commit_id = branches[default_branch].get('commitId')
        else:
            raise CommitDoesNotExistException("No commits in repository")
        if not commit_id:
            raise CommitDoesNotExistException("No commits in repository")

    commits = store.commits.get(repository_name, {})
    commit = commits.get(commit_id)
    if not commit:
        raise CommitDoesNotExistException(
            f"Commit {commit_id} does not exist"
        )

    # Get file from commit's stored files
    files = commit.get('_files', {})
    if file_path not in files:
        raise FileDoesNotExistException(
            f"File {file_path} does not exist in commit {commit_id}"
        )

    content = files[file_path]
    if isinstance(content, str):
        file_content_b64 = base64.b64encode(content.encode()).decode()
    else:
        file_content_b64 = base64.b64encode(content).decode()

    return {
        'commitId': commit_id,
        'blobId': hashlib.sha1(content.encode() if isinstance(content, str) else content).hexdigest(),
        'filePath': file_path,
        'fileSize': len(content),
        'fileContent': file_content_b64,
        'fileMode': 'NORMAL',
    }


import hashlib

class CommitDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class FileDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)