def handler(store, request: dict) -> dict:
    r = store.datasources(request["AwsAccountId"], request["DataSourceId"])
    if not r:
        raise ResourceNotFoundException(f"DataSource {request['DataSourceId']} not found")
    return {"DataSource": r.to_dict(), "RequestId": "", "Status": r.Status}
