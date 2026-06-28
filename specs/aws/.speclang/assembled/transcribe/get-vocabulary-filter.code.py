def handler(store, request: dict) -> dict:
    return store.get_vocabulary_filter(request["VocabularyFilterName"])

