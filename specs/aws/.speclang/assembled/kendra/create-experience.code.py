def handler(store, request: dict) -> dict:
    args = {k: v for k, v in request.items() if k != 'ClientToken'}
    return store.create_experience(**args)

