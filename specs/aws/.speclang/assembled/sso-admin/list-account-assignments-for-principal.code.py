def handler(store, request: dict) -> dict:
    return store.list_account_assignments_for_principal(request["instanceArn"], request["principalId"], request["principalType"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
