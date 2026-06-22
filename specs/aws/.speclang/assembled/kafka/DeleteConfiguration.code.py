def delete_configuration(store, request: dict) -> dict:
    return store.delete_configuration(request["Arn"])
