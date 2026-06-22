def handler(store, request: dict) -> dict:
    record = store.prepare_agent(request["agentId"])
    return {"agentId": record.agentId, "agentStatus": record.agentStatus,
            "agentVersion": record.agentVersion, "preparedAt": record.preparedAt}
