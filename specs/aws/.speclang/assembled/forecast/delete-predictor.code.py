def handler(store, request: dict) -> dict:
    r = store.predictors(request["PredictorArn"])
    if not r:
        raise ResourceNotFoundException(f"Predictor {request['PredictorArn']} not found")
    store.delete_predictor(request["PredictorArn"])
    return {}
