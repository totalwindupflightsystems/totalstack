# spec:trace: aws/lightsail/get_alarms.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-alarms
# spec:generated: DO NOT EDIT — edit the spec instead

def get_alarms(store, request: dict) -> dict:
    """Returns information about the configured alarms. Specify an alarm name in your request to return information about a specific alarm, or specify a monitored resource name to return information about al"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)

