---
id: "@specs/aws/lightsail/put_instance_public_ports"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_PutInstancePublicPorts"
---

# PutInstancePublicPorts

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/put_instance_public_ports
> **spec:implements:** @kind:operation PutInstancePublicPorts
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_PutInstancePublicPorts.spec.md

Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol. This action also closes all currently open ports that are not included in the request. Include all of the ports and the protocols you want to open in your PutInstancePublicPorts request. Or use the OpenInstancePublicPorts action to open ports without closing currently open ports. The PutInstancePublicPorts action supports tag-based access control via resource tags applied to the resource identified by instanceName . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: PutInstancePublicPortsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceName | Any  # complex shape | ✓ | The name of the instance for which to open ports. |
| portInfos | list[Any  # complex shape] | ✓ | An array of objects to describe the ports to open for the specified instance. |

## Output Shape: PutInstancePublicPortsResult

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
def put_instance_public_ports(store, request: dict) -> dict:
    """Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol. This action also closes all currently open """
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    port_infos = request.get("portInfos", "").strip() if isinstance(request.get("portInfos"), str) else request.get("portInfos")
    if not port_infos:
        raise ValidationException("portInfos is required")

    if store.instance_public_portss(instance_name):
        raise ResourceInUseException(f"Resource instance_name already exists")

    record = {
        "portInfos": port_infos,
        "instanceName": instance_name,
    }

    store.instance_public_portss(instance_name, record)

    return {
        "operation": record.get("operation", {}),
    }
```
