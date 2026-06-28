def delete_thing_type(store, request: dict) -> dict:
    store.delete_thing_type(request["thingTypeName"])
    return {}
