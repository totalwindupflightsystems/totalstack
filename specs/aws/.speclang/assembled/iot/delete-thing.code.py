def delete_thing(store, request: dict) -> dict:
    store.delete_thing(request["thingName"])
    return {}
