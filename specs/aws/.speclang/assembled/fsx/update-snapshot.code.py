def handler(store, request: dict) -> dict:
    record = store.update_snapshot(
        request["SnapshotId"], request["Name"])
    return record.to_dict()
