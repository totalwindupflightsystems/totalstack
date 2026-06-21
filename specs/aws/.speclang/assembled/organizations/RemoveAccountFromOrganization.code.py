"""RemoveAccountFromOrganization handler."""


def handle_remove_account_from_organization(store, request: dict) -> dict:
    account_id = request.get("AccountId", "")
    if not account_id:
        raise InvalidInputException("AccountId is required")

    store.remove_account_from_organization(account_id=account_id)
    return {}
