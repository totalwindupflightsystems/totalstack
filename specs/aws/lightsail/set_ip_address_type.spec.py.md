---
id: "@specs/aws/lightsail/set_ip_address_type"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_SetIpAddressType"
---

# SetIpAddressType

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/set_ip_address_type
> **spec:implements:** @kind:operation SetIpAddressType
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_SetIpAddressType.spec.md

Sets the IP address type for an Amazon Lightsail resource. Use this action to enable dual-stack for a resource, which enables IPv4 and IPv6 for the specified resource. Alternately, you can use this action to disable dual-stack, and enable IPv4 only.

## Input Shape: SetIpAddressTypeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| acceptBundleUpdate | Any  # complex shape |  | Required parameter to accept the instance bundle update when changing to, and from, IPv6-only. An instance bundle will c |
| ipAddressType | Any  # complex shape | ✓ | The IP address type to set for the specified resource. The possible values are ipv4 for IPv4 only, ipv6 for IPv6 only, a |
| resourceName | Any  # complex shape | ✓ | The name of the resource for which to set the IP address type. |
| resourceType | Any  # complex shape | ✓ | The resource type. The resource values are Distribution , Instance , and LoadBalancer . Distribution-related APIs are av |

## Output Shape: SetIpAddressTypeResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

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
def set_ip_address_type(store, request: dict) -> dict:
    """Sets the IP address type for an Amazon Lightsail resource. Use this action to enable dual-stack for a resource, which enables IPv4 and IPv6 for the specified resource. Alternately, you can use this ac"""
    ip_address_type = request.get("ipAddressType", "").strip() if isinstance(request.get("ipAddressType"), str) else request.get("ipAddressType")
    if not ip_address_type:
        raise ValidationException("ipAddressType is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    resource_type = request.get("resourceType", "").strip() if isinstance(request.get("resourceType"), str) else request.get("resourceType")
    if not resource_type:
        raise ValidationException("resourceType is required")

    if store.set_ip_address_types(resource_name):
        raise ResourceInUseException(f"Resource resource_name already exists")

    record = {
        "resourceType": resource_type,
        "resourceName": resource_name,
        "ipAddressType": ip_address_type,
        "acceptBundleUpdate": accept_bundle_update,
    }

    store.set_ip_address_types(resource_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
