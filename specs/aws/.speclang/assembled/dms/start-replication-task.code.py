def start_replication_task(store, request: dict) -> dict:
    store.start_replication_task(request["ReplicationTaskIdentifier"])
    return {}
