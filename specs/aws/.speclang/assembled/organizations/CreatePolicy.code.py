"""CreatePolicy handler."""
import json


def handle_create_policy(store, request: dict) -> dict:
    content = request.get("Content", "")
    description = request.get("Description", "")
    name = request.get("Name", "")
    type = request.get("Type", "SERVICE_CONTROL_POLICY")

    if not content:
        raise InvalidInputException("Content is required")
    if not description:
        raise InvalidInputException("Description is required")
    if not name:
        raise InvalidInputException("Name is required")
    if type not in ("SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"):
        raise InvalidInputException(f"Invalid policy type: {type}")

    try:
        json.loads(content)
    except json.JSONDecodeError:
        raise MalformedPolicyDocumentException("Content is not valid JSON")

    tags = request.get("Tags")

    policy = store.create_policy(
        content=content, description=description, name=name, type=type, tags=tags,
    )
    return {"Policy": {"PolicySummary": policy.to_summary_dict(), "Content": policy.content}}
