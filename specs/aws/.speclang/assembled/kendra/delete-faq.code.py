def handler(store, request: dict) -> dict:
    return store.delete_faq(request['Id'], request['IndexId'])

