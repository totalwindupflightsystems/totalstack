def handler(store, request: dict) -> dict:
    models = store.list_foundation_models(
        byProvider=request.get("byProvider"),
        byCustomizationType=request.get("byCustomizationType"),
        byOutputModality=request.get("byOutputModality"),
        byInferenceType=request.get("byInferenceType"))
    return {"modelSummaries": [m.to_dict() for m in models]}
