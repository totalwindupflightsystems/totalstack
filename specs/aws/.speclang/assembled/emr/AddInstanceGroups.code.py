def handler(store, request: dict) -> dict:
    groups = store.add_instance_groups(request["JobFlowId"], request["InstanceGroups"])
    return {"InstanceGroupIds": [g.Id for g in groups]}
