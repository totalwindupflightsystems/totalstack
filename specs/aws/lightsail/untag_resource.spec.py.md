---
id: "@specs/aws/lightsail/untag_resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UntagResource"
---

# UntagResource

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/untag_resource
> **spec:implements:** @kind:operation UntagResource
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UntagResource.spec.md

Deletes the specified set of tag keys and their values from the specified Amazon Lightsail resource. The untag resource operation supports tag-based access control via request tags and resource tags applied to the resource identified by resource name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: UntagResourceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| resourceArn | str |  | The Amazon Resource Name (ARN) of the resource from which you want to remove a tag. |
| resourceName | Any  # complex shape | ✓ | The name of the resource from which you are removing a tag. |
| tagKeys | list[Any  # complex shape] | ✓ | The tag keys to delete from the specified resource. |

## Output Shape: UntagResourceResult

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
def untag_resource(store, request: dict) -> dict:
    """Deletes the specified set of tag keys and their values from the specified Amazon Lightsail resource. The untag resource operation supports tag-based access control via request tags and resource tags a"""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    tag_keys = request.get("tagKeys", "").strip() if isinstance(request.get("tagKeys"), str) else request.get("tagKeys")
    if not tag_keys:
        raise ValidationException("tagKeys is required")

    # Tag/untag resource
    resource_arn = request.get("ResourceARN", request.get("ResourceName", ""))
    store.tag_resource(resource_arn, request.get("Tags", []))
    return {}
```
