def handler(store, request: dict) -> dict:
    record = store.get_provisioned_model_throughput(request["provisionedModelId"])
    return record.to_dict()
