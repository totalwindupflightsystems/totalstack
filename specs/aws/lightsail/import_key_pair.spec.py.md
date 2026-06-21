---
id: "@specs/aws/lightsail/import_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_ImportKeyPair"
---

# ImportKeyPair

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/import_key_pair
> **spec:implements:** @kind:operation ImportKeyPair
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_ImportKeyPair.spec.md

Imports a public SSH key from a specific key pair.

## Input Shape: ImportKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| keyPairName | Any  # complex shape | ✓ | The name of the key pair for which you want to import the public key. |
| publicKeyBase64 | Any  # complex shape | ✓ | A base64-encoded public key of the ssh-rsa type. |

## Output Shape: ImportKeyPairResult

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
def import_key_pair(store, request: dict) -> dict:
    """Imports a public SSH key from a specific key pair."""
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")
    if not key_pair_name:
        raise ValidationException("keyPairName is required")
    public_key_base64 = request.get("publicKeyBase64", "").strip() if isinstance(request.get("publicKeyBase64"), str) else request.get("publicKeyBase64")
    if not public_key_base64:
        raise ValidationException("publicKeyBase64 is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ImportKeyPair", request)
```
