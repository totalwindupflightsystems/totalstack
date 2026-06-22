def handler(store, request: dict) -> dict:
    return store.reboot_db_cluster(
        dbClusterId=request["dbClusterId"],
        instanceIds=request.get("instanceIds"),
    )
