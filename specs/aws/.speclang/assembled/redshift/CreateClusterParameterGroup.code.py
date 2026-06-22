def handler(store, request: dict) -> dict:
    record = store.create_cluster_parameter_group(
        request["ParameterGroupName"],
        request["ParameterGroupFamily"],
        request["Description"],
        Tags=request.get("Tags"))
    return {"ClusterParameterGroup": record.to_dict()}
