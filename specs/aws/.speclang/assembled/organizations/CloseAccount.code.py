"""CloseAccount handler."""


def handle_close_account(store, request: dict) -> dict:
    account_id = request.get("AccountId", "")
    if not account_id:
        raise InvalidInputException("AccountId is required")

    store.close_account(account_id=account_id)
    return {}
