def handler(store, request: dict) -> dict:
    return store.describe_voices(
        Engine=request.get("Engine"),
        LanguageCode=request.get("LanguageCode"),
        IncludeAdditionalLanguageCodes=request.get("IncludeAdditionalLanguageCodes"),
        NextToken=request.get("NextToken"))

