def handler(store, request: dict) -> dict:
    return store.delete_vocabulary_filter(request["VocabularyFilterName"])

