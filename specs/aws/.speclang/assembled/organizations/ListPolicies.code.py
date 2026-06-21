"""ListPolicies handler."""


def handle_list_policies(store, request: dict) -> dict:
    filter = request.get("Filter", "SERVICE_CONTROL_POLICY")
    if filter not in ("SERVICE_CONTROL_POLICY", "TAG_POLICY", "BACKUP_POLICY", "AISERVICES_OPT_OUT_POLICY"):
        raise InvalidInputException(f"Invalid filter: {filter}")

    next_token = request.get("NextToken")
    max_results = request.get("MaxResults", 20)

    result = store.list_policies(filter=filter, next_token=next_token, max_results=max_results)
    return result
