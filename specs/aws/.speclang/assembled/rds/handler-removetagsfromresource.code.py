def handler(store, request: dict) -> dict:
    return store.remove_tags(request["ResourceName"], request["TagKeys"])
