---
id: "@specs/aws/lightsail/get_key_pairs"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetKeyPairs"
---

# GetKeyPairs

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_key_pairs
> **spec:implements:** @kind:operation GetKeyPairs
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetKeyPairs.spec.md

Returns information about all key pairs in the user's account.

## Input Shape: GetKeyPairsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includeDefaultKeyPair | Any  # complex shape |  | A Boolean value that indicates whether to include the default key pair in the response of your request. |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetKeyPairs  |

## Output Shape: GetKeyPairsResult

- **keyPairs** (list[Any  # complex shape]): An array of key-value pairs containing information about the key pairs.
- **nextPageToken** (Any  # complex shape): The token to advance to the next page of results from your request. A next page token is not returned if there are no mo

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
def get_key_pairs(store, request: dict) -> dict:
    """Returns information about all key pairs in the user's account."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
