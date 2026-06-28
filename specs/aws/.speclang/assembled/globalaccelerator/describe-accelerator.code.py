def handler(store, request: dict) -> dict:
    return store.describe_accelerator(request["AcceleratorArn"])
