---
id: "@specs/aws/lightsail/delete_contact_method"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteContactMethod"
---

# DeleteContactMethod

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_contact_method
> **spec:implements:** @kind:operation DeleteContactMethod
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteContactMethod.spec.md

Deletes a contact method. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail .

## Input Shape: DeleteContactMethodRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| protocol | Any  # complex shape | ✓ | The protocol that will be deleted, such as Email or SMS (text messaging). To delete an Email and an SMS contact method i |

## Output Shape: DeleteContactMethodResult

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
def delete_contact_method(store, request: dict) -> dict:
    """Deletes a contact method. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Ama"""
    protocol = request.get("protocol", "").strip() if isinstance(request.get("protocol"), str) else request.get("protocol")

    if not store.contact_methods(protocol):
        raise ResourceNotFoundException(f"Resource protocol not found")
    store.delete_contact_methods(protocol)
    return {}
```
