def publish(store, request: dict) -> dict:
    return store.publish(request["topic"], request.get("payload", b""), request.get("qos", 0))
