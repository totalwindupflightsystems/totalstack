# spec:trace: aws/lightsail/test_alarm.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/test-alarm
# spec:generated: DO NOT EDIT — edit the spec instead

def test_alarm(store, request: dict) -> dict:
    """Tests an alarm by displaying a banner on the Amazon Lightsail console. If a notification trigger is configured for the specified alarm, the test also sends a notification to the notification protocol """
    alarm_name = request.get("alarmName", "").strip() if isinstance(request.get("alarmName"), str) else request.get("alarmName")
    if not alarm_name:
        raise ValidationException("alarmName is required")
    state = request.get("state", "").strip() if isinstance(request.get("state"), str) else request.get("state")
    if not state:
        raise ValidationException("state is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("TestAlarm", request)

