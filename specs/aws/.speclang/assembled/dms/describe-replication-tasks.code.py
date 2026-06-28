def describe_replication_tasks(store, request: dict) -> dict:
    tasks = store.describe_replication_tasks()
    return {"ReplicationTasks": tasks}
