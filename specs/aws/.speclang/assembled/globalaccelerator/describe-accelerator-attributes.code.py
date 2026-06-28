def handler(store, request: dict) -> dict:
    return store.describe_accelerator_attributes(request["AcceleratorArn"])
