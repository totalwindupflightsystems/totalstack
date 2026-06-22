def handler(store, request: dict):
    return store.send_email(**request)
