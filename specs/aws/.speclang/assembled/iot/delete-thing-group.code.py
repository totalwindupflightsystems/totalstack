def delete_thing_group(store, request: dict) -> dict:
    store.delete_thing_group(request["thingGroupName"])
    return {}
