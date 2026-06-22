def handler(store, request: dict) -> dict:
    record = store.describe_studio(request["StudioId"])
    return {"Studio": record.to_dict()}
