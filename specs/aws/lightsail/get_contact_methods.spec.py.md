---
id: "@specs/aws/lightsail/get_contact_methods"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContactMethods"
---

# GetContactMethods

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_contact_methods
> **spec:implements:** @kind:operation GetContactMethods
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContactMethods.spec.md

Returns information about the configured contact methods. Specify a protocol in your request to return information about a specific contact method. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail .

## Input Shape: GetContactMethodsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| protocols | list[Any  # complex shape] |  | The protocols used to send notifications, such as Email , or SMS (text messaging). Specify a protocol in your request to |

## Output Shape: GetContactMethodsResult

- **contactMethods** (list[Any  # complex shape]): An array of objects that describe the contact methods.

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
def get_contact_methods(store, request: dict) -> dict:
    """Returns information about the configured contact methods. Specify a protocol in your request to return information about a specific contact method. A contact method is used to send you notifications a"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
