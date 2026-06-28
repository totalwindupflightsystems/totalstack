def handler(store, request: dict) -> dict:
    sources = store.datasources(request["AwsAccountId"])
    items = [{"Arn": s.Arn, "DataSourceId": s.DataSourceId, "Name": s.Name,
              "Type": s.Type, "CreatedTime": s.CreatedTime} for s in sources]
    return {"DataSources": items, "NextToken": "", "RequestId": "", "Status": 200}
