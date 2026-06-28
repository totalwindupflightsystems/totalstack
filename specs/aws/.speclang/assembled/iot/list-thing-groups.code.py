def list_thing_groups(store, request: dict) -> dict:
    groups = store.list_thing_groups()
    return {"thingGroups": groups}
