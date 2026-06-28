def describe_agent(store, request: dict) -> dict:
    return store.describe_agent(AgentArn=request["AgentArn"])
