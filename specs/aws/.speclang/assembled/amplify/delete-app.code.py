def handler(store, request: dict) -> dict:
    record = store.delete_app(request["appId"])
    return {"app": record.to_dict()}
