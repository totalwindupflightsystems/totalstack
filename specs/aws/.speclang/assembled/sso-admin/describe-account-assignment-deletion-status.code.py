def handler(store, request: dict) -> dict:
    return store.describe_account_assignment_deletion_status(request["instanceArn"], request["accountAssignmentDeletionRequestId"])
