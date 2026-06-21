---
id: "@specs/aws/lightsail/create_contact_method"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateContactMethod"
---

# CreateContactMethod

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_contact_method
> **spec:implements:** @kind:operation CreateContactMethod
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateContactMethod.spec.md

Creates an email or SMS text message contact method. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail .

## Input Shape: CreateContactMethodRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| contactEndpoint | Any  # complex shape | ✓ | The destination of the contact method, such as an email address or a mobile phone number. Use the E.164 format when spec |
| protocol | Any  # complex shape | ✓ | The protocol of the contact method, such as Email or SMS (text messaging). The SMS protocol is supported only in the fol |

## Output Shape: CreateContactMethodResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def create_contact_method(store, request: dict) -> dict:
    """Creates an email or SMS text message contact method. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number"""
    contact_endpoint = request.get("contactEndpoint", "").strip() if isinstance(request.get("contactEndpoint"), str) else request.get("contactEndpoint")
    if not contact_endpoint:
        raise ValidationException("contactEndpoint is required")
    protocol = request.get("protocol", "").strip() if isinstance(request.get("protocol"), str) else request.get("protocol")
    if not protocol:
        raise ValidationException("protocol is required")

    if store.contact_methods(contact_endpoint):
        raise ResourceInUseException(f"Resource contact_endpoint already exists")

    record = {
        "protocol": protocol,
        "contactEndpoint": contact_endpoint,
    }

    store.contact_methods(contact_endpoint, record)

    return {
        "operations": record.get("operations", {}),
    }
```
