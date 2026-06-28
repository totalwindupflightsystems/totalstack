def handler(store, request: dict) -> dict:
    return store.describe_thesaurus(request['Id'], request['IndexId'])

