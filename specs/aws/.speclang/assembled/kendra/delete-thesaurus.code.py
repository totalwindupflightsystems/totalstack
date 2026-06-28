def handler(store, request: dict) -> dict:
    return store.delete_thesaurus(request['Id'], request['IndexId'])

