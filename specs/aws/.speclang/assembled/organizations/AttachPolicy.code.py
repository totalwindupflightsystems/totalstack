"""AttachPolicy handler."""


def handle_attach_policy(store, request: dict) -> dict:
    policy_id = request.get("PolicyId", "")
    target_id = request.get("TargetId", "")

    if not policy_id:
        raise InvalidInputException("PolicyId is required")
    if not target_id:
        raise InvalidInputException("TargetId is required")

    store.attach_policy(policy_id=policy_id, target_id=target_id)
    return {}
