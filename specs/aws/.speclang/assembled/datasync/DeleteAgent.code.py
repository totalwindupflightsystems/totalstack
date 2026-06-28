def delete_agent(store, request: dict) -> dict:
    return store.delete_agent(AgentArn=request["AgentArn"])
