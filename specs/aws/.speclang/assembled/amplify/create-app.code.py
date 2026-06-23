def handler(store, request: dict) -> dict:
    record = store.create_app(request["name"], **{k: v for k, v in request.items() if k != "name"})
    return {"app": record.to_dict()}
