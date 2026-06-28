def handler(store, request: dict) -> dict:
    r = store.create_dataset(
        request["DatasetName"],
        Domain=request.get("Domain"),
        DatasetType=request.get("DatasetType"),
        Schema=request.get("Schema"),
        **{k: v for k, v in request.items() if k not in ("DatasetName", "Domain", "DatasetType", "Schema")})
    return {"DatasetArn": r.DatasetArn}
