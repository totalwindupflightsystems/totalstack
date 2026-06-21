---
id: "@specs/aws/lightsail/tag_resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_TagResource"
---

# TagResource

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/tag_resource
> **spec:implements:** @kind:operation TagResource
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_TagResource.spec.md

Adds one or more tags to the specified Amazon Lightsail resource. Each resource can have a maximum of 50 tags. Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see the Amazon Lightsail Developer Guide . The tag resource operation supports tag-based access control via request tags and resource tags applied to the resource identified by resource name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: TagResourceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| resourceArn | str |  | The Amazon Resource Name (ARN) of the resource to which you want to add a tag. |
| resourceName | Any  # complex shape | ✓ | The name of the resource to which you are adding tags. |
| tags | list[Any  # complex shape] | ✓ | The tag key and optional value. |

## Output Shape: TagResourceResult

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
def tag_resource(store, request: dict) -> dict:
    """Adds one or more tags to the specified Amazon Lightsail resource. Each resource can have a maximum of 50 tags. Each tag consists of a key and an optional value. Tag keys must be unique per resource. F"""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    tags = request.get("tags", "").strip() if isinstance(request.get("tags"), str) else request.get("tags")
    if not tags:
        raise ValidationException("tags is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
