def handler(store, request: dict) -> dict:
    record = store.create_agent(request)
    return {"agent": record.to_dict()}
