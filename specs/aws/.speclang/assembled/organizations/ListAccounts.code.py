"""ListAccounts handler."""


def handle_list_accounts(store, request: dict) -> dict:
    next_token = request.get("NextToken")
    max_results = request.get("MaxResults", 20)

    result = store.list_accounts(next_token=next_token, max_results=max_results)
    return result
