def handler(store, request: dict) -> dict:
    return store.update_vocabulary(
        VocabularyName=request["VocabularyName"],
        LanguageCode=request["LanguageCode"],
        Phrases=request.get("Phrases"),
        VocabularyFileUri=request.get("VocabularyFileUri"),
        DataAccessRoleArn=request.get("DataAccessRoleArn"))

