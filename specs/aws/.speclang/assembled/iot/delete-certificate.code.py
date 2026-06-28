def delete_certificate(store, request: dict) -> dict:
    store.delete_certificate(request["certificateId"])
    return {}
