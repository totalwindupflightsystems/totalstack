def handler(store, request: dict) -> dict:
    record = store.create_data_source(request)
    return {"dataSource": record.to_dict()}
