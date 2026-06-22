def handler(store, request: dict) -> dict:
    record = store.create_provisioned_model_throughput(request)
    return {"provisionedModelArn": record.provisionedModelArn}
