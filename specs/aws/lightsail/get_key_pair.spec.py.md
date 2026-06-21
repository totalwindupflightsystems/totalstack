---
id: "@specs/aws/lightsail/get_key_pair"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetKeyPair"
---

# GetKeyPair

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_key_pair
> **spec:implements:** @kind:operation GetKeyPair
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetKeyPair.spec.md

Returns information about a specific key pair.

## Input Shape: GetKeyPairRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| keyPairName | Any  # complex shape | ✓ | The name of the key pair for which you are requesting information. |

## Output Shape: GetKeyPairResult

- **keyPair** (Any  # complex shape): An array of key-value pairs containing information about the key pair.

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
def get_key_pair(store, request: dict) -> dict:
    """Returns information about a specific key pair."""
    key_pair_name = request.get("keyPairName", "").strip() if isinstance(request.get("keyPairName"), str) else request.get("keyPairName")
    if not key_pair_name:
        raise ValidationException("keyPairName is required")

    resource = store.key_pairs(key_pair_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource key_pair_name not found")
    return {"keyPairName": key_pair_name, **resource}
```
