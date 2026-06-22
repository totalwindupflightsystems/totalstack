def handler(store, request: dict) -> dict:
    store.delete_event_subscription(request["SubscriptionName"])
    return {}
