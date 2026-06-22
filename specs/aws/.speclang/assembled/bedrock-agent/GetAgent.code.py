def handler(store, request: dict) -> dict:
    record = store.get_agent(request["agentId"])
    return {"agent": record.to_dict()}
