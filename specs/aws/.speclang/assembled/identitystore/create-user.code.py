def handler(store, request: dict) -> dict:
    return store.create_user(request["identityStoreId"], userName=request.get("userName"), displayName=request.get("displayName"), emails=request.get("emails"), name=request.get("name"), UserName=request.get("UserName"), DisplayName=request.get("DisplayName"), Emails=request.get("Emails"), Name=request.get("Name"))
