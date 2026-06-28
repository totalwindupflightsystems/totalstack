def handler(store, request: dict) -> dict:
    r = store.update_datasource(request["AwsAccountId"], request["DataSourceId"],
        Name=request["Name"],
        **{k: v for k, v in request.items() if k not in ("AwsAccountId", "DataSourceId", "Name")})
    return {"Arn": r.Arn, "DataSourceId": r.DataSourceId, "RequestId": "", "Status": r.Status,
            "UpdateStatus": "UPDATE_SUCCESSFUL"}
