def create_web_login_token(store, request: dict) -> dict:
    return store.create_web_login_token(request["Name"])
