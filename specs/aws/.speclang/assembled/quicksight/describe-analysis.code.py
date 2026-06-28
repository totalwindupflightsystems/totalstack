def handler(store, request: dict) -> dict:
    r = store.analyses(request["AwsAccountId"], request["AnalysisId"])
    if not r:
        raise ResourceNotFoundException(f"Analysis {request['AnalysisId']} not found")
    return {"Analysis": r.to_dict(), "RequestId": "", "Status": r.Status}
