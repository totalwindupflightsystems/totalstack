def handler(store, request: dict) -> dict:
    return store.describe_account_assignment_creation_status(request["instanceArn"], request["accountAssignmentCreationRequestId"])
