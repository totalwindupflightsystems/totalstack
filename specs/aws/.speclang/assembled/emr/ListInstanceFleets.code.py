def handler(store, request: dict) -> dict:
    fleets = store.list_instance_fleets(request["ClusterId"])
    return {"InstanceFleets": [f.to_dict() for f in fleets]}
