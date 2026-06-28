def delete_bot(store, request: dict) -> dict:
    store.delete_bot(request["botId"])
    return {}
