def handler(store, request: dict) -> dict:
    return store.update_provisioned_model_throughput(
        request["provisionedModelId"],
        desiredProvisionedModelName=request.get("desiredProvisionedModelName"),
        desiredModelId=request.get("desiredModelId"))
