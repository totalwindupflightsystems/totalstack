def handler(store, request: dict) -> dict:
    record = store.get_app(request["appId"])
    return {"app": record.to_dict()}
