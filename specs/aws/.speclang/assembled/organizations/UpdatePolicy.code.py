"""UpdatePolicy handler."""
import json


def handle_update_policy(store, request: dict) -> dict:
    policy_id = request.get("PolicyId", "")
    if not policy_id:
        raise InvalidInputException("PolicyId is required")

    content = request.get("Content")
    description = request.get("Description")
    name = request.get("Name")

    if content is not None:
        try:
            json.loads(content)
        except json.JSONDecodeError:
            raise MalformedPolicyDocumentException("Content is not valid JSON")

    result = store.update_policy(
        policy_id=policy_id, content=content, description=description, name=name,
    )
    return result
