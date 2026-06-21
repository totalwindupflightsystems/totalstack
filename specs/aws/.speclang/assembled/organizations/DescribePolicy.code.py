"""DescribePolicy handler."""


def handle_describe_policy(store, request: dict) -> dict:
    policy_id = request.get("PolicyId", "")
    if not policy_id:
        raise InvalidInputException("PolicyId is required")

    result = store.describe_policy(policy_id=policy_id)
    return result
