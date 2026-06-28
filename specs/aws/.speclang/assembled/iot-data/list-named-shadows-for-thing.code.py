def list_named_shadows_for_thing(store, request: dict) -> dict:
    results = store.list_named_shadows_for_thing(request["thingName"])
    return {"results": results}
