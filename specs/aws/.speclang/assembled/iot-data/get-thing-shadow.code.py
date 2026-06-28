def get_thing_shadow(store, request: dict) -> dict:
    return store.get_thing_shadow(request["thingName"], request.get("shadowName"))
