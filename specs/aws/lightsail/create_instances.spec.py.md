---
id: "@specs/aws/lightsail/create_instances"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateInstances"
---

# CreateInstances

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_instances
> **spec:implements:** @kind:operation CreateInstances
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateInstances.spec.md

Creates one or more Amazon Lightsail instances. The create instances operation supports tag-based access control via request tags. For more information, see the Lightsail Developer Guide .

## Input Shape: CreateInstancesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| addOns | list[Any  # complex shape] |  | An array of objects representing the add-ons to enable for the new instance. |
| availabilityZone | Any  # complex shape | ✓ | The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). You can g |
| blueprintId | Any  # complex shape | ✓ | The ID for a virtual private server image ( app_wordpress_x_x or app_lamp_x_x ). Use the get blueprints operation to ret |
| bundleId | Any  # complex shape | ✓ | The bundle of specification information for your virtual private server (or instance ), including the pricing plan ( med |
| customImageName | Any  # complex shape |  | (Discontinued) The name for your custom image. In releases prior to June 12, 2017, this parameter was ignored by the API |
| instanceNames | list[Any  # complex shape] | ✓ | The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for exampl |
| ipAddressType | Any  # complex shape |  | The IP address type for the instance. The possible values are ipv4 for IPv4 only, ipv6 for IPv6 only, and dualstack for  |
| keyPairName | Any  # complex shape |  | The name of your key pair. |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |
| userData | Any  # complex shape |  | A launch script you can create that configures a server with additional user data. For example, you might want to run ap |

## Output Shape: CreateInstancesResult

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
def create_instances(store, request: dict) -> dict:
    """Creates one or more Amazon Lightsail instances. The create instances operation supports tag-based access control via request tags. For more information, see the Lightsail Developer Guide ."""
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    blueprint_id = request.get("blueprintId", "").strip() if isinstance(request.get("blueprintId"), str) else request.get("blueprintId")
    if not blueprint_id:
        raise ValidationException("blueprintId is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")
    instance_names = request.get("instanceNames", "").strip() if isinstance(request.get("instanceNames"), str) else request.get("instanceNames")
    if not instance_names:
        raise ValidationException("instanceNames is required")

    if store.instancess(instance_names):
        raise ResourceInUseException(f"Resource instance_names already exists")

    record = {
        "instanceNames": instance_names,
        "availabilityZone": availability_zone,
        "customImageName": custom_image_name,
        "blueprintId": blueprint_id,
        "bundleId": bundle_id,
        "userData": user_data,
        "keyPairName": key_pair_name,
        "tags": tags,
        "addOns": add_ons,
        "ipAddressType": ip_address_type,
    }

    store.instancess(instance_names, record)

    return {
        "operations": record.get("operations", {}),
    }
```
