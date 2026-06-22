def handler(store, request: dict) -> dict:
    return store.delete_provisioned_model_throughput(request["provisionedModelId"])
