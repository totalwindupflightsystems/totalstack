def handler(store, request: dict) -> dict:
    items = store.forecasts()
    summaries = [{"ForecastArn": f.ForecastArn, "ForecastName": f.ForecastName,
                  "PredictorArn": f.PredictorArn, "Status": f.Status} for f in items]
    return {"Forecasts": summaries, "NextToken": ""}
