def handler(store, request: dict) -> dict:
    return store.describe_event_subscriptions(
        SubscriptionName=request.get("SubscriptionName"))
