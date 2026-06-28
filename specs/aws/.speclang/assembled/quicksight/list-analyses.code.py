def handler(store, request: dict) -> dict:
    items = store.analyses(request["AwsAccountId"])
    summaries = [{"AnalysisId": a.AnalysisId, "Arn": a.Arn, "Name": a.Name,
                  "Status": a.Status, "CreatedTime": a.CreatedTime} for a in items]
    return {"AnalysisSummaryList": summaries, "NextToken": "", "RequestId": "", "Status": 200}
