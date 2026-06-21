"""DescribeAccount handler."""


def handle_describe_account(store, request: dict) -> dict:
    account_id = request.get("AccountId", "")
    if not account_id:
        raise InvalidInputException("AccountId is required")

    account = store.describe_account(account_id=account_id)
    return {"Account": account.to_dict()}
