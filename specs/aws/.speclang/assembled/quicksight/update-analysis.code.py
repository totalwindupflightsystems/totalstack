def handler(store, request: dict) -> dict:
    r = store.update_analysis(request["AwsAccountId"], request["AnalysisId"],
        Name=request["Name"],
        **{k: v for k, v in request.items() if k not in ("AwsAccountId", "AnalysisId", "Name")})
    return {"AnalysisId": r.AnalysisId, "Arn": r.Arn, "RequestId": "", "Status": r.Status,
            "UpdateStatus": "UPDATE_SUCCESSFUL"}
