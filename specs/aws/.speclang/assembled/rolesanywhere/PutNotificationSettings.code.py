def handler(store, request):
    settings = store.put_notification_settings(
        enabled=request.get("enabled"),
        channel=request.get("channel"),
        threshold=request.get("threshold"),
        eventTypes=request.get("eventTypes"),
    )
    return settings
