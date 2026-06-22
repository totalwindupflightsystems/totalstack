def handler(store, request: dict) -> dict:
    return store.delete_db_cluster(
        dbClusterId=request["dbClusterId"],
    )
