def create_policy_store(store, request: dict) -> dict:
    return store.create_policy_store(
        ValidationSettings=request["ValidationSettings"],
        Description=request.get("Description"),
        Tags=request.get("Tags"),
    )
