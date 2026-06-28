def list_thing_types(store, request: dict) -> dict:
    types = store.list_thing_types()
    return {"thingTypes": types}
