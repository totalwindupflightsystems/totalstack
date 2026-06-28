def handler(store, request: dict) -> dict:
    return store.get_vocabulary(request["VocabularyName"])

