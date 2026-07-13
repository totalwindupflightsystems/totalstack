---
id: "@specs/aws/sts/decode_authorization_message"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_DecodeAuthorizationMessage"
---

# DecodeAuthorizationMessage

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/decode_authorization_message
> **spec:implements:** @kind:operation DecodeAuthorizationMessage
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_DecodeAuthorizationMessage.spec.md

Decodes additional information about the authorization status of a request from an encoded message returned in response to an Amazon Web Services request. For example, if a user is not authorized to perform an operation that he or she has requested, the request returns a Client.UnauthorizedOperation response (an HTTP 403 response). Some Amazon Web Services operations additionally return an encoded message that can provide details about this authorization failure. Only certain Amazon Web Services operations return an encoded authorization message. The documentation for an individual operation indicates whether that operation returns an encoded message in addition to returning an HTTP code. The message is encoded because the details of the authorization status can contain privileged information that the user who requested the operation should not see. To decode an authorization status message, a user must be granted permissions through an IAM policy to request the DecodeAuthorizationMessage ( sts:DecodeAuthorizationMessage ) action. The decoded message includes the following type of information: Whether the request was denied due to an explicit deny or due to the absence of an explicit allow. For more information, see Determining Whether a Request is Allowed or Denied in the IAM User Guide . The principal who made the request. The requested action. The requested resource. The values of condition keys in the context of the user's request.

## Input Shape: DecodeAuthorizationMessageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| EncodedMessage | Any  # complex shape | ✓ | The encoded message that was returned with the response. |

## Output Shape: DecodeAuthorizationMessageResponse

- **DecodedMessage** (Any  # complex shape): The API returns a response with the decoded message.

## Errors
- **InvalidAuthorizationMessageException**: The error returned if the message passed to DecodeAuthorizationMessage was invalid. This can happen if the token contains invalid characters, such as line breaks, or if the message has expired.

## Implementation

```speclang
def decode_authorization_message(store, request: dict) -> dict:
    """Decodes additional information about the authorization status of a request from an encoded message returned in response to an Amazon Web Services request. For example, if a user is not authorized to p"""
    encoded_message = request.get("EncodedMessage", "").strip() if isinstance(request.get("EncodedMessage"), str) else request.get("EncodedMessage")
    if not encoded_message:
        raise ValidationException("EncodedMessage is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DecodeAuthorizationMessage", request)
```
