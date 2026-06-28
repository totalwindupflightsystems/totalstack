def handler(store, request: dict) -> dict:
    return store.list_managed_policies_in_permission_set(request["instanceArn"], request["permissionSetArn"], maxResults=request.get("maxResults"), nextToken=request.get("nextToken"))
