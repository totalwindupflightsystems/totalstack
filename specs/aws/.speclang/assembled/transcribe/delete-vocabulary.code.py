def handler(store, request: dict) -> dict:
    return store.delete_vocabulary(request["VocabularyName"])

