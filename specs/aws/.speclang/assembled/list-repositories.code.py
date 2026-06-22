
@aws-operation: ListRepositories
@required: []
@errors: [InvalidSortByException, InvalidOrderException, InvalidContinuationTokenException]

def list_repositories(store, request):
    sort_by = request.get('sortBy', 'repositoryName')
    order = request.get('order', 'ascending')
    next_token = request.get('nextToken')
    max_results = request.get('maxResults', 25)

    # Validate sort
    valid_sort = ['repositoryName', 'lastModifiedDate']
    if sort_by not in valid_sort:
        raise InvalidSortByException(f"Invalid sortBy: {sort_by}")

    # Validate order
    valid_order = ['ascending', 'descending']
    if order not in valid_order:
        raise InvalidOrderException(f"Invalid order: {order}")

    # Get all repos
    repos = list(store.repositories.values())

    # Sort
    if sort_by == 'repositoryName':
        repos.sort(key=lambda r: r['repositoryName'], reverse=(order == 'descending'))
    elif sort_by == 'lastModifiedDate':
        repos.sort(key=lambda r: r['lastModifiedDate'], reverse=(order == 'descending'))

    # Paginate (simple: return all for MVP)
    return {
        'repositories': [{'repositoryName': r['repositoryName'],
                          'repositoryId': r['repositoryId']} for r in repos]
    }


class InvalidSortByException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidOrderException(Exception):
    def __init__(self, message):
        super().__init__(message)