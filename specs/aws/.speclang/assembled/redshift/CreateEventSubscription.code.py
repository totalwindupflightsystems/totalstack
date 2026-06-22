def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k not in ("SubscriptionName", "SnsTopicArn")}
    record = store.create_event_subscription(
        request["SubscriptionName"], request["SnsTopicArn"], **kwargs)
    return {"EventSubscription": record.to_dict()}
