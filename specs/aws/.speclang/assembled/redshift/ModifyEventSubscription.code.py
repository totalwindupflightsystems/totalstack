def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k != "SubscriptionName"}
    record = store.modify_event_subscription(
        request["SubscriptionName"], **kwargs)
    return {"EventSubscription": record.to_dict()}
