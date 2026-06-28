def stop_replication_task(store, request: dict) -> dict:
    store.stop_replication_task(request["ReplicationTaskIdentifier"])
    return {}
