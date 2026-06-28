def delete_replication_instance(store, request: dict) -> dict:
    store.delete_replication_instance(request["ReplicationInstanceIdentifier"])
    return {}
