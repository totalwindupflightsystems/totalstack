def handler(store, request: dict) -> dict:
    r = store.create_datasource(
        request["AwsAccountId"], request["DataSourceId"],
        Name=request["Name"], Type=request.get("Type"),
        **{k: v for k, v in request.items() if k not in ("AwsAccountId", "DataSourceId", "Name", "Type")})
    return {"Arn": r.Arn, "CreationStatus": r.CreationStatus, "DataSourceId": r.DataSourceId,
            "RequestId": "", "Status": r.Status}
