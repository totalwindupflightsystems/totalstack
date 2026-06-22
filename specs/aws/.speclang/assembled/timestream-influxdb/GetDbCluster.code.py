def handler(store, request: dict) -> dict:
    return store.get_db_cluster(
        dbClusterId=request["dbClusterId"],
    )
