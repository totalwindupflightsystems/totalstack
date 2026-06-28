def handler(store, request: dict) -> dict:
    r = store.update_dataset(request["AwsAccountId"], request["DataSetId"],
        Name=request["Name"],
        **{k: v for k, v in request.items() if k not in ("AwsAccountId", "DataSetId", "Name")})
    return {"Arn": r.Arn, "DataSetId": r.DataSetId, "IngestionArn": "", "IngestionId": "", "RequestId": "", "Status": r.Status}
