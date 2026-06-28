def handler(store, request: dict) -> dict:
    return store.update_vocabulary_filter(
        VocabularyFilterName=request["VocabularyFilterName"],
        Words=request.get("Words"),
        VocabularyFilterFileUri=request.get("VocabularyFilterFileUri"),
        DataAccessRoleArn=request.get("DataAccessRoleArn"))

