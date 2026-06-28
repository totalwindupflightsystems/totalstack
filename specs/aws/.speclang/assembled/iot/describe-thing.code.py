def describe_thing(store, request: dict) -> dict:
    return store.describe_thing(request["thingName"])
