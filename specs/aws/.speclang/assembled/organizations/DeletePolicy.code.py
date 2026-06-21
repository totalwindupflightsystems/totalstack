"""DeletePolicy handler."""


def handle_delete_policy(store, request: dict) -> dict:
    policy_id = request.get("PolicyId", "")
    if not policy_id:
        raise InvalidInputException("PolicyId is required")

    store.delete_policy(policy_id=policy_id)
    return {}
