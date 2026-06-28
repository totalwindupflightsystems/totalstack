def handler(store, request: dict) -> dict:
    return store.describe_faq(request['Id'], request['IndexId'])

