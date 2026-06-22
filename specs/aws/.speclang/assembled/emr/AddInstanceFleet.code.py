def handler(store, request: dict) -> dict:
    fleet = store.add_instance_fleet(request["ClusterId"], request["InstanceFleet"])
    return {"InstanceFleetId": fleet.Id}
