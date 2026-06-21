---
id: "@specs/aws/lightsail/get_bundles"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetBundles"
---

# GetBundles

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_bundles
> **spec:implements:** @kind:operation GetBundles
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetBundles.spec.md

Returns the bundles that you can apply to an Amazon Lightsail instance when you create it. A bundle describes the specifications of an instance, such as the monthly cost, amount of memory, the number of vCPUs, amount of storage space, and monthly network data transfer quota. Bundles are referred to as instance plans in the Lightsail console.

## Input Shape: GetBundlesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| appCategory | Any  # complex shape |  | Returns a list of bundles that are specific to Lightsail for Research. You must use this parameter to view Lightsail for |
| includeInactive | Any  # complex shape |  | A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request. |
| pageToken | Any  # complex shape |  | The token to advance to the next page of results from your request. To get a page token, perform an initial GetBundles r |

## Output Shape: GetBundlesResult

- **bundles** (list[Any  # complex shape]): An array of key-value pairs that contains information about the available bundles.
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
def get_bundles(store, request: dict) -> dict:
    """Returns the bundles that you can apply to an Amazon Lightsail instance when you create it. A bundle describes the specifications of an instance, such as the monthly cost, amount of memory, the number """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
