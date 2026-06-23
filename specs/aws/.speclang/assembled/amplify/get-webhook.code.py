def handler(store, request: dict) -> dict:
    record = store.get_webhook(request["webhookId"])
    return {"webhook": record.to_dict()}
