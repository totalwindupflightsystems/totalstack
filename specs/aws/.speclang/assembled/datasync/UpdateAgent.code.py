def update_agent(store, request: dict) -> dict:
    return store.update_agent(
        AgentArn=request["AgentArn"],
        Name=request.get("Name"),
    )
