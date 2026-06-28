def describe_replication_instances(store, request: dict) -> dict:
    insts = store.describe_replication_instances()
    return {"ReplicationInstances": insts}
