---
id: "@specs/aws/lightsail/test_alarm"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_TestAlarm"
---

# TestAlarm

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/test_alarm
> **spec:implements:** @kind:operation TestAlarm
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_TestAlarm.spec.md

Tests an alarm by displaying a banner on the Amazon Lightsail console. If a notification trigger is configured for the specified alarm, the test also sends a notification to the notification protocol ( Email and/or SMS ) configured for the alarm. An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail .

## Input Shape: TestAlarmRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| alarmName | Any  # complex shape | ✓ | The name of the alarm to test. |
| state | Any  # complex shape | ✓ | The alarm state to test. An alarm has the following possible states that can be tested: ALARM - The metric is outside of |

## Output Shape: TestAlarmResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
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
```
