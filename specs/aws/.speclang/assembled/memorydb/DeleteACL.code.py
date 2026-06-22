def handler(store, request: dict) -> dict:
    return store.delete_acl(request["ACLName"])

