def handler(store, request: dict) -> dict:
    return store.delete_agent(
        request["agentId"],
        skipResourceInUseCheck=request.get("skipResourceInUseCheck"))
