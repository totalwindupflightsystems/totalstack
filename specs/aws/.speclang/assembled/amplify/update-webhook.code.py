def handler(store, request: dict) -> dict:
    record = store.update_webhook(request["webhookId"], **{k: v for k, v in request.items() if k != "webhookId"})
    return {"webhook": record.to_dict()}
