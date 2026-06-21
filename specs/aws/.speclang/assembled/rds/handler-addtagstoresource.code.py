def handler(store, request: dict) -> dict:
    return store.add_tags(request["ResourceName"], request["Tags"])
