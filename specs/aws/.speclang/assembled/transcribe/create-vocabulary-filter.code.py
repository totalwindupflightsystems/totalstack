def handler(store, request: dict) -> dict:
    return store.create_vocabulary_filter(
        VocabularyFilterName=request["VocabularyFilterName"],
        LanguageCode=request["LanguageCode"],
        Words=request.get("Words"),
        VocabularyFilterFileUri=request.get("VocabularyFilterFileUri"),
        DataAccessRoleArn=request.get("DataAccessRoleArn"),
        Tags=request.get("Tags"))

