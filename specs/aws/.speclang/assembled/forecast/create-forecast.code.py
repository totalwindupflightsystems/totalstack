def handler(store, request: dict) -> dict:
    r = store.create_forecast(
        request["ForecastName"],
        PredictorArn=request.get("PredictorArn"),
        **{k: v for k, v in request.items() if k not in ("ForecastName", "PredictorArn")})
    return {"ForecastArn": r.ForecastArn}
