def describe_thing_type(store, request: dict) -> dict:
    return store.describe_thing_type(request["thingTypeName"])
