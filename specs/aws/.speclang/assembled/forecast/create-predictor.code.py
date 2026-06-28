def handler(store, request: dict) -> dict:
    r = store.create_predictor(
        request["PredictorName"],
        ForecastHorizon=request.get("ForecastHorizon"),
        InputDataConfig=request.get("InputDataConfig"),
        FeaturizationConfig=request.get("FeaturizationConfig"),
        **{k: v for k, v in request.items() if k not in ("PredictorName", "ForecastHorizon", "InputDataConfig", "FeaturizationConfig")})
    return {"PredictorArn": r.PredictorArn}
