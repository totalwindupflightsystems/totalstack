def handler(store, request: dict) -> dict:
    datasets = store.datasets(request["AwsAccountId"])
    summaries = [{"Arn": d.Arn, "DataSetId": d.DataSetId, "Name": d.Name,
                   "ImportMode": d.ImportMode, "CreatedTime": d.CreatedTime}
                  for d in datasets]
    return {"DataSetSummaries": summaries, "NextToken": "", "RequestId": "", "Status": 200}
