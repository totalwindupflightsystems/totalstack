// spec:trace spec=/home/kara/totalstack/specs/aws/codecommit/create-pull-request.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

@aws-operation: CreatePullRequest
@required: [title, targets]
@errors: [RepositoryNameRequiredException, RepositoryDoesNotExistException, InvalidRepositoryNameException,
          TitleRequiredException, InvalidTitleException, TargetsRequiredException, InvalidTargetsException,
          ReferenceDoesNotExistException, MaximumOpenPullRequestsExceededException]

import uuid, time

def create_pull_request(store, request):
    title = request.get('title')
    description = request.get('description', '')
    targets = request.get('targets', [])
    client_request_token = request.get('clientRequestToken')

    if not title:
        raise ValidationException("title is required")
    if not targets:
        raise ValidationException("targets is required")

    # Extract repository from first target
    if not targets or 'repositoryName' not in targets[0]:
        raise InvalidTargetsException("Each target must have repositoryName")

    repository_name = targets[0]['repositoryName']
    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    # Validate source/destination references exist
    source_ref = targets[0].get('sourceReference')
    destination_ref = targets[0].get('destinationReference')

    branches = store.branches.get(repository_name, {})
    if source_ref and source_ref not in branches and not source_ref.startswith('refs/'):
        raise ReferenceDoesNotExistException(f"Source reference {source_ref} does not exist")
    if destination_ref and destination_ref not in branches and not destination_ref.startswith('refs/'):
        raise ReferenceDoesNotExistException(f"Destination reference {destination_ref} does not exist")

    now = time.time()
    pr_id = str(uuid.uuid4())

    pull_request = {
        'pullRequestId': pr_id,
        'title': title,
        'description': description,
        'authorArn': 'arn:aws:iam::000000000000:user/test-user',
        'pullRequestStatus': 'OPEN',
        'creationDate': now,
        'lastModifiedDate': now,
        'pullRequestTargets': targets,
        'revisionId': hashlib.sha1(f"{pr_id}:{now}".encode()).hexdigest(),
    }

    store.pull_requests.setdefault(repository_name, {})[pr_id] = pull_request

    return {
        'pullRequest': pull_request
    }


import hashlib

class InvalidTargetsException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ReferenceDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)