def handler(store, request: dict) -> dict:
    r = store.datasources(request["AwsAccountId"], request["DataSourceId"])
    if not r:
        raise ResourceNotFoundException(f"DataSource {request['DataSourceId']} not found")
    store.delete_datasource(request["AwsAccountId"], request["DataSourceId"])
    return {"Arn": r.Arn, "DataSourceId": r.DataSourceId, "RequestId": "", "Status": 200}
