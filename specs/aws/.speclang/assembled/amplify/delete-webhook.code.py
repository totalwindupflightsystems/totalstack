def handler(store, request: dict) -> dict:
    record = store.delete_webhook(request["webhookId"])
    return {"webhook": record.to_dict()}
