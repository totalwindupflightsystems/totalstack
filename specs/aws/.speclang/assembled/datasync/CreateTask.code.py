def create_task(store, request: dict) -> dict:
    kw = {k: v for k, v in request.items() if k not in ("TaskArn",)}
    return store.create_task(**kw)
