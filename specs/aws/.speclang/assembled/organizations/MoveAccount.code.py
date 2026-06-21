"""MoveAccount handler."""


def handle_move_account(store, request: dict) -> dict:
    account_id = request.get("AccountId", "")
    source_parent_id = request.get("SourceParentId", "")
    destination_parent_id = request.get("DestinationParentId", "")

    if not account_id:
        raise InvalidInputException("AccountId is required")
    if not source_parent_id:
        raise InvalidInputException("SourceParentId is required")
    if not destination_parent_id:
        raise InvalidInputException("DestinationParentId is required")

    store.move_account(
        account_id=account_id,
        source_parent_id=source_parent_id,
        destination_parent_id=destination_parent_id,
    )
    return {}
