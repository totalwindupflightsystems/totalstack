def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k != "StudioId"}
    store.update_studio(request["StudioId"], **kwargs)
    return {}
