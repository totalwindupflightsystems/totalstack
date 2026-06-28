def handler(store, request: dict) -> dict:
    return store.delete_experience(request['Id'], request['IndexId'])

