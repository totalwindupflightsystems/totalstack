def handler(store, request: dict) -> dict:
    an = request.get("ACLName")
    return store.describe_acls(ACLName=an)

