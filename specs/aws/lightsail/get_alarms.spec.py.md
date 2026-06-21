---
id: "@specs/aws/lightsail/get_alarms"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetAlarms"
---

# GetAlarms

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_alarms
> **spec:implements:** @kind:operation GetAlarms
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetAlarms.spec.md

Returns information about the configured alarms. Specify an alarm name in your request to return information about a specific alarm, or specify a monitored resource name to return information about all alarms for a specific resource. An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see Alarms in Amazon Lightsail .

## Input Shape: GetAlarmsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| alarmName | Any  # complex shape |  | The name of the alarm. Specify an alarm name to return information about a specific alarm. |
| monitoredResourceName | Any  # complex shape |  | The name of the Lightsail resource being monitored by the alarm. Specify a monitored resource name to return information |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetAlarms re |

## Output Shape: GetAlarmsResult

- **alarms** (list[Any  # complex shape]): An array of objects that describe the alarms.
- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo

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
def get_alarms(store, request: dict) -> dict:
    """Returns information about the configured alarms. Specify an alarm name in your request to return information about a specific alarm, or specify a monitored resource name to return information about al"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
