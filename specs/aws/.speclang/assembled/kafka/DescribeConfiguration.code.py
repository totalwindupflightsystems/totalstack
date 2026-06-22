def describe_configuration(store, request: dict) -> dict:
    return store.describe_configuration(request["Arn"])
