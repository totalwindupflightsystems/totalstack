def handler(store, request: dict) -> dict:
    record = store.update_agent(request)
    return {"agent": record.to_dict()}
