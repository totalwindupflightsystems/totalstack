def handler(store, request: dict) -> dict:
    r = store.analyses(request["AwsAccountId"], request["AnalysisId"])
    if not r:
        raise ResourceNotFoundException(f"Analysis {request['AnalysisId']} not found")
    store.delete_analysis(request["AwsAccountId"], request["AnalysisId"])
    return {"AnalysisId": r.AnalysisId, "Arn": r.Arn, "DeletionTime": 0, "RequestId": "", "Status": 200}
