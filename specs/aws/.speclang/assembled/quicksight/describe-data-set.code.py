def handler(store, request: dict) -> dict:
    r = store.datasets(request["AwsAccountId"], request["DataSetId"])
    if not r:
        raise ResourceNotFoundException(f"DataSet {request['DataSetId']} not found")
    return {"DataSet": r.to_dict(), "RequestId": "", "Status": r.Status}
