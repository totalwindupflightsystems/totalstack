def handler(store, request: dict) -> dict:
    un = request.get("UserName")
    return store.describe_users(UserName=un)

