def handler(store, request: dict) -> dict:
    return store.create_user(
        BrokerId=request["BrokerId"],
        Username=request["Username"],
        Password=request.get("Password"),
        ConsoleAccess=request.get("ConsoleAccess", False),
        Groups=request.get("Groups"),
        ReplicationUser=request.get("ReplicationUser", False))
