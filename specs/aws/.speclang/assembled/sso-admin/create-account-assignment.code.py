def handler(store, request: dict) -> dict:
    return store.create_account_assignment(request["instanceArn"], request["targetId"], request["targetType"], request["permissionSetArn"], request["principalType"], request["principalId"])
