---
id: "@specs/aws/lightsail/update_instance_metadata_options"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateInstanceMetadataOptions"
---

# UpdateInstanceMetadataOptions

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_instance_metadata_options
> **spec:implements:** @kind:operation UpdateInstanceMetadataOptions
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateInstanceMetadataOptions.spec.md

Modifies the Amazon Lightsail instance metadata parameters on a running or stopped instance. When you modify the parameters on a running instance, the GetInstance or GetInstances API operation initially responds with a state of pending . After the parameter modifications are successfully applied, the state changes to applied in subsequent GetInstance or GetInstances API calls. For more information, see Use IMDSv2 with an Amazon Lightsail instance in the Amazon Lightsail Developer Guide .

## Input Shape: UpdateInstanceMetadataOptionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| httpEndpoint | Any  # complex shape |  | Enables or disables the HTTP metadata endpoint on your instances. If this parameter is not specified, the existing state |
| httpProtocolIpv6 | Any  # complex shape |  | Enables or disables the IPv6 endpoint for the instance metadata service. This setting applies only when the HTTP metadat |
| httpPutResponseHopLimit | Any  # complex shape |  | The desired HTTP PUT response hop limit for instance metadata requests. A larger number means that the instance metadata |
| httpTokens | Any  # complex shape |  | The state of token usage for your instance metadata requests. If the parameter is not specified in the request, the defa |
| instanceName | Any  # complex shape | ✓ | The name of the instance for which to update metadata parameters. |

## Output Shape: UpdateInstanceMetadataOptionsResult

- **operation** (Any  # complex shape): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def update_instance_metadata_options(store, request: dict) -> dict:
    """Modifies the Amazon Lightsail instance metadata parameters on a running or stopped instance. When you modify the parameters on a running instance, the GetInstance or GetInstances API operation initial"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_metadata_optionss(instance_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_name not found")

    # Update mutable fields
    if "httpTokens" in request:
        resource["httpTokens"] = http_tokens
    if "httpEndpoint" in request:
        resource["httpEndpoint"] = http_endpoint
    if "httpPutResponseHopLimit" in request:
        resource["httpPutResponseHopLimit"] = http_put_response_hop_limit
    if "httpProtocolIpv6" in request:
        resource["httpProtocolIpv6"] = http_protocol_ipv6

    store.instance_metadata_optionss(instance_name, resource)
    return resource
```
