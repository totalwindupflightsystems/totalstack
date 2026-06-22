def handler(store, request: dict) -> dict:
    store.modify_instance_groups(
        ClusterId=request.get("ClusterId"),
        InstanceGroups=request.get("InstanceGroups"))
    return {}
