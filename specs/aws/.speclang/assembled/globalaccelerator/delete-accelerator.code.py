def handler(store, request: dict) -> dict:
    return store.delete_accelerator(request["AcceleratorArn"])
