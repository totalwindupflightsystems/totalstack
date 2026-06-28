def handler(store, request: dict) -> dict:
    return store.create_language_model(
        LanguageCode=request["LanguageCode"],
        BaseModelName=request["BaseModelName"],
        ModelName=request["ModelName"],
        InputDataConfig=request["InputDataConfig"],
        Tags=request.get("Tags"))

