def handler(store, request: dict) -> dict:
    r = store.datasets(request["AwsAccountId"], request["DataSetId"])
    if not r:
        raise ResourceNotFoundException(f"DataSet {request['DataSetId']} not found")
    store.delete_dataset(request["AwsAccountId"], request["DataSetId"])
    return {"Arn": r.Arn, "DataSetId": r.DataSetId, "RequestId": "", "Status": 200}
