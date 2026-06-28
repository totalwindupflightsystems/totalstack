def handler(store, request: dict) -> dict:
    return store.list_account_assignments(request["instanceArn"], request["accountId"], request["permissionSetArn"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
