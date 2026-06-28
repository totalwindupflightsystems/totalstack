def handler(store, request: dict) -> dict:
    r = store.create_dataset(
        request["AwsAccountId"], request["DataSetId"],
        Name=request["Name"],
        PhysicalTableMap=request.get("PhysicalTableMap"),
        ImportMode=request.get("ImportMode"),
        **{k: v for k, v in request.items() if k not in ("AwsAccountId", "DataSetId", "Name", "PhysicalTableMap", "ImportMode")})
    return {"Arn": r.Arn, "DataSetId": r.DataSetId, "IngestionArn": "", "IngestionId": "", "RequestId": "", "Status": r.Status}
