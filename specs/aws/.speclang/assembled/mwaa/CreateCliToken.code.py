def create_cli_token(store, request: dict) -> dict:
    return store.create_cli_token(request["Name"])
