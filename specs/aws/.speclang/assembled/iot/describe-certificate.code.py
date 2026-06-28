def describe_certificate(store, request: dict) -> dict:
    return store.describe_certificate(request["certificateId"])
