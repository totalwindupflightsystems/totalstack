def delete_replication_task(store, request: dict) -> dict:
    store.delete_replication_task(request["ReplicationTaskIdentifier"])
    return {}
