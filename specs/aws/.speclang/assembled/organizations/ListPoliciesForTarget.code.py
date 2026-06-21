"""ListPoliciesForTarget handler."""


def handle_list_policies_for_target(store, request: dict) -> dict:
    target_id = request.get("TargetId", "")
    filter = request.get("Filter", "SERVICE_CONTROL_POLICY")

    if not target_id:
        raise InvalidInputException("TargetId is required")
    if filter not in ("SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"):
        raise InvalidInputException(f"Invalid filter: {filter}")

    next_token = request.get("NextToken")
    max_results = request.get("MaxResults", 20)

    result = store.list_policies_for_target(
        target_id=target_id, filter=filter, next_token=next_token, max_results=max_results,
    )
    return result
