def describe_bot(store, request: dict) -> dict:
    return store.describe_bot(request["botId"])
