---
id: "@specs/aws/lightsail/delete_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteKeyPair"
---

# DeleteKeyPair

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_key_pair
> **spec:implements:** @kind:operation DeleteKeyPair
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteKeyPair.spec.md

Deletes the specified key pair by removing the public key from Amazon Lightsail. You can delete key pairs that were created using the ImportKeyPair and CreateKeyPair actions, as well as the Lightsail default key pair. A new default key pair will not be created unless you launch an instance without specifying a custom key pair, or you call the DownloadDefaultKeyPair API. The delete key pair operation supports tag-based access control via resource tags applied to the resource identified by key pair name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| expectedFingerprint | Any  # complex shape |  | The RSA fingerprint of the Lightsail default key pair to delete. The expectedFingerprint parameter is required only when |
| keyPairName | Any  # complex shape | ✓ | The name of the key pair to delete. |

## Output Shape: DeleteKeyPairResult

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
def delete_key_pair(store, request: dict) -> dict:
    """Deletes the specified key pair by removing the public key from Amazon Lightsail. You can delete key pairs that were created using the ImportKeyPair and CreateKeyPair actions, as well as the Lightsail """
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")

    if not store.key_pairs(key_pair_name):
        raise ResourceNotFoundException(f"Resource key_pair_name not found")
    store.delete_key_pairs(key_pair_name)
    return {}
```
