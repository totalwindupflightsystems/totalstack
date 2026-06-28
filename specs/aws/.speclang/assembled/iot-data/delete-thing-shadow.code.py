def delete_thing_shadow(store, request: dict) -> dict:
    store.delete_thing_shadow(request["thingName"], request.get("shadowName"))
    return {}
