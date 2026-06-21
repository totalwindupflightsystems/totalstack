# spec:trace: aws/lightsail/delete_alarm.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-alarm
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_alarm(store, request: dict) -> dict:
    """Deletes an alarm. An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on """
    alarm_name = request.get("alarmName", "").strip() if isinstance(request.get("alarmName"), str) else request.get("alarmName")

    if not store.alarms(alarm_name):
        raise ResourceNotFoundException("Resource alarm_name not found")
    store.delete_alarms(alarm_name)
    return {}

