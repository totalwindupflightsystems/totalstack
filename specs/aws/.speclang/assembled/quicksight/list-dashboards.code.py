def handler(store, request: dict) -> dict:
    items = store.dashboards(request["AwsAccountId"])
    summaries = [{"Arn": d.Arn, "DashboardId": d.DashboardId, "Name": d.Name,
                  "CreatedTime": d.CreatedTime} for d in items]
    return {"DashboardSummaryList": summaries, "NextToken": "", "RequestId": "", "Status": 200}
