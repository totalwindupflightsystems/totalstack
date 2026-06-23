def handler(store, request: dict) -> dict:
    record = store.update_app(request["appId"], **{k: v for k, v in request.items() if k != "appId"})
    return {"app": record.to_dict()}
