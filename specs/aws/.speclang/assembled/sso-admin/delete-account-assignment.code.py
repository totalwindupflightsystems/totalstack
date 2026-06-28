def handler(store, request: dict) -> dict:
    return store.delete_account_assignment(request["instanceArn"], request["targetId"], request["targetType"], request["permissionSetArn"], request["principalType"], request["principalId"])
