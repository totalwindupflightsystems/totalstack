def update_thing_shadow(store, request: dict) -> dict:
    return store.update_thing_shadow(request["thingName"], request.get("payload", {}), request.get("shadowName"))
