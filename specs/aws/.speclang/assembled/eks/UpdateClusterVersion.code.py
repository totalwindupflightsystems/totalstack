def handler(store, request: dict) -> dict:
    return store.update_cluster_version(
        name=request["name"], version=request["version"])
