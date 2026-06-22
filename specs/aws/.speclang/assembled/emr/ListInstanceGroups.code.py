def handler(store, request: dict) -> dict:
    groups = store.list_instance_groups(request["ClusterId"])
    return {"InstanceGroups": [g.to_dict() for g in groups]}
