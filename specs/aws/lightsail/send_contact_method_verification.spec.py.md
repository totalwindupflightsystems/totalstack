---
id: "@specs/aws/lightsail/send_contact_method_verification"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_SendContactMethodVerification"
---

# SendContactMethodVerification

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/send_contact_method_verification
> **spec:implements:** @kind:operation SendContactMethodVerification
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_SendContactMethodVerification.spec.md

Sends a verification request to an email contact method to ensure it's owned by the requester. SMS contact methods don't need to be verified. A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see Notifications in Amazon Lightsail . A verification request is sent to the contact method when you initially create it. Use this action to send another verification request if a previous verification request was deleted, or has expired. Notifications are not sent to an email contact method until after it is verified, and confirmed as valid.

## Input Shape: SendContactMethodVerificationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| protocol | Any  # complex shape | ✓ | The protocol to verify, such as Email or SMS (text messaging). |

## Output Shape: SendContactMethodVerificationResult

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
def send_contact_method_verification(store, request: dict) -> dict:
    """Sends a verification request to an email contact method to ensure it's owned by the requester. SMS contact methods don't need to be verified. A contact method is used to send you notifications about y"""
    protocol = request.get("protocol", "").strip() if isinstance(request.get("protocol"), str) else request.get("protocol")
    if not protocol:
        raise ValidationException("protocol is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("SendContactMethodVerification", request)
```
