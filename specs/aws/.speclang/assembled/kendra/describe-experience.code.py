def handler(store, request: dict) -> dict:
    return store.describe_experience(request['Id'], request['IndexId'])

