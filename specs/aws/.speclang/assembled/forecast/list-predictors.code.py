def handler(store, request: dict) -> dict:
    items = store.predictors()
    summaries = [{"PredictorArn": p.PredictorArn, "PredictorName": p.PredictorName,
                  "Status": p.Status} for p in items]
    return {"Predictors": summaries, "NextToken": ""}
