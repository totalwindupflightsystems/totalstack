def handler(store, request: dict) -> dict:
    return store.delete_lexicon(request["Name"])

