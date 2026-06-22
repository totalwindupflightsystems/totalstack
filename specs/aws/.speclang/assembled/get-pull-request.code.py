
@aws-operation: GetPullRequest
@required: [pullRequestId]
@errors: [PullRequestDoesNotExistException, InvalidPullRequestIdException,
          PullRequestIdRequiredException]

def get_pull_request(store, request):
    pull_request_id = request.get('pullRequestId')

    if not pull_request_id:
        raise ValidationException("pullRequestId is required")

    # Search all repos for the PR
    for repo_name, prs in store.pull_requests.items():
        if pull_request_id in prs:
            return {
                'pullRequest': prs[pull_request_id]
            }

    raise PullRequestDoesNotExistException(
        f"Pull request {pull_request_id} does not exist"
    )


class PullRequestDoesNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)