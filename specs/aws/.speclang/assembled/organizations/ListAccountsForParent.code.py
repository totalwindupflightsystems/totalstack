"""ListAccountsForParent handler."""


def handle_list_accounts_for_parent(store, request: dict) -> dict:
    parent_id = request.get("ParentId", "")
    if not parent_id:
        raise InvalidInputException("ParentId is required")

    next_token = request.get("NextToken")
    max_results = request.get("MaxResults", 20)

    result = store.list_accounts_for_parent(
        parent_id=parent_id, next_token=next_token, max_results=max_results,
    )
    return result
