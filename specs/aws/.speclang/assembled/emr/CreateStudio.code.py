def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k != "Name"}
    record = store.create_studio(request["Name"], **kwargs)
    return {"StudioId": record.StudioId}
