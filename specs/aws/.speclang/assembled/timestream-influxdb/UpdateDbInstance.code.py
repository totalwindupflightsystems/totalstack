def handler(store, request: dict) -> dict:
    return store.update_db_instance(
        identifier=request["identifier"],
        logDeliveryConfiguration=request.get("logDeliveryConfiguration"),
        dbParameterGroupIdentifier=request.get("dbParameterGroupIdentifier"),
        port=request.get("port"),
        dbInstanceType=request.get("dbInstanceType"),
        deploymentType=request.get("deploymentType"),
        dbStorageType=request.get("dbStorageType"),
        allocatedStorage=request.get("allocatedStorage"),
    )
