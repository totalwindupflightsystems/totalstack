def describe_thing_group(store, request: dict) -> dict:
    return store.describe_thing_group(request["thingGroupName"])
