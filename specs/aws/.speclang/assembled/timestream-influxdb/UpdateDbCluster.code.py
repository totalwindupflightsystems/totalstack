def handler(store, request: dict) -> dict:
    return store.update_db_cluster(
        dbClusterId=request["dbClusterId"],
        logDeliveryConfiguration=request.get("logDeliveryConfiguration"),
        dbParameterGroupIdentifier=request.get("dbParameterGroupIdentifier"),
        port=request.get("port"),
        dbInstanceType=request.get("dbInstanceType"),
        failoverMode=request.get("failoverMode"),
    )
