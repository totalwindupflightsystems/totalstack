---
id: "@specs/aws/lightsail/create_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateKeyPair"
---

# CreateKeyPair

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_key_pair
> **spec:implements:** @kind:operation CreateKeyPair
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateKeyPair.spec.md

Creates a custom SSH key pair that you can use with an Amazon Lightsail instance. Use the DownloadDefaultKeyPair action to create a Lightsail default key pair in an Amazon Web Services Region where a default key pair does not currently exist. The create key pair operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| keyPairName | Any  # complex shape | ✓ | The name for your new key pair. |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateKeyPairResult

- **keyPair** (Any  # complex shape): An array of key-value pairs containing information about the new key pair you just created.
- **operation** (Any  # complex shape): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ
- **privateKeyBase64** (Any  # complex shape): A base64-encoded RSA private key.
- **publicKeyBase64** (Any  # complex shape): A base64-encoded public key of the ssh-rsa type.

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
def create_key_pair(store, request: dict) -> dict:
    """Creates a custom SSH key pair that you can use with an Amazon Lightsail instance. Use the DownloadDefaultKeyPair action to create a Lightsail default key pair in an Amazon Web Services Region where a """
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")
    if not key_pair_name:
        raise ValidationException("keyPairName is required")

    if store.key_pairs(key_pair_name):
        raise ResourceInUseException(f"Resource key_pair_name already exists")

    record = {
        "keyPairName": key_pair_name,
        "tags": tags,
    }

    store.key_pairs(key_pair_name, record)

    return {
        "keyPair": record.get("keyPair", {}),
        "publicKeyBase64": record.get("publicKeyBase64", {}),
        "privateKeyBase64": record.get("privateKeyBase64", {}),
        "operation": record.get("operation", {}),
    }
```
