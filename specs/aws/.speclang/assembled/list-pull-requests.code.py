
@aws-operation: ListPullRequests
@required: [repositoryName]
@errors: [RepositoryDoesNotExistException, RepositoryNameRequiredException,
          InvalidRepositoryNameException, InvalidPullRequestStatusException]

def list_pull_requests(store, request):
    repository_name = request.get('repositoryName')
    pull_request_status = request.get('pullRequestStatus', 'OPEN')

    if not repository_name:
        raise ValidationException("repositoryName is required")

    if repository_name not in store.repositories:
        raise RepositoryDoesNotExistException(
            f"Repository {repository_name} does not exist"
        )

    if pull_request_status not in ('OPEN', 'CLOSED'):
        raise InvalidPullRequestStatusException(
            f"Invalid pull request status: {pull_request_status}"
        )

    prs = store.pull_requests.get(repository_name, {})
    matching = [
        pr_id for pr_id, pr in prs.items()
        if pr.get('pullRequestStatus') == pull_request_status
    ]

    return {
        'pullRequestIds': matching
    }


class InvalidPullRequestStatusException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RepositoryDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)