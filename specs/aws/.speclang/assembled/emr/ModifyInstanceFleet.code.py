def handler(store, request: dict) -> dict:
    store.modify_instance_fleet(request["ClusterId"], request["InstanceFleet"])
    return {}
