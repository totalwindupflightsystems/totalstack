def handler(store, request: dict) -> dict:
    record = store.create_backup(**request)
    return record.to_dict()
