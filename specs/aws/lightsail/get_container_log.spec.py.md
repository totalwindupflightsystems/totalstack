---
id: "@specs/aws/lightsail/get_container_log"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContainerLog"
---

# GetContainerLog

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_container_log
> **spec:implements:** @kind:operation GetContainerLog
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContainerLog.spec.md

Returns the log events of a container of your Amazon Lightsail container service. If your container service has more than one node (i.e., a scale greater than 1), then the log events that are returned for the specified container are merged from all nodes on your container service. Container logs are retained for a certain amount of time. For more information, see Amazon Lightsail endpoints and quotas in the Amazon Web Services General Reference .

## Input Shape: GetContainerLogRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| containerName | Any  # complex shape | ✓ | The name of the container that is either running or previously ran on the container service for which to return a log. |
| endTime | Any  # complex shape |  | The end of the time interval for which to get log data. Constraints: Specified in Coordinated Universal Time (UTC). Spec |
| filterPattern | Any  # complex shape |  | The pattern to use to filter the returned log events to a specific term. The following are a few examples of filter patt |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetContainer |
| serviceName | Any  # complex shape | ✓ | The name of the container service for which to get a container log. |
| startTime | Any  # complex shape |  | The start of the time interval for which to get log data. Constraints: Specified in Coordinated Universal Time (UTC). Sp |

## Output Shape: GetContainerLogResult

- **logEvents** (list[Any  # complex shape]): An array of objects that describe the log events of a container.
- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_container_log(store, request: dict) -> dict:
    """Returns the log events of a container of your Amazon Lightsail container service. If your container service has more than one node (i.e., a scale greater than 1), then the log events that are returned"""
    container_name = request.get("containerName", "").strip() if isinstance(request.get("containerName"), str) else request.get("containerName")
    if not container_name:
        raise ValidationException("containerName is required")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_logs(service_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_name not found")
    return {"serviceName": service_name, **resource}
```
