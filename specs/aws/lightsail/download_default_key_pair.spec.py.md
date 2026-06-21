---
id: "@specs/aws/lightsail/download_default_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DownloadDefaultKeyPair"
---

# DownloadDefaultKeyPair

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/download_default_key_pair
> **spec:implements:** @kind:operation DownloadDefaultKeyPair
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DownloadDefaultKeyPair.spec.md

Downloads the regional Amazon Lightsail default key pair. This action also creates a Lightsail default key pair if a default key pair does not currently exist in the Amazon Web Services Region.

## Input Shape: DownloadDefaultKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: DownloadDefaultKeyPairResult

- **createdAt** (Any  # complex shape): The timestamp when the default key pair was created.
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
def download_default_key_pair(store, request: dict) -> dict:
    """Downloads the regional Amazon Lightsail default key pair. This action also creates a Lightsail default key pair if a default key pair does not currently exist in the Amazon Web Services Region."""


    record = {
    }

    store.download_default_key_pairs(record)

    return {
        "publicKeyBase64": record.get("publicKeyBase64", {}),
        "privateKeyBase64": record.get("privateKeyBase64", {}),
        "createdAt": record.get("createdAt", {}),
    }
```
